# 10.07 — JWKS and Public Keys

## Status
- Editorial maturity: working draft
- Normative readiness: not started

## Purpose

This section defines the key discovery aspect of the canonical API. It describes how token validation material (public signing keys) is published by the control plane and consumed by applications and SDKs in the workspace plane.

## Standards Compliance

This section implements the following standards:

- [RFC 7517 — JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517) for the key set structure and format.
- [RFC 8615 — Well-Known URIs](https://www.rfc-editor.org/rfc/rfc8615.html) for the discovery endpoint path convention.

## Why Key Discovery Matters

The DSL model relies on local token validation — the application SDK verifies lease tokens without calling the control plane on every check. To do this, the SDK needs the public key that corresponds to the private key used to sign the token.

The JWKS (JSON Web Key Set) endpoint provides this public key in the standard format defined by RFC 7517.

## Endpoint

```http
GET /.well-known/jwks.json
```

This follows the standard well-known URI convention used in OAuth 2.0 and OpenID Connect ecosystems. The path is fixed and does not require authentication, since public keys are not sensitive — they are meant to be distributed.

## Interaction Flow

1. On first startup (or when the cached keys expire), the SDK or license agent fetches the JWKS from the control plane.
2. The response contains one or more public keys, each identified by a key ID (`kid`).
3. The SDK caches the keys locally.
4. When validating a token, the SDK:
   - Reads the `kid` from the token header.
   - Looks up the corresponding public key in the local cache.
   - Verifies the token signature using that key.
5. If the token references a `kid` that is not in the cache (e.g., after key rotation), the SDK fetches the JWKS again to obtain the new key.

## Response Structure

The JWKS response follows [RFC 7517 — JSON Web Key Set](https://datatracker.ietf.org/doc/html/rfc7517):

```json
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "key-2025-10",
      "use": "sig",
      "alg": "RS256",
      "n": "<base64url-encoded modulus>",
      "e": "<base64url-encoded exponent>"
    }
  ]
}
```

| Field | Description |
|---|---|
| `kty` | Key type (e.g., `"RSA"`, `"EC"`) |
| `kid` | Key identifier — matches the `kid` in token headers |
| `use` | Key usage — always `"sig"` (signature) for this purpose |
| `alg` | Algorithm (e.g., `"RS256"`, `"ES256"`) |
| `n`, `e` | Key material (format depends on key type) |

The response may contain multiple keys to support key rotation (the current key and the previous key during a transition period).

## Key Rotation

Key rotation is the process of replacing the signing key periodically to limit the impact of a potential key compromise. The DSL model supports key rotation as follows:

1. The control plane generates a new signing key in the key management service.
2. New tokens are signed with the new key (new `kid`).
3. The JWKS endpoint publishes both the new and old public keys.
4. SDKs that encounter the new `kid` refresh their cache and obtain the new key.
5. After a transition period (long enough for all active tokens signed with the old key to expire), the old key is removed from the JWKS response.

This ensures that tokens signed with either key can be validated during the transition, and no workload experiences a validation failure due to rotation.

## Caching Behavior

The SDK should cache JWKS responses to avoid unnecessary network calls:

- Cache the keys after the first fetch.
- Refresh the cache only when:
  - A token contains a `kid` not found in the cache (indicates key rotation).
  - A configurable cache TTL has elapsed.
- Do not fetch JWKS on every token validation — this would defeat the purpose of local validation.

The control plane may include standard HTTP cache headers (`Cache-Control`, `max-age`) to guide caching behavior.

## Availability Considerations

The JWKS endpoint should be highly available because:

- If the endpoint is unreachable during first startup, the SDK cannot validate any tokens.
- If the endpoint is unreachable during key rotation, SDKs cannot obtain the new key.

However, because keys are cached, a temporary outage of the JWKS endpoint does not affect workloads that already have the keys cached. The impact is limited to:

- New workloads starting for the first time.
- Key rotation transitions.

For environments with strict availability requirements, the JWKS response can be pre-distributed or cached at an edge layer.

## Security Considerations

- The JWKS endpoint serves public keys only. Private signing keys never leave the key management service.
- The endpoint is served over TLS to prevent key substitution via man-in-the-middle attacks.
- The endpoint does not require authentication — public keys are intended to be freely accessible.
- Key identifiers (`kid`) are included in both the JWKS response and token headers to ensure unambiguous key matching.

## Relationship to Other Operations

- Issue and Renew produce signed tokens that reference a `kid`.
- The SDK uses the JWKS endpoint to obtain the public key for that `kid`.
- Token validation (signature, expiry, claims) happens locally using the cached key — no further API call is needed.
- Key rotation is managed by the control plane's key management service and reflected automatically in the JWKS response.

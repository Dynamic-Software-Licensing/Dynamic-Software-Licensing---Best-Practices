# 04.03. License and Policy Terms

## Purpose

This section establishes consistent vocabulary for behavior rules, license management mechanics, data models, and enforcement policies across runtime environments.

## Scope Statement

This section supports terminological alignment for the requirement, API, and data model chapters. It explicitly excludes legal contract wording, vendor-specific pricing models, and licensing economics.

---

## Definitions

**Entitlement** - The legal and commercial right to use a software application, module, or specific feature set, as granted by a software publisher (ISV) to a customer organization.

**Grace Period** - A deterministic, policy-defined temporal safety envelope that permits a media function to bypass strict enforcement and continue normal operations during transient connectivity loss to the licensing authority.

**Lease** - An active, cryptographically signed, and time-bounded allocation of a specific entitlement to a designated executing media function or deployment context.

**License Modality** - The distinct commercial and operational framework (e.g., time-based, process-based, or outcome-based) that dictates how software usage metrics are mapped to commercial terms and entitlements.

**Time-Based License Modality** - A lease model governed by start time, end time, or continuous duration (for example hourly, daily, monthly, or annual use). Within DSL, use this term when the primary enforcement dimension is time or duration.

**Process-Based License Modality** - A lease model governed by throughput or capacity units, such as channel count, FPS, sessions, or bandwidth. Within DSL, use this term when the primary enforcement dimensions are continuous operational counters rather than elapsed time.

**Outcome-Based License Modality** - A consumption model governed by discrete outputs or completed results, such as generated clips, rendered frames, transcode jobs, or analysis reports. Within DSL, use this term when value is tied directly to produced outcomes that can be counted or attributed.

**Credit or Unit-Pool License Modality** - A model in which runtime usage depletes a pre-purchased or pre-allocated pool of generic licensing units. Within DSL, use this term when entitlements are managed as shared pools at tenant or organizational level, and distinguish explicitly between depleting-pool and floating-pool behavior where relevant.

**Perpetual License** - An entitlement model that grants a customer organization the indefinite, non-expiring legal right to use a specific software version or feature set.

**Policy Object** - A structured data envelope containing the control settings and configuration constraints governing a lease's behavior, including renewal windows, grace intervals, and alerting thresholds.

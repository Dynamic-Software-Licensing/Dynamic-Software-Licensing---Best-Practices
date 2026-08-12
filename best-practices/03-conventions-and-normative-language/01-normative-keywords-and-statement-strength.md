# 03.01 Normative Keywords and Statement Strength

## Purpose

This section defines how statement strength is expressed in the Dynamic Software Licensing best
practices and how readers should interpret normative keywords.

The objective is not to imitate a formal standard mechanically, but to apply disciplined wording
where interpretation strength matters for interoperability, implementation behavior, or
conformance assessment.

## Normative Keywords

The core keyword set used in the best practices is:
- **MUST**
- **SHOULD**
- **MAY**

These keywords are used only where the text needs to distinguish clearly between required,
strongly recommended, and optional behavior.

## Interpretation of Statement Strength

The keywords are interpreted as follows:

- **MUST** expresses a required behavior, constraint, or interpretation rule that is necessary
  for consistent application of the best practices.
- **SHOULD** expresses a strong recommendation. Alternative approaches are possible, but a
  departure should be intentional and justified.
- **MAY** expresses an allowed option or acceptable variation that remains compatible with the
  overall model.

Where no normative keyword is used, the text should normally be read as descriptive,
interpretive, or explanatory rather than as a testable requirement.

## When Normative Keywords Belong

Normative keywords are appropriate where the text defines:
- interoperability expectations,
- trust and security behavior,
- lifecycle or state handling constraints,
- API or data model interpretation rules,
- conformance-relevant implementation behavior.

They are generally not appropriate in background, motivation, or purely illustrative passages.

## Use Discipline

Normative keywords are only useful when they remain selective and meaningful. Overuse weakens
interpretation and makes review harder.

For that reason:
- introductory sections should normally avoid normative wording,
- explanatory examples should not introduce accidental requirements,
- informative annexes should only contain normative terms where they restate or clarify rules
  already grounded in the main document or normative annexes,
- mixed passages should make it clear which sentence carries the requirement and which sentence
  only explains it.

## Relationship to Conformance

Not every normative sentence has the same practical weight, but normative keywords form the
main basis for conformance interpretation. They help identify which expectations are central to
profile alignment, implementation review, and cross-vendor consistency.

## Section Positioning

This section provides the baseline interpretation model for requirement strength across the full
repository. It should be used whenever wording is reviewed for precision, consistency, or
normative effect.

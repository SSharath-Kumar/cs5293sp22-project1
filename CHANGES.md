# Changes

Issues reported:

1. Moderate features for
- Gender
- Dates
- Concept


2. Small amount of features for *Addresses*

## Fixes Done

### Redaction of gender Revealing Terms
Added keywords to expand the redaction criteria. (Previously used 20+ keywords, updated to 70+)

### Redaction of dates
Added one more regex pattern to redact dates in (xx/xx/xx) format.

### Redaction of sentences related to given concept
Used *hyponymns* from wordnet to expand the redaction criteria.
Converted each word in the sentence to lowercase for comparison and redaction.

### Redaction of addresses
Used the *pyap* library to identify addresses in the data.

*Note: Redaction is still buggy, postal code is not being redacted.*
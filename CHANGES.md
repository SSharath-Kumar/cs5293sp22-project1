# Changes

* Moderate features for Gender (-2) --- Added keywords to expand the redaction criteria. (Previously used 20+ keywords, updated to 70+)


* Moderate features for Dates (-2) --- Added one more regex pattern to redact dates in (xx/xx/xx) format.


* Moderate features for Concept (-2) --- Used *hyponymns* from wordnet to expand the redaction criteria.
Converted each word in the sentence to lowercase for comparison and redaction.


* Small amount of features for *Addresses* (-3) --- Used the *pyap* library to identify addresses in the data.

*Note: Address Redaction is still buggy, postal code is not being redacted.*

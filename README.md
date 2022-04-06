# cs5293sp22-project1
# Text Analytics - Project 1 - Redactor

# **Libraries used for NLP**

* spacy (en_core_web_md )- https://spacy.io/models/en

* nltk - https://www.nltk.org/


# **Libraries Used**

* **argparse** - https://docs.python.org/3/library/argparse.html

Library used for command line options and arguments

* **sys** - https://docs.python.org/3/library/sys.html

Library used for the statistics outputs for stdout and stderr

* **os** - https://docs.python.org/3/library/os.html

Library used for checking available folders

* **glob** - https://docs.python.org/3/library/glob.html

Library used to get all files matching the specified pathname

* **pytest** - https://docs.pytest.org/en/7.0.x/

The above module is used to run the test cases written.

* **re (Regex)** - https://docs.python.org/3/library/re.html

The re module is used to perform regular expression operations


# **Assumptions**

Inputs: All input files are assumed to be text files with .txt extension placed a separate directory.

**As the redactions are done using spacy and NLTK libraries, models provided by these llibraries are not 100% accurate.
Hence the redaction in the project is also not 100% accurate.**


## Arguments and corresponding functionalities programmed: ##

## **--INPUTS**

A glob is provided as the input for the redactor. 
Assuming that all the files are in a separate directory (input), the sample value for input is *\<file extension>

All matching file names are picked up and iterated upon to redact information.

**Error Handling - **

A try catch block is in place to display an error message if any file is not readable. This has been tested using a locked PDF file. 

## **--NAME**

Names of people are only considered for redaction. 

Function: **redact_names**

*input: string (file data to be passed as a string)*

Using spacy tokenized the data from the input file and all entities with the label PERSON are redacted using replace.

To increase accuracy, NLTK is also used to find any other names missed. 
The data is tokenized into chunks (ne_chunk) and all chunks with the PERSON label are redacted using replace.


## **--DATES**

**Date formats considered for redaction:**

* XX/XX/XXXX example: 04/05/2022

* X/X/XXXX example: 4/5/2022

* Date formats recongized by spacy 

Function: **redact_dates**

*input: string (file data to be passed as a string)*

Using spacy tokenized the data from the input file and all entities with the label DATE are redacted using replace.

To handle the 2 other formats of dates, regular expressions are used to redact dates in such formats.

## **--PHONES**

**Phone number formats considered for redaction:**

* XXX-XXX-XXXX

* XXX.XXX.XXXX

* (XXX) XXX-XXXX

* XXX.XXX-XXXX

* XXX.XXX.XXXX

* XXX XXX XXXX

* XXXXXXXXXX

Function: **redact_phones**

*input: string (file data to be passed as a string)*

All the above patterns are found in the files using regular expressions and redacted using replace.

## **--GENDERS**

The following words are considered to be gender revealing and are redacted.

['grandfather', 'grandmother', 'father', 'mother', 'male', 'female', 'sister', 'brother', 'wife', 'husband', 'son', 'daughter', 'nephew', 'niece',
 'grandson', 'granddaughter', 'stepmother', 'stepfather', 'godfather', 'godmother', he', 'him', 'his', 'she', 'her']

Function: **redact_genders**

*input: string (file data to be passed as a string)*

Using NLTK tokenizers, the input data is tokenized to words. These words are converted to lower case and then checked against the above list.
If the word matches, it is then replaced using re.sub instead of replace to avoid other words containing these words to be redacted.
Example: Refresher -> contains she and he. Using a regex with word boundaries would make sure the exact word is redacted.


## **--ADDRESS**

Note: Addresses and Locations recognized by spacy are only considered for redaction

Function: **redact_address**

*input: string (file data to be passed as a string)*

Using spacy tokenized the data from the input file and all entities with the labels GEP and LOC are redacted using replace.

## **--CONCEPT**

Wordnet is used for redacting similar words. All synonyms or similar words recognized by wordnet are only redacted.

Function: **redact_concepts**

*input: string (file data to be passed as a string)*

The synonyms for the given concept are fetched from wordnet and stored in an array.
The data from the input file is tokenized into sentences and words. If the word matches with any of the synonyms, the whole sentence is redacted using replace

## **--STATS**

For each of the argument mentioned above, the count of redaction is incremented by 1 each time redaction occurs either by replace or re.sub().
These statistics are either written to a file or written to stdout/stderr based on the input provided. 

Note: stats are always written to the stats directory and the file extension is .log

## **--OUTPUT**

The extensions of the files provided as input are extracted from the argument initially.
This extension is replaced by .redacted. As the files are picked from input directory, 'input\' is present in the file names.
This part of the file names is trimmed and the rest of the file name is used to create the output file to which the redacted data is written to.

## **unicode_block_gen:**

*input: length (length of redacted block to be generated)*

This function generates a string of the unicode block of the provided length. The unicode character (█) is defined and an empty string is appended with the defined unicode character in a loop to generate the redaction block.


# Test Cases:

## *test_redaction:*

**NOTE: This test case is to be run after running the redactor atleast once.**

The test case looks for files with the .redacted extension. All such files are read and checked for the number of unicode characters.
The test case fails if it doesnot contain any unicode characters.
----

**NOTE: Below test cases pick all the text files from the input directory.**

## *test_redact_names*

data from text file is read and passed as an input to the redact_names function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

## *test_redact_dates*

data from text file is read and passed as an input to the redact_dates function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

## *test_redact_phones*

data from text file is read and passed as an input to the redact_phones function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

## *test_redact_address*

data from text file is read and passed as an input to the redact_address function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

## *test_redact_genders*

data from text file is read and passed as an input to the redact_genders function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

## *test_redact_concepts*

data from text file is read and passed as an input to the redact_concepts function. 
Data returned from the function is compared with the actual data from the file. If both strings are same, the test case fails.

- - - - -

# Steps for local deployment:
1] Clone the repository using the below command git clone https://github.com/SSharath-Kumar/cs5293sp22-project1

2] Install the required dependencies using the command: pipenv install

# Running the project:
pipenv run python .\redactor.py --input *\*.txt --names --dates --phones --address --genders --concept depression --output redacted --stats redaction_stats

# Runnning the test cases:
pipenv run python -m pytest

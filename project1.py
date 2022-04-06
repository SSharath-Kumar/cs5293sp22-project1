import en_core_web_md
import nltk
import re
from nltk.corpus import wordnet
from nltk import word_tokenize, sent_tokenize

# For using chunks
nltk.download('punkt',quiet=True)
nltk.download('averaged_perceptron_tagger',quiet=True)
nltk.download('maxent_ne_chunker',quiet=True)
nltk.download('words',quiet=True)
# For Concepts
nltk.download('wordnet',quiet=True)
nltk.download('omw-1.4',quiet=True)


# Block to generate Unicode characters of given length
def unicode_block_gen(length):
    unicode_block = u'\u2588'
    block = ''
    for idx in range(length):
        block += unicode_block
    return block


# Load the English Model
nlp = en_core_web_md.load()


def redact_names(data):
    # Using SPACY
    doc = nlp(data)

    redactions = 0
    # words_to_redact = []

    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            # print(entity.text)
            # words_to_redact.append(entity.text)
            data = data.replace(entity.text, unicode_block_gen(len(entity.text)))
            redactions += 1

    # Using NLTK
    for sentence in nltk.sent_tokenize(data):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                # print(chunk[0][0])
                # words_to_redact.append(chunk[0][0])
                data = data.replace(chunk[0][0], unicode_block_gen(len(chunk[0][0])))
                redactions += 1

    return data, redactions
    # return words_to_redact


def redact_dates(data):
    # Using SPACY
    doc = nlp(data)
    redactions = 0
    # dates_to_redact = []
    for entity in doc.ents:
        if entity.label_ == 'DATE':
            # print(entity.text)
            # dates_to_redact.append(entity.text)
            data = data.replace(entity.text, unicode_block_gen(len(entity.text)))
            redactions += 1

    # To handle other occurrences
    # Format: 04/01/2022
    date_list1 = re.match(r"\d{2}/\d{2}/\d{4}", data)
    if date_list1 is not None:
        for occurrence in date_list1:
            # dates_to_redact.append(occurrence)
            data = data.replace(occurrence, unicode_block_gen(len(occurrence)))
            redactions += 1

    # Format: 4/1/2022
    date_list2 = re.match(r"\d/\d/\d{4}", data)
    if date_list2 is not None:
        for occurrence in date_list2:
            # dates_to_redact.append(occurrence)
            data = data.replace(occurrence, unicode_block_gen(len(occurrence)))
            redactions += 1

    return data, redactions
    # return dates_to_redact


def redact_phones(data):
    redactions = 0
    # redact_phone_numbers = []

    # Pattern -> XXX-XXX-XXXX or XXX.XXX.XXXX
    pattern1 = re.findall(r"\d{3}[-.]\d{3}[-.]\d{4}", data)

    for item in pattern1:
        # redact_phone_numbers.append(item)
        data = data.replace(item, unicode_block_gen(len(item)))
        redactions += 1

    # Pattern -> (XXX) XXX-XXXX
    pattern2 = re.findall(r"[(]\d{3}[)] \d{3}-\d{4}", data)

    for item in pattern2:
        # redact_phone_numbers.append(item)
        data = data.replace(item, unicode_block_gen(len(item)))
        redactions += 1

    # Pattern -> XXX.XXX-/.XXXX?
    pattern3 = re.findall(r"\d{3}[.]\d{3}[-.]\d{4}", data)

    for item in pattern3:
        # redact_phone_numbers.append(item)
        data = data.replace(item, unicode_block_gen(len(item)))
        redactions += 1

    # Pattern -> XXX XXX XXXX
    pattern4 = re.findall(r"\d{3} \d{3} \d{4}", data)

    for item in pattern4:
        # redact_phone_numbers.append(item)
        data = data.replace(item, unicode_block_gen(len(item)))
        redactions += 1

    # Pattern -> XXXXXXXXXX
    pattern5 = re.findall(r"\d{10}", data)

    for item in pattern5:
        # redact_phone_numbers.append(item)
        data = data.replace(item, unicode_block_gen(len(item)))
        redactions += 1

    return data, redactions
    # return redact_phone_numbers


def redact_genders(data):
    gender_words = ['grandfather', 'grandmother', 'father', 'mother', 'male', 'female',
                    'sister', 'brother', 'wife', 'husband', 'son', 'daughter', 'nephew', 'niece',
                    'grandson', 'granddaughter', 'stepmother', 'stepfather', 'godfather', 'godmother',
                    'he', 'him', 'his', 'she', 'her']
    redactions = 0

    words_to_redact = []

    for sent in sent_tokenize(data):
        for word in word_tokenize(sent):
            for gw in gender_words:
                if word.lower() == gw:
                    # print(word)
                    # words_to_redact.append(word)
                    rp = r'\b' + word + r'\b'
                    data = re.sub(rp, unicode_block_gen(len(word)), data)
                    redactions += 1

    return data, redactions
    # return words_to_redact


def redact_address(data):
    # Using SPACY
    doc = nlp(data)
    redactions = 0
    # redacted_address = []
    for entity in doc.ents:
        if entity.label_ == 'GPE' or entity.label_ == 'LOC':
            # print(entity.text)
            # redacted_address.append(entity.text)
            data = data.replace(entity.text, unicode_block_gen(len(entity.text)))
            redactions += 1
    return data, redactions
    # return redacted_address


def redact_concepts(data, concept):
    synonyms = []
    redactions = 0
    # sentences_to_redact = []

    for syn in wordnet.synsets(concept):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    for sent in sent_tokenize(data):
        for word in word_tokenize(sent):
            for syn in synonyms:
                if syn == word:
                    # sentences_to_redact.append(sent)
                    data = data.replace(sent, unicode_block_gen(len(sent)))
                    redactions += 1
    return data, redactions
    # return sentences_to_redact

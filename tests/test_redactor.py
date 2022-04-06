import project1
import glob

test_files = []
input_data = []
# Get all text files from input folder
test_files += glob.glob('/home/sharath11397/cs5293sp22-project1/tests/*.txt')

for test_file in test_files:
    with open(test_file, 'r') as file:
        input_data.append(file.read())


def test_redact_names():
    counter = []
    for data in input_data:
        output_data = project1.redact_names(data)
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


def test_redact_dates():
    counter = []
    for data in input_data:
        output_data = project1.redact_dates(data)
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


def test_redact_phones():
    counter = []
    for data in input_data:
        output_data = project1.redact_phones(data)
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


def test_redact_address():
    counter = []
    for data in input_data:
        output_data = project1.redact_address(data)
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


def test_redact_genders():
    counter = []
    for data in input_data:
        output_data = project1.redact_genders(data)
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


def test_redact_concepts():
    counter = []
    for data in input_data:
        output_data = project1.redact_concepts(data,'depression')
        if data == output_data:
            counter.append(False)
        else:
            counter.append(True)

    flag = True
    for c in counter:
        if not c:
            flag = False
            break
    assert flag


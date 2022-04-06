import glob


def test_redaction():
    redacted_files = []

    # Look for redacted files in current directory
    redacted_files += glob.glob("*.redacted")

    # Look for redacted files in any directories
    redacted_files += glob.glob("\\*.redacted")

    # Look for redacted files in any subdirectories
    redacted_files += glob.glob("\\**\\*.redacted")

    # print(redacted_files)
    counter = []

    # Loop through all the redacted files
    for file in redacted_files:
        # Open files in read mode
        with open(file,'r') as redacted_file:
            data = redacted_file.read()
            unicode_block = u'\u2588'
            count = 0

            # Count unicode characters in file
            for i in data:
                if i == unicode_block:
                    count += 1
            counter.append(count)

    # print(counter)

    flag = True
    for count in counter:
        if count == 0:
            flag = False

    assert flag
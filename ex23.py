from sys import argv
script, input_encoding, error = argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip() removes \n from the end of line
    next_lang = line.strip()
    # encode() converts the utf-8 string into raw bytes
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # decode() converts the raw bytes into utf-8 string
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)

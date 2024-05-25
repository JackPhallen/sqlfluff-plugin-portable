import os
from os import listdir
from os.path import isfile, join

DIALECTS_DIR = os.path.abspath("dialects")
OUTPUT_FILE = os.path.join(os.path.abspath("output"), "intersection")


def main():
    print("Looking for dialects in: " + DIALECTS_DIR)
    dialects = get_dialects()
    if len(dialects) == 0:
        print("No dialects are defined")
        return
    print("Generating intersect of:")
    for dialect in dialects:
        print("  " + dialect)
    # Create a list of each set
    funct_sets = []
    for dialect in dialects:
        files = get_funct_files(dialect)
        functs = get_dialect_functions(files)
        funct_sets.append(functs)
    # Get intersect
    a_set = funct_sets.pop()
    intersect = a_set.intersection(*funct_sets)
    with open(OUTPUT_FILE, 'w+') as f:
        for line in intersect:
            f.write(f"{line}\n")
    print(intersect)


def get_funct_files(dialect):
    path = os.path.join(DIALECTS_DIR, dialect, "functions")
    return [os.path.join(path, f) for f in listdir(path) if isfile(join(path, f))]


def get_dialects():
    return next(os.walk('./dialects'))[1]


def get_dialect_functions(files):
    funct_set = set()
    for file in files:
        functs = set(line.strip() for line in open(file))
        funct_set = funct_set.union(functs)
    return funct_set


if __name__ == "__main__":
    main()

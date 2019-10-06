# Exercise 17 - More files - Friendlier version
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}\nThe input file is {len(open(from_file).read())} bytes long\nDoes the output file exist? {exists(to_file)} {open(to_file, 'w').write(open(from_file).read())}")

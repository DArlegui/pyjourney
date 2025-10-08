# Reading contents from of a File
from pathlib import Path

path = Path("./pi_digits.txt")
contents = path.read_text()
# print(contents)
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

from pathlib import Path

path = Path(__file__).parent / "alice.txt"
path = Path("alice.txt")

contents = path.read_text(encoding="utf-8")
words = contents.split()
num_words = len(words)

print(f"The file {path.name} has about {num_words} words.")
path = Path("pcc_exercises/ch10_files_exceptions/alice.txt")
path = Path("alice.txt")

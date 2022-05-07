from art import text2art

from .screen import GREEN, NC
from .compare import Compare

print(GREEN + text2art("Hello, world!") + NC)

print("Type a message:")
message = input()

compare = Compare("Hello, world!", message)
print(f"Diff: {compare.diff():.1f}%")

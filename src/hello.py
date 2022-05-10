from art import text2art

from .screen import YELLOW, NC
from .compare import Compare

print(YELLOW + text2art("Hello, world!") + NC)

print("Type a message:")
message = input()

compare = Compare("Hello, world!", message)
print(f"Diff: {compare.diff():.1f}%")

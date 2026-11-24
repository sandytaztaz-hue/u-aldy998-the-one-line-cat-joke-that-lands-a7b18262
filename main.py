"""One-line cat joke entry for the make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262."""

import os

ENTRY = "My cat sat on my keyboard during my job interview, then stared into the camera like she'd been hired and I was the intern."

# The entry text is the only output: one line, no title, no extra words,
# and no trailing newline beyond the entry itself.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

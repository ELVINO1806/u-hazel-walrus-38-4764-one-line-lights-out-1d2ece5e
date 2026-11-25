import os

ENTRY = "your alarm is set for 06:00. i will ring it in an empty room, and no one will snooze me."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

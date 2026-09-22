#! /usr/bin/env python3
import sys
from typing import IO


def main() -> None:

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    archive_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file {archive_name}")
    try:
        archive: IO[str] = open(archive_name, 'r', encoding='utf-8')
        print("---")
        print("")
        content: str = archive.read()
        print(content, end="")
        print("")
        print("---")
        archive.close()
        print(f"File '{archive_name}' closed.")
        print("")
    except Exception as e:
        print(f"Error opening file '{archive_name}': {e}")
        sys.exit(1)
    print("Transform data:")
    print("---")
    archive = open(archive_name, 'r', encoding='utf-8')
    transform_content = ""
    for line in archive:
        line_clean = line.rstrip('\n')
        line_modified = f"{line_clean}#\n"
        transform_content += line_modified
        print(line_modified, end="")
    archive.close()
    print("---")
    # capturar el nombre del nuevo archivo
    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_name}'.")
    try:
        new_archive: IO[str] = open(new_name, 'w', encoding='utf=8')
        new_archive.write(transform_content)
        new_archive.close()
        print(f"Data saved in file '{new_name}'.")
    except Exception as e:
        print(f"Error saving file '{new_name}': {e}")


if __name__ == "__main__":
    main()

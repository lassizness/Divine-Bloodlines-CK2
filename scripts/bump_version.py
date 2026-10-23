#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
VERSION_PATTERN = re.compile(r"\d+\.[0-9]\.[0-9]")


def next_version(version):
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"Invalid three-part version: {version}")

    major, minor, patch = map(int, version.split("."))
    patch += 1
    if patch == 10:
        patch = 0
        minor += 1
    if minor == 10:
        minor = 0
        major += 1

    return f"{major}.{minor}.{patch}"


def main():
    current_version = VERSION_FILE.read_text(encoding="ascii").strip()
    try:
        updated_version = next_version(current_version)
    except ValueError as error:
        raise SystemExit(str(error))

    updates = {}
    for language in ("EN", "RU"):
        descriptor = ROOT / f"Divine_Bloodlines_{language}.mod"
        content = descriptor.read_text(encoding="utf-8")
        name_pattern = re.compile(
            rf'(?m)^(name="Divine Bloodlines v)\d+\.[0-9]\.[0-9]( \[{language}\]")$'
        )
        updated, count = name_pattern.subn(
            lambda match: f"{match.group(1)}{updated_version}{match.group(2)}",
            content
        )
        if count != 1 or f'path="mod/Divine_Bloodlines_{language}"' not in updated:
            raise SystemExit(f"Unexpected descriptor format: {descriptor.name}")
        updates[descriptor] = updated

    for descriptor, content in updates.items():
        descriptor.write_text(content, encoding="utf-8")

    VERSION_FILE.write_text(updated_version + "\n", encoding="ascii")
    print(f"{current_version} -> {updated_version}")


if __name__ == "__main__":
    main()

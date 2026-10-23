#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
VERSION_PATTERN = re.compile(r"\d+(?:\.\d+){4}")


def main():
    current_version = VERSION_FILE.read_text(encoding="ascii").strip()
    if not VERSION_PATTERN.fullmatch(current_version):
        raise SystemExit(f"Invalid five-part version: {current_version}")

    parts = current_version.split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    next_version = ".".join(parts)

    updates = {}
    for language in ("EN", "RU"):
        descriptor = ROOT / f"Divine_Bloodlines_{language}.mod"
        content = descriptor.read_text(encoding="utf-8")
        name_pattern = re.compile(
            rf'(?m)^(name="Divine Bloodlines v)\d+(?:\.\d+){{4}}( \[{language}\]")$'
        )
        updated, count = name_pattern.subn(
            lambda match: f"{match.group(1)}{next_version}{match.group(2)}",
            content
        )
        if count != 1 or f'path="mod/Divine_Bloodlines_{language}"' not in updated:
            raise SystemExit(f"Unexpected descriptor format: {descriptor.name}")
        updates[descriptor] = updated

    for descriptor, content in updates.items():
        descriptor.write_text(content, encoding="utf-8")

    VERSION_FILE.write_text(next_version + "\n", encoding="ascii")
    print(f"{current_version} -> {next_version}")


if __name__ == "__main__":
    main()

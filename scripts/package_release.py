#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def main():
    version = (ROOT / "VERSION").read_text(encoding="ascii").strip()
    if len(version.split(".")) != 5 or not all(part.isdigit() for part in version.split(".")):
        raise SystemExit(f"Invalid version: {version}")

    DIST.mkdir(exist_ok=True)

    for language in ("EN", "RU"):
        folder = ROOT / f"Divine_Bloodlines_{language}"
        descriptor = ROOT / f"Divine_Bloodlines_{language}.mod"
        if not folder.is_dir() or not descriptor.is_file():
            raise SystemExit(f"Missing {language} mod files")

        text = descriptor.read_text(encoding="utf-8")
        if f'name="Divine Bloodlines v{version} [{language}]"' not in text:
            raise SystemExit(f"Version mismatch in {descriptor.name}")
        if f'path="mod/Divine_Bloodlines_{language}"' not in text:
            raise SystemExit(f"Invalid mod path in {descriptor.name}")

        files = sorted(path for path in folder.rglob("*") if path.is_file())
        if not files:
            raise SystemExit(f"Empty mod folder: {folder.name}")
        if any(path.is_symlink() for path in files):
            raise SystemExit(f"Symlinks are not allowed in {folder.name}")

        archive = DIST / f"Divine_Bloodlines_{language}_v{version}.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as target:
            target.write(descriptor, descriptor.name)
            for path in files:
                target.write(path, path.relative_to(ROOT).as_posix())

        with ZipFile(archive) as target:
            if target.testzip() is not None:
                raise SystemExit(f"Corrupt archive: {archive.name}")
            names = set(target.namelist())
            if descriptor.name not in names or not any(
                name.startswith(f"{folder.name}/") for name in names
            ):
                raise SystemExit(f"Invalid archive layout: {archive.name}")

        print(f"Created {archive.name} ({len(files) + 1} files)")


if __name__ == "__main__":
    main()

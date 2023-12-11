import csv
import frontmatter
from pathlib import Path


def extract_frontmatter(entries_path: Path) -> list[str, str, bool]:
    entries = []

    for entry in entries_path.glob("*.md"):
        with open(entry, "r", encoding="utf-8") as f:
            try:
                front = frontmatter.loads(f.read())
                date = front["date"] or entry.stem
                feeling = front["feeling"] or "unknown"
                important = front["important"] or False
            except:
                print(f"error while reading: {f.name}")

            entries.append([date, feeling, important])

    return entries


def write_entries_to_csv(entries: list[str, str, bool], output_csv: Path) -> None:
    fieldnames = ["date", "feeling", "important"]

    with open(output_csv, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)

        for entry in entries:
            writer.writerow(entry)

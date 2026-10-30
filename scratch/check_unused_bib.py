import re
from pathlib import Path

bib_path = Path("thesis/references.bib")
bib_text = bib_path.read_text(encoding="utf-8")

# Extract citations used in all .tex files
tex_citations = set()
for tex_file in Path("thesis/chapters").glob("*.tex"):
    txt = tex_file.read_text(encoding="utf-8")
    matches = re.findall(r"\\cite[a-zA-Z]*\{([^}]+)\}", txt)
    for m in matches:
        for k in m.split(","):
            tex_citations.add(k.strip())

# Also check main.tex itself
for m in re.findall(r"\\cite[a-zA-Z]*\{([^}]+)\}", Path("thesis/main.tex").read_text(encoding="utf-8")):
    for k in m.split(","):
        tex_citations.add(k.strip())

# Parse entries in bib
pattern = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,\s*(.*?)(?=\n@|\Z)", re.DOTALL)
entries = pattern.findall(bib_text)

print(f"Total entries parsed in references.bib: {len(entries)}")
print(f"Explicitly cited entries in text: {len(tex_citations)}")

unused = []
for entry_type, key, body in entries:
    if key not in tex_citations:
        title_m = re.search(r"title\s*=\s*[\"{](.*?)[\"}]", body, re.DOTALL)
        author_m = re.search(r"author\s*=\s*[\"{](.*?)[\"}]", body, re.DOTALL)
        year_m = re.search(r"year\s*=\s*[\"{]?(\d+)[\"}]?", body)
        title = " ".join(title_m.group(1).split()) if title_m else "No title"
        author = " ".join(author_m.group(1).split()) if author_m else "No author"
        year = year_m.group(1) if year_m else "No year"
        unused.append((key, entry_type, author, year, title))

print(f"\nUnused entries ({len(unused)}):")
for k, t, a, y, title in unused:
    print(f"Key: {k} ({y})")
    print(f"  Title: {title}")
    print(f"  Authors: {a}\n")

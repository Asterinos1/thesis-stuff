import re
from pathlib import Path

# 1. Update thesis/main.tex
main_path = Path("thesis/main.tex")
main_text = main_path.read_text(encoding="utf-8")
new_main_text = re.sub(r"[ \t]*\\nocite\{\*\}[ \t]*\r?\n", "", main_text)
assert new_main_text != main_text, "Failed to remove \\nocite{*} from main.tex"
main_path.write_text(new_main_text, encoding="utf-8")
print("Removed \\nocite{*} from thesis/main.tex")

# 2. Prune unused entries from thesis/references.bib
bib_path = Path("thesis/references.bib")
bib_text = bib_path.read_text(encoding="utf-8")

unused_keys = {
    "bottou2010large",
    "dean2012large",
    "devlin2019bert",
    "goodfellow2016deep",
    "kelaidis2025federated",
    "lai2021oort",
    "rumelhart1986learning",
    "socher2013recursive",
    "theologitis2023algorithms",
    "theologitis2025edbt",
    "wang2020tackling",
    "williams2018broad",
    "zhao2024loratheexplorer",
}

# Split into entries while preserving formatting
# Each entry starts with @type{key, and ends before the next @ or end of file
pattern = re.compile(r"(@\w+\s*\{\s*([^,\s]+)\s*,.*?\n\s*\})", re.DOTALL)

pruned_count = 0
kept_count = 0

def filter_entries(text):
    global pruned_count, kept_count
    # Find all entry matches and positions
    matches = list(pattern.finditer(text))
    new_chunks = []
    last_idx = 0
    for m in matches:
        full_entry = m.group(1)
        key = m.group(2)
        # Add any intervening comments/whitespace
        new_chunks.append(text[last_idx:m.start()])
        if key in unused_keys:
            pruned_count += 1
            print(f"Pruning: {key}")
        else:
            kept_count += 1
            new_chunks.append(full_entry)
        last_idx = m.end()
    new_chunks.append(text[last_idx:])
    return "".join(new_chunks)

pruned_bib_text = filter_entries(bib_text)
# Clean up any excessive blank lines
pruned_bib_text = re.sub(r"\n{3,}", "\n\n", pruned_bib_text)

bib_path.write_text(pruned_bib_text, encoding="utf-8")
print(f"Pruning complete: {pruned_count} entries removed, {kept_count} entries kept.")

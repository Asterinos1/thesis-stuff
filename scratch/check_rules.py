import re

with open('thesis/chapters/evaluation.tex', 'r', encoding='utf-8') as f:
    text = f.read()

tables = re.findall(r'(\\begin\{table\}.*?\\end\{table\})', text, re.DOTALL)
print(f'Total tables: {len(tables)}')
for i, t in enumerate(tables):
    m = re.search(r'\\label\{([^}]+)\}', t)
    col = re.search(r'\\begin\{tabular\}\{([^}]+)\}', t)
    has_toprule = 'toprule' in t
    has_cmidrule = 'cmidrule' in t
    has_bottomrule = 'bottomrule' in t
    has_midrule = 'midrule' in t
    print(f'Table {i+1} ({m.group(1)}):')
    print(f'  tabular spec: {col.group(1) if col else "NONE"}')
    print(f'  rules check: toprule={has_toprule}, midrule={has_midrule}, cmidrule={has_cmidrule}, bottomrule={has_bottomrule}')

import re

with open('thesis/chapters/evaluation.tex', 'r', encoding='utf-8') as f:
    text = f.read()

figs = re.findall(r'(\\begin\{figure\}.*?\\end\{figure\})', text, re.DOTALL)
print(f'Total figures in Chapter 5: {len(figs)}')
for i, fig in enumerate(figs):
    lbl = re.search(r'\\label\{([^}]+)\}', fig)
    img = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', fig)
    print(f'Figure {i+1}: label={lbl.group(1) if lbl else "none"}, images={img}')

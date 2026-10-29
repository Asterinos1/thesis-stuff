import re

def convert_table(tex_str):
    # Table 3: tab:iid_detailed_benchmarks
    # Columns: 9 columns -> |l|l|l|c|c|c|c|c|c|
    def fix_tab3(m):
        t = m.group(0)
        t = re.sub(r'\\begin\{tabular\}\{llccccccc\}', r'\\begin{tabular}{|l|l|l|c|c|c|c|c|c|}', t)
        t = t.replace('\\toprule\n', '\\hline\n')
        t = t.replace('\\midrule\n', '\\hline\n')
        t = t.replace('\\cmidrule{2-9}', '\\cline{2-9}')
        t = t.replace('\\bottomrule', '\\hline')
        return t

    # Table 4: tab:non_iid_detailed_benchmarks
    # Columns: 10 columns -> |l|l|l|c|c|c|c|c|c|c|
    def fix_tab4(m):
        t = m.group(0)
        t = re.sub(r'\\begin\{tabular\}\{llcccccccc\}', r'\\begin{tabular}{|l|l|l|c|c|c|c|c|c|c|}', t)
        t = t.replace('\\toprule\n', '\\hline\n')
        t = t.replace('\\midrule\n', '\\hline\n')
        t = t.replace('\\cmidrule{2-10}', '\\cline{2-10}')
        t = t.replace('\\bottomrule', '\\hline')
        return t

    # Table 5: tab:milestone_synthesis
    # Columns: 7 columns -> |l|l|l|c|c|c|c|
    def fix_tab5(m):
        t = m.group(0)
        t = re.sub(r'\\begin\{tabular\}\{lllcccc\}', r'\\begin{tabular}{|l|l|l|c|c|c|c|}', t)
        t = t.replace('\\toprule\n', '\\hline\n')
        t = t.replace('\\midrule\n', '\\hline\n')
        t = t.replace('\\cmidrule{2-7}', '\\cline{2-7}')
        t = t.replace('\\bottomrule', '\\hline')
        return t

    tex_str = re.sub(r'\\begin\{table\}.*?\\label\{tab:iid_detailed_benchmarks\}.*?\\end\{table\}', fix_tab3, tex_str, flags=re.DOTALL)
    tex_str = re.sub(r'\\begin\{table\}.*?\\label\{tab:non_iid_detailed_benchmarks\}.*?\\end\{table\}', fix_tab4, tex_str, flags=re.DOTALL)
    tex_str = re.sub(r'\\begin\{table\}.*?\\label\{tab:milestone_synthesis\}.*?\\end\{table\}', fix_tab5, tex_str, flags=re.DOTALL)

    return tex_str

with open('thesis/chapters/evaluation.tex', 'r', encoding='utf-8') as f:
    text = f.read()

new_text = convert_table(text)

with open('thesis/chapters/evaluation.tex', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated thesis/chapters/evaluation.tex successfully')

import re

with open('scratch/generate_evaluation_chapter.py', 'r', encoding='utf-8') as f:
    gen_text = f.read()

m = re.search(r'content = r?"""(.*?)"""', gen_text, re.DOTALL)
if m:
    gen_content = m.group(1).lstrip()
    with open('thesis/chapters/evaluation.tex', 'r', encoding='utf-8') as f:
        tex_content = f.read()
    if gen_content == tex_content:
        print('Contents are IDENTICAL!')
    else:
        print(f'Length diff: gen={len(gen_content)}, tex={len(tex_content)}')
else:
    print('Could not find content in generate_evaluation_chapter.py')

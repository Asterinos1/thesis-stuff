import pypdf

reader = pypdf.PdfReader('thesis/main.pdf')
for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ''
    for tab in ['Table 5.1', 'Table 5.2', 'Table 5.3', 'Table 5.4', 'Table 5.5']:
        if tab in text:
            print(f'Physical Page {idx+1}: contains "{tab}"')

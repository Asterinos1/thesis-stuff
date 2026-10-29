def update_links():
    path_tex = "presentation/presentation.tex"
    with open(path_tex, "r", encoding="utf-8") as f:
        tex = f.read()

    # Configure hyperref options if needed
    if r"\hypersetup{" not in tex:
        tex = tex.replace(
            r"\usepackage{hyperref}",
            r"\usepackage{hyperref}" + "\n" + r"\hypersetup{hidelinks}"
        )

    # 1. Update institute
    old_inst = r"""\institute[]{
    School of Electrical \& Computer Engineering\\
    Technical University of Crete
}"""
    new_inst = r"""\institute[]{
    \href{https://www.ece.tuc.gr/}{School of Electrical \& Computer Engineering}\\
    \href{https://www.tuc.gr/}{Technical University of Crete}
}"""
    assert old_inst in tex, "old_inst not found"
    tex = tex.replace(old_inst, new_inst)

    # 2. Update title slide masthead
    old_masthead = r"""    \begin{columns}[c]
        \begin{column}{0.10\textwidth}
            \includegraphics[height=1.35cm,keepaspectratio]{tuc_logo.png}
        \end{column}
        \begin{column}{0.88\textwidth}
            {\large \textbf{\color{tucblue}TECHNICAL UNIVERSITY OF CRETE}}\\[0.18em]
            {\small \color{tucgray}School of Electrical \& Computer Engineering}
        \end{column}
    \end{columns}"""

    new_masthead = r"""    \begin{columns}[c]
        \begin{column}{0.10\textwidth}
            \href{https://www.tuc.gr/}{\includegraphics[height=1.35cm,keepaspectratio]{tuc_logo.png}}
        \end{column}
        \begin{column}{0.88\textwidth}
            {\large \href{https://www.tuc.gr/}{\textbf{\color{tucblue}TECHNICAL UNIVERSITY OF CRETE}}}\\[0.18em]
            {\small \href{https://www.ece.tuc.gr/}{\color{tucgray}School of Electrical \& Computer Engineering}}
        \end{column}
    \end{columns}"""
    assert old_masthead in tex, "old_masthead not found"
    tex = tex.replace(old_masthead, new_masthead)

    # 3. Update final slide and repo url
    old_closing = r"""    Asterinos Karalis -- Technical University of Crete\\
    \vspace{0.5em}
    \small Open-Source Repository: \url{https://github.com/Asterinos1/FDA-LoRA}"""

    new_closing = r"""    Asterinos Karalis -- \href{https://www.tuc.gr/}{\textbf{\color{tucblue}Technical University of Crete}}\\[0.2em]
    \href{https://www.ece.tuc.gr/}{\small \color{tucgray}School of Electrical \& Computer Engineering}\\
    \vspace{0.5em}
    \small Open-Source Repository: \url{https://github.com/Asterinos1/FDA-RoLoRA}"""

    assert old_closing in tex, "old_closing not found"
    tex = tex.replace(old_closing, new_closing)

    with open(path_tex, "w", encoding="utf-8") as f:
        f.write(tex)

    print("Updated presentation.tex!")

    # Update PRESENTATION_SCRIPT.md
    path_script = "presentation/PRESENTATION_SCRIPT.md"
    with open(path_script, "r", encoding="utf-8") as f:
        script = f.read()

    script = script.replace(
        "https://github.com/Asterinos1/FDA-LoRA",
        "https://github.com/Asterinos1/FDA-RoLoRA"
    )

    with open(path_script, "w", encoding="utf-8") as f:
        f.write(script)

    print("Updated PRESENTATION_SCRIPT.md!")

if __name__ == "__main__":
    update_links()

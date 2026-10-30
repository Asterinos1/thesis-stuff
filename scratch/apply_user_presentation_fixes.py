import re

with open('presentation/presentation.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Slide 7 to height=2.05cm and scriptsize caption to eliminate the 3.4pt overfull vbox
old_slide_7 = """\\begin{frame}{Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)}
    \\framesubtitle{Chen et al., NeurIPS 2025 -- Alternating Coordinate Optimization}
    \\vspace{-0.3em}
    \\begin{block}{Alternating Coordinate Optimization Restores Aggregation Linearity}
        \\footnotesize
        \\textbf{RoLoRA} resolves the bilinear inconsistency by alternating the active trainable matrix while freezing the other globally across all clients:
        \\begin{itemize}
            \\item \\textbf{Odd Rounds (Train $B$, Freeze $A$)}:
            $\\frac{1}{N}\\sum_{i=1}^N (B_i A) = \\left(\\frac{1}{N}\\sum_{i=1}^N B_i\\right) A = \\bar{B} A$
            \\item \\textbf{Even Rounds (Train $A$, Freeze $B$)}:
            $\\frac{1}{N}\\sum_{i=1}^N (B A_i) = B \\left(\\frac{1}{N}\\sum_{i=1}^N A_i\\right) = B \\bar{A}$
            \\item \\textbf{Core Limitation}: Enforces a rigid, static local epoch schedule ($E$), leaving temporal synchronization completely unoptimized.
        \\end{itemize}
    \\end{block}
    \\vspace{0.15em}
    
    \\centering
    \\includegraphics[width=0.92\\textwidth,height=2.3cm,keepaspectratio]{figures/rolora_framework.png}\\\\[0.2em]
    {\\footnotesize \\textbf{Figure}: RoLoRA alternating framework across communication rounds.}
\\end{frame}"""

new_slide_7 = """\\begin{frame}{Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)}
    \\framesubtitle{Chen et al., NeurIPS 2025 -- Alternating Coordinate Optimization}
    \\vspace{-0.3em}
    \\begin{block}{Alternating Coordinate Optimization Restores Aggregation Linearity}
        \\footnotesize
        \\textbf{RoLoRA} resolves the bilinear inconsistency by alternating the active trainable matrix while freezing the other globally across all clients:
        \\begin{itemize}
            \\item \\textbf{Odd Rounds (Train $B$, Freeze $A$)}:
            $\\frac{1}{N}\\sum_{i=1}^N (B_i A) = \\left(\\frac{1}{N}\\sum_{i=1}^N B_i\\right) A = \\bar{B} A$
            \\item \\textbf{Even Rounds (Train $A$, Freeze $B$)}:
            $\\frac{1}{N}\\sum_{i=1}^N (B A_i) = B \\left(\\frac{1}{N}\\sum_{i=1}^N A_i\\right) = B \\bar{A}$
            \\item \\textbf{Core Limitation}: Enforces a rigid, static local epoch schedule ($E$), leaving temporal synchronization completely unoptimized.
        \\end{itemize}
    \\end{block}
    \\vspace{0.1em}
    
    \\centering
    \\includegraphics[width=0.90\\textwidth,height=2.0cm,keepaspectratio]{figures/rolora_framework.png}\\\\[0.15em]
    {\\scriptsize \\textbf{Figure}: RoLoRA alternating framework across communication rounds.}
\\end{frame}"""

has_crlf = '\r\n' in content
c_norm = content.replace('\r\n', '\n')
c_norm = c_norm.replace(old_slide_7.replace('\r\n', '\n'), new_slide_7.replace('\r\n', '\n'))
final_content = c_norm.replace('\n', '\r\n') if has_crlf else c_norm

with open('presentation/presentation.tex', 'w', encoding='utf-8', newline='') as f:
    f.write(final_content)

print("Slide 7 adjusted for 0 overfull.")

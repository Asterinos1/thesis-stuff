# Diploma Thesis & Presentation LaTeX Project Structure

This repository contains two main sub-projects: the diploma thesis document and its defense presentation.

## 📂 Directory Layout

```text
Thesis_STUFF/
├── thesis/                  # Thesis LaTeX project directory
│   ├── main.tex             # Main orchestrator (packages, metadata, title page, structure)
│   ├── references.bib       # BibTeX bibliography database
│   ├── build.bat            # Windows batch script for one-click thesis compilation
│   ├── watch.ps1            # PowerShell auto-compilation script
│   ├── tuc_logo.png         # School logo used on the title page
│   ├── figures/             # Directory to store all image assets (graphs, charts, diagrams)
│   └── chapters/            # Directory containing modular LaTeX files for each chapter
│       ├── abstract.tex
│       ├── acknowledgements.tex
│       ├── introduction.tex
│       ├── background.tex
│       ├── methodology.tex
│       ├── implementation.tex
│       ├── evaluation.tex
│       └── conclusion.tex
├── presentation/            # Defense presentation LaTeX project directory
│   ├── presentation.tex     # Beamer presentation source file
│   ├── tuc_logo.png         # Logo copy for slides title page
│   └── build.bat            # Windows batch script to compile slides
├── sources/                 # Reference literature PDFs
└── examples/                # Prior example PDFs from research group
```

---

## 🛠️ Instructions for Working with this Structure

### 1. Adding/Editing Chapters
Write the content in the respective files inside the `thesis/chapters/` folder. 
* To add a new chapter (e.g., `thesis/chapters/discussion.tex`):
  1. Create the file `thesis/chapters/discussion.tex`.
  2. In `thesis/main.tex`, insert it at the desired position using:
     ```latex
     \input{chapters/discussion}
     ```

### 2. Inserting Figures (Images & Graphs)
Place your images inside the `thesis/figures/` directory.
In your LaTeX chapters, reference them using:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/graph.png}
    \caption{Experimental Results.}
    \label{fig:results_graph}
\end{figure}
```

### 3. Adding Citations & Bibliography
Add your BibTeX reference entries into the `thesis/references.bib` file.
* To cite an entry in your text, use standard LaTeX command:
  ```latex
  \cite{cite_key}
  ```

### 4. Compiling the Document
* **Thesis**: Run `build.bat` inside the `thesis/` folder.
* **Presentation**: Run `build.bat` inside the `presentation/` folder.

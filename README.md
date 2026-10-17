# Thesis Stuff

This repository contains the complete research, writing, and presentation materials for the diploma thesis on Federated Learning parameter-efficient fine-tuning (FDA-LoRA / RoLoRA variants) at the Technical University of Crete (TUC).

Inside this repository you will find the modular LaTeX manuscript source files, presentation slides, experiment trajectory plots, literature sources, and reference materials.

---

## Windows 11 Prerequisites

To build and work on this repository on a Windows 11 machine, install the following software.

### 1. MiKTeX (LaTeX Distribution)

MiKTeX provides the TeX engine (`pdflatex`), bibliography processor (`bibtex`), and package management utilities required to compile the thesis manuscript and presentation slides.

1. Download the Windows installer from [miktex.org/download](https://miktex.org/download).
2. During installation, when prompted with **"Install missing packages on-the-fly"**, select **Yes** (not "Ask me first"). This setting ensures that required CTAN packages (such as `beamer`, `amsmath`, `hyperref`, `algorithm`, `algorithmicx`, and font packages) download automatically without blocking your builds with interactive confirmation dialogs.
3. Once installation completes, open **MiKTeX Console**, check for updates to ensure your package database is current, and verify that `pdflatex` is available in your PATH by running `pdflatex --version` in PowerShell or Windows Terminal.

### 2. Git for Windows

Git is required to clone, synchronize, and track changes across the project.

Download and install Git from [git-scm.com/download/win](https://git-scm.com/download/win). Use the default setup options, making sure Windows Credential Manager is enabled so your GitHub authentication persists smoothly.

### 3. Antigravity CLI (`agy`)

The workspace includes metadata, session journals, and semantic graphs managed by the Antigravity developer environment. If you want to use the agentic coding tools or regenerate knowledge graph representations:

1. Install the Antigravity CLI according to your organization's setup instructions.
2. Ensure `agy` is registered in your user environment PATH.
3. The root directory contains graphify artifacts in `graphify-out/` representing the structural relationships between thesis chapters, notes, and algorithms.

### 4. Recommended Editor and PDF Viewer

While you can edit LaTeX files in any text editor, the following combination offers a smooth authoring experience on Windows 11:

- **Visual Studio Code** with the **LaTeX Workshop** extension.
- **SumatraPDF**: Unlike Adobe Acrobat Reader, SumatraPDF does not lock open PDF files, allowing `pdflatex` to overwrite `main.pdf` or `presentation.pdf` while the viewer stays open with automatic live refresh.

---

## Repository Structure

The project files are organized into dedicated directories:

- **`thesis/`**: The complete thesis manuscript. The root document is `main.tex`, which imports individual sections from `chapters/` (such as introduction, background, methodology, implementation, evaluation, conclusion, and abbreviations). It also contains bibliography entries in `references.bib`, university assets like `tuc_logo.png`, and automated build scripts.
- **`presentation/`**: The Beamer slide presentation (`presentation.tex`), slide figures, and its standalone build script.
- **`figures/`**: High-resolution PNG and JSON experiment outputs, including toy problem convergence trajectories, accuracy vs. rounds comparisons, and parameter efficiency plots.
- **`sources/`**: Curated PDF literature and core papers on LoRA, RoLoRA, FFA-LoRA, and Federated Learning survey papers used during research.
- **`examples/`**: Past diploma thesis PDFs from TUC used as structural references for formatting, table layout, and styling.
- **`scratch/`**: Work-in-progress drafts, layout review snapshots, page proof checks, and committee feedback logs.
- **`graphify-out/`**: Pre-rendered knowledge graph files (`graph.html`, `graph.json`, `GRAPH_REPORT.md`) summarizing the document hierarchy and cross-references.

---

## How to Build the Documents

All compilation steps can be executed through convenient batch scripts or directly from the command line.

### Compiling the Thesis

To produce `thesis/main.pdf`:

Open File Explorer, navigate to the `thesis` directory, and double-click `build.bat`.

Alternatively, run the following commands from PowerShell:

```powershell
cd thesis
.\build.bat
```

The build script automatically runs `pdflatex` followed by `bibtex` and two additional `pdflatex` passes. This multi-pass sequence guarantees that all chapter cross-references, citation numbers, list of figures, and table of contents entries resolve accurately.

### Continuous Live Recompilation

If you are actively writing chapters, you can use the included PowerShell watcher to automatically recompile `main.pdf` whenever any `.tex` file is saved:

```powershell
cd thesis
powershell -ExecutionPolicy Bypass -File .\watch.ps1
```

The watcher monitors all `.tex` files across the workspace. When a change is detected, it runs a fast single-pass `pdflatex` compilation and notifies you in the terminal. When you are done editing, press `Ctrl + C` to stop the watcher.

### Compiling the Presentation

To produce `presentation/presentation.pdf`:

Navigate to the `presentation` folder and double-click `build.bat`, or execute:

```powershell
cd presentation
.\build.bat
```

This runs two `pdflatex` passes on `presentation.tex` to resolve Beamer navigation frames, slide counters, and table of contents entries.

---

## Helpful Tips & Troubleshooting

- **PDF File Locked Error**: If `pdflatex` fails with a permission error stating that the output file cannot be written, check if `main.pdf` is open in Adobe Acrobat or another locking viewer. Close the document or switch to SumatraPDF.
- **Missing Packages**: If MiKTeX prompts for package installation, grant permission or ensure that automatic package installation is set to "Yes" inside the MiKTeX Console settings tab.
- **PowerShell Script Execution**: If Windows blocks `watch.ps1` due to execution policy restrictions, open PowerShell as an administrator once and run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, or pass `-ExecutionPolicy Bypass` when calling the script.

# Formula Editor

This repository contains a minimal interactive formula editor built with Flask and MathJax.

## Features

- Real-time rendering of LaTeX expressions as you type
- Simple web interface with an input area and preview pane

## Requirements

- Python 3.8+
- `flask` Python package

Install dependencies using:

```bash
pip install flask
```

## Running the editor

Run the interactive editor module directly:

```bash
python -m formula_editor.interactive_editor
```

Then open your browser at [http://localhost:5000](http://localhost:5000) to use the editor.

Type LaTeX code in the text area and the rendered formula will appear in the preview pane automatically.

## Running tests

The project includes a small test suite. Run the tests using the bundled pytest
stub:

```bash
python -m pytest -q
```

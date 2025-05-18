# Formula Editor

This repository contains a minimal interactive formula editor that uses a tiny
Flask-compatible web server bundled in the project. MathJax handles the LaTeX
rendering on the client side.

## Features

- Real-time rendering of LaTeX expressions as you type
- Simple web interface with an input area and preview pane

## Requirements

- Python 3.8+

No external packages are required because a lightweight Flask stub is included.

## Running the editor

Run the interactive editor module directly:

```bash
python -m formula_editor.interactive_editor
```

Then open your browser at [http://localhost:5000](http://localhost:5000) to use the editor.

1. Optionally pick one of the built-in example formulas from the drop-down list.
2. Edit the LaTeX expression in the text area.
3. The preview pane updates automatically to show the rendered result.

Use this page to experiment with common formulas or input your own expressions.

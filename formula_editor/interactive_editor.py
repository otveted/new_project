from flask import Flask, render_template_string

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Formula Editor</title>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    #input { width: 100%; height: 100px; }
    #preview { border: 1px solid #ccc; padding: 10px; margin-top: 20px; min-height: 100px; }
  </style>
</head>
<body>
  <h1>Interactive Formula Editor</h1>
  <textarea id="input" placeholder="Type LaTeX here"></textarea>
  <div id="preview"></div>
<script>
  const input = document.getElementById('input');
  const preview = document.getElementById('preview');
  function update() {
    preview.innerHTML = '\\(' + input.value + '\\)';
    MathJax.typesetPromise([preview]);
  }
  input.addEventListener('input', update);
  update();
</script>
</body>
</html>
'''

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template_string(HTML_TEMPLATE)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

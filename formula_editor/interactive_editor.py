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
    #input { width: 100%; height: 100px; margin-top: 10px; }
    #preview { border: 1px solid #ccc; padding: 10px; margin-top: 20px; min-height: 100px; }
    #examples { width: 100%; }
  </style>
</head>
<body>
  <h1>Interactive Formula Editor</h1>
  <label for="examples">Example formulas:</label>
  <select id="examples">
    <option value="">-- choose an example --</option>
    <option value="ax^2 + bx + c = 0">Quadratic equation</option>
    <option value="e^{i\\pi} + 1 = 0">Euler's identity</option>
    <option value="(a + b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k} b^k">Binomial theorem</option>
    <option value="a^2 + b^2 = c^2">Pythagorean theorem</option>
    <option value="\\frac{d}{dx} x^n = n x^{n-1}">Power rule</option>
  </select>
  <textarea id="input" placeholder="Type LaTeX here"></textarea>
  <div id="preview"></div>
<script>
  const input = document.getElementById('input');
  const preview = document.getElementById('preview');
  const examples = document.getElementById('examples');

  function update() {
    preview.innerHTML = '\\(' + input.value + '\\)';
    MathJax.typesetPromise([preview]);
  }

  input.addEventListener('input', update);
  examples.addEventListener('change', () => {
    if (examples.value) {
      input.value = examples.value;
      update();
    }
  });

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

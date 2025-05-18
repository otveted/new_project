import unittest
import types

from formula_editor import interactive_editor

class TestInteractiveEditor(unittest.TestCase):
    def test_html_contains_preview(self):
        self.assertIn('id="preview"', interactive_editor.HTML_TEMPLATE)

    def test_create_app_callable(self):
        app = interactive_editor.create_app()
        self.assertTrue(hasattr(app, 'run'))
        self.assertIsInstance(app, interactive_editor.Flask)

if __name__ == '__main__':
    unittest.main()

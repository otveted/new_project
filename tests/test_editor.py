import unittest
import sys
import types

# Create a stub Flask module for environments without flask installed
class FakeResponse:
    def __init__(self, data='', status=200):
        self.data = data.encode('utf-8') if isinstance(data, str) else data
        self.status_code = status

class FakeFlask:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def test_client(self):
        app = self
        class Client:
            def get(self, path):
                if path not in app.routes:
                    return FakeResponse(status=404)
                result = app.routes[path]()
                return FakeResponse(result)
        return Client()

# only patch flask if not installed
try:
    import flask  # noqa: F401
except ImportError:  # pragma: no cover
    flask_stub = types.SimpleNamespace(
        Flask=FakeFlask,
        render_template_string=lambda x: x,
    )
    sys.modules['flask'] = flask_stub

from formula_editor.interactive_editor import create_app

class EditorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Interactive Formula Editor', response.data)

if __name__ == '__main__':
    unittest.main()

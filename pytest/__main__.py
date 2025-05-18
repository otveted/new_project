import sys
import unittest

if __name__ == "__main__":
    verbosity = 2
    if '-q' in sys.argv:
        verbosity = 1
        sys.argv.remove('-q')
    tests = unittest.defaultTestLoader.discover('tests')
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(tests)
    sys.exit(not result.wasSuccessful())

import unittest
import requests
import subprocess

class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(200, requests.codes.ok)

    def test_pyenv_version(self):
        # Ensure that the pyenv version is pinned, not latest
        result = subprocess.run([".pyenv/bin/pyenv", "--version"], stdout=subprocess.PIPE, text=True, check=True)
        self.assertTrue(result.stdout.startswith("pyenv 2.4.23"), result)

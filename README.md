# Python.pyenv

[![Build and Test](https://github.com/build-and-test/Python.pyenv/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/build-and-test/Python.pyenv/actions/workflows/build-and-test.yml?query=branch%3Amain)

# Advantages

- Python version is pinned
- Local development doesn't require pre-installed Python - great for a clean machine
- CI doesn't install Python either

# Limitations

- Pyenv version is not pinned
- Python is installed to a shared cache, so anyone can leave cruft in it
- The build-and-test script is too long; pyenv should do more of this work for me
- Mac/Linux only, no Windows
- Requires Bash
- No natural place to make additional tasks, like update_dependencies

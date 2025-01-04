# Python

Edit `.python_version`.

# Python modules

Automatically updated by dependabot. Or manually:

```bash
pip uninstall -y $(pip freeze) || true
pip install --requirement requirements.dev.in pip-tools  # warning: unpinned dependency
# Consider --allow-unsafe and --generate-hashes
pip-compile --upgrade --strip-extras --newline LF --quiet --output-file=requirements.txt requirements.in
pip-compile --upgrade --strip-extras --newline LF --quiet --output-file=requirements.dev.txt requirements.dev.in
```

# GitHub Actions

Automatically updated by dependabot.

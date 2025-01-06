# Python

Edit `.python_version`.

# Python modules

Automatically updated by dependabot. Or manually, run `build-and-test` once to bootstrap pyenv and then:

```bash
.pyenv/bin/pyenv exec pip install --requirement requirements.dev.in pip-tools  # warning: unpinned dependency
# Consider --allow-unsafe and --generate-hashes
.pyenv/bin/pyenv exec pip-compile --upgrade --strip-extras --newline LF --quiet --output-file=requirements.txt requirements.in
.pyenv/bin/pyenv exec pip-compile --upgrade --strip-extras --newline LF --quiet --output-file=requirements.dev.txt requirements.dev.in
```

# Pyenv

Edit `build-and-test` to set `PYENV_GIT_TAG`.

# GitHub Actions

Automatically updated by dependabot.

# Installation

### In order to build the package locally run the next commands.

Uninstall local package
```
python3 -m pip uninstall opensubtitles_downloader
```

Build wheel package
```
python3 setup.py sdist bdist_wheel
```

Install the package locally
```
python3 -m pip install --user dist/opensubtitles_downloader-0.1-py3-none-any.whl
```

#### Pip Test repo
Upload to Pip Test
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Install from Pip Test
```
python3 -m pip install --user --index-url https://test.pypi.org/simple/ opensubtitles_downloader
```

#### Pip repo (stable)
Upload to Pip
```
twine upload dist/*
```

Install from Pip
```
pip3 install --user opensubtitles_downloader
```

Upgrade
```
pip3 install --user --upgrade opensubtitles_downloader
```
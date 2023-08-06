# zn
Zinc

## Development Environment

### Setup
Follow these steps to create a development environment for Zinc:

    cd ~/projects
    git clone git@github.com:blinkdog/zn.git
    cd zn
    python3.7 -m venv ./env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

### Maintenance
If you install a new package using `pip install` then update the
`requirements.txt` file with the following command:

    pip freeze --all >requirements.txt

### Working
The helper script `snake` defines some common project tasks:

    Try one of the following tasks:

    snake clean                # Remove build cruft
    snake coverage             # Perform coverage analysis
    snake dist                 # Create a distribution tarball and wheel
    snake lint                 # Run static analysis tools
    snake publish              # Publish the module to Test PyPI
    snake rebuild              # Test and lint the module
    snake test                 # Test the module

The task `rebuild` doesn't really build (no need to compile Python),
but it does run the unit tests and lint the project.

#### Version Bumping
If you need to increase the version number of the project, don't
forget to edit the following:

    CHANGELOG.md
    setup.py

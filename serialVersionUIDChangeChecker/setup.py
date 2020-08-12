import setuptools


setuptools.setup(
    name="serialVersionUIDChangeChecker",
    version="0.1.0",
    author="Exasol",
    description="pre-commit plugin that shows a warning if a file was changed but serialVersionUID was not",
    url="https://github.com/jakobbraun/serialVersionUIDChangeChecker",
    packages=["serialVersionUIDChangeChecker"],
    entry_points = {
        "console_scripts": [
            "serialVersionUIDChangeChecker = serialVersionUIDChangeChecker.__main__:main",
        ]
    },
    python_requires='>=3.6',
) 

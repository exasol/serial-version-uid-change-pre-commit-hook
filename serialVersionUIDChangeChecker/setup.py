import setuptools


setuptools.setup(
    name="serialVersionUIDChangeChecker",
    version="0.1.1",
    author="Jakob Braun",
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

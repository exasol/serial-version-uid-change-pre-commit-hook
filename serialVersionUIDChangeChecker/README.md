# SerialVersionUID Change Checker

This [pre-commit](https://pre-commit.com/) checks requires the serialVersionUID to be changed if the containing file was changed.
If a change is not required, simply add or remove an empty comment in the line of the serialVersionUID.

## Setup

Add the following lines to your `.pre-commit-config.yaml`:
```yaml
  - repo: https://github.com/exasol/exasol-pre-commit-hooks
    rev: master
    hooks:
      - id: serial-version-uid
```

## Limitations

This script does only check on a file system level. Accordingly it does may produce false positives in case a single file contains multiple classes (e.g a nested Exception class). 

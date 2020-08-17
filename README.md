# SerialVersionUID Change Pre-commit Hook

This [pre-commit](https://pre-commit.com/) hook requires the serialVersionUID to be changed if the containing file was changed.
If a change is not required, simply add or remove an empty comment in the line of the serialVersionUID.

## Setup

1. [install pre-commit](https://pre-commit.com/#installation) on your machine
1. Add the following lines to your `.pre-commit-config.yaml` (if not already present):
    ```yaml
      - repo: https://github.com/exasol/serial-version-uid-change-pre-commit-hook
        rev: master
        hooks:
          - id: serial-version-uid
    ```
 1. Install the hooks using:
     ``` shell script
    pre-commit install
    ``` 
 1. Now `git commit` will fail if a check does not pass.
    You can also run the checks manual by executing `pre-commit`.   

## Limitations

This script does only check on a file system level. Accordingly, it may produce false positives in case a single file contains multiple classes (e.g a nested Exception class). 

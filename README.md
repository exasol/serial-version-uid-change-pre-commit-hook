# Pre-commit Hooks

This repository contains [pre-commit](https://pre-commit.com/) hooks developed for Exasol projects.
Each hook defines a check that pre-commit automatically installs and runs before each commit.

## Available Hooks

 * [SerialVersionUID change checker](serialVersionUIDChangeChecker/README.md)
 
 Checkout the [pre-commit website](https://pre-commit.com/hooks.html) for a list of other pre-commit hooks.
 
## How to Use
 
 You can define which hooks pre-commit should use for a specific project using a `.pre-commit-config.yaml` 
 file in the projects root directory.
 For more details see the [pre-commit quickstart guide](https://pre-commit.com/#quick-start).
Usually you also commit this file into the projects git repository.
 Hence for the existing projects the file may already exist.
 
 Next [install pre-commit](https://pre-commit.com/#installation) on your machine.
 
 Then you can install the hooks by running:
 
 ``` shell script
pre-commit install
``` 

Now `git commit` will fail if a check does not pass.
You can also run the checks manual by executing `pre-commit`.

  
 
 

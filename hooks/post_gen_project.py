#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DATA_README = """# Local Data Directory

Use this directory to keep data sources that you might reference as part
of your project, but don't want to version control.  Typical examples might
be a set of documents, csv files, or outputs of analyses.
"""

def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    # create data directory and readme
    # we do it here because we explicitly git ignore the data directory
    os.mkdir(os.path.join(PROJECT_DIRECTORY, "data"))
    with open(os.path.join(PROJECT_DIRECTORY, "data", "README.md"), "w") as f:
        f.write(DATA_README)


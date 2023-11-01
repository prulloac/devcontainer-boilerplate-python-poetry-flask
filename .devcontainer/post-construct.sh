#!/bin/zsh
pip install --upgrade pip
pipx install poetry
poetry config virtualenvs.in-project true
poetry install

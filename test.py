#!/usr/bin/env python3
import importlib_metadata
plugins = importlib_metadata.entry_points(group='mkdocs.plugins')

for p in plugins:
  print(p)
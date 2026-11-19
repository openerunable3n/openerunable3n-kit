"""Command line entry point for openerunable3n_kit."""
import argparse

from .core import Openerunable3nTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="organize files by type")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    sorter = Openerunable3nTool(args.path)
    if args.dry_run:
        for name, folder in sorter.plan():
            print(f"{name} -> {folder}/")
        return 0
    for name, folder in sorter.apply():
        print(f"{name} -> {folder}/")
    return 0

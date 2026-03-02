"""Command-line interface for python-cli-example."""

from __future__ import annotations

import argparse
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="python-cli-example — A sample CLI tool.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "input_file",
        help="Path to the input file to process",
    )
    return parser.parse_args(argv)


def main() -> int:
    """Main entry point."""
    args = parse_args()
    if args.verbose:
        print(f"Processing: {args.input_file}")
    # TODO: implement core logic
    print(f"Done: {args.input_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

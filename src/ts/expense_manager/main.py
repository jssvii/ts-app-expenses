"""
Expense Manager application
"""

import argparse
import os
import sys


def main():
    """Entry point to the Expense Manager app"""

    parser = argparse.ArgumentParser(
        description="Launch the PySide Expense Manager application",
        usage="ts_expman",
    )
    args = parser.parse_args()

    try:
        print(f"Running with args: {args}")
        return 1
    except KeyboardInterrupt:
        print("The application was terminated...")
        sys.exit(1)
    except Exception as error:
        print(f"Something went wrong: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()

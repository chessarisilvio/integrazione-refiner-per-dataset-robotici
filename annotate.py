#!/usr/bin/env python3
"""
annotate.py
Simple annotation script: adds a placeholder annotation column.

Usage:
    python3 annotate.py --input input.csv --output output.csv
"""
import argparse
import pandas as pd
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Add annotation column to CSV")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV file")
    parser.add_argument("--output", "-o", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        sys.exit(f"Error: Input file '{args.input}' not found.")

    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        sys.exit(f"Error reading CSV file: {e}")

    # Add a placeholder annotation column
    df['annotation'] = 'pending'

    try:
        df.to_csv(args.output, index=False)
    except Exception as e:
        sys.exit(f"Error writing CSV file: {e}")

    print(f"Successfully annotated '{args.input}' -> '{args.output}' ({len(df)} rows)")

if __name__ == "__main__":
    main()
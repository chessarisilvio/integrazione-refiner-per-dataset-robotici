#!/usr/bin/env python3
"""
import_parquet.py
Import a Parquet file and save it as CSV.

Usage:
    python3 import_parquet.py --input input.parquet --output output.csv
"""
import argparse
import pandas as pd
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Convert Parquet to CSV")
    parser.add_argument("--input", "-i", required=True, help="Path to input Parquet file")
    parser.add_argument("--output", "-o", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        sys.exit(f"Error: Input file '{args.input}' not found.")

    try:
        df = pd.read_parquet(args.input)
    except Exception as e:
        sys.exit(f"Error reading Parquet file: {e}")

    try:
        df.to_csv(args.output, index=False)
    except Exception as e:
        sys.exit(f"Error writing CSV file: {e}")

    print(f"Successfully converted '{args.input}' to '{args.output}' ({len(df)} rows)")

if __name__ == "__main__":
    main()
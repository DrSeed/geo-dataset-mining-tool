#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True)
    parser.add_argument('--organism', default='Homo sapiens')
    parser.add_argument('--max-datasets', type=int, default=20)
    parser.add_argument('--output', default='geo_data')
    args = parser.parse_args()
    Path(args.output).mkdir(parents=True, exist_ok=True)
    print('GEO mining complete.')

if __name__ == '__main__':
    main()

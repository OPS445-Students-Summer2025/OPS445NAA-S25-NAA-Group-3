#!/usr/bin/env python3

import argparse
from diskreport import get_disk_usage  # assuming your function is in diskreport.py

def main():
    parser = argparse.ArgumentParser(description="System Reports and Metrics")

    parser.add_argument('--disk', action='store_true', help='Show disk usage report')
    
    args = parser.parse_args()

    if args.disk:
        results = get_disk_usage()
        for line in results:
            print(line)

if __name__ == "__main__":
    main()

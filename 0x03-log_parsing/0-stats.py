#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys


def print_metric(stats, filesize):
    """Print file size and number of status codes"""
    print("File size: {}".format(filesize))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


line_count = 0
total_file_size = 0
status_code_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            list = line.split()
            try:
                file_size = int(list[-1])
                total_file_size += file_size
                status_code = list[-2]
                if status_code in status_code_dict:
                    status_code_dict[status_code] += 1
            except Exception:
                pass

            if line_count % 10 == 0:
                print_metric(status_code_dict, total_file_size)
        print_metric(status_code_dict, total_file_size)
    except KeyboardInterrupt:
        print_metric(status_code_dict, total_file_size)
        raise

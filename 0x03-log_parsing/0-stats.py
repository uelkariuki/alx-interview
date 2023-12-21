#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_count = {code: 0 for code in status_codes}
line_count = 0
total_size = 0

try:
    for line in sys.stdin:
        try:
            line_count = line_count + 1
            data = line.split()  # default is split by space
            try:
                status_code = int(data[-2])
                if status_code in status_codes:
                    status_code_count[status_code] += 1
            except (ValueError, IndexError):
                pass
            try:
                file_size = int(data[-1])
                total_size += file_size
            except (ValueError, IndexError):
                pass
            if line_count % 10 == 0:
                print(f'File Size: {total_size}')
                for code in sorted(status_code_count.keys()):
                    if status_code_count[code] > 0:
                        print(f'{code}:{status_code_count[code]}')
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    pass
finally:
    print(f'File Size: {total_size}')
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f'{code}:{status_code_count[code]}')

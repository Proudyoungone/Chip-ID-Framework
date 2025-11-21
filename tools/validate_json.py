import json
import sys
from pathlib import Path

p = Path(r"c:\Users\AFT 24-05\Desktop\Chip_ID_Framework-master\public\arf.json")
try:
    with p.open('r', encoding='utf-8') as f:
        json.load(f)
    print('OK: JSON parsed successfully')
    sys.exit(0)
except json.JSONDecodeError as e:
    print('JSONDecodeError:')
    print(f'  msg: {e.msg}')
    print(f'  line: {e.lineno} col: {e.colno} pos: {e.pos}')
    # print surrounding context
    try:
        text = p.read_text(encoding='utf-8')
        lines = text.splitlines()
        L = e.lineno
        start = max(0, L-3)
        end = min(len(lines), L+2)
        print('Context:')
        for i in range(start, end):
            prefix = '>' if i+1==L else ' '
            print(f"{prefix} {i+1:6d}: {lines[i]}")
    except Exception as ex:
        print('Could not read context:', ex)
    sys.exit(2)
except Exception as ex:
    print('Other error:', ex)
    sys.exit(3)

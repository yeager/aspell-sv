#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--local', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
base = ['aspell', '--lang=sv', '--encoding=utf-8', '--per-conf=/dev/null']
if args.local:
    directory = args.local.resolve()
    base += ['--local-data-dir='+str(directory), '--dict-dir='+str(directory), '--master=sv.rws']
vocabulary = json.loads((root/'tests/vocabulary.json').read_text())
words = vocabulary['positive'] + vocabulary['negative']
result = subprocess.run(base+['list'], input='\n'.join(words)+'\n', text=True, capture_output=True, check=True)
assert not result.stderr, result.stderr
assert set(result.stdout.splitlines()) == set(vocabulary['negative']), result.stdout
expected = set((root/'sv.wl').read_text().splitlines())
dump = subprocess.run(base+['dump','master'], text=True, capture_output=True, check=True)
assert set(dump.stdout.splitlines()) == expected
print(f'PASS: {len(vocabulary["positive"])} positive, {len(vocabulary["negative"])} negative; {len(expected)} compiled forms')

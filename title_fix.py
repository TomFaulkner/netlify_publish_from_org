#!/usr/bin/env python3

from glob import glob
from shutil import copyfile


def run():
    for file in glob('*.org'):
        if 'backup' in file:
            continue
        copyfile(file, f"{file}.backup")
        with open(file) as f:
            contents = f.read()
            title_line = contents.splitlines()[0]
            if '#+TITLE' not in title_line:
                print(f"{file} lacks a title.")
                continue
            title = title_line.replace('_', ' ')
            body = contents.splitlines()[1:]
            full_contents = '\n'.join([title] + body)
            with open(file, 'w') as w:
                w.write(full_contents)

if __name__ == '__main__':
    run()

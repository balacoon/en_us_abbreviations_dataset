
import sys
import re


def adjust_abbreviation(abbr):
    # check that it contains only large letters, dots
    # long enough
    abbr = abbr.replace('.', '')
    if abbr.endswith('\'S'):
        abbr = abbr[:-2]
    if len(abbr) <= 1:
        return None
    # just capital letters
    if not re.match('^[A-Z]+$', abbr):
        return None 
    return abbr


def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip()
            m = re.search(sys.argv[2], line)
            if not m or len(m.groups()) < 1:
                continue
            abbr = m.group(1)
            abbr = adjust_abbreviation(abbr)
            if abbr is None:
                continue
            print(abbr)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise RuntimeError('Usage: <html file> <regex>')
    main()


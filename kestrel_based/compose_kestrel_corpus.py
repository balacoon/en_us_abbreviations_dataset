import sys, os
import glob
import re
import argparse
import logging


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dataset-dir', required=True)
    ap.add_argument('--out-abbreviations', required=True)
    ap.add_argument('--out-words', required=True)
    args = ap.parse_args()
    return args


def store(path, d):
    with open(path, 'w') as fp:
        for x in sorted(list(d.keys())):
            fp.write('{} {}\n'.format(x, d[x]))


def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_args()
    words = dict()
    abbreviations = dict()
    for path in glob.glob(os.path.join(args.dataset_dir, "output-000*-of-00100")):
        with open(path, 'r', encoding='utf-8') as fp:
            logging.info('Reading {}'.format(path))
            lines_num = 0
            for line in fp:
                line = line.strip()
                semiotic_class, word = line.split('\t', 1)
                word = word.split('\t')[0].upper()
                if re.match(r'^[A-Z]+$', word):
                    if semiotic_class == 'LETTERS':
                        abbreviations[word] = abbreviations.get(word, 0) + 1
                    elif semiotic_class == 'PLAIN':
                        words[word] = words.get(word, 0) + 1
                lines_num += 1
                if lines_num % 1000000 == 0:
                    logging.info('.')

    store(args.out_abbreviations, abbreviations)
    store(args.out_words, words)


if __name__ == '__main__':
    main()

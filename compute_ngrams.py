

import os
import sys
import argparse
import numpy as np


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--abbreviations', required=True)
    ap.add_argument('--words', required=True)
    ap.add_argument('--n', type=int, default=2)
    ap.add_argument('--report', required=True)
    args = ap.parse_args()
    return args



def compute_ngrams(path, n):

    ngrams = dict()

    with open(path, 'r', encoding='utf-8') as fp:
        for line in fp:
            chars = line.strip().split()[0].upper()
            chars = '^' + chars + '$'
            for i in range(0, len(chars) - n + 1):
                gram = chars[i:(i + n)]
                ngrams[gram] = ngrams.get(gram, 0) + 1

    # normalize frequency by mean frequency
    mean_freq = np.mean(np.array([x[1] for x in ngrams.items()]))
    ngrams = {k: v / mean_freq for k, v in ngrams.items()}

    return ngrams



def main():
    args = parse_args()
    abbr_ngrams = compute_ngrams(args.abbreviations, args.n)
    word_ngrams = compute_ngrams(args.words, args.n)

    merged_ngrams = dict()
    for gram in abbr_ngrams:
        freq_in_words = word_ngrams.get(gram, 0)
        merged_ngrams[gram] = (freq_in_words, abbr_ngrams[gram])

    # first sort by frequency of ngram in abbreviations in reverse order
    # more frequent ngrams are on top
    ngrams = sorted(merged_ngrams.items(), key=lambda item: item[1][1], reverse=True)

    # then sort by frequency of ngrams in words.
    # least frequent are on top
    ngrams = sorted(ngrams, key=lambda item: item[1][0])

    with open(args.report, 'w') as fp:
        for gram, (word_freq, abbr_freq) in ngrams:
            fp.write('{} {} {}\n'.format(gram, word_freq, abbr_freq))



if __name__ == '__main__':
    main()

import argparse
import pandas as pd

def create_ngrams(word, n):

    # Break word into tokens
    tokens = [token for token in word]

    # generate ngram using zip
    ngrams = zip(*[tokens[i:] for i in range(n)])

    # concat with empty space & return
    return [''.join(ngram) for ngram in ngrams]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert Japanese text to romaji.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'textfile',
        help='Japanese text to convert.'
    )

    parser.add_argument(
        '-n',
        help='n',
        type=int,
        default=2
    )
    

    args = parser.parse_args()
    textfile = args.textfile
    n = args.n
    text = open(textfile, 'r').read()

    bigram = create_ngrams(text, n)

    pd.set_option("display.max_rows", None)
    result = pd.Series(bigram).value_counts()
    print(result)
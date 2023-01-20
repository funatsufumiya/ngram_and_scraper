import argparse

parser = argparse.ArgumentParser(
    description='Convert large 2 small',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    'textfile',
    help='Japanese text to convert.'
)

args = parser.parse_args()
textfile = args.textfile

text = open(textfile, 'r').read()
# text = "これは日本語分かち書きのテストになります。"

result = text.lower()
print(result)
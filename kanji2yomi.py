import pykakasi
import argparse

parser = argparse.ArgumentParser(
    description='Convert Japanese text to romaji.',
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

kakasi = pykakasi.kakasi()

# モードの設定
kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
kakasi.setMode("r","Passport") # default: use Hepburn Roman table

conv = kakasi.getConverter()
result = conv.do(text)
print(result)
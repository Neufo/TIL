import glob

# https://docs.python.org/ja/3/library/glob.html

# ' 再帰的に検索する場合のパス指定(例) ./**/*.py
paths = glob.glob('*.py', recursive=True)

print(paths)

import json, sys

src = sys.argv[1]
dst = sys.argv[2]
with open(src, encoding='utf-8') as f:
    data = json.load(f)
text = data[0]['text']
with open(dst, 'w', encoding='utf-8') as f:
    f.write(text)
print(len(text))

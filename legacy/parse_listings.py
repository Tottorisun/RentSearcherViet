import re, sys, json

def parse_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')
    results = []
    i = 0
    link_re = re.compile(r'^\s*link "(.*)" \[ref_\d+\] href="([^"]*-pr\d+)"')
    while i < len(lines):
        m = link_re.match(lines[i])
        if m:
            title = m.group(1)
            href = m.group(2)
            # look ahead up to 6 lines for heading/generic price/area/district
            price = area = district = ''
            j = i + 1
            extras = []
            while j < len(lines) and j < i + 8:
                line = lines[j]
                # stop if next top-level link starts (indentation same or less, starts with 'link ' or other top tag not indented under this one)
                stripped = line.strip()
                if stripped.startswith('link "') and 'href=' in stripped and j != i:
                    break
                if stripped.startswith('generic "'):
                    gm = re.match(r'generic "([^"]*)"', stripped)
                    if gm:
                        extras.append(gm.group(1))
                j += 1
            results.append({'title': title, 'href': href, 'extras': extras})
            i = j
        else:
            i += 1
    return results

if __name__ == '__main__':
    path = sys.argv[1]
    outpath = sys.argv[2] if len(sys.argv) > 2 else path + '.out.txt'
    res = parse_file(path)
    with open(outpath, 'w', encoding='utf-8') as f:
        for r in res:
            f.write(f"{r['title']} | {r['extras']} | {r['href']}\n")
        f.write(f"TOTAL: {len(res)}\n")
    print('wrote', outpath, 'count', len(res))

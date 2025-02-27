txts = [
    'subdomains-from-fofa_1year_export.txt',
    'subdomains-from-zhubai_wiki.txt',
    'subdomains-from-arkiver.txt',
    'subdomains-from-exorcism.txt',
]
export_to = 'subdomains-deduped.urls.txt'

line_loaded = 0
sub_set = set()
for txt in txts:
    with open(txt) as f:
        for line in f:
            line_loaded += 1
            sub_set.add(line.strip())
print(len(sub_set), "found", "from", line_loaded, "lines")

with open(export_to, "w") as f:
    for sub in sorted(sub_set):
        f.write("https://" + sub + "\n")
print("Exported to", export_to)
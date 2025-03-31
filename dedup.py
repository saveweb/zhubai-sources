txts = [
    'subdomains-from-fofa_1year_export.txt',
    'subdomains-from-zhubai_wiki.txt',
    'subdomains-from-arkiver.txt',
    'subdomains-from-exorcism.txt',
    'subdomains-from-baidu.txt',
    'subdomains-from-haosou.txt',
    'subdomains-from-threads.txt',
    'subdomains-from-ecosia.txt',
]
export_to = 'subdomains-deduped.urls.txt'

line_loaded = 0
sub_set = set()

for txt in txts:
    with open(txt) as f:
        for line in f:
            line_loaded += 1
            # Nettoyage de la ligne
            cleaned = line.strip()
            cleaned = cleaned.replace("https://", "").replace("http://", "")  # Enlève les protocoles
            cleaned = cleaned.rstrip("/")  # Enlève le slash final
            sub_set.add(cleaned)

print(f"{len(sub_set)} sous-domaines uniques trouvés sur {line_loaded} lignes lues")

with open(export_to, "w") as f:
    for sub in sorted(sub_set):
        f.write(f"https://{sub}\n")  # Reconstruction propre de l'URL

print(f"Exporté vers {export_to}")
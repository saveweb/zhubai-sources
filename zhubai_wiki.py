from typing import TypedDict
import requests

class PostData(TypedDict):
    pu: str # https://open.zhubai.wiki/a/l/t/z/pl/yzhu1015/2506548629855879168

class CreatorData(TypedDict):
    zu: str # https://open.zhubai.wiki/a/l/t/z/al/offbeat/1894938101902192653

class PostResponse(TypedDict):
    code: str
    data: list[PostData]

class CreatorResponse(TypedDict):
    code: str
    data: list[CreatorData]

ss = requests.Session()

def tosub(pu: str) -> str:
    parts = pu.split("/")
    assert parts[-1].isdigit()
    return parts[-2]

def hip():
    URL = "https://open.zhubai.wiki/a/zb/s/pl/hip"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: PostResponse = r.json()
    assert r_data["code"] == "200"
    for post in r_data["data"]:
        yield tosub(post["pu"])

def hia():
    URL = "https://open.zhubai.wiki/a/zb/s/al/hia"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: CreatorResponse = r.json()
    assert r_data["code"] == "200"
    for creator in r_data["data"]:
        yield tosub(creator["zu"])

def nep():
    URL = "https://open.zhubai.wiki/a/zb/s/pl/nep"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: PostResponse = r.json()
    assert r_data["code"] == "200"
    for post in r_data["data"]:
        yield tosub(post["pu"])

def nea():
    URL = "https://open.zhubai.wiki/a/zb/s/al/nea"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: CreatorResponse = r.json()
    assert r_data["code"] == "200"
    for creator in r_data["data"]:
        yield tosub(creator["zu"])

def dua():
    URL = "https://open.zhubai.wiki/a/zb/s/al/dua"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: CreatorResponse = r.json()
    assert r_data["code"] == "200"
    for creator in r_data["data"]:
        yield tosub(creator["zu"])

def wua():
    URL = "https://open.zhubai.wiki/a/zb/s/al/wua"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: CreatorResponse = r.json()
    assert r_data["code"] == "200"
    for creator in r_data["data"]:
        yield tosub(creator["zu"])

def nra():
    URL = "https://open.zhubai.wiki/a/zb/s/al/nra"
    r = ss.post(URL)
    r.raise_for_status()
    r_data: CreatorResponse = r.json()
    assert r_data["code"] == "200"
    for creator in r_data["data"]:
        yield tosub(creator["zu"])

funcs = [
    hip,
    hia,
    nep,
    nea,
    dua,
    wua,
    nra
]


def main():
    sub_set = set()
    for func in funcs:
        print("calling", func.__name__)
        for sub in func():
            sub_set.add(sub)
    print(len(sub_set), "found")

    with open("subdomains-from-zhubai_wiki.txt", "w") as f:
        for sub in sorted(sub_set):
            f.write(sub + ".zhubai.love\n")
    

if __name__ == "__main__":
    main()

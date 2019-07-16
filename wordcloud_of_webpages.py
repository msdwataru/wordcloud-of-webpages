# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import MeCab
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

word_list = []
word_cnt = Counter()

def get_description_of_webpage(encoding="UTF-8"):
    for url in sys.stdin:
        print(url.strip())
        try:
            #res = requests.get("http://"+url.strip())
            res = requests.get(url.strip())
        except:
            print("GET request failed")
            continue
        res.encoding = encoding
        soup = BeautifulSoup(res.text, 'html.parser')
        
        for meta_tag in soup.find_all('meta', attrs={'name': 'description'}):
            yield meta_tag.get('content')

def parse_description(description):
    m = MeCab.Tagger("-Ochasen")
    for row in m.parse(description).split("\n"):
        word = row.split()[0]
        if word == "EOS":
            break
        pos = row.split()[-1]
        if "名詞-サ変接続" in pos or "数" in pos:
            continue
        if "名詞" in pos or "形容詞" in pos or "動詞" in pos:
            #print(row)    
            word_list.append(word)
            word_cnt.update([word])

def create_wordcloud():

    # 環境に合わせてフォントのパスを指定する。
    #fpath = "/System/Library/Fonts/HelveticaNeue-UltraLight.otf"
    #fpath = "/Library/Fonts/ヒラギノ角ゴ Pro W3.otf"
    #fpath = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf"
    fpath = "/Users/wataru-masuda/.font/NotoSansCJKjp-Regular.otf"
    
    #ストップワードの設定
    stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して',
                   u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',
                   u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で',
                   u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'',
                   u'無料', u'まとめ', u'ニュース', u'サイト', u'情報']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500,
                          stopwords=set(stop_words)).generate(" ".join(word_list))
    #                      ).generate(" ".join(word_list))

    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("wordcloud.png")
    plt.show()


def main():
    for description in get_description_of_webpage():
        #print(description)
        parse_description(description)

    with open("word_cnt_map.txt","w") as wf:
        for word, cnt in word_cnt.items():
            wf.write("{}\t{}\n".format(word, cnt))

    create_wordcloud()
        

if __name__ == "__main__":
    main()

# wordcloud-of-webpages
webページのdescriptionからwordcloudを生成する。
## What is implemented?
URLのリストを標準入力として受け取り、そのWebページに含まれるdescriptionを取得する。
そして、そのテキストをMeCabをもちいて構文解析し、単語のリストに加える。
最後にそのリストからwordcloudを生成する。出現単語と頻度のマップもテキストファイルとして出力している。

## requirements
- requests
- matplotlib
- collections
- BeautifulSoup
- MeCab
- wordcloud

## How to start?
```
cat urllist.txt | python wordcloud_of_webpages.py
```
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
出力例
![wordcloud](https://user-images.githubusercontent.com/29521139/61180586-a1e2c300-a653-11e9-93e4-72bea0a9c990.png)

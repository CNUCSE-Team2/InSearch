# InSearch

## 📚 Introduce
전문 검색을 지원하는 파이썬 기반 역색인 구조 라이브러리

- 형태소 분석기 : [은전한잎](http://eunjeon.blogspot.com/)
- 검색 알고리즘 : BM25 알고리즘 구현

Python-based inverted index structure library with full-text search support

- Morphology Analyzer : [eunjeon](http://eunjeon.blogspot.com/)
- Algorithm of Search : BM25

## 🤝 Team

|     2ternal      |   fortune00    |
| :--------------: | :------------: | 
|ddft97@gmail.com|sinyoungbok99@gmail.com|
| dev. BM25 & Analyzer| dev. main function | 

## 🔧 Installation

```
pip install InSearch
```
- Recent release version : 0.1.4
## 🍏 Using
 
### Initalize
``` python
import InSearch as IS

docs = ["동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세",
        "남산 위에 저 소나무 철갑을 두른 듯 바람 서리 불변함은 우리 기상일세 무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세",
        "가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세 무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세",
        "이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세 무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세"]


insearch = IS.InSearch()
for doc_id, doc_content in enumerate(docs):
    insearch.add_document(doc_id, doc_content)

```

### Search with full-text

``` python

query = "구름과 달"

insearch.get_scores(query)
# [(0.6978270940070869, 0), (2.4242033059345935, 2), (0.6794766371887851, 3)]

insearch.search(query)
# [2, 0, 3]

```
### More about Document
``` python
# update
insearch.update_document(doc_id, doc_content)

# delete
insearch.delete_document(doc_id)
```

### More about Table
``` python
# get table
insearch.return_table()

# get size of table 
insearch.get_size()

# initialize table 
insearch.delete_all()
```

### More about Search
``` python
# search top n
insearch.search_top_n()
```


## 🕸 Web for Test 
CNUCSE-Team2의 [InSearch-web](https://github.com/CNUCSE-Team2/InSearch-web)를 통해 해당 라이브러리 작동을 확인할 수 있어요!

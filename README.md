# InSearch

## ๐ Introduce
์ ๋ฌธ ๊ฒ์์ ์ง์ํ๋ ํ์ด์ฌ ๊ธฐ๋ฐ ์ญ์์ธ ๊ตฌ์กฐ ๋ผ์ด๋ธ๋ฌ๋ฆฌ

- ํํ์ ๋ถ์๊ธฐ : [์์ ํ์](http://eunjeon.blogspot.com/)
- ๊ฒ์ ์๊ณ ๋ฆฌ์ฆ : BM25 ์๊ณ ๋ฆฌ์ฆ ๊ตฌํ

Python-based inverted index structure library with full-text search support

- Morphology Analyzer : [eunjeon](http://eunjeon.blogspot.com/)
- Algorithm of Search : BM25

## ๐ค Team

|     2ternal      |   fortune00    |
| :--------------: | :------------: | 
|ddft97@gmail.com|sinyoungbok99@gmail.com|
| dev. BM25 & Analyzer| dev. main function | 

## ๐ง Installation

```
pip install InSearch
```
- Recent release version : 0.1.4
## ๐ Using
 
### Initalize
``` python
import InSearch as IS

docs = ["๋ํด๋ฌผ๊ณผ ๋ฐฑ๋์ฐ์ด ๋ง๋ฅด๊ณ  ๋ณ๋๋ก ํ๋๋์ด ๋ณด์ฐํ์ฌ ์ฐ๋ฆฌ๋๋ผ ๋ง์ธ ๋ฌด๊ถํ ์ผ์ฒ๋ฆฌ ํ๋ ค ๊ฐ์ฐ ๋ํ ์ฌ๋ ๋ํ์ผ๋ก ๊ธธ์ด ๋ณด์ ํ์ธ",
        "๋จ์ฐ ์์ ์  ์๋๋ฌด ์ฒ ๊ฐ์ ๋๋ฅธ ๋ฏ ๋ฐ๋ ์๋ฆฌ ๋ถ๋ณํจ์ ์ฐ๋ฆฌ ๊ธฐ์์ผ์ธ ๋ฌด๊ถํ ์ผ์ฒ๋ฆฌ ํ๋ ค ๊ฐ์ฐ ๋ํ ์ฌ๋ ๋ํ์ผ๋ก ๊ธธ์ด ๋ณด์ ํ์ธ",
        "๊ฐ์ ํ๋ ๊ณตํํ๋ฐ ๋๊ณ  ๊ตฌ๋ฆ ์์ด ๋ฐ์ ๋ฌ์ ์ฐ๋ฆฌ ๊ฐ์ด ์ผํธ๋จ์ฌ์ผ์ธ ๋ฌด๊ถํ ์ผ์ฒ๋ฆฌ ํ๋ ค ๊ฐ์ฐ ๋ํ ์ฌ๋ ๋ํ์ผ๋ก ๊ธธ์ด ๋ณด์ ํ์ธ",
        "์ด ๊ธฐ์๊ณผ ์ด ๋ง์ผ๋ก ์ถฉ์ฑ์ ๋คํ์ฌ ๊ดด๋ก์ฐ๋ ์ฆ๊ฑฐ์ฐ๋ ๋๋ผ ์ฌ๋ํ์ธ ๋ฌด๊ถํ ์ผ์ฒ๋ฆฌ ํ๋ ค ๊ฐ์ฐ ๋ํ ์ฌ๋ ๋ํ์ผ๋ก ๊ธธ์ด ๋ณด์ ํ์ธ"]


insearch = IS.InSearch()
for doc_id, doc_content in enumerate(docs):
    insearch.add_document(doc_id, doc_content)

```

### Search with full-text

``` python

query = "๊ตฌ๋ฆ๊ณผ ๋ฌ"

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


## ๐ธ Web for Test 
CNUCSE-Team2์ [InSearch-web](https://github.com/CNUCSE-Team2/InSearch-web)๋ฅผ ํตํด ํด๋น ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์๋์ ํ์ธํ  ์ ์์ด์!

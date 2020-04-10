# cotohacall
Make it easy to use Japanese processing API, [Cotoha](https://www.ntt.com/business/services/application/ai/cotoha-nlp.html),  offered by NTT Group.

## Description
**cotohacall** is a tool to use Cotoha API easily. What you need to use the API is installing this package and API account.

### What's Cotoha?
"COTOHA is Japanese Native AI originated from Japanese processing technology that NTT Group have developed over 40 years."  
by NTT communications.  
[More details](https://api.ce-cotoha.com/contents/about-cotoha.html)

## Demo
![Demo](https://user-images.githubusercontent.com/45617592/78994983-54f93200-7b7c-11ea-9d17-8eb11170291e.gif)

## Features
- Easy use.
- You don't have to worry about how to send the request.
- You can do Named Entity Extraction, Parsing, Reference Resolution, Keyword Extraction, Similarity Calculation, Sentence Type Classification, User Attribute Estimation (β), Filler Removal (β), Detect Misrecognition (β), Sentiment Analysis, and Summarization (About [them](https://api.ce-cotoha.com/contents/api-all.html)).

## Requirement

- Python3 or more
- Cotoha Developers Account (Get it from [here](https://api.ce-cotoha.com/contents/developers/index.html), it's free!)

## Usage
1. Install the package.
```py
pip install cotoha_at_python
```

2. Import the libraries.
```py
import os
from cotohacall.main  import cotoha_call
```
  
3. Get the Cotoha's CLIENT_ID and CLIENT_SECRET from [here](https://api.ce-cotoha.com/contents/developers/index.html), and set them as the environment variables.
```py
os.environ['CLIENT_ID'] = 'Your ID'
os.environ['CLIENT_SECRET'] = 'Your secret'
```
  
4. Prepare the sentence/sentences.
```py
sentence = 'えーっと、前線が太平洋上に停滞しています。えー、一方、高気圧が千島近海にあって、あーっと北日本から東日本をゆるやかに覆っています。'

# For Similarity Calculation
sentence_no_2 = '比較対象となる文。'
```
  
5. Select the type below.

| **Type** | ne | parse | coref | keyword | simi | sent_type | user_at | filler | detect | senti | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mean** | Named Entity Extraction | Parsing | Reference Resolution | Keyword Extraction | Similarity Calculation | Sentence Type Classification | User Attribute Estimation (β) | Filler Removal (β) | Detect Misrecognition (β) | Sentiment Analysis | Summarization |
  
Detail about these types from [here](https://api.ce-cotoha.com/contents/api-all.html).
  
6. Write the code.
```py
cotoha_call('SELECTED TYPE', sentence)

# For Similarity Calculation
cotoha_call('simi', sentence, sentence_2 = sentence_no_2)

# For Summarization (x = the number of the sentences, default = 1)
cotoha_call('summary', sentence, sent_len = x)
```

## Installation
```py
pip install cotoha_at_python
```

## Samples
Ran at the Google Colaboratory.
```py
!pip install cotoha_at_python

from cotohacall.main  import cotoha_call
import os

os.environ['CLIENT_ID'] = 'Your ID'
os.environ['CLIENT_SECRET'] = 'Ypur Secret'
```

### 1
Try keyword extraction.  
```py
sentence = '日本語の高精度な自然言語解析を実現するAPIサービス。NTTグループの40年以上の研究成果を活かした自然言語解析技術をCOTOHA APIでお手軽にご利用いただけます。'
cotoha_call('keyword', sentence)

# Return
"""
[{'form': '高精度', 'score': 20.0},
 {'form': '実現', 'score': 16.8278},
 {'form': 'お手軽', 'score': 10.8133},
 {'form': '研究成果', 'score': 10.0},
 {'form': 'cotoha api', 'score': 10.0}]
"""
```

### 2
Try all.  
```py
sentence_no_1 = '今日は早起きだね。えーっと、せっかくだし、美味しいと評判の喫茶店に行ってみよっか。'
sentence_no_2 = '朝食は友人に勧められたカフェで食べようか。'

for api_type in ["ne", "parse", "coref", "keyword", "simi", "sen_type", "user_at", "filler", "detect", "senti", "summary"]:
    print('API type : {}'.format(api_type))
    display(cotoha_call(api_type, sentence_no_1, sentence_2 = sentence_no_2))
    print('\n')

Return
"""
omit (too long to show)
"""
```


## Link
[Google colab上でCotohaを超手軽に使うためのコピペ用コード](https://qiita.com/Tommyyyyyyy/items/60f11a36c3a0fa789fd9)

## Reference
[Cotoha API](https://api.ce-cotoha.com/contents/index.html)  
[自然言語処理を簡単に扱えると噂のCOTOHA APIをPythonで使ってみた](https://qiita.com/gossy5454/items/83072418fb0c5f3e269f)

## Author
[TOOOOOOMY](https://github.com/TOOOOOOMY)

## License
MIT

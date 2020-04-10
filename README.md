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

<details><summary>Return</summary><div>
API type : ne
[{'begin_pos': 0,
  'class': 'DAT',
  'end_pos': 2,
  'extended_class': '',
  'form': '今日',
  'source': 'basic',
  'std_form': '今日'}]


API type : parse
[{'chunk_info': {'chunk_func': 1,
   'chunk_head': 0,
   'dep': 'D',
   'head': 1,
   'id': 0,
   'links': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'case', 'token_id': 1}],
    'features': ['日時'],
    'form': '今日',
    'id': 0,
    'kana': 'キョウ',
    'lemma': '今日',
    'pos': '名詞'},
   {'attributes': {},
    'features': [],
    'form': 'は',
    'id': 1,
    'kana': 'ハ',
    'lemma': 'は',
    'pos': '連用助詞'}]},
 {'chunk_info': {'chunk_func': 2,
   'chunk_head': 0,
   'dep': 'O',
   'head': -1,
   'id': 1,
   'links': [{'label': 'time', 'link': 0}, {'label': 'manner', 'link': 8}]},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'nmod', 'token_id': 0},
     {'label': 'advcl', 'token_id': 19},
     {'label': 'cop', 'token_id': 3},
     {'label': 'mark', 'token_id': 4},
     {'label': 'punct', 'token_id': 5}],
    'features': ['動作'],
    'form': '早起き',
    'id': 2,
    'kana': 'ハヤオキ',
    'lemma': '早起き',
    'pos': '名詞'},
   {'attributes': {},
    'features': ['終止'],
    'form': 'だ',
    'id': 3,
    'kana': 'ダ',
    'lemma': 'だ',
    'pos': '判定詞'},
   {'attributes': {},
    'features': [],
    'form': 'ね',
    'id': 4,
    'kana': 'ネ',
    'lemma': 'ね',
    'pos': '終助詞'},
   {'attributes': {},
    'features': [],
    'form': '。',
    'id': 5,
    'kana': '',
    'lemma': '。',
    'pos': '句点'}]},
 {'chunk_info': {'chunk_func': 0,
   'chunk_head': 0,
   'dep': 'D',
   'head': 8,
   'id': 2,
   'links': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'punct', 'token_id': 7}],
    'features': [],
    'form': 'えーっと',
    'id': 6,
    'kana': 'エーット',
    'lemma': 'えーと',
    'pos': '独立詞'},
   {'attributes': {},
    'features': [],
    'form': '、',
    'id': 7,
    'kana': '',
    'lemma': '、',
    'pos': '読点'}]},
 {'chunk_info': {'chunk_func': 0,
   'chunk_head': 0,
   'dep': 'D',
   'head': 4,
   'id': 3,
   'links': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [],
    'features': [],
    'form': 'せっかく',
    'id': 8,
    'kana': 'セッカク',
    'lemma': '折角',
    'pos': '連用詞'}]},
 {'chunk_info': {'chunk_func': 1,
   'chunk_head': 0,
   'dep': 'P',
   'head': 8,
   'id': 4,
   'links': [{'label': 'manner', 'link': 3}],
   'predicate': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'advmod', 'token_id': 8},
     {'label': 'aux', 'token_id': 10},
     {'label': 'punct', 'token_id': 11}],
    'features': ['S'],
    'form': 'だ',
    'id': 9,
    'kana': 'ダ',
    'lemma': '出す',
    'pos': '動詞語幹'},
   {'attributes': {},
    'features': ['連用'],
    'form': 'し',
    'id': 10,
    'kana': 'シ',
    'lemma': 'し',
    'pos': '動詞接尾辞'},
   {'attributes': {},
    'features': [],
    'form': '、',
    'id': 11,
    'kana': '',
    'lemma': '、',
    'pos': '読点'}]},
 {'chunk_info': {'chunk_func': 2,
   'chunk_head': 0,
   'dep': 'D',
   'head': 8,
   'id': 5,
   'links': [],
   'predicate': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'aux', 'token_id': 13},
     {'label': 'mark', 'token_id': 14}],
    'features': ['イ段'],
    'form': '美味し',
    'id': 12,
    'kana': 'オイシ',
    'lemma': 'おいしい',
    'pos': '形容詞語幹'},
   {'attributes': {},
    'features': ['終止'],
    'form': 'い',
    'id': 13,
    'kana': 'イ',
    'lemma': 'い',
    'pos': '形容詞接尾辞'},
   {'attributes': {},
    'features': ['連用'],
    'form': 'と',
    'id': 14,
    'kana': 'ト',
    'lemma': 'と',
    'pos': '引用助詞'}]},
 {'chunk_info': {'chunk_func': 1,
   'chunk_head': 0,
   'dep': 'D',
   'head': 7,
   'id': 6,
   'links': []},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'case', 'token_id': 16}],
    'features': [],
    'form': '評判',
    'id': 15,
    'kana': 'ヒョウバン',
    'lemma': '評判',
    'pos': '名詞'},
   {'attributes': {},
    'features': ['連体'],
    'form': 'の',
    'id': 16,
    'kana': 'ノ',
    'lemma': 'の',
    'pos': '格助詞'}]},
 {'chunk_info': {'chunk_func': 1,
   'chunk_head': 0,
   'dep': 'D',
   'head': 8,
   'id': 7,
   'links': [{'label': 'adjectivals', 'link': 6}]},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'nmod', 'token_id': 15},
     {'label': 'case', 'token_id': 18}],
    'features': [],
    'form': '喫茶店',
    'id': 17,
    'kana': 'キッサテン',
    'lemma': '喫茶店',
    'pos': '名詞'},
   {'attributes': {},
    'features': ['連用'],
    'form': 'に',
    'id': 18,
    'kana': 'ニ',
    'lemma': 'に',
    'pos': '格助詞'}]},
 {'chunk_info': {'chunk_func': 6,
   'chunk_head': 0,
   'dep': 'Q',
   'head': 1,
   'id': 8,
   'links': [{'label': 'manner', 'link': 2},
    {'label': 'manner', 'link': 4},
    {'label': 'object', 'link': 5},
    {'label': 'goal', 'link': 7}],
   'predicate': ['past']},
  'tokens': [{'attributes': {},
    'dependency_labels': [{'label': 'discourse', 'token_id': 6},
     {'label': 'advcl', 'token_id': 9},
     {'label': 'dobj', 'token_id': 12},
     {'label': 'nmod', 'token_id': 17},
     {'label': 'aux', 'token_id': 20},
     {'label': 'aux', 'token_id': 21},
     {'label': 'aux', 'token_id': 22},
     {'label': 'aux', 'token_id': 23},
     {'label': 'aux', 'token_id': 24},
     {'label': 'mark', 'token_id': 25},
     {'label': 'punct', 'token_id': 26}],
    'features': ['IKU'],
    'form': '行',
    'id': 19,
    'kana': 'イ',
    'lemma': '行く',
    'pos': '動詞語幹'},
   {'attributes': {},
    'features': [],
    'form': 'っ',
    'id': 20,
    'kana': 'ッ',
    'lemma': 'っ',
    'pos': '動詞活用語尾'},
   {'attributes': {},
    'features': ['接続', '連用'],
    'form': 'て',
    'id': 21,
    'kana': 'テ',
    'lemma': 'て',
    'pos': '動詞接尾辞'},
   {'attributes': {},
    'features': ['A', 'Lて連用'],
    'form': 'み',
    'id': 22,
    'kana': 'ミ',
    'lemma': 'みる',
    'pos': '動詞語幹'},
   {'attributes': {},
    'features': [],
    'form': 'よ',
    'id': 23,
    'kana': 'ヨ',
    'lemma': 'よ',
    'pos': '動詞活用語尾'},
   {'attributes': {},
    'features': ['終止'],
    'form': 'っ',
    'id': 24,
    'kana': 'ッ',
    'lemma': 'う',
    'pos': '動詞接尾辞'},
   {'attributes': {},
    'features': [],
    'form': 'か',
    'id': 25,
    'kana': 'カ',
    'lemma': 'か',
    'pos': '終助詞'},
   {'attributes': {},
    'features': [],
    'form': '。',
    'id': 26,
    'kana': '',
    'lemma': '。',
    'pos': '句点'}]}]


API type : coref
{'coreference': [],
 'tokens': [['今日',
   'は',
   '早起き',
   'だ',
   'ね',
   '。',
   'えーっと',
   '、',
   'せっかく',
   'だ',
   'し',
   '、',
   '美味し',
   'い',
   'と',
   '評判',
   'の',
   '喫茶店',
   'に',
   '行',
   'っ',
   'て',
   'み',
   'よ',
   'っ',
   'か',
   '。']]}


API type : keyword
[{'form': '早起き', 'score': 25.6106}, {'form': '喫茶店', 'score': 11.0135}]


API type : simi
{'score': 0.90180045}


API type : sen_type
{'dialog_act': ['information-seeking'], 'modality': 'interrogative'}


API type : user_at
{'age': '20-29歳',
 'civilstatus': '既婚',
 'hobby': ['COOKING', 'INTERNET', 'MOVIE', 'TVDRAMA', 'TVGAME'],
 'occupation': '会社員'}


API type : filler
[{'fillers': [{'begin_pos': 9, 'end_pos': 14, 'form': 'えーっと、'}],
  'fixed_sentence': '今日は早起きだね。せっかくだし、美味しいと評判の喫茶店に行ってみよっか。',
  'normalized_sentence': '今日は早起きだね。えーっと、せっかくだし、美味しいと評判の喫茶店に行ってみよっか。'}]


API type : detect
{'candidates': [], 'score': 0}


API type : senti
{'emotional_phrase': [{'emotion': 'P', 'form': '美味しい'}],
 'score': 0.23242221988572817,
 'sentiment': 'Positive'}


API type : summary
'えーっと、せっかくだし、美味しいと評判の喫茶店に行ってみよっか。'
</div></details>

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

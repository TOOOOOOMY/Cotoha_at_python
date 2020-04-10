# cotohacall
Make it easy to use Japanese processing API, [Cotoha](https://www.ntt.com/business/services/application/ai/cotoha-nlp.html),  offered by NTT Group.

## Description
**cotohacall** is a tool to use Cotoha API easily. What you need to use is copy and paste, and pip instyall will be available soon.

### What's Cotoha?
"COTOHA is Japanese Native AI originated from Japanese processing technology that NTT Group have developed over 40 years."  
by NTT communications.  
[More details](https://api.ce-cotoha.com/contents/about-cotoha.html)

## Demo
![GifMaker_20200410112914873](https://user-images.githubusercontent.com/45617592/78956943-e043da80-7b1e-11ea-9672-ab4936f189f8.gif)
  
### Image
![demo](https://user-images.githubusercontent.com/45617592/78956257-a83b9800-7b1c-11ea-8155-8e3a9c46a96a.jpg)

## Features
- Easy use.
- You don't have to worry about how to send the request.
- You can do Named Entity Extraction, Parsing, Reference Resolution, Keyword Extraction, Similarity Calculation, Sentence Type Classification, User Attribute Estimation (β), Filler Removal (β), Detect Misrecognition (β), Sentiment Analysis, and Summarization (About [them](https://api.ce-cotoha.com/contents/api-all.html)).

## Requirement

- Python3 or more
- Cotoha Developers Account (Get it from [here](https://api.ce-cotoha.com/contents/developers/index.html), it's free!)

## Usage
1. Import the libraries.
```py
import os
import urllib.request
import json
import sys
```
  
2. Get the Cotoha's CLIENT_ID and CLIENT_SECRET from [here](https://api.ce-cotoha.com/contents/developers/index.html), and set them as the environment variables.
```py
os.environ['CLIENT_ID'] = 'Your ID'
os.environ['CLIENT_SECRET'] = 'Your secret'
```
  
3. Copy and paste the code in `cotohacall.py`.
  
4. 

| **Type** | ne | parse | coref | keyword | simi | sent_type | user_at | filler | detect | senti | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mean** | Named Entity Extraction | Parsing | Reference Resolution | Keyword Extraction | Similarity Calculation | Sentence Type Classification | User Attribute Estimation (β) | Filler Removal (β) | Detect Misrecognition (β) | Sentiment Analysis | Summarization |

## Installation



## Anything Else

AnythingAnythingAnything
AnythingAnythingAnything
AnythingAnythingAnything

## Author


## License

[MIT](http://b4b4r07.mit-license.org)

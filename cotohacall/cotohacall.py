import os
import urllib.request
import json
import sys

def cotoha_call(api_type, sentence_1, sentence_2 = "比較したい文章", sent_len = 1):
    api_name_show_switch = 0 #api名を表示させたくない場合は0にする
    developer_api_base_url = "https://api.ce-cotoha.com/api/dev/nlp/"
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    access_token_publish_url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"

    # アクセストークン取得
    def getAccessToken():
        # アクセストークン取得URL指定
        url = access_token_publish_url
        # ヘッダ指定
        headers={
            "Content-Type": "application/json;charset=UTF-8"
        }
        # リクエストボディ指定
        data = {
            "grantType": "client_credentials",
            "clientId": client_id,
            "clientSecret": client_secret
        }
        # リクエストボディ指定をJSONにエンコード
        data = json.dumps(data).encode()

        # リクエスト生成
        req = urllib.request.Request(url, data, headers)

        # リクエストを送信し、レスポンスを受信
        res = urllib.request.urlopen(req)

        # レスポンスボディ取得
        res_body = res.read()

        # レスポンスボディをJSONからデコード
        res_body = json.loads(res_body)

        # レスポンスボディからアクセストークンを取得
        access_token = res_body["access_token"]

        return access_token

    # API URL指定
    if api_type == "parse":
        api_name = "構文解析"
        base_url_footer = "v1/" + api_type
        request_body_type = 1
    elif api_type == "ne":
        api_name = "固有表現抽出"
        base_url_footer = "v1/" + api_type
        request_body_type = 1
    elif api_type == "keyword":
        api_name = "キーワード抽出"
        base_url_footer = "v1/" + api_type
        request_body_type = 2
    elif api_type == "coref":
        api_name = "照応解析"
        base_url_footer = "v1/coreference"
        request_body_type = 2
    elif api_type == "simi":
        api_name = "類似度算出"
        base_url_footer = "v1/similarity"
        request_body_type = 3
    elif api_type == "sen_type":
        api_name = "文タイプ判定"
        base_url_footer = "v1/sentence_type"
        request_body_type = 1
    elif api_type == "user_at":
        api_name = "ユーザ属性推定(β)"
        base_url_footer = "beta/user_attribute"
        request_body_type = 2
    elif api_type == "filler":
        api_name = "言い淀み除去(β)"
        base_url_footer = "beta/remove_filler"
        request_body_type = 4
    elif api_type == "detect":
        api_name = "音声認識誤り検知(β)"
        base_url_footer = "beta/detect_misrecognition"
        request_body_type = 1
    elif api_type == "senti":
        api_name = "感情分析"
        base_url_footer = "v1/sentiment"
        request_body_type = 1
    elif api_type == "summary":
        api_name = "要約(β)"
        base_url_footer = "beta/summary"
        request_body_type = 5
    else :
        print("Api Type Error.")
        sys.exit()

    if api_name_show_switch == 1:
        print("===>\n" + api_name + "\n===>")

    url = developer_api_base_url + base_url_footer

    # ヘッダ指定
    headers={
        "Authorization": "Bearer " + getAccessToken(), #access_token,
        "Content-Type": "application/json;charset=UTF-8",
    }
    # リクエストボディ指定
    if request_body_type == 1:
        data = {
            "sentence": sentence_1
        }
    elif request_body_type == 2:
        data = {
            "document": sentence_1
        }
    elif request_body_type == 3:
        data = {
            "s1": sentence_1,
            "s2": sentence_2
        }
    elif request_body_type == 4:
        data = {
            "text": sentence_1
        }
    elif request_body_type == 5:
        data = {
            "document": sentence_1,
            "sent_len": sent_len
        }

    # リクエストボディ指定をJSONにエンコード
    data = json.dumps(data).encode()
        # リクエスト生成
    req = urllib.request.Request(url, data, headers)
        # リクエストを送信し、レスポンスを受信
    try:
        res = urllib.request.urlopen(req)
    # リクエストでエラーが発生した場合の処理
    except urllib.request.HTTPError as e:
        # ステータスコードが401 Unauthorizedならアクセストークンを取得し直して再リクエスト
        if e.code == 401:
            access_token = getAccessToken()
            headers["Authorization"] = "Bearer " + access_token
            req = urllib.request.Request(url, data, headers)
            res = urllib.request.urlopen(req)
        # 401以外のエラーなら原因を表示
        else:
            return print ("<Error> " + e.reason)
            #sys.exit()

    # レスポンスボディ取得
    res_body = res.read()
    # レスポンスボディをJSONからデコード
    res_body = json.loads(res_body)
    # レスポンスボディから解析結果を取得
    return res_body["result"]

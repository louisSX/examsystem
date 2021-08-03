import requests
import pymysql


# 根据小程序传参的code，获取微信用户的openid，并返回。
def getOpenID(code):
    # 获取openid
    appid = 'wxe807e8c4c67558f9'
    secret = '68dfeca301a2afc08679cce65a38f86d'
    url = "https://api.weixin.qq.com/sns/jscode2session"
    r = requests.get(url, params={'appid': appid, 'secret': secret,
                                  'js_code': code, 'grant_type': 'authorization_code'})
    openid = r.json()['openid']
    return  openid


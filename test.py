from flask import Flask
from flask import request
from User import User
import Controller

app = Flask(__name__)

@app.route('/', methods=['POST'])
def test():
    if request.method == 'POST':
      name = str(request.json['name'])
      return 'hello,%s' % name

@app.route('/api/getOpenId', methods=['POST'])
def getUser():
    if request.method == 'POST':
      code = str(request.json['code'])
      openid = Controller.getOpenID(code)
      return openid

@app.route('/api/getUserInfo', methods=['POST'])
def getUserInfo():
    if request.method == 'POST':
      code = str(request.json['code'])
      openid = Controller.getOpenID(code)
      user = User(openid)
      userInfoToJson = user.getUserInfoToJson()
      return userInfoToJson

if __name__ == '__main__':
    app.run(host='0.0.0.0')

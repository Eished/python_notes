"""
    Create by Eished on 2022-06-06
"""

from email.mime import application
from urllib import response
from flask import Flask, make_response

__author__ = 'Eished'

app = Flask(__name__)
app.config.from_object('config')

# config 参数必须全大写
# print(app.config['DEBUG'])


@app.route('/hi')
def hi():
    # content-type = text/html
    return 'Hello, world! <h1>Hi</h1>'


@app.route('/hello')
def hello():
    headers = {'content-type': 'text/plain'}
    response = make_response('<h1></h1>', 404)
    response.headers = headers
    return response


@app.route('/redirect')
def redirect():
    headers = {
        'content-type': 'text/plain',
        'location': '/hi'
    }
    response = make_response('redirect', 301)
    response.headers = headers
    return response


@app.route('/json')
def json():
    headers = {
        'content-type': 'application/json',
    }
    response = '{"a":"1"}'
    return response, 200, headers


# 基于类的视图（即插视图），路由注册方式
# app.add_url_rule('/hi', view_func=hello)

# 作为入口模块启动时，使用默认web服务
if __name__ == '__main__':
    # 入站流量，入站端口
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port='5000')

'''
@Author: your name
@Date: 2020-03-18 19:49:06
@LastEditTime: 2020-03-20 09:39:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import requests
from enum import Enum

url_env = 'debug'


class ENV(Enum):
    debug = 'http://127.0.0.1:5000'
    pro = 'https://todo.winn.online'


def url(url: str, env=url_env):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                prefix = ENV[env].value+'/'
            except:
                prefix = ENV['debug'].value+'/'
            return func(prefix+url.lstrip('/'), *args, **kwargs)
        return wrapper
    return decorator


@url('/', env='debug')
def get_hello(url, *args, **kwargs):
    r = requests.get(url)
    print(r.text)


@url('/ContributorList')
def get_ContributorList(url, *args, **kwargs):
    r = requests.get(url, data=kwargs)
    print(r.text)


if __name__ == "__main__":
    test = 456
    get_hello()
    get_ContributorList(test=test)
    get_ContributorList(name=test)

import requests, json


def get_method(url, headers, params1):
    """封装get方法"""
    try:
        res = requests.get(url=url, headers=headers, params=params1)
        return res
    except Exception as e:
        print("get请求错误: %s" % e)


def post_method(url, headers, json1):
    """封装post方法"""
    try:
        res = requests.post(url=url, headers=headers, json=json1)
        return res
    except Exception as e:
        print("post请求错误: %s" % e)


def delete_method(url, headers, json1):
    """封装delete方法"""
    try:
        res = requests.delete(url=url, headers=headers, json=json1)
        return res
    except Exception as e:
        print("delete请求错误: %s" % e)


def put_method(url, headers, json1):
    """封装put方法"""
    try:
        res = requests.put(url=url, headers=headers, json=json1)
        return res
    except Exception as e:
        print("put请求错误: %s" % e)





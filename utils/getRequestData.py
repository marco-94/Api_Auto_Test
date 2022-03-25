"""
获取上一个接口返回的参数，指定传入下一个接口的参数
"""
from utils import getExecldata
import json


# 获取上一个接口返回的参数,用list形式全部存储起来
class GetKeyValue(object):
    def __init__(self, o, mode='j'):
        self.json_object = None
        if mode == 'j':
            self.json_object = o
        elif mode == 's':
            self.json_object = json.loads(o)
        else:
            raise Exception('Unexpected mode argument.Choose "j" or "s".')

        self.result_list = []

    def search_key(self, key):
        self.result_list = []
        self.__search(self.json_object, key)
        return self.result_list

    def __search(self, json_object, key):

        for k in json_object:
            if k == key:
                self.result_list.append(json_object[k])
            if isinstance(json_object[k], dict):
                self.__search(json_object[k], key)
            if isinstance(json_object[k], list):
                for item in json_object[k]:
                    if isinstance(item, dict):
                        self.__search(item, key)
        return


# 把传参全部拼接好，并返回
def get_request_data(m, n, json_data):
    """
    传入：
    用例所在行(rows),
    下一个接口校验的参数所在列(next_columns),
    请求参数所在列(request_columns),
    上一个接口返回的参数(json_data)gghj
    返回：
    dict类型json格式的请求参数，可直接传参使用
    """
    # 基于上个接口拿参数
    gkv = GetKeyValue(o=json_data, mode='j')

    # 获取整个json
    data_json = getExecldata.execljson(int(5+m), int(5+6*n))

    # 获取请求参数
    request_json = getExecldata.execljson(int(5+m), int(8+6*n))
    for j in range(0, len(data_json)):
        # 请求参数的值被替换成接口返回参数的值
        request_json[list(data_json.keys())[j]] = gkv.search_key(list(data_json.keys())[j])[int(list(data_json.values())[j])]
    # 把拼接好的请求参数，以dict类型json格式返回
    return request_json

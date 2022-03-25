from collections import Counter
from utils.GetKeyValue import *
from utils.get_exldata import data_res


# api_num--每一行的第几个接口
# api_rows--用例行调用的具体行数
# api_res--接口响应报文，传值json格式
# 判断是否包含断言调用方法
def test_in(api_num, api_rows, api_res1):
    print("接口响应报文为%s" %api_res1)
    (exl_keys, exl_values, api_keys, api_values) = key_value(api_num, api_rows, api_res1)
    counter1 = Counter(exl_keys)
    counter2 = Counter(api_keys)
    counter3 = Counter(exl_values)
    counter4 = Counter(api_values)
    result_key = all(v <= counter1[k] for k, v in counter2.items())
    result_value = all(v <= counter3[k] for k, v in counter4.items())
    print(result_key, result_value, type(result_key))
    if result_value and result_value == True:
        return "断言成功"
    else:
        return "断言失败"


def key_value(api_num, api_rows, api_res2):
    exl_data = data_res(api_num,api_rows)
    print("表格响应报文为%s" % exl_data)
    # mode=j意味传入的object是一个json对象也可以：
    gkv = GetKeyValue(o=api_res2, mode='j')
    (api_keys, api_values) = gkv.search_key()
    try:
        json.loads(exl_data)
    except Exception as e:
        print("表格数据非json报错信息:%s" %e)
        return "a", "b", api_keys, api_values
    else:
        data = exl_data
        gkv1 = GetKeyValue(o=data, mode='s')
        (exl_keys, exl_values) = gkv1.search_key()
        print(exl_keys, exl_values, api_keys, api_values)
        return exl_keys, exl_values, api_keys, api_values



# if __name__ == '__main__':
#     api_res = {
#         "msg": "None1",
#         "succeed": "true",
#         "code": "200"
#     }
#     result = test_in(1, 6, api_res)
#     print(result)


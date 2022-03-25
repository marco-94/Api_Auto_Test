"""
读取excel，返回是否执行该用例，账号，密码，分公司ID，城市行政区划，请求头
"""
from utils import getExecldata, getYaml
import base64
data = getYaml.getyamldata()


def userinfoList():
    """获取用户名，密码，分公司ID，城市行政区划"""
    username = getExecldata.execlstr(3, 4)
    passwordbase64 = getExecldata.execlstr(3, 6)
    password = str(base64.b64decode(passwordbase64[6:-6]), encoding="utf-8")
    branchId = getExecldata.execlstr(3, 8)
    cityCode = str(getExecldata.execlstr(3, 10))
    return username, password, branchId, cityCode


def request_mode(i, j):
    """获取请求方法"""
    requsetMode = getExecldata.execlstr(i+5, int(6+6*j))
    return requsetMode


def request_url(i, j):
    """判断测试环境，拼接域名和地址"""
    try:
        if getExecldata.execlstr(3, 2) == "BETA" or "beta":
            requestUrl = data["beta"] + getExecldata.execlstr(i+5, int(7+6*j))
            return requestUrl

        elif getExecldata.execlstr(3, 2) == "PROD" or "prod":
            requestUrl = data["prod"] + getExecldata.execlstr(i+5, int(7+6*j))
            return requestUrl
    except Exception:
        print("请确认测试环境配置是否正确")


def next_request(i, j):
    """下一个接口需要修改的字段"""
    nextRequest = getExecldata.execlstr(i, j)
    return nextRequest


def request_data(i, j):
    """获取请求参数"""
    requestData = getExecldata.execljson(int(5+5*i), int(8+6*j))
    return requestData


def case_title():
    """获取用例标题"""
    caseTtile = getExecldata.execlstr(1, 2)
    return caseTtile

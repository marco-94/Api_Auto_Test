"""
测试用例，执行该脚本接口轮询所有用例
"""
from utils import getExecldata, requestMethod, getRequestData, userinfo, setToken, get_assert
import json
import unittest
import time


class Test(unittest.TestCase):
    def setUp(self):
        # """开始执行用例"""
        print("开始执行用例")

    def tearDown(self):
        # """用例执行完成"""
        print("全部用例执行完成")
        time.sleep(1)

    def test_run(self):
        # 总行数、用例总数、每个用例内的接口总数
        case_total = getExecldata.getRowsColumns()[0]
        interfaces_total = getExecldata.getRowsColumns()[1]

        # 轮询用例
        for i in range(0, case_total):

            # 判断该用例是否执行,0不执行，1执行
            if getExecldata.execlstr(int(5+i), 3) == 0:
                continue

            # 定义一个列表，存放每个接口的出参
            response_list = []
            try:
                headers = {
                    "X-Organ-Id": userinfo.userinfoList()[2],
                    "X-City-Code": userinfo.userinfoList()[3],
                    "authorization": setToken.get_accessToken()
                }
                # 轮询每个用例中的接口
                for j in range(0, interfaces_total):
                    # 先获取下个接口入参需要修改的值
                    if userinfo.next_request(int(5+i), int(4+6*j)) is None or userinfo.next_request(int(5+i), int(5+6*j)) is None:
                        request_data = json.loads(getExecldata.execlstr(int(5+i), int(8+6*j)))
                    else:
                        # 需要从上面倒数第N个接口拿参数，上一个接口为1
                        before_response = getExecldata.execlstr(int(5+i), int(4+6*j))

                        # 拿取出参列表的参数，转化为入参
                        response_data = response_list[int(j-int(before_response))]
                        request_data = getRequestData.get_request_data(i, j, response_data)

                    # 选择不同的请求方式，把每次的出参都更新到列表(request_list)中
                    if userinfo.request_mode(i, j) == "get" or userinfo.request_mode(i, j) == "GET":
                        print("用例-" + getExecldata.execlstr(int(5+i), 1) + "-的第", j+1,
                              "个接口开始执行----------------------------------")
                        response = requestMethod.get_method(userinfo.request_url(i, j), headers, request_data).json()

                        # 把出参存起来
                        response_list.append(response)

                        # 输出部分
                        print("接口地址", userinfo.request_mode(i, j), "-", userinfo.request_url(i, j))
                        print("请求参数：", request_data)
                        print("返回参数：", response)
                        print("响应断言：", getExecldata.execljson(5+i, int(9+6*j)))

                        if get_assert.test_in(j+1, 5+i, response) == "Fail":
                            print("断言结果：", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                            break
                        elif get_assert.test_in(j+1, 5+i, response) == "Pass":
                            print("断言结果：", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                        else:
                            print("断言失败：", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")

                    elif userinfo.request_mode(i, j) == "post" or userinfo.request_mode(i, j) == "POST":
                        print("用例-" + getExecldata.execlstr(int(5+i), 1) + "-的第", j+1,
                              "个接口开始执行----------------------------------")
                        response = requestMethod.post_method(userinfo.request_url(i, j), headers, request_data).json()

                        # 把出参存起来
                        response_list.append(response)

                        print("接口地址", userinfo.request_mode(i, j), "-", userinfo.request_url(i, j))
                        try:
                            # 登录的，需要隐藏密码
                            password_hide = request_data
                            password_hide["input_param"]["password"] = "******"
                            print("请求参数：", password_hide)
                        except Exception:
                            print("请求参数：", request_data)

                        print("返回参数：", response)
                        print("响应断言：", getExecldata.execljson(5+i, int(9+6*j)))

                        if get_assert.test_in(j+1, 5+i, response) == "Fail":
                            print("断言结果", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                            break
                        elif get_assert.test_in(j+1, 5+i, response) == "Pass":
                            print("断言结果：", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                        else:
                            print("断言失败：", get_assert.test_in(j+1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")

                    elif userinfo.request_mode(i, j) == "put" or userinfo.request_mode(i, j) == "PUT":
                        print("用例-" + getExecldata.execlstr(int(5+i), 1) + "-的第", j+1,
                              "个接口开始执行----------------------------------")
                        response = requestMethod.put_method(userinfo.request_url(i, j), headers, request_data).json()

                        # 把出参存起来
                        response_list.append(response)

                        print("接口地址：", userinfo.request_mode(i, j), "-", userinfo.request_url(i, j))
                        print("请求参数：", request_data)
                        print("返回参数：", response)
                        print("响应断言：", getExecldata.execljson(5+i, int(9+6*j)))
                        if get_assert.test_in(j+1, 5+i, response) == "Fail":
                            print("断言结果：", get_assert.test_in(j + 1, 5+i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                            break
                        elif get_assert.test_in(j+1, 5+i, response) == "Pass":
                            print("断言结果：", get_assert.test_in(j + 1, 5 + i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                        else:
                            print("断言失败：", get_assert.test_in(j + 1, 5 + i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")

                    elif userinfo.request_mode(i, j) == "delete" or userinfo.request_mode(i, j) == "DELETE":
                        print("用例-" + getExecldata.execlstr(int(5+i), 1) + "-的第", j+1,
                              "个接口开始执行----------------------------------")
                        response = requestMethod.delete_method(userinfo.request_url(i, j), headers, request_data).json()

                        # 把出参存起来
                        response_list.append(response)

                        print("接口地址：", userinfo.request_mode(i, j), "-", userinfo.request_url(i, j))
                        print("请求参数：", request_data)
                        print("返回参数：", response)
                        print("响应断言：", getExecldata.execljson(5+i, int(9+6*j)))
                        if get_assert.test_in(j + 1, 5 + i, response) == "Fail":
                            print("断言结果：", get_assert.test_in(j + 1, 5 + i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                            break
                        elif get_assert.test_in(j + 1, 5 + i, response) == "Pass":
                            print("断言结果：", get_assert.test_in(j + 1, 5 + i, response))
                            print("用例-" + getExecldata.execlstr(int(5 + i), 1) + "-的第", j + 1,
                                  "个接口执行完成----------------------------------")
                            print("     ")
                        else:
                            print("断言失败：", get_assert.test_in(j + 1, 5 + i, response))
                            print("用例-" + getExecldata.execlstr(int(5+i), 1) + "-的第", j+1,
                                  "个接口执行完成----------------------------------")
                            print("     ")

                    else:
                        print("请求方式错误：", userinfo.request_mode(i, j))
            except Exception as e:
                print("报错信息：", e)

            print("------------------------------------------------------------用例-" +
                  getExecldata.execlstr(int(5+i), 1) +
                  "-执行完成------------------------------------------------------------")


if __name__ == '__main__':
    unittest.main()

import xlrd
import numpy as np
from config.config import EXCEL_PATH
from utils import getExecldata
#utf-8


def get_exlres():
    # 0 empty，1 string，2 number， 3 date，4 boolean，5 error
    workbook = xlrd.open_workbook(filename=EXCEL_PATH)
    df = workbook.sheet_by_name("Sheet1")
    print(df)
    """CaseTotal=获取用例总数，interfacesTotal=单用例总接口数"""
    (CaseTotal, interfacesTotal) = getExecldata.getRowsColumns()
    print(CaseTotal, interfacesTotal)
    res_list = []
    for curr_row in range(4, CaseTotal + 4):
        list1 = []
        for api_num in range(1, interfacesTotal + 1):
            curr_col = api_num + 2 * (2 * api_num + 1)
            # ctype :  0 empty，1 string，2 number， 3 date，4 boolean，5 error
            raw_val = df.cell(curr_row, curr_col).value
            if type(raw_val) != str:
                list1.append("表格内容为空")
            else:
                list1.append(raw_val)
        res_list.append(list1)
    return res_list


def data_res(api_num, curr_row):
    curr_row = curr_row-4
    api_num = api_num-1
    a = get_exlres()
    list_numpy = np.array(a)
    print(curr_row, api_num)
    res = list_numpy[curr_row][api_num]
    return res

# if __name__ == '__main__':
#     result = data_res(1, 7)
#     print(result)

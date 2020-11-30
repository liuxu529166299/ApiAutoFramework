# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :operatorexcel
# @Date     :2020/11/28 10:20
# @Author   :刘旭
-------------------------------------------------
"""

import os
from openpyxl import *
from logger.logger import LoggerInfo

log = LoggerInfo().logger()


class excelData:
    def getExcel(self):
        log.info("遍历用例目录读取用例excel开始。。。。。。。。。。。。。")
        # os.getcwd()当前工作目录
        base_path = os.getcwd()
        # os.path.join()把目录和文件名合成一个路径
        test_case_path = os.path.join(base_path, 'data')
        # os.walk()文件、目录遍历器
        file_name_list = os.walk(test_case_path, topdown=True)
        dict = {}
        for root, dirs, file_name in file_name_list:
            try:
                for name in file_name:
                    log.info(os.path.join(root, name))
                    log.info("读取用例excel中sheet开始。。。。。。。。。。。。。")
                    # 取workbook
                    workbook = load_workbook(os.path.join(root, name))
                    # 取sheet
                    sheet = workbook['Sheet1']
                    # 定义外层的list结构
                    lists = []
                    # 读取rows
                    rows_sheet = sheet.iter_rows()
                    # 循环读取每一行，需要赋值每一行为一个list
                    for item in rows_sheet:
                        if item[0].value == "url":
                            continue;
                        list = []
                        for col in item:
                            # 遍历每一列加入到一行测试数据
                            list.append(col.value)
                        lists.append(list)
                    dict[name] = lists
            except Exception as e:
                log.error("历用例目录读取用例excel执行出错，请查看问题！原因: s%", e)
        log.info(dict)
        return dict

    def get_excel_data(self):
        log.info("执行转换用例开始。。。。")
        contents = []
        if len(contents) >= 0:
            log.info("读取excel用例数据。。。。")
            casedata = excelData().getExcel()
            log.info("循环读取excel中每行数据开始。。。。")
            for case in casedata:
                name = case
                listcase = casedata[name]
                for list in listcase:
                    contents.append(list)
            log.info("excel用例数据读取完成。。。。")
        log.info(contents)
        return contents

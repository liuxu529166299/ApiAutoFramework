"""
-------------------------------------------------
# @File     :test_case
# @Date     :2020/11/11 16:24
# @Author   :刘旭
-------------------------------------------------
"""
import pytest
from tools.operator_Common import operator_Common
from logger.logger import LoggerInfo
from tools.convertoperator import operatorConvert, depend
import json
import jsonpath
from tools.operatorexcel import excelData


class TestCase():
    @pytest.mark.parametrize("case", excelData().get_excel_data())
    def test_get_commonapi(self, case):
        # print(case)
        url = case[0]
        body = case[1]
        header = case[2]
        method = case[3]
        method_type = case[4]
        expect = case[5]
        jsonpaths = case[6]
        dependency = case[7]

        print(url + "-" + str(body) + "-" + str(
            header) + "-" + method + "-" + method_type + "-" + expect + "-" + jsonpaths + "-" + dependency)
        common = operator_Common()
        LoggerInfo().logger().info("替换body中的空格换行特殊字符开始。。。。")
        body = body.replace('\r', '').replace('\n', '').replace('\t', '') if body is not None else ""
        #
        LoggerInfo().logger().info("转换存在可变变量开始。。。。")
        # 假如body中存在变量获取符号，调用convertBody重新对变量进行转化
        body = operatorConvert().convertBody(body) if body.find('$') >= 0 else body
        header = operatorConvert().convertBody(header) if (header is not None and header.find('$') >= 0) else header
        header = "" if header is None else header
        res = common.request(method, url, method_type, body, header)
        #
        # # 判断dependency是否有值需要存储
        #
        if len(res.content) > 0 and dependency.find('/') < 0:
            depend[dependency] = res.content
        # 获取请求返回值
        resjson = json.loads(res.content)
        #
        # 判断是否有多个预期值断言
        if jsonpaths.find(",") > 0:
            # 切片预期值变成list
            expect = expect.split(",")
            # 切片jsonpath
            jsonpaths = jsonpaths.split(",")
            num = 0
            assert_ex = []
            LoggerInfo().logger().info('多个json数据开始解析。。。。。。')
            for j in jsonpaths:
                # 获得预期jsonpath路径下的值
                result = jsonpath.jsonpath(resjson, expr=j)
                # 把所有实际返回值加入assert_ex列表中
                js_value = str(result[0])
                assert_ex.append(js_value)
                num = num + 1
            LoggerInfo().logger().info("多个预期值判言。。。。。。。")
            # 断言预期值和实际返回值对比
            assert expect == assert_ex
        else:
            # 获得预期jsonpath路径下的值
            result = jsonpath.jsonpath(resjson, expr=jsonpaths)
            # 断言预期值和实际返回值对比
            LoggerInfo().logger().info("单个预期值判言。。。。。。。")
            assert expect.strip() == str(result[0])
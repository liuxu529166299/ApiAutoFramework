# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :operator_Common
# @Date     :2020/11/28 10:20
# @Author   :刘旭
-------------------------------------------------
"""
import requests
import json
from logger.logger import LoggerInfo


class operator_Common:
    log = LoggerInfo().logger()

    # requests的post请求
    def post(self, url, data=None, headers=None, **kargs):
        self.log.info("执行post请求开始。。。。。。。。。。。。。")
        try:
            response = requests.post(url=url, data=data, headers=headers)
        except Exception as e:
            self.log.error("执行post请求出错，请查看问题！原因: s%", e)
        return response

    # requests的get请求
    def get(self, url, params=None, headers=None, **kargs):
        self.log.info("执行get请求开始。。。。。。。。。。。。")
        try:
            response = requests.get(url=url, params=params, headers=headers)
        except Exception as e:
            self.log.error("执行get请求出错，请查看问题！原因: s%", e)
        return response

    def request(self, requestMethod, requestUrl, paramsType, requestData=None, headers=None):
        # 判断requestMethod是否是post
        if requestMethod.lower() == "post":
            # paramsType是form表单提交
            if paramsType == "form":
                response = self.post(url=requestUrl, data=requestData, headers=headers
                                     )
                return response
            # json提交
            elif paramsType == 'json':
                requestData = eval(requestData)
                requestData = json.dumps(requestData)
                headers = eval(headers)
                response = self.post(url=requestUrl, data=requestData, headers=headers
                                     )
                return response

        # 判断requestMethod是否是get
        elif requestMethod == "get":
            if paramsType == "url":

                request_url = "%s%s" % (requestUrl, "" if requestData is None else requestData)
                if headers != "":
                    headers = json.loads(headers)
                response = self.get(url=request_url, headers=headers)

                return response
            elif paramsType == "params":
                response = self.get(url=requestUrl, params=requestData, headers=headers)
                return response

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :runner
# @Date     :2020/11/28 10:20
# @Author   :刘旭
-------------------------------------------------
"""
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "./test_case/test_case.py", "--alluredir", "./report/xml"])

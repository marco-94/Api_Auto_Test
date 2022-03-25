# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
from config.config import BASE_PATH, REPORT_PATH
from utils import userinfo
import time

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(BASE_PATH, pattern="testCase.py")
    result = BeautifulReport(test_suite)
    result.report(
        filename='testreport-'+userinfo.case_title()+'-'+time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()),
        description=userinfo.case_title(),
        report_dir=REPORT_PATH)



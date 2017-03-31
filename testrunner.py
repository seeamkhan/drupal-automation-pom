#!/usr/bin/env python
# coding: utf-8
import unittest, time, os
from custom_methods import Logger, Email_Sender
from basetestcase import BaseTestCase
from basic_testcases import HomePage
from basic_testcases import SiteUp
from search_testcases import Site_Search


class RunTestCases(BaseTestCase):
    def test010_site_up(self):
        output = SiteUp(self).site_up()
        Logger().save_log("test-result-log", output)
        Logger().save_log('temp', output)

    def test020_site_check(self):
        output = HomePage(self.driver).site_check()
        Logger().save_log("test-result-log", output)
        Logger().save_log('temp', output)

    def test_030_site_search(self):
        output = Site_Search(self.driver).do_search()
        Logger().save_log("test-result-log", output)
        Logger().save_log('temp', output)


    def test_050_email(self):
        test_log = open('temp', 'r').read()
        Email_Sender().send_email(test_log, 'test')
        os.remove('temp')


        time.sleep(1)
if __name__ == '__main__':
    unittest.main(verbosity=2)
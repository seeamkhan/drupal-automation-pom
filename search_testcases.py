#!/usr/bin/env python
# coding: utf-8
from selenium.webdriver.common.keys import Keys
from base import BasePage
from elements import HomePageCommonEelements, SearchResultPageElements
from custom_methods import AllCustomMethods


class Site_Search(BasePage):
    message = []
    def __init__(self, driver):
        super(Site_Search, self).__init__(driver)
        self.home = HomePageCommonEelements(self.driver)
        self.element = AllCustomMethods(self.driver)
        self.search = SearchResultPageElements(self.driver)

    def do_search(self):
        self.driver.find_element_by_xpath(self.home.search).send_keys('health')
        self.driver.find_element_by_xpath(self.home.search).send_keys(Keys.RETURN)
        self.element.verify(self.search.search_result_title)
        if 'found' in (self.element.verify(self.search.search_result_listing)):
            self.message.append("Site Search is working properly.")
            print "Search result found. Site Search is working properly."
        else:
            self.message.append("Search result not found. Site search may not work properly, please test manually.")
            print "Search result not found. Site search may not work properly, please test manually."
        return self.message

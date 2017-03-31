#!/usr/bin/env python
# coding: utf-8

import requests
from datetime import datetime
from base import BasePage
from elements import HomePageCommonEelements
from custom_methods import AllCustomMethods

class SiteUp(BasePage):
    message = []
    def __init__(self, driver):
        super(SiteUp, self).__init__(driver)

    def site_up(self):
        # Site is UP checking
        status = "Unknown"
        try:
            req = requests.get(self.site_url)
            status = req.status_code, req.reason
            site_status = str(status)
            if site_status == "(200, 'OK')":
                wp_site_status = True
                self.message.append("%s site status: %s" % (self.site_name, site_status))
                print "%s site status: %s" % (self.site_name, site_status)
            else:
                self.message.append("%s site status: %s" % (self.site_name, site_status))
                print "%s site status: %s" % (self.site_name, site_status)
        except requests.exceptions.ConnectionError as e:
            self.message.append("%s site has the following error:\n%s" %(self.site_name, e))
            print "%s site has the following error:\n%s" %(self.site_name, e)
        return self.message

class HomePage(BasePage):
    message = []
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.home = HomePageCommonEelements(self.driver)
        self.element = AllCustomMethods(self.driver)

    def site_check(self):
        self.driver.get(self.site_url)
        print "Site URL: %s" % self.site_url
        self.message.append('Testing started at: ' + str(datetime.now()))
        print 'Testing started at: ' + str(datetime.now())

        # Check site search box
        if "found" in self.element.verify(self.home.search):
            self.message.append("Site search box leaded properly.")
            print "Site search box leaded properly."
        else:
            self.message.append("Site search box did not load properly.")
            print "Site search box did not load properly."

        # Check top navigation
        if "found" in self.element.verify(self.home.top_nav):
            self.message.append("Site Top Navigation leaded properly.")
            print "Site Top Navigation leaded properly."
        else:
            self.message.append("Site Top Navigation did not load properly.")
            print "Site Top Navigation did not load properly."

        # Check Logo
        if "found" in self.element.verify(self.home.logo):
            self.message.append("Site Logo leaded properly.")
            print "Site Logo leaded properly."
        else:
            self.message.append("Site Logo did not load properly.")
            print "Site Logo did not load properly."

        # Check site Inner Navigation
        if "found" in self.element.verify(self.home.inner_nav):
            self.message.append("Site Inner Navigation leaded properly.")
            print "Site Inner Navigation leaded properly."
        else:
            self.message.append("Site Inner Navigation did not load properly.")
            print "Site Inner Navigation did not load properly."

        # Check site Hero Image
        if "found" in self.element.verify(self.home.hero):
            self.message.append("Site Hero Image leaded properly.")
            print "Site Hero Image leaded properly."
        else:
            self.message.append("Site Hero Image did not load properly.")
            print "Site Hero Image did not load properly."

        # Check site Our Activity section
        if "found" in self.element.verify(self.home.our_activity):
            self.message.append("Site Our Activity section leaded properly.")
            print "Site Our Activity section leaded properly."
        else:
            self.message.append("Site Our Activity section did not load properly.")
            print "Site Our Activity section did not load properly."

        # Check site Our Work section
        if "found" in self.element.verify(self.home.our_work):
            self.message.append("Site Our Work section leaded properly.")
            print "Site Our Work section leaded properly."
        else:
            self.message.append("Site Our Work section did not load properly.")
            print "Site Our Work section did not load properly."

        # Check site How We Do section
        if "found" in self.element.verify(self.home.how_we_do):
            self.message.append("Site How We Do section leaded properly.")
            print "Site How We Do section leaded properly."
        else:
            self.message.append("Site How We Do section did not load properly.")
            print "Site How We Do section did not load properly."

        # Check site Impact section
        if "found" in self.element.verify(self.home.impact):
            self.message.append("Site Impact section leaded properly.")
            print "Site Impact section leaded properly."
        else:
            self.message.append("Site Impact section did not load properly.")
            print "Site Impact section did not load properly."

        # Check site Left floating menu
        if "found" in self.element.verify(self.home.float_menu):
            self.message.append("Site Left floating menu leaded properly.")
            print "Site Left floating menu leaded properly."
        else:
            self.message.append("Site Left floating menu did not load properly.")
            print "Site Left floating menu did not load properly."

        # Check site footer section
        if "found" in self.element.verify(self.home.footer):
            self.message.append("Site footer section leaded properly.")
            print "Site footer section leaded properly."
        else:
            self.message.append("Site footer section did not load properly.")
            print "Site footer section did not load properly."

        # Check site footer navigation
        if "found" in self.element.verify(self.home.footer_navigate):
            self.message.append("Site footer navigation leaded properly.")
            print "Site footer navigation leaded properly."
        else:
            self.message.append("Site footer navigation did not load properly.")
            print "Site footer navigation did not load properly."

        # Check site footer more section
        if "found" in self.element.verify(self.home.footer_more):
            self.message.append("Site footer more section leaded properly.")
            print "Site footer more section leaded properly."
        else:
            self.message.append("Site footer more section did not load properly.")
            print "Site footer more section did not load properly."

        # Check site footer social icons
        if "found" in self.element.verify(self.home.footer_social_icons):
            self.message.append("Site footer social icons leaded properly.")
            print "Site footer social icons leaded properly."
        else:
            self.message.append("Site footer social icons did not load properly.")
            print "Site footer social icons did not load properly."

        # Check site footer subscription link
        if "found" in self.element.verify(self.home.footer_subscribe):
            self.message.append("Site footer subscription link leaded properly.")
            print "Site footer subscription link leaded properly."
        else:
            self.message.append("Site footer subscription link did not load properly.")
            print "Site footer subscription link did not load properly."

        # Check site footer policies section
        if "found" in self.element.verify(self.home.footer_policies):
            self.message.append("Site footer policies section leaded properly.")
            print "Site footer policies section leaded properly."
        else:
            self.message.append("Site footer policies section did not load properly.")
            print "Site footer policies section did not load properly."

        # Take screen-shot
        self.driver.save_screenshot("website-screen.png")
        return self.message

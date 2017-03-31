import sys

class BasePage(object):
    """All page objects inherit from this."""

    def __init__(self, driver):
        self.driver = driver
        # self.log = ''
        # self.message = []
        # self.site_url = 'http://af.stg.lin.panth.com/'
        self.site_url = sys.argv[1]
        self.site_name = 'APha Foundation'

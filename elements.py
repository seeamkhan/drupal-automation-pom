from base import BasePage


class HomePageCommonEelements(BasePage):
    def __init__(self, driver):
        super(HomePageCommonEelements, self).__init__(driver)

        # Page elements
        self.search = "//input[@name='search_block_form']"
        self.top_nav = "//div[@class='main-wrapper top-header-color']"
        self.logo = "//a[@class='logo']"
        self.inner_nav = "//div[@class='nav-collapse collapse navbar-responsive-collapse']"
        self.hero = "//div[@class='hero-shade']"
        self.our_activity = "//div[@class='our-activities']"
        self.float_menu = "//li[@class='first last expanded']"
        self.our_work = "//div[@class='our-work']"
        self.how_we_do = "//div[@class='how-we-do']"
        self.impact = "//div[@class='impact-the-transformation']"
        self.footer = "//div[@class='footer']"
        self.footer_navigate = "//div[@class='span3']//ul[@class='menu nav nav-list']"
        self.footer_more = "//div[@class='span4']//ul[@class='menu nav nav-list']"
        self.footer_social_icons = "//div[@class='span5']//div[@class='nav-header-social-icons']"
        self.footer_subscribe = "//div[@class='span5']//a[contains(text(), 'Subscribe to our newsletter')]"
        self.footer_policies = "//div[@class='span5']//div[@id='block-block-6']"

class SearchResultPageElements(BasePage):
    def __init__(self, driver):
        super(SearchResultPageElements, self).__init__(driver)

        # Page elements
        self.search_result_title = "//h2[contains(text(), 'Search results')]"
        self.search_result_listing = "//ul[@class='search-results apachesolr_search-results']"

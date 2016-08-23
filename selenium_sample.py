import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s (%(threadName)-10s) %(message)s',
#                     filename='test.log',
#                     datefmt='%Y/%m/%d %H:%M:%S'
#                     )

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1400,1000)

    def test_search_in_python_OK(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("org1.png")
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_NG(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("org4.png")
        assert "No results found." in driver.page_source

    def test_search_in_google_OK(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn(u"Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("org2.png")
        assert "No results found." not in driver.page_source

    # def test_search_in_python_org3(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     driver.save_screenshot("org3.png")
    #     assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
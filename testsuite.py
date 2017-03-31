import unittest
# import HTMLTestRunner
import os
from testrunner import RunTestCases

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
run_all_tests = unittest.TestLoader().loadTestsFromTestCase(RunTestCases)

# Create test suite:
smoke_test = unittest.TestSuite(run_all_tests)

# run the suite
unittest.TextTestRunner(verbosity=1).run(smoke_test)

# The following section is for crating HTML test report using HTML test runner.
# open the report file
# outfile = open(dir + "/SmokeTestReport.html", "w")

# configure HTMLTestRunner options
# runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests')

# run the suite using HTMLTestRunner
# runner.run(smoke_test)
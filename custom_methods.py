#!/usr/bin/env python
# coding: utf-8

from base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Conf_Reader
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders



class AllCustomMethods(BasePage):
    def __init__(self, driver):
        super(AllCustomMethods, self).__init__(driver)

    def verify(self, elem, time=5):
        """
        Method for verifying an element (XPATH) present or not.
        :param elem: xpath of an element
        :param time: how long should we wait for the element to load.
        :return: predefined message depending on element found or not.
        """
        elem_status = ''
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem)))
            elem_status = "%s element found." % elem
        except:
            elem_status = "Driver did not recognize '%s' element." % elem
        # print elem_status
        return elem_status

class Logger():
    """
    Method for saving output in a log file.
    """
    def save_log(self, file_name, message):
        log = '\n'.join(message)
        # file_name = "test-result-log"
        target = open(file_name, 'a')
        # target.truncate()
        target.write("\n\n%s" % log)
        target.close()

class Email_Sender():
    """
    Method for sending automated email.
    """
    def send_email(self, email_body, mode = 'test'):
        if mode=='live':
            toaddr = ['sdteam@dev.panth.com']
        else:
            toaddr = ['seeam@dev.panth.com']
        # email_body = '\n'.join(email_body)  # If the email_body parameter is a string then you need to comment out this line.

        print "Sending email, please wait..."
        email_log = ''
        message = []
        credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
        fromaddr = Conf_Reader.get_value(credentials_file, 'EMAIL_USER')
        email_password = Conf_Reader.get_value(credentials_file, 'EMAIL_PASSWORD')

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        # msg['To'] = toaddr
        ", ".join(toaddr)
        msg['Subject'] = "Pantheon Drupal Update Notification Email"
        msg.attach(MIMEText(email_body, 'plain'))

        # FOR ATTCAHMENTS
        filename = "website-screen.png"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'website-screen.png')
        attachment = open(file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        # END OF Attachments change

        server = smtplib.SMTP('dev.panth.com', 25)
        server.starttls()
        server.login(fromaddr, email_password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print 'Email Sent.'
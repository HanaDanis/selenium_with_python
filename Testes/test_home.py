import sys
sys.path.insert(0, r'C:\Users\Hana Danis\Downloads\Bootcamp-automation\python\HtmlPro')
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locators.locatorsHome import *
from Util.WriteToLog import *
from selenium import webdriver
from dotenv import load_dotenv
import unittest
import datetime
import time
import json
import os
import re


class TestHome(unittest.TestCase):
    
    load_dotenv()
    log = Log()
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(os.getenv('HOMEDRIVER') )
        with open(os.getenv('JSONPATH'), 'r') as f:
          self.data = json.load(f)
        self.a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.pattern = os.getenv('PATTERN1') 

    def test_firstname(self):
        """
        Hana, 20-2-23
        test check special characters
        and length firstname
        """
        try:
            firstname = self.driver.find_element(*LocatorsHome.firstname_locator)
            json_firstname = self.data['FirstName']
            firstname.send_keys(json_firstname)
            self.assertEqual(firstname.text, json_firstname)
            assert re.match(self.pattern, json_firstname)
            assert int(os.getenv('MIN')) <= len(json_firstname) <= int(os.getenv('MAX'))
            self.log.write(f'{self.a} test firstname success\n')
        except Exception as e:
            self.log.write(f'{self.a} test firstname unsuccess\n {e} ') 
            self.driver.save_screenshot(r'Screenshots\screenshot.png')  
            
    def test_lastname(self):
        """
        Hana, 20-2-23
        test check special characters
        and length lastname
        """
        try:
            lastname = self.driver.find_element(*LocatorsHome.lastname_locator)
            json_lastname = self.data['LastName']
            lastname.send_keys(json_lastname)
            self.assertEqual(lastname.text, json_lastname)
            assert re.match(self.pattern, json_lastname)
            assert int(os.getenv('MIN')) <= len(json_lastname) <= int(os.getenv('MAX'))
            self.log.write(f'{self.a} test lastname success\n')
        except Exception as e:
            self.log.write(f'{self.a} test lastname unsuccess\n {e} ') 
            self.driver.save_screenshot(r'Screenshots\screenshot.png')  
            
    def test_firstname_null(self):  
        """
        Hana, 20-2-23
        test check firstname characters
        not null 
        """        
        try:
            firstname = self.driver.find_element(*LocatorsHome.firstname_locator)
            json_firstname = os.getenv('None')
            self.assertEqual(firstname.text, json_firstname)
            self.log.write(f'{self.a} test firstname_null success\n')
        except Exception as e:
            self.log.write(f'{self.a} test firstname_null unsuccess\n {e} ') 
            self.driver.save_screenshot(r'Screenshots\screenshot.png')   
    
    def test_lastname_null(self):  
        """
        Hana, 20-2-23
        test check lastname characters
        not null 
        """          
        try:
            lastname = self.driver.find_element(*LocatorsHome.lastname_locator)
            json_lastname = os.getenv('None')
            self.assertEqual(lastname.text, json_lastname)
            self.log.write(f'{self.a} test lastname_null success\n')
        except Exception as e:
            self.log.write(f'{self.a} test lastname_null unsuccess\n {e} ') 
            self.driver.save_screenshot(r'Screenshots\screenshot.png') 
       
    def test_email(self):
        """
        Hana, 20-2-23
        test check email is valid
        """
        try:
            email = self.driver.find_element(*LocatorsHome.email_locator)
            json_email = self.data['email']
            email.send_keys(json_email)
            self.assertEqual(email.text, json_email)
            assert re.match(os.getenv('PATTERN2'), json_email)
            self.log.write(f'{self.a} test email success\n')
        except Exception as e:
            self.log.write(f'{self.a} test email unsuccess\n {e} ') 
            self.driver.save_screenshot(r'Screenshots\screenshot.png') 
     
    def test_female_radio_button(self):
        """
        Hana, 20-2-23
        the test check ןf choosing a female gender
        locks choosing a different gender
        """
        try:
            radio_buttonF = self.driver.find_element(*LocatorsHome.female_locator)
            radio_buttonM = self.driver.find_element(*LocatorsHome.male_locator)
            radio_buttonO = self.driver.find_element(*LocatorsHome.other_locator)
            radio_buttonF.click()
            self.assertTrue(radio_buttonF.is_selected())  
            self.assertFalse(radio_buttonM.is_selected())
            self.assertFalse(radio_buttonO.is_selected())
            self.log.write(f'{self.a} test female radio button success\n') 
        except Exception as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')            
            self.log.write(f'{self.a} test female radio button unsuccess\n {e}') 
            
    def test_male_radio_button(self):
        """
        Hana, 20-2-23
        the test check ןf choosing a male gender
        locks choosing a different gender
        """
        try:
            radio_buttonF = self.driver.find_element(*LocatorsHome.female_locator)
            radio_buttonM = self.driver.find_element(*LocatorsHome.male_locator)
            radio_buttonO = self.driver.find_element(*LocatorsHome.other_locator)
            radio_buttonM.click()
            self.assertTrue(radio_buttonM.is_selected())  
            self.assertFalse(radio_buttonF.is_selected())
            self.assertFalse(radio_buttonO.is_selected())
            self.log.write(f'{self.a} test male radio button success\n') 
        except Exception as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')            
            self.log.write(f'{self.a} test male radio button unsuccess\n {e}') 

    def test_other_gender_radio_button(self):
        """
        Hana, 20-2-23
        the test check ןf choosing a other gender
        locks choosing a different gender
        """
        try:
            radio_buttonF = self.driver.find_element(*LocatorsHome.female_locator)
            radio_buttonM = self.driver.find_element(*LocatorsHome.male_locator)
            radio_buttonO = self.driver.find_element(*LocatorsHome.other_locator)
            radio_buttonO.click()
            self.assertTrue(radio_buttonO.is_selected())  
            self.assertFalse(radio_buttonF.is_selected())
            self.assertFalse(radio_buttonM.is_selected())
            self.log.write(f'{self.a} test other gender radio button success\n') 
        except Exception as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')            
            self.log.write(f'{self.a} test other gender radio button unsuccess\n {e}') 
            
    def test_links_count(self):
        """
        Hana, 20-2-23
        test check links count
        """
        try:
            element = self.driver.find_elements(*LocatorsHome.links_locator)
            self.assertEqual(len(element),int(os.getenv('NUM1')))
            self.log.write(f'{self.a} test links count success\n') 
        except Exception as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')            
            self.log.write(f'{self.a} test links count unsuccess\n {e} ') 
     
     
    def test_select_TelAviv_city(self):
        """
        Hana, 20-2-23
        test check if the selected dropdown
        have the same value
        """
        try:
            city_dropdown = self.driver.find_elements(*LocatorsHome.city_locator)
            self.assertEqual(city_dropdown[int(os.getenv('ZERO'))].get_attribute("value"), os.getenv('CITY'))
            self.log.write(f'{self.a} test select TelAviv city success\n') 
        except Exception as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')            
            self.log.write(f'{self.a} test select TelAviv city unsuccess\n {e} ')
   

           
    def test_link_windy(self):
        """
        Hana, 20-2-23
        test check  if can access
        the windy website
        """   
        try:
            element = self.driver.find_element(*LocatorsHome.windy_locator)
            element.click()
            self.assertAlmostEqual(self.driver.title, os.getenv('WINDY_TITLE'))
            self.log.write(f'{self.a} test link windy success\n')
        except StaleElementReferenceException as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')
            self.log.write(f'{self.a} test link windy unsuccess\n {e}') 
        
    def test_link_nextpage(self):
        """
        Hana, 20-2-23
        test check  if can access
        the nextPage page
        """        
        try:
            element = self.driver.find_element(*LocatorsHome.nextpage_locator)
            self.driver.execute_script("arguments[0].target='_blank'; arguments[0].click();", element)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(10)
            self.assertAlmostEqual(self.driver.title, os.getenv('NEXTPAGE_TITLE'))
            self.log.write(f'{self.a} test link nextpage success\n')
        except StaleElementReferenceException as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')
            self.log.write(f'{self.a} test link nextpage unsuccess\n {e}')  
            
    def test_link_tera(self):
        """
        Hana, 20-2-23
        test check  if can access
        the tera website
        """
        try:
            element = self.driver.find_element(*LocatorsHome.tera_locator)
            element.click()
            self.assertAlmostEqual(self.driver.title, os.getenv('TERA_TITLE'))
            self.log.write(f'{self.a} test link tera success\n')
        except StaleElementReferenceException as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')
            self.log.write(f'{self.a} test link tera unsuccess\n {e}')     
            
    def test_link_java(self):
        """
        Hana, 20-2-23
        test check if can access
        the java website
        """        
        try:
            element = self.driver.find_element(*LocatorsHome.java_locator)
            element.click()
            self.assertEqual(self.driver.title, os.getenv('JAVA_TITLE'))
            self.log.write(f'{self.a} test link java success\n')
        except StaleElementReferenceException as e:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')
            self.log.write(f'{self.a} test link java unsuccess\n {e}')         
                       
    def test_link_youtube(self):
        """
        Hana, 20-2-23
        test check  if can access
        the YouTube website
        """
        try:
            elements = self.driver.find_elements(*LocatorsHome.links_locator)
            element = elements[int(os.getenv('NUM2'))]
            element.click()
            self.assertEqual(self.driver.title, os.getenv('YOUTUBE_TITLE'))
            self.log.write(f'{self.a} test link youtube success\n')
        except StaleElementReferenceException:
            self.driver.save_screenshot(r'Screenshots\screenshot.png')
            self.log.write(f'{self.a} test link youtube unsuccess\n {e}')    
    
    

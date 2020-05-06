'''
Created on Mar 27, 2020
This is a python program that finds all deployed objects on HCI Monitor. Prints object name, type, deployed date, deployer, version

@author: 08925
'''

import os,sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup as bs 




#===============================================================================
# class ChromeDriverWindows():
# 
#     def test(self):
#         # Instantiate Chrome Browser Command
#         driver = webdriver.Chrome(executable_path="C:\\Users\\08925\\Downloads\\chromedriver.exe")
#         # Open the provided URL
#         driver.get("http://www.letskodeit.com")
# 
# cc = ChromeDriverWindows()
# cc.test()
#===============================================================================

# Instantiate Chrome Browser Command
#driver = webdriver.Chrome(executable_path="C:\\Users\\08925\\Downloads\\chromedriver.exe")
#driver = webdriver.Chrome()
#chrome_options = webdriver.ChromeOptions(); 
#chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
#driver = webdriver.Chrome(options=chrome_options);
#driver = webdriver.Chrome()  
# Open the provided URL

class FindByLinkText():

    def test(self):
        baseUrl = 'https://l250097-tmn.hci.us3.hana.ondemand.com/itspaces/shell/monitoring/Artifacts/%7B%22type%22:%22ALL%22,%22status%22:%22STARTED%22%7D'
#        loginUrl = "https://accounts.sap.com/saml2/idp/sso"
        freq = 0.5 # seconds
        timeout = 6
        driver = webdriver.Ie()
        driver.get(baseUrl)
        #=======================================================================
        # userXpath = "//input[@id='j_username']"
        # userblock = driver.find_element_by_xpath(userXpath);
        # userblock.send_keys(loginUser)
        # user_passwd_xpath="//input[@name='j_password']"
        # user_passwd = driver.find_element_by_xpath(user_passwd_xpath)
        # user_passwd.send_keys(loginOther)
        #=======================================================================
        signin_button_xpath="//button[@id='logOnFormSubmit']"
        signin_button = driver.find_element_by_xpath(signin_button_xpath)
        signin_button.click()
        driver.get(baseUrl)
        wait_path = "//span[@id='__header0-innerTitle']"
        try:
            myFrame = WebDriverWait(driver, timeout, freq, ignored_exceptions=[NoSuchElementException\
                ]).until(EC.presence_of_element_located((By.XPATH, wait_path)))
        except TimeoutException:
            x = 1
        elements_xpath = "//tbody/tr[contains(@id,'__item4-ARTIFACTS_TABLE-')]"
        elements = driver.find_elements_by_xpath(elements_xpath)
        ele_count = len(elements)//2
        print_string = "FLOW,TYPE,DEPLOYED_ON,DEPLOYED_BY,VERSION"
        print(print_string)
        for i in range(0, ele_count):
            flow_elements_xpath = "//tbody/tr[@id='__item4-ARTIFACTS_TABLE-$ELENUM']".replace('$ELENUM',str(i))
            flow_element = driver.find_element_by_xpath(flow_elements_xpath)
            selected_tf = flow_element.get_attribute("aria-selected")
            flow_name_xpath = "//tbody//td/span[contains(@id,'__text10-ARTIFACTS_TABLE-$ELENUM')]".replace('$ELENUM',str(i))
            flow_name = driver.find_element_by_xpath(flow_name_xpath).text
            flow_type_xpath = "//tbody/tr[@id='__item4-ARTIFACTS_TABLE-$ELENUM-sub']".replace('$ELENUM',str(i))
            flow_type = driver.find_element_by_xpath(flow_type_xpath).text
            if selected_tf != "true":
                flow_element.click()
                id_path = "//div/span[text()='ID: $FLOW']".replace('$FLOW',flow_name)
                try:
                    myEle = WebDriverWait(driver, timeout, freq, ignored_exceptions=[NoSuchElementException\
                        ]).until(EC.presence_of_element_located((By.XPATH, id_path)))
                except TimeoutException:
                    x = 1
            deployed_xpath = "//div/span[contains(text(),'Deployed On: ')]"
            deployed = driver.find_element_by_xpath(deployed_xpath).text.replace("Deployed On: ",'')
            deployedby_xpath = "//div/span[contains(text(),'Deployed By: ')]"
            deployedby = driver.find_element_by_xpath(deployedby_xpath).text.replace("Deployed By: ",'')
            version_xpath = "//div/span[contains(text(),'Version: ')]"
            version = driver.find_element_by_xpath(version_xpath).text.replace("Version: ",'')
            print_string = "FLOW,TYPE,DEPLOYED,DEPLOY_BY,VERSION".replace('FLOW',flow_name).replace('TYPE',flow_type).replace('DEPLOYED','"'+deployed+'"')\
                  .replace('DEPLOY_BY',deployedby).replace('VERSION',version)
            print(print_string)
        print()
            
cm_num = sys.argv[1]
ff = FindByLinkText()
ff.test()
print("Finished")


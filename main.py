import time
import subprocess
import secret
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Browser:
    def __init__(self, driver: str):
        # Initialize the browser service an browser instance
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        # Opens a webpage in the new bowser
        self.browser.get(url)

    def close_browser(self):
        # Closes the browser
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        # Finds an imput field by the specified locators (by and value) and enters text into it
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        # Finds a button by the specified locator like above and clicks it
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_olat(self, username: str, password: str):
        # Fills in the login form in Olat with the provided username and password
        self.add_input(by=By.ID, value='o_fiooldap_login_name', text=username)
        self.add_input(by=By.ID, value='o_fiooldap_login_pass', text=password)
        self.click_button(by=By.ID, value='o_fiooldap_login_button')

class Network:
    def get_connected_wlan_name():
        # Uses subprocess to run the 'netsh wlan show interfaces' command and takes the output
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('latin-1')
        # Uses regex to find the wlan name (SSID) in the output
        matches = re.findall(r"SSID\s+:\s(.+)\r\n", output)
        if matches:
            # If there is a match, return the first SSID found
            return matches[0]
        # If no SSID is found, return None. Means we are not connected to Wlan. A alert would be nice here
        return None



if __name__ == '__main__':
    
    connected_wlan = Network.get_connected_wlan_name()

    # Let's pretend that this is the school wlan
    if connected_wlan == 'FRITZ!Repeater 6000':
        # Open Microsoft Teams
        os.startfile(r"C:\\Users\\minde\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk")

        # Start browser automation
        browser = Browser('drivers\chromedriver.exe')
        browser.open_page('https://olat.bbw.ch')
        time.sleep(3)
        # I am using imported username and password values so you can't see my pw
        browser.login_olat(secret.username, secret.password)
        time.sleep(10)
        browser.close_browser()

    # check if connected to hypotetical home wlan
    if connected_wlan == 'home wlan':
        # Open Discord
        os.startfile(r"C:\\Users\\minde\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
        # Open Spotify
        os.startfile(r"C:\\Users\\minde\\OneDrive\\Desktop\\Spotify.lnk")

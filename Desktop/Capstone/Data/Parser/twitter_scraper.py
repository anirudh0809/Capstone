from bs4 import BeautifulSoup
import pprint
import time
from csv import DictWriter
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import date, timedelta
import os
import json


def driver(type):
    if type == 1:
        driver_type = webdriver.Chrome()
    elif type == 2:
        driver_type = webdriver.Ie()
    elif type == 3:
        driver_type = webdriver.Safari()
    elif type == 4:
        driver_type = webdriver.Opera()
    driver_type.wait = WebDriverWait(driver_type,4)
    return driver_type




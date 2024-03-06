

import pandas as pd
from selenium import webdriver
# from selenium.webdriver.chrome.options import ChromeOptions


# Atidarykite naršyklę ir eikite į norimą puslapį
# options = ChromeOptions()
browser = webdriver.Chrome()
browser.get('https://www.marketwatch.com/investing/stock/tsla/download-data?mod=mw_quote_tab')




data = pd.read_csv('https://www.example.com/nuoroda/iki/csv-failo.csv')




print(data.head()) 



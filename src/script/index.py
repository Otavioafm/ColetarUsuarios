import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

caminhoDriver = r"C:\Users\otavi\OneDrive\Área de Trabalho\coletarInvestidor\src\driver\chromedriver.exe"
chrome_options = Options()
googleDriver = webdriver.Chrome(service=Service(caminhoDriver), options=chrome_options)

googleDriver.get("https://www.linkedin.com/feed/")

def log():
    login =googleDriver.find_element(By.XPATH,'//*[@id="username"]')
    login.send_keys("findinvest24@gmail.com")

    time.sleep(1)

    senha =googleDriver.find_element(By.XPATH,'//*[@id="password"]')
    senha.send_keys("zaxS6EG%N-CvXH&U,$")

    btnEntrar =googleDriver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]')
    btnEntrar.click()
log()

time.sleep(10)

def coletarNomes():
    exibirNomes =googleDriver.find_element(By.XPATH, '//*[@id="ember355"]')
    exibirNomes.click()
coletarNomes()









from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime

TIBIA_BLACKJACK_URL = 'https://tibiablackjack.com/crash'

class Browser:
    def __init__(self):
        """
        Constrói instancia do browser
        """
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    def open_url(self, url):
        """
        Abre url na aba ativa no browser
        """
        print('open')
        self.driver.get(url)
    
    def close(self):
        print('close')
        #  

    def find_element_by_class_name(self, element):
        """
        Procura por um elemento na página a partir de sua classe
        """
        trial = 0
        last_results = pd.DataFrame()
        second_value = None
        third_value = None
        file_name = 'blackjack-report.csv'

        try:
            last_first_value = None
            last_second_value = None
            last_third_value = None
            while True:
                first_value = self.driver.find_element_by_xpath(element).text
                second_value = self.driver.find_element_by_xpath('/html/body/div/main/div/div[1]/section[2]/div[3]/div[2]/div[2]/div/span').text
                third_value = self.driver.find_element_by_xpath('/html/body/div/main/div/div[1]/section[2]/div[3]/div[2]/div[3]/div/span').text
                if first_value != last_first_value and second_value != last_second_value and third_value != last_third_value:
                    last_first_value = first_value
                    last_second_value = second_value
                    print('novo valor')
                    third_value = last_third_value
                    last_results = last_results.append({
                        'results': first_value.replace('x', ''),
                        'timestamp': datetime.now()
                    }, ignore_index=True)
                    if len(last_results) % 10 == 0:
                        try:
                            df = pd.read_csv(file_name)
                            df = df.append(last_results)
                            df.to_csv(file_name, index=False)
                            print('salvando ja existente')
                        except:
                            print('salvando pela primeira vez')
                            last_results.to_csv(file_name, index=False)
                            last_results = pd.DataFrame()

                sleep(1)
                trial = trial + 1
        except Exception as e:
            print('nao achou, erro', e)
            raise e

class Agent(Browser):
    def __init__(self):
        super().__init__()
        
agent = Agent()
agent.open_url(TIBIA_BLACKJACK_URL)
sleep(5)
# onde os resultados estão
# trial = '/html/body/div/main/div/div[1]/section[2]/div[3]/div[2]/div[2]/div/span'
trial = '/html/body/div/main/div/div[1]/section[2]/div[3]/div[2]/div[1]/div/span'
# trigger_xpath = '/html/body/div/main/div/div[1]/section[1]/div[2]/div[1]'
agent.find_element_by_class_name(trial)













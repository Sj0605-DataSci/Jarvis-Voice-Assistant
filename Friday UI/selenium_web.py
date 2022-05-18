from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\webdrivers\\chromedriver.exe')

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.google.co.in/search?q=" + query)
        

        
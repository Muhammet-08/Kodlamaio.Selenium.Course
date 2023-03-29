from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By






class Test_KodlamaIo:
    
    def test_invalid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.kodlama.io/")
        sleep(5)
        loginBtn=driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[3]/a")
        loginBtn.click()
        sleep(40)
    

testClass=Test_KodlamaIo()
testClass.test_invalid_login()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #ilgili bekleme işlemlerini ele alcak konu bekleme süreleri içim
from selenium.webdriver.support import expected_conditions as ec #hangi şarta göre bekleme işlemi yapacağını gösterir.
from selenium.webdriver.common.action_chains import ActionChains






class Test_SauceIo:
    
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        

    
    def test_invalid_login(self):
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #ilgili webdriveri maximum 5 sn beklet,until= ne zamana kadar şart olarak,verilen locater visible olunca yani bulunnca uyumayı iptal et
        usernameInput=self.driver.find_element(By.ID,"user-name")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(testResult)
        
    
    def test_valid_login(self):
        
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        #Action Chains zincir misali aksiyonları tek bir yapıya bağlar
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()   
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
            
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(10)
        
        

testClass=Test_SauceIo()
testClass.test_invalid_login()
testClass.test_valid_login()


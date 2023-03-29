from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #ilgili bekleme işlemlerini ele alcak konu bekleme süreleri içim
from selenium.webdriver.support import expected_conditions as ec #hangi şarta göre bekleme işlemi yapacağını gösterir.
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path #klasör oluşturmak için kullanılır.
from datetime import date

#prefix =Z ön ek test_
#postfix

class Test_DemoClass:


    #her testten önce çağırılır.
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        #günü tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
        self.folderPath=str(date.today()) #günün tarihini almaya yarıyor self.folder da tutuyor
        Path(self.folderPath).mkdir(exist_ok=True) #eğer ilgili klasör oluşturulmuşsa yeni klasör oluşturma oluşturulmuş olanı kabul et
        #24.03.2023
        
    
    #her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()


    def readData(self): #test_ olmadığı için pytest bunu görmüyor ve çalıştırmıyor bu bir yardımcı fonksiyondur verileri falan çekmek vs için kullanılır.
        print("x")


    #setup -> test_demoFunc -> teardown
    def test_demoFunc(self):
        #3A Act Arrange Assert
        text="Hello"
        assert text=="Hello"


    #setup -> test_demo2 -> teardown
    def test_demo2(self):
        assert True    


    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","password"),("muhammet","bayrak")]) #burada aşağıdaki metotattaki praamtereleri kullanıp öyle test edecek
    #@pytest.mark.skip() #bu ilgili fonksiyonu durdur(skip ed) çalıştırma.Bu fonksiyonu atla demek kısaca.
    def test_invalid_login(self,username,password):
        self.waitForElementsVisible((By.ID,"user-name"))
        #WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #ilgili webdriveri maximum 5 sn beklet,until= ne zamana kadar şart olarak,verilen locater visible olunca yani bulunnca uyumayı iptal et
        #bunu yapmamızın amacı orada değer girireln yeri bulup daha sonrasında bir değere atamak için
        usernameInput=self.driver.find_element(By.ID,"user-name")

        self.waitForElementsVisible((By.ID,"password"),10)
        #WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text== "Epic sadface: Username and password do not match any user in this service"


    #yukarıda kullanıldı
    def waitForElementsVisible(self,locator,timeout = 5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
        
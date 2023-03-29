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
        

class Test_Sauce:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = "Ödevin test tarihi"+str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)


    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout =5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def test_empty_login(self):
        self.waitForElementVisible(By.ID,"login-button") # bu işlemin asıl amacı sen login button adlı id yi bulana kadar ekranı kapatma
        loginBtn=self.driver.find_element(By.ID,"login-button") #yukarıdaki işlem bu butonu bulduğunda kapanmayacağı için find elemen ile bu veriyi loginBtn ye atıyoruz
        loginBtn.click()

        self.waitForElementVisible(
            By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"
        )

        errorMessage=self.driver.find_element(
            By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"
        )

        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login.png")
        
        assert errorMessage.text =="Epic sadface: Username is required"
        
    
    @pytest.mark.parametrize("username",["locked_out_user","standard_user","problem_user"])
    def test_empty_password(self,username):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))

        self.driver.save_screenshot(
            f"{self.folderPath}/boş-şifre-{username}-giriş.png"
        )

        assert errorMessage.text == 'Epic sadface: Password is required'

    
    @pytest.mark.parametrize("password",["61","81","08","75"])
    def test_empty_username(self,password):
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))

        self.driver.save_screenshot(
            f"{self.folderPath}/boş-isim-{password}-giriş.png"
        )

        assert errorMessage.text == "Epic sadface: Username is required"

    def test_blocked_login(self):
        self.waitForElementVisible(By.ID,"user-name")
        usernameIntput=self.driver.find_element(By.ID,"user-name")
        usernameIntput.send_keys("locked_out_user")

        self.waitForElementVisible(By.ID,"password")
        passwordInput=self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/bloklu-giris.png")

        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."


    def test_succes_login(self):
        self.waitForElementVisible(By.ID,"user-name")
        usernameIntput=self.driver.find_element(By.ID,"user-name")
        usernameIntput.send_keys("standard_user")

        self.waitForElementVisible(By.ID,"password")
        password=self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        self.waitForElementVisible(By.ID,"login-button")
        lgnBtn=self.driver.find_element(By.ID,"login-button")
        lgnBtn.click()
        print("Ürün sayfasına girildi !!!")

    def test_number_of_products(self):
        self.waitForElementVisible(By.ID,"user-name")
        usernameIntput=self.driver.find_element(By.ID,"user-name")
        usernameIntput.send_keys("standard_user")

        self.waitForElementVisible(By.ID,"password")
        password=self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")

        self.waitForElementVisible(By.ID,"login-button")
        lgnBtn=self.driver.find_element(By.ID,"login-button")
        lgnBtn.click()
        print("Ürün sayfasına girildi !!!")

        
        self.waitForElementVisible(By.CLASS_NAME,"inventory_item_description")
        products=self.driver.find_elements(By.CLASS_NAME,("inventory_item_description"))
        number_products=len(products)

        if number_products != 6:
            result=False
            print("Ürün sayısı 6 adet olmalıydı !!!")
            self.driver.save_screenshot(f"{self.folderPath}/ürün_sayıs-standar_user-secret_sauce.png")
            assert result

        else:
            result=True
            print("Ürün adeti doğrudur")
            self.driver.save_screenshot(f"{self.folderPath}/ürün_sayıs-standar_user-secret_sauce.png")
            assert result

    @pytest.mark.parametrize("username","password",[("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
    def test_full_choice_login(self,username,password):
        self.waitForElementVisible(By.ID,"user-name")
        usernameInput=self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible(By.ID,"password")
        passwordInput=self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(By.ID,"password")

        self.waitForElementVisible(By.ID,"login-button")
        lgnBtn=self.driver.find_element(By.ID,"login-button")
        lgnBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-basarili-giris-ve-diğer-giris-türleri.png")

        assert self.driver.current_url== "https://www.saucedemo.com/inventory.html"

        

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_correct_login(self, username, password):
        self.wait_for_element_visible((By.ID, "user-name"))
        name_input = self.driver.find_element(By.ID, "user-name")
        name_input.send_keys(username)

        self.wait_for_element_visible((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

        url = "https://www.saucedemo.com/inventory.html"

        screenshot_file_path = str(Path(self.folder_path) / f"test-correct-login-{username}-{password}.png")
        self.driver.save_screenshot(screenshot_file_path)

        assert self.driver.current_url == url


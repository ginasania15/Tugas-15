import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_success_login(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('jagoqaindonesia@gmail.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, 'Welcome Jago QA')
        self.assertEqual(respon_berhasil, 'Anda Berhasil Login')
    def test_b_failed_login_email_not_registered(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertIn('not found',respon_welcome)
        self.assertIn('Salah', respon_berhasil)
        self.assertEqual(respon_welcome, "User's not found")
        self.assertEqual(respon_berhasil, 'Email atau Password Anda Salah')
    def test_a_email_empty_login(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, 'Gagal Login!')
    def test_a_success_signup(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element_by_id("signUp").click()
        driver.find_element_by_id("name_register").send_keys('Gina Sania')
        time.sleep(1)
        rand = randint(0, 100)
        driver.find_element_by_id("email_register").send_keys('ginasania'+str(rand)+'@gmail.com')        
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('test123')        
        time.sleep(1)
        driver.find_element_by_id("signup_register").click()
        time.sleep(1) 
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, "berhasil")
        self.assertEqual(respon_berhasil, 'created user!')
    def test_email_empty_signup(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element_by_id("signUp").click()
        driver.find_element_by_id("name_register").send_keys('Gina Sania')
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('test123')        
        time.sleep(1)
        driver.find_element_by_id("signup_register").click()
        time.sleep(1) 
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, 'Gagal Register!')
    def test_name_empty_signup(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element_by_id("signUp").click()
        rand = randint(0, 100)
        driver.find_element_by_id("email_register").send_keys('ginasania'+str(rand)+'@gmail.com')        
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('test123')        
        time.sleep(1)
        driver.find_element_by_id("signup_register").click()
        time.sleep(1) 
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, 'Gagal Register!')
    def test_email_duplicat_signup(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element_by_id("signUp").click()
        driver.find_element_by_id("name_register").send_keys('Gina Sania')
        time.sleep(1)
        rand = randint(0, 100)
        driver.find_element_by_id("email_register").send_keys('ginasania15@gmail.com')        
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('test123')        
        time.sleep(1)
        driver.find_element_by_id("signup_register").click()
        time.sleep(1) 
        respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, 'Gagal Register!')
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
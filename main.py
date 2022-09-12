from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://ogrenci.baskent.edu.tr/tr")

# Fetch credentials
credentials = open("credentials.txt")
studentid = credentials.readline()
password = credentials.readline()
credentials.close()

# Login Webpage
search_id = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"user")))
search_id.send_keys(studentid)

search_password = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"password")))
search_password.send_keys(password)

print("Enter Captcha: ")
captcha = input()

search_captcha = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"captcha")))
search_captcha.send_keys(captcha.upper())
search_captcha.send_keys(Keys.RETURN)

sleep(10) # Wait html file to load

# Dashboard Webpage
search_course_management = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Ders İşlemleri")))
search_course_management.click()

search_course_register = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Ders Kayıt")))
search_course_register.click()

sleep(10) # Wait html file to load

coursenamelist = ["BİL387","BİL390","BİL429","ENG460"]
courseclasslist = ["1","1","1","7"]

coursecount = len(coursenamelist)

# Register Webpage
while True:
    for i in range(coursecount):
        search_course_code = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.ID,"ders_kisa_adi")))
        search_course_code.send_keys(coursenamelist[i])

        search_course_class = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.ID,"ders_sube")))
        search_course_class.send_keys(courseclasslist[i])

        search_course_add = WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.ID, "ekle")))
        search_course_add.click()

        sleep(1.5)

        search_modal_close = WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.ID,"bilgilendirmeBtnKapat")))
        search_modal_close.click()

        sleep(1)

        # Clear text fields
        search_course_code.clear()
        search_course_class.clear()

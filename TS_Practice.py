import time
from builtins import print

from selenium import webdriver
from fpdf import FPDF

driver = webdriver.Chrome(executable_path="C:/BIDS/TestProjectPython/Chrome/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.top-seos.com/")
driver.implicitly_wait(5)
print()
# driver.find_element_by_xpath("//a[text()='Features']").click()
# driver.find_element_by_xpath("//a[text()='Projects']").click()
# driver.find_element_by_xpath("//a[text()='Professionals']").click()
# driver.find_element_by_xpath("//a[text()='Jobs']").click()
# driver.find_element_by_xpath("//a[text()='Conference']").click()
# driver.find_element_by_xpath("//a[text()='Blog']").click()
# driver.find_element_by_xpath("//a[text()='Contact us']").click()

driver.find_element_by_xpath("//div[@class='collapse navbar-collapse login-register']/ul/li[9]/a").click()
email = "vinod@promotingwebs.com"
password = "vinod"

driver.find_element_by_id('loginEmail').send_keys(email)
driver.find_element_by_id('loginPassword').send_keys(password)

driver.find_element_by_xpath("//button[@type='button' and @name='login']").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/a").click()

driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/ul/li[1]/a").click()

driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/ul/li[2]/a").click()

driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/ul/li[3]/a").click()

driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[8]/a").click()

WIDTH = 210
HEIGHT = 297

pdf = FPDF(format='Letter')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10,'Login Successfully')

pdf.image("1160279.jpg", WIDTH/2-5, 30, WIDTH/2-5)

pdf.output('LoginPage.pdf', 'F')
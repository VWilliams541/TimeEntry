from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


mon = '//div[@automationdid="nonTimedDaySeparator_0"]'
tues = '//div[@automationdid="nonTimedDaySeparator_1"]'
wed = '//div[@automationdid="nonTimedDaySeparator_2"]'
thurs ='//div[@automationdid="nonTimedDaySeparator_3"]'
fri = '//div[@automationdid="nonTimedDaySeparator_4"]'

options = Options()
options.add_argument("--start-maximized")
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(chrome_options=options)
#insert company specific workday link here
driver.get("")
#Allows time to login with 2FA
sleep(30)

view = driver.find_element(By.XPATH, '//button[@data-automation-id="pex-view-all-apps"]')
view.click()
sleep(2)

time = driver.find_element(By.XPATH, '//button[@aria-label="Time"]')
time.click()
sleep(2)

thisWeek = driver.find_element(By.XPATH, '//button[@class="WCHN WGHN WBTO WC0N WDIN"]')
thisWeek.click()
sleep(3)

#enters time before lunch break
def beforeLunch(day, in1, out1):
    
    elem = driver.find_element(By.XPATH, day)
    ActionChains(driver).move_to_element_with_offset(elem, 5, 0).click().perform()
    sleep(2)

    inTime = driver.find_element(By.XPATH, '//input[starts-with(@aria-labelledby, "56$187009")]')
    inTime.send_keys(in1)
    sleep(1)

    outTime = driver.find_element(By.XPATH, '//input[starts-with(@aria-labelledby, "56$187008")]')
    outTime.click()
    sleep(1)
    outTime.send_keys(out1)
    sleep(1)

    reason = driver.find_element(By.XPATH, '//div[@data-automation-id="selectSelectedOption"]')
    reason.click()
    sleep(1)

    meal = driver.find_element(By.XPATH, '//div[@title="Meal"]')
    meal.click()
    sleep(1)

    ok = driver.find_element(By.XPATH, '//button[@class="WCHN WBTO WC0N WGIN WGHN"]')
    ok.click()
    sleep(3)

#enters time after lunch break
def afterLunch(day, in2, out2):
   
    elem = driver.find_element(By.XPATH, day)
    ActionChains(driver).move_to_element_with_offset(elem, 5, 0).click().perform()
    sleep(2)

    inTime = driver.find_element(By.XPATH, '//input[starts-with(@aria-labelledby, "56$187009")]')
    inTime.send_keys(in2)
    sleep(1)

    outTime = driver.find_element(By.XPATH, '//input[starts-with(@aria-labelledby, "56$187008")]')
    outTime.click()
    sleep(1)
    outTime.send_keys(out2)
    sleep(1)

    reason = driver.find_element(By.XPATH, '//div[@data-automation-id="selectSelectedOption"]')
    reason.click()
    sleep(1)

    out = driver.find_element(By.XPATH, '//div[@title="Out"]')
    out.click()
    sleep(1)

    ok = driver.find_element(By.XPATH, '//button[@class="WCHN WBTO WC0N WGIN WGHN"]')
    ok.click()
    sleep(3)
#beforeLunch(day, time in, time out)
beforeLunch(mon, "8", "12")
beforeLunch(fri, "8", "12")

#afterLunch(day, time in, time out)
afterLunch(mon, "1", "5")
afterLunch(tues, "8", "230")
afterLunch(wed, "8", "5")
afterLunch(thurs, "8", "5")
afterLunch(fri, "1", "5")

#finishes the time submission process
review = driver.find_element(By.XPATH, '//button[@class="WCHN WGHN WBTO WC0N WGIN"]')
review.click()
sleep(2)
submit = driver.find_element(By.XPATH, '//button[@class="WCHN WBTO WC0N WGIN WGHN"]')
submit.click()
sleep(10)
driver.close()

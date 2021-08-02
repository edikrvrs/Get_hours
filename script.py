from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import dotenv_values

config = dotenv_values(".env")

students = []
with open('students.txt') as f:
    for line in f:
        students.append(line.strip())

driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')

driver.get("https://sport.innopolis.university")
driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
username = driver.find_element_by_id("userNameInput")
password = driver.find_element_by_id("passwordInput")
button = driver.find_element_by_id("submitButton")
username.send_keys(config['LOGIN'])
password.send_keys(config['PASSWORD'])
button.click()

for email in students:
    base_url = "https://sport.innopolis.university/dashboard/d/xXmAF_xGz/student-dashboard?orgId=1&from=1610053200000&to=now"
    url = base_url + "&var-studentEmail=" + email

    driver.get(url)
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "flotGaugeValue0"))
        )
    except:
        print('Element not found: ' + email)

    hours = element.text
    print(email + " " + hours)

    with open('hours.txt', 'a') as f:
        f.write(email + " " + hours + '\n')

print('Finished')
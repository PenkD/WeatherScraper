from time import sleep
import tkinter as tk
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import actions
from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button
from selenium.webdriver.common.devtools.v136.input_ import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

root = tk.Tk()
root.title("Weather")
root.configure(background="white")
root.minsize(400, 380)
root.maxsize(400, 380)
root.geometry("400x300+450+130")
entry = tk.Entry(root, width=40, )
entry.pack()
entry.configure(state="readonly")





service = Service(executable_path="chromedriver.exe")
options = Options()
options.add_argument("--headless=new")   # comment out these 3 lines to make Chrome visible
options.add_argument("--disable-gpu")    # comment out these 3 lines to make Chrome visible
options.add_argument("--window-size=1920,1080")    # comment out these 3 lines to make Chrome visible
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.theweathernetwork.com/en")
action = ActionChains(driver)
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[data-testid="location-card"]')
    )
)





input_element = driver.find_element(By.CSS_SELECTOR, '[data-testid="location-card"]')




action.click(input_element).perform()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[data-testid="temperature-text"]')
    )
)




weather = driver.find_element(By.CSS_SELECTOR, '[data-testid="temperature-text"]')


print(weather.text)
entry.configure(state="normal")
entry.delete(0, "end")
entry.insert(tk.END, "The weather is " + weather.text + "°")
entry.configure(state="readonly")
root.mainloop()


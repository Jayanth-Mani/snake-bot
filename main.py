from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

bot = webdriver.Firefox()
bot.get('https://www.google.com/search?q=google+snake+game&rlz=1C1CHBF_enUS914US914&oq=google+snake+game&aqs=chrome..69i57j0i512l9.4277j0j7&sourceid=chrome&ie=UTF-8')
time.sleep(4)
bot.find_element_by_class_name("XlTvtc").click()
time.sleep(3)
bot.find_element_by_class_name("FL0z2d").click()
time.sleep(2)
# bot.find_element_by_class_name("rNjvu").send_keys(Keys.UP)
action = ActionChains(bot)
  
# click the item

element = bot.find_element_by_class_name("ahZmw")
action.click(on_element = element)
  
# send keys
action.send_keys(Keys.DOWN)
action.send_keys(Keys.RIGHT)

# perform the operation
#action.perform()
  
# perform the operation
action.perform()
print("Game ready!")
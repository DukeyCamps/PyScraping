from selenium import webdriver
import time
path_to_driver = '/home/manjaro/Downloads/geckodriver'

fire_driver = webdriver.Firefox(executable_path=path_to_driver)
fire_driver.get("https://web.whatsapp.com")
people = []
print(">>>status : enabled")
time.sleep(10)



try:
	fire_driver.find_element_by_class_xpath("""//html/body/div[1]/div/div/div[3]/div/div[1]/div""")
	print("logged in..resuming in 2...")
	time.sleep(2)
except:
	print("not logged in...10 second pause...")

for x in range(30):
	try:
		print("         chat "+str(x))
		time.sleep(0.5)
		protter = fire_driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[""" + str(x) + """]/div/div/div[2]""")
		print(protter.text + "\n")		
	except:
		print("error occured" +"\n")
	
#JESUS FUCK WHY AM I WASTING
#MY LIFE ON THIS
#SNAP OUT OF IT
#*slap*
#FUCK IT
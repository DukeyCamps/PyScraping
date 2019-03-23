from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
import threading

def full_proc(name="Default"):
    chrome_options = Options()  
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    driver.set_window_size(1024,768)
    driver.get("http://be42c9ce.ngrok.io/")
    jscript_create = '''
    function driverFunction(){
    socket.emit('vote')
    }
    '''
    jscript_exec = '''
    driverFunction()
    '''

    thebutton = driver.find_element_by_xpath("""//*[@id="myButton"]""")
    for x in range(1000):
        print("voted | source : "+name)
        thebutton.click()

    driver.quit()


t1 = threading.Thread(target=full_proc)
t2 = threading.Thread(target=full_proc)
t3 = threading.Thread(target=full_proc)
t4 = threading.Thread(target=full_proc)
t5 = threading.Thread(target=full_proc)
t6 = threading.Thread(target=full_proc)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()





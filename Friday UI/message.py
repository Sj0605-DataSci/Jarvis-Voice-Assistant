# from selenium import webdriver
# import time

# class sendmessage():
#     def __init__(self):
#         self.driver = webdriver.Chrome(executable_path='C:\\webdrivers\\chromedriver.exe')
    
#     def whatsappmessage(self,query,message):
#         self.driver.get(url="https://web.whatsapp.com/")

#         time.sleep(30)
    

#         self.user_name = query
#         user = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(self.user_name))
#         user.click()

#         self.message = message

#         message_box = self.driver.find_element_by_xpath('//div[@class="_2A8P4"]')
#         message_box.send_keys(self.message)

#         message_box = self.driver.find_element_by_xpath('//div[@class = "EBaI7"]')
#         message_box.click()



import pywhatkit as kt
import getpass as gp

class sendmessage():
    p_num = gp.getpass(prompt='Phonenumber:', stream=None)

    msg = input("Type your message")
    hours = int(input("Enter the time for the message in hr"))
    mins = int(input("Enter the time for the message in min"))
    kt.sendwhatmsg(p_num,msg,hours,mins)

w=sendmessage()
 

         

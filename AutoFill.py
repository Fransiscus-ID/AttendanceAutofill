#AUTOFILL BY FRANSISCUS XAVERIUS

import selenium
from selenium import webdriver
import time

#Prints a string to notify you that the script is running
print("AutoFill is waiting for user input")

#waits for the user input (Pilihan means Choices in English, but you're free to change it to whatever.
#all of the statements here are basically copy and pasted, so bear that in mind.
Pilihan = input()
#waits for the user input to determine its course of action.

if Pilihan == 'choice1':
    #this section gets the webdriver and opens up the destination link through the browser that you chose.
    web = webdriver.Chrome()
    web.get('Your form link')
    #lets the browser load the content of the link, to ensure that the elements are interactable.
    time.sleep(3)
    #tells the value of the name and attendee's number (nama lengkap = full name, noAbsen = attendee's number)
    namalengkap = "Your full name"
    noAbsen = "Your attendee's number"
    #finds the destination element that you wish to interact with
    nama = web.find_element_by_xpath(
        'your xpath')
    nama.send_keys(namalengkap)
    #sends the value of namalengkap to the destination element that you wish to interact with
    absen = web.find_element_by_xpath(
        'your xpath')
    absen.send_keys(noAbsen)
    #basically the same as the one before, but for the attendee's number
    Choice1 = web.find_element_by_xpath(
        'your xpath')
    Choice1.click()
    #finds the element, which in this case is one of the options that you may choose from on the attendee's list
elif Pilihan == 'choice2':
    #basically the same as the last statement, but for a different choice.
    web = webdriver.Chrome()
    web.get('form link')

    time.sleep(3)

    namalengkap = "Your name"
    noAbsen = "Your attendee's number"

    nama = web.find_element_by_xpath(
        'your xpath')
    nama.send_keys(namalengkap)
    absen = web.find_element_by_xpath(
        'your xpath')
    absen.send_keys(noAbsen)

    Choice2 = web.find_element_by_xpath(
        'your xpath')
    Choice2.click()


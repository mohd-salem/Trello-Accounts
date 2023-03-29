import sys
from datetime import datetime, timedelta
import datetime as dt
from datetime import date
from datetime import datetime
import datetime
import msvcrt
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from sys import argv
import qrtools
from pyzbar.pyzbar import decode
from urllib.request import urlopen
import urllib.request
from PIL import Image
from selenium import webdriver
from time import sleep
import random
import os
from selenium.webdriver import ActionChains
import re
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pyperclip import copy as clipCopy
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




def connect():
    global board

    global driver
    driver = None

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")

    options.add_argument("--disable-gpu")

    options.add_argument("--silent")
    options.add_argument("--start-maximized")

    # options.add_argument("--headless")

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get('https://trello.com/login')

    print("login to trello")

    driver.find_element_by_xpath(
        '//*[@id="user"]').send_keys("****")

    driver.find_element_by_xpath('//*[@id="login"]').click()

    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="password"]').send_keys("*****")

    sleep(2)

    driver.find_element_by_xpath('//*[@id="login-submit"]/span/span').click()

    sleep(5)

    driver.get('url')

    print("Going to board ")
    mechanism()





def mechanism():
    sleep(15)
    todayList()
    sleep(5)
    timeNow = datetime.datetime.now().time()
    Question = input("do you want to repeat")
    if timeNow.hour >= 19 :
            whats()
            print('the driver is going to Close')
            # driver.close()
    else :
        print('lesa badry')
    if Question == (" "):
        todayList()
        print("well done i will repeat")
        if timeNow.hour >= 19 :
            whats()
            print('the driver is going to Close')
            # driver.close()
    elif Question == (chr(27).encode()):
        driver.close()
        print('the driver is going to Close')
    else:
        print('the driver is going to Close')
        # driver.close()

    


def counting(day):
    ibanPocket , ahmedPocket, MohdPocket, abdelsalam, s ,y  = 0, 0, 0, 0,0,0
    umut = 0
    pocket = 0
    noMethod =''
    noValue =[]
    
    # card = input("Enter the card Num ")
    try:
        for x in range(2, 50):
            A1pat = '//*[@id="board"]/div[' + str(day) + ']/div/div[2]/a[' + str(x) + ']'
            driver.find_element_by_xpath(A1pat).click()
            sleep(3)
            labPrice = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input')
            sellPrice = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input')
            cardExit = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/a')
            addU = driver.find_element_by_xpath ('//*[@id="js-dialog-title"]')
            try:
                s = labPrice.get_attribute('value')
                umut += float(s)
            except:
                countingError =' No toxic code for this Card ' + str(addU.get_attribute('innerHTML'))+ ' and the Card number is ' + str(x) + '    '
                print(countingError)
                noValue.append(countingError) 
            try:
                 y = sellPrice.get_attribute('value')
                 pocket += float(y)
            except:
                countingError =' No SellPrice price for this Card '+ str(addU.get_attribute('innerHTML'))+ ' and the Card number is ' + str(x) + '     '
                print(countingError)
                noValue.append(countingError)

            print(umut)

            print(pocket)

            options = driver.find_elements_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[2]/div/select/option')
            for option in options:
                is_selected = option.is_selected()
                if (is_selected == True) : 
                    kmethod = option.get_attribute('innerHTML')
                    print (kmethod)
                    if (kmethod=='أيبان'or kmethod=='نقدا في المختبر ') : 
                        ibanPocket += float(sellPrice.get_attribute('value'))
                    elif (kmethod=='نقدا مع د أحمد') :
                        ahmedPocket += float(sellPrice.get_attribute('value'))
                    elif (kmethod=='نقدا مع د محمد') :
                        MohdPocket += float(sellPrice.get_attribute('value'))
                    elif (kmethod=='نقدا مع م. عبد السلام ') :
                        abdelsalam += float(sellPrice.get_attribute('value'))
                    else : 
                        addU = driver.find_element_by_xpath ('//*[@id="js-dialog-title"]')
                        noMethod = " No paymet method for the   "+ str(addU.get_attribute('innerHTML')) +"   card    " 
                        noValue.append(noMethod)    
            sleep(0.5)
            tests()
            cardExit.click()
            
    except:
        print('bitti')
        try:
            cardExit.click()
        except: 
            print('there is no opened Cards ')

    umut = str(umut)

    pocket = str(pocket)
    sleep(0.5)
    calc = '//*[@id="board"]/div['+str(day)+']/div/div[2]/a[1]'

    driver.find_element_by_xpath(calc).click()

    cardExit = driver.find_element_by_xpath(
            '//*[@id="chrome-container"]/div[3]/div/div/a')
    # and timeNow.minute >= 30
    summary = 'summary: \n the cash with DrMohd = '+str(MohdPocket)+'\n the cash with DrAhmed = '+str(ahmedPocket)+'\n the transactions with iban = '+str(ibanPocket)+'\n the cash with AhmedAbdelsalam = '+str(abdelsalam) +'\n Errors ='+ str(noValue) + '\n Finaly Total Pocket = '+str(pocket)+ '\n Finaly Total TOXIC CODE = '+str(umut)
    errorSummary = 'errors must be resolved علشان نبقى حبايب يعني =  \n => ' + str(noValue) + '      @marchmcdonald  @elhasanmohamed7821 '
    sleep(1)
    timeNow = datetime.datetime.now().time()
    if timeNow.hour >= 14 :
        for m in range(len(summary)) :
            driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea').send_keys(summary[m])
        driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/div[1]/input').click()
    elif timeNow.hour >= 14 and timeNow.hour < 17  :
        for m in range(len(errorSummary)) :
            driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea').send_keys(errorSummary[m])
        driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/div[1]/input').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input').send_keys(pocket)
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input').send_keys(Keys.ENTER)

    sleep(1)
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input').clear()
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input').send_keys(umut)
    driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input').send_keys(Keys.ENTER)
    sleep(1)

    cardExit.click()


def board():

    umut = 0
    pocket = 0
    card = input("Enter the card Num ")
    try:

        for x in range(2, 50):

            try:

                A1pat = '//*[@id="board"]/div[' + \
                    str(card) + ']/div/div[2]/a[' + str(x) + ']'
                driver.find_element_by_xpath(A1pat).click()
                sleep(1.5)
                labPrice = driver.find_element_by_xpath(
                    '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input')
                sellPrice = driver.find_element_by_xpath(
                    '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input')
                cardExit = driver.find_element_by_xpath(
                    '//*[@id="chrome-container"]/div[3]/div/div/a')

                try:
                    z = 0
                    t = 0
                    for m in range(1, 20):
                        picX = '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[9]/div[2]/div/div[' + str(
                            m) + ']/a'
                        loc = driver.find_element_by_xpath(picX)
                        src = loc.get_attribute('href')
                        urllib.request.urlretrieve(src, "captcha.png")
                        sleep(1)
                        data = decode(Image.open('captcha.png'))
                        sleep(1)
                        try:
                            x = int(data[0].data)
                            y = math.pow(2, 31)
                            sleep(1)
                            z = x/y
                            t += float(z)
                            print(z)
                            editX = '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[9]/div[2]/div/div['+str(
                                m)+']/p/span[2]/span[4]/a/span'
                            driver.find_element_by_xpath(editX).click()
                            driver.find_element_by_xpath(
                                '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/label/input').send_keys(str(z))
                            driver.find_element_by_xpath(
                                '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/input').click()
                        except:
                            print("No Qr ")

                except:
                    print("finish QRs")

                if (labPrice.get_attribute('value') == ''):
                    if(t == 0):
                        labPrice.send_keys(0)
                    else:
                        labPrice.send_keys(str(t))
                        labPrice.clear()
                        sleep(1)
                        labPrice.send_keys(str(t))
                        sleep(1)

                else:
                    x = labPrice.get_attribute('value')
                    labPrice.clear()
                    sleep(0.4)
                    labPrice.send_keys(str(x))
                    sleep(0.4)
                x = labPrice.get_attribute('value')
                y = sellPrice.get_attribute('value')
                cardExit.click()
                umut += float(y)

                pocket += float(x)

                print(umut)

                print(pocket)

            except:

                print('fail')
    except:
        print("cardsfinished")

    umut = str(umut)

    pocket = str(pocket)

    calc = '//*[@id="board"]/div['+str(card)+']/div/div[2]/a[1]'

    driver.find_element_by_xpath(calc).click()

    sellPrice.clear()

    sellPrice.send_keys(pocket)

    labPrice.click()

    labPrice.clear()

    labPrice.send_keys(umut)

    cardExit.click()


def month():
    umut = 0
    pocket = 0
    fees = 0
    cases = 0
    low = input("Enter the Lowest valu ")
    high = input("Enter the highest value ")
    high = int(high)+1
    low = int(low)
    for x in range(low, high):

        try:

            A1pat = '//*[@id="board"]/div[' + str(x) + ']/div/div[2]/a[1]'
            driver.find_element_by_xpath(A1pat).click()
            print(A1pat)
            sleep(1)
            x = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[1]/input').get_attribute('value')

            y = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[3]/input').get_attribute('value')
           # z = driver.find_element_by_xpath(
               # '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[9]/input').get_attribute('value')
            # v = driver.find_element_by_xpath(
               # '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[8]/input').get_attribute('value')
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/a').click()

            umut += float(y)

            pocket += float(x)
            # fees += float(z)
            # cases += int(v)

            print(umut)
            print(pocket)
            # print(fees)
           # print(cases)
        except:
            print('hata')
            # driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/a').click()


def tests():
    try:
        try:
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div').send_keys(Keys.PAGE_DOWN)
        except: 
            print("انزل فين تاني")
        for m in range(1, 10):
            picX = '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[9]/div[2]/div/div[' + \
                str(m) + ']/a'
            loc = driver.find_element_by_xpath(picX)
            src = loc.get_attribute('href')
            urllib.request.urlretrieve(src, "captcha.png")
            data = decode(Image.open('captcha.png'))
            try:
                x = int(data[0].data)
                y = math.pow(2, 31)
                sleep(1)
                z = x/y
                print(z)
                editX = '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[9]/div[2]/div/div['+str(
                    m)+']/p/span[2]/span[4]/a/span'
                driver.find_element_by_xpath(editX).click()
                driver.find_element_by_xpath(
                    '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/label/input').send_keys(str(z))
                driver.find_element_by_xpath(
                    '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/input').click()
            except:
                print("No Qr ")
        try:
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div').send_keys(Keys.PAGE_UP)
        except: 
            print("اطلع فين تاني")    
    except:
        print("finish ")


def whats():
    high = input("Enter the highest value ")
    card = input("Enter the card Num ")
    high = int(high)
    high = high + 2
    for x in range(2, high):
        try:
            A1pat = '//*[@id="board"]/div['
            A1pat += str(card)
            A1pat += ']/div/div[2]/a['
            A1pat += str(x)
            A1pat += ']'
            print(A1pat)
            driver.find_element_by_xpath(A1pat).click()
            sleep(1)
            p = driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[6]/input').get_attribute('value')
            p = p.replace(" ", "")
            p = p.replace("+", "https://wa.me/")
            print(p)
            # driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[2]/div/a[3]').click()
            # driver.find_element_by_xpath('//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/span/select').click()
            # driver.find_element_by_xpath('//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/span/select/optgroup[100]/option').click()
            # driver.find_element_by_xpath('//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/form/input[2]').click()
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea').clear()
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea').send_keys(p)
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/div[1]/input').click()
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/a').click()
        except:
            print('this number is incorrect')
            driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/a').click()


def test():

    umut = 0

    pocket = 0

    high = input("Enter the highest value ")

    high = high + 2

    card = input("Enter the card Num ")

    high = int(high)

    for x in range(2, high):

        A1pat = '//*[@id="board"]/div[' + \
            str(card) + ']/div/div[2]/a[' + str(x) + ']'

        print(A1pat)

        driver.find_element_by_xpath(A1pat).click()

        src = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div/div/div[4]/div[9]/div[2]/div/div/a').get_attribute('href')
        print(src)

        x = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div/div/div[3]/div[1]/h2').text

        print(x)

        urllib.request.urlretrieve(src,  str(x)+".png")

        img = Image.open(str(x)+".png")

        text = tess.image_to_string(img)

        driver.find_element_by_xpath(
            '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[2]/div/div/div[2]/div/div/p[1]/a').send_keys(text)


class Appointment:
  def __init__(self, m, p):
    self.clockBefore = clockBefore
    self.clockAfter = clockAfter
    self.phone = phone


def send_appo():
    # driver.switch_to.window(driver.window_handles[0])
    high = input("Enter the highest value ")
    low = input("Enter the Lowest value ")
    card = input("Enter the card Num ")
    # print("Connecting ...")

    # print("Going to Whatsapp page")
    # driver.implicitly_wait(30)
    # driver.execute_script("window.open('http://web.whatsapp.com','_blank')")
    # driver.switch_to.window(driver.window_handles[1])
    # sent = 0


    # # Waiting you to enter QRcode
    # print("Scan QRcode...")
    # while(1):
    #     try:
    #         driver.find_element_by_class_name('_1pw2F')
    #         time.sleep(2)
    #     except:
    #         print("QRcode Done")
    #         break
    # driver.switch_to.window(driver.window_handles[0])
    high = int(high)
    low = int(low)
    high = high + 2
    FMT = '%H:%M:%S'
    sleep(3)
    for x in range(low, high):
        A1pat = '//*[@id="board"]/div['
        A1pat += str(card)
        A1pat += ']/div/div[2]/a['
        A1pat += str(x)
        A1pat += ']'
        print(A1pat)
        driver.find_element_by_xpath(A1pat).click()
        sleep(1)
        x_span = driver.find_element_by_id(
            'js-dialog-title').get_attribute('innerHTML')
        y_span = int(x_span.index(':', 0, 11))
        clock = x_span[y_span-2:y_span+3]+":00"
        print(clock)
        clockBefore =dt.datetime.strptime(clock, FMT)

        delta = str(timedelta(hours=23))
        delta= dt.datetime.strptime(delta, FMT)

        clockAfter = clockBefore - delta
        clockAfter = str(clockAfter).split(", ")
        clockAfter = str(clockAfter[1])

        fastClock = str(timedelta(hours=9))
        fastClock= dt.datetime.strptime(fastClock, FMT)
        clockFasting = clockBefore - fastClock
        clockFasting = str(clockFasting).split(", ")
        clockFasting = str(clockFasting[1])

        print(clockAfter)

        msg = '''السلام عليكم ورحمه الله وبركاته..
        	 مجمع العائله الطبي 

  الموعد المقرر لحضرتك غدا بين '''+clock + ''' و '''+clockAfter + ''' صباحا  ان شاء الله 

  يفضل الصيام من الساعة '''+ clockFasting + ''' ان شاء الله

   لطفا ارسلوا لنا كلمة *تم* للتاكيد على استلامكم رسالة الموعد '''
        
        print(msg)
        for m in range(len(msg)) :
            driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/textarea').send_keys(msg[m])

        driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[11]/div[2]/form/div/div/div[1]/input').click()
        driver.find_element_by_xpath(
                '//*[@id="chrome-container"]/div[3]/div/div/a').click()
        print('-'*50)

        # phone = driver.find_element_by_id(
        #      'js-dialog-title').get_attribute('value')
        # p=driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[4]/div[2]/div/div/div[6]/input').get_attribute('value')
        # p= p.replace (" ","")
        # driver.find_element_by_xpath(
        #     '//*[@id="chrome-container"]/div[3]/div/div/a').click()
        # print(p)
        # driver.switch_to.window(driver.window_handles[1])
        # driver.get('https://web.whatsapp.com/send?phone='+str(p)+'&text=&source=&data=')
        # time.sleep(2)

        # driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').click()
        # time.sleep(2)
        # for line in msg.split('\n') :
        #     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').click()
        #     ActionChains(driver).send_keys(line).perform()    
        #     ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        # ActionChains(driver).send_keys(Keys.RETURN).perform()
        # time.sleep(2)

        # driver.switch_to.window(driver.window_handles[0])

def todayList() : 
    sleep(3)
    today = str(date.today().strftime('%d.%m.%Y'))
    print(today)

    for day in range(1,25) :
        try : 
            todayList=driver.find_element_by_xpath('//*[@id="board"]/div['+str(day)+']/div/div[1]/h2')
            todayList= str(todayList.get_attribute('innerHTML'))
            print(todayList)
            listdate = todayList.split()[1]
            print (listdate)
            if (listdate == today): 
                print ('this is the date')
                try:
                    counting(day)
                except:
                    print('Errors while Counting')
                break
        except:
           print ("this isn't the date")
        




if __name__ == '__main__':

    print('user Commands ')

    print('-'*50)

    print('For login type ')
    print('connect()')
    print('')

    print('For calculations type')

    print('board()')
    print('')
    connect()

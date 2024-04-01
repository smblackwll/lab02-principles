# Complete project details: https://RandomNerdTutorials.com/micropython-send-emails-esp32-esp826/
# Micropython lib to send emails: https://github.com/shawwwn/uMail
# The email sending part is mostly from that complete project details above.
# The timestamps was stuff I got from tutorials on utime, and on time.
# Here: https://docs.micropython.org/en/latest/library/time.html
# and here for ntptime: https://forum.micropython.org/viewtopic.php?t=12726
# If you have any questions please ask me, Spencer Blackwell, at smblackwll@uiowa.edu
import umail
import network
import time
import ntptime
from time import sleep, sleep_ms
from machine import Pin, I2C

pinIn = Pin(15, Pin.IN, Pin.PULL_DOWN)


# Your network credentials
ssid = 'UI-DeviceNet'
password = 'UI-DeviceNet'


# ##Setting the current time
# time.localtime()
ntptime.settime()
getTime = time.localtime()

# Email details
sender_email = 'ece220434@gmail.com'
sender_name = 'Group Alert' #sender name
sender_app_password = 'reyo pgmz rqdc njyy'
recipient_email ='spencerblackwell02@gmail.com'
email_subject =f'Critical Safety Event at {getTime[3]-5}:{getTime[4]} {getTime[1]}/{getTime[2]}/{getTime[0]}'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Connect to your network
connect_wifi(ssid, password)

while(True):
  # ntptime.settime()
  # getTime = time.localtime()
  email_subject =f'Critical Safety Event at {getTime[3]-5}:{getTime[4]} {getTime[1]}/{getTime[2]}/{getTime[0]}'
  if pinIn.value() == 0:
  # Send the email
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    smtp.write("There was a safety alert at the given time.")
    smtp.send()
    smtp.quit()
    print("Email Sent")
    sleep_ms(10000)
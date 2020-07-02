import pycurl
from io import BytesIO 
import RPi.GPIO as GPIO
import time
import sys



#### 3.3v ---> 110Ohms ----> Button Pin1 |||| Button Pin2 ---> GPIO Pin

b_obj = BytesIO() 
crl = pycurl.Curl() 

button_1 = 17
button_2 = 27
button_3 = 22

crly_1 = 2
crly_2 = 3
crly_3 = 4



GPIO.setmode(GPIO.BCM)
GPIO.setup(crly_1, GPIO.OUT)
GPIO.setup(crly_2, GPIO.OUT)
GPIO.setup(crly_3, GPIO.OUT)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 8 to be an input pin and set initial value to be pulled low (off) 
GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(button_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)

url_1 = 'http://127.0.0.1/queue-system/read?task=print'
url_2 = 'http://127.0.0.1/queue-system/read?task=recall'
url_3 = 'http://127.0.0.1/queue-system/read?task=next'



def relay_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def relay_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


def cleanAndExit():
        linear_stop()
        print ("Cleaning...")
        GPIO.cleanup()
        print ("Bye!")
        sys.exit()




def send_curl():
    data = {
    #'barcode': read_sachet,
    #'total': log_total,
    #'device_id': deviceID,
    #'phone_number': curl_nmber
           
    'url': url_1,
    'total': 1,
    'device_id': 1,
            }
    print ("url: %s , total: %s , device_id %s " %(url_1,1,1))
    crl.setopt(crl.URL, url)
    pf = urlencode(data)
    crl.setopt(crl.POSTFIELDS, pf)
    crl.perform()
    crl.close()       

        '''
       crl.setopt(crl.URL, url_2)
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.perform() 
        crl.close()
        get_body = b_obj.getvalue()
        '''

while True: # Run forever
 try:
    if GPIO.input(button_1) == GPIO.HIGH:
        print("button_1 was pushed!")
        relay_on(crly_1)
        print("crly_1 ON!")
        send_curl()
        print("Curl Sent!")
        
        time.sleep(2)
        relay_off(crly_1)
        print("crly_1 off!")
        time.sleep(1)
        relay_on(crly_2)
        print("crly_1 ON!")
        relay_off(crly_2)
        print("crly_1 off!")


 except(KeyboardInterrupt, SystemExit)
    cleanAndExit()        
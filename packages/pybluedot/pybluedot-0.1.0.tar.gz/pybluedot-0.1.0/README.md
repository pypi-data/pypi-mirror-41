# Bluedot-sms unofficial API

This is an unofficial API for [Bluedot-sms](http://bluedotsms.com)

Requirements:
  Python 3

Installation:

>  pip install pybluedot

Usage
```python

from pybluedot import Bluedot
client = Bluedot(username="SuperCode", password="I don't know", sender="PyBluedot")


@client.send("SuperCode") #Your registered Sender Name
def my_callback(result):

    print(result.status) #200
    print(result.response) #Get response body from Bluedot
    print(client['balance']) #Get Current Balance

#send sms  
data = {"recipients" :  ["263784442662", "26378123456"], "msg" : "Hey i sent a text with pybluedot"}

my_callback(data) #That's All !!!



```

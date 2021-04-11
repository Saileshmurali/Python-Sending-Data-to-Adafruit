from Adafruit_IO import Client, Feed, RequestError
"""
#ADAFRUIT_IO_USERNAME = '123dragon'
#ADAFRUIT_IO_KEY = 'aio_BGPJ15el87aqpfdYDQ7PntUEJWdh'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#test=aio.feeds('test')
v=aio.feeds('voltage')
i=aio.feeds('current')
aio.send(v.key,421.234)
aio.send(i.key,4.3452)
#aio.send(test.key,42)

#data = aio.receive('Voltage')
#print('Received value: {0}'.format(data.value))
"""
ADAFRUIT_IO_KEY = 'aio_SKcv478WCyQ9FdIz51YuwG4YOKOV'
ADAFRUIT_IO_USERNAME = 'ssudhirsai'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    voltage = aio.feeds('voltage')
except RequestError:
    voltage = Feed(name="voltage")
    voltage = aio.create_feed(voltage)
aio.send_data(voltage.key, 300.21)
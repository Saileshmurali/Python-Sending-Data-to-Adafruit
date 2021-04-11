from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'type key here'
ADAFRUIT_IO_USERNAME = 'type user name here'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    voltage = aio.feeds('voltage')
except RequestError:
    voltage = Feed(name="voltage")
    voltage = aio.create_feed(voltage)
aio.send_data(voltage.key, 300.21)

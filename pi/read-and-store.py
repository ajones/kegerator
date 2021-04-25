import requests
import serial
import time
import threading
import os
import sys
import psycopg2

# optional serial send disable for local development
DISABLE_SERIAL = (os.getenv('DISABLE_SERIAL') == "true")

# optional debug prints messages to serial 
DEBUG = (os.getenv('DEBUG') == "true")

# REQUIRED identifies which keg number this service is measuring
KEG_ID = os.getenv('KEG_ID') or sys.exit("KEG_ID required") 

# Define the port the arduino is connected to 
# can be found byt doing ls /dev/tty* and locating the new interface
COM_PORT = os.getenv('ARDUINO_COM_PORT') or '/dev/tty.usbmodem14401'


# serial connection 
ser = None
if not DISABLE_SERIAL:
  ser = serial.Serial(
    port=COM_PORT, 
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
  )
print("Serial connected successfully")

# database connection
db_conn = psycopg2.connect("")
print("Database connected successfully")

def insert_into_db(weight):
  sql = """INSERT INTO kegweights(keg_id, weight_lbs) VALUES(%s, %s);"""
  cur = db_conn.cursor()
  # execute the INSERT statement
  cur.execute(sql, (KEG_ID,weight,))
  # commit the changes to the database
  db_conn.commit()
  # close communication with the database
  cur.close()


# gets the current unix time in millis
def current_milli_time():
  return round(time.time() * 1000)

last_time = 0
development_weight = 20.0
def local_development():
  global last_time
  global development_weight
  # create a weight that starts at given value 
  # and slowly decreases over time
  if last_time == 0 : 
    last_time = current_milli_time()
    return

  # rate that the red weight changes (higher = slower)
  change_rate = 2000
  now = current_milli_time()
  delta_millis = now - last_time
  development_weight -= delta_millis/change_rate
  last_time = now
  
  # clamp at 0
  if development_weight < 0: 
    development_weight = 0


# reads data sent to us from the active serial connection
# it also looks for the sentinal to detect when to send fresh data
def read_and_handle():
  global development_weight
  if DISABLE_SERIAL:
    while True:
      try:
        local_development()
        formatted = "{:.2f}".format(development_weight)
        print(f"dev_weight: {formatted}")
        insert_into_db(development_weight)
        threading.Timer(1,read_and_handle).start()
      except:
        e = sys.exc_info()[0]
        if DEBUG:
          print("read and print exception", e)
      return
  
  while True:
    try:
      lineData=str(ser.readline())
      data = lineData[2:][:-5] # line format : "b'end of message : \r\n'"
      
      #
      # TODO : parse serial message and pass to insert_into_db()
      #
    except:
      e = sys.exc_info()[0]
      if DEBUG:
        print("read and print exception", e)
      

# main program kickoff
if __name__ == "__main__":
  # Begin the loop of reading data from the serial line
  threading.Timer(0,read_and_handle).start()
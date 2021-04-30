# Kegerator
## Introduction
Welcome to the Kegerator project. The initial goal is to create a fun and interesting data visualization of the remaining beer inside a keg held inside a kegerator. 


---
## Part List

| Part      | Description | Link |
| ----------- | ----------- | ----------- |
| Scale       | Sacrifitial scale to "make smart" |[link](https://www.amazon.com/gp/product/B07RV6X8LZ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)|
| Arduino       | Analog data interface|[link](https://www.amazon.com/Adafruit-Metro-Mini-328-5V-16MHz/dp/B016RBLUZE/ref=sr_1_1?dchild=1&keywords=metro+mini&qid=1619801970&sr=8-1)|
| RaspberryPi       | Wifi connectivity and server |[link](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX/ref=sr_1_5?crid=2SYJL6G3FXPBE&dchild=1&keywords=raspberry+pi+zero+w&qid=1619802051&sprefix=raspberry+pi+z%2Caps%2C203&sr=8-5)|
| Wheatstone Bridge       | Make load cell connection easier |[link](https://www.sparkfun.com/products/13878)|
| Load Cell Amp       | Talk to arduino|[link](https://www.amazon.com/SparkFun-Load-Cell-Amplifier-HX711/dp/B079LVMC6X/ref=sr_1_5?crid=1R1FZ5JLQTTBS&dchild=1&keywords=load+cell+amplifier&qid=1619802121&sprefix=load+cell+amp%2Caps%2C188&sr=8-5)|
| Thermometer      | Temperature based calibration|[link](https://www.amazon.com/One-Wire-Digital-Temperature-Sensor/dp/B004G53D54/ref=sr_1_2?dchild=1&keywords=sparkfun+thermometer&qid=1619802350&sr=8-2)|

---

## Repo layout

| Component   | Job |
| -----------  | ----------- |
| scale |  read values from load cells and print to serial |  
| pi |  read values from serial and insert them into pg db |  
| www |  read values from DB and display them in some cool way |  

---
## Development
Most folders have a `./dev.sh` file that will run the service locally with example/test env vars.
# Kegerator
## Introduction
Welcome to the Kegerator project. The initial goal is to create a fun and interesting data visualization of the remaining beer inside a keg held inside a kegerator. 


---
## Part List

| Part      | Description | Link |
| ----------- | ----------- | ----------- |
| Scale       | Sacrifitial scale to "make smart" |[link](https://www.amazon.com/gp/product/B07RV6X8LZ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)|
| Arduino       | Analog data interface|[link](https://www.adafruit.com/product/2590)|
| RaspberryPi       | Wifi connectivity and server |[link](https://www.adafruit.com/product/3400)|
| Wheatstone Bridge       | Make load cell connection easier |[link](https://www.sparkfun.com/products/13878)|
| Load Cell Amp       | Talk to arduino|[link](https://www.sparkfun.com/products/13879)|
| Thermometer      | Temperature based calibration|[link](https://www.sparkfun.com/products/245)|

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
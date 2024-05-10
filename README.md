* sh1106 is the Library that is used to run the oled screen without this library or the Adafruit_SSD1306 library it is not possible to run the oled screen on Raspberry Pi Pico Rp2040
* Data fetching is the Python Class file what helps in reading the data from all the sensors and return the data in the form of dictinary(a key value pair )
* InitializeSensor is the file that i have used here is to turn on the VCC pins of the sensors which is connected to the GPIO pins here we have used this because connecting all the sensors parallely
  to the 3v3 out will not be enough for all the sonsors to work so connecting it to the GPIO and oning the GPIO will make the solution for the problem,so i have power oned all the required sensors
  before reading the data from then and then turned off all of them after reading the data
  


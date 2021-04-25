#include "HX711.h"

#define DOUT  2
#define CLK  3

HX711 scale;

float calibration_factor = 23100; // Derived from running the ../calibration sketch

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);

  scale.set_scale(calibration_factor); // Adjust to this calibration factor
  scale.tare(); // Reset the scale to 0
}

void loop() {
  Serial.print(scale.get_units(), 1);
  Serial.print(" lbs"); // Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
  Serial.println();
}
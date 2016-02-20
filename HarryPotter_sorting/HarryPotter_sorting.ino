#include <Servo.h>
#include <Adafruit_NeoPixel.h>

int val;
      #define PIN 6

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(2, PIN, NEO_GRB + NEO_KHZ800);
    

void setup() {
  Serial.begin(9600); 
  strip.begin();
  strip.setPixelColor(0, 75, 0, 130);
  strip.show();
}

void loop() {
  if (Serial.available()){
    val = Serial.read();
    if (val == '0'){
      Serial.print("Rawenclaw");
      strip.setPixelColor(0, 0, 0, 150);
      strip.setPixelColor(1, 0, 0, 150);
      strip.show();
    }
    if (val == '1'){
      Serial.print("Sytherin");
      strip.setPixelColor(0, 0, 150, 0);
      strip.setPixelColor(1, 0, 150, 0);
      strip.show();
    }
    if (val == '2'){
    Serial.print("Gryffindor");
    strip.setPixelColor(0, 150, 0, 0);
    strip.setPixelColor(1, 150, 0, 0);
    strip.show();
    }
    if (val == '3'){
      Serial.print("Hufflepuff");
      strip.setPixelColor(0, 255, 150, 0);
      strip.setPixelColor(1, 255, 150, 0);
      strip.show();
    }
   }
}


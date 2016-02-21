#include <Adafruit_NeoPixel.h>

int val;

//      #define PIN 6

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//Adafruit_NeoPixel strip = Adafruit_NeoPixel(2, PIN, NEO_GRB + NEO_KHZ800);
    

void setup() {
  Serial.begin(9600); 
  //strip.begin();
 // strip.show(); // Initialize all pixels to 'off'
}

void loop() {
   if (Serial.available()){
    val = Serial.read();
    if (val == '0'){
      Serial.print("Ravenclaw");
      Serial.println();
    }
    if (val == '1'){
      Serial.print("Sytherin");
      Serial.println();
    }
    if (val == '2'){
    Serial.print("Gryffindor");
    Serial.println();
    }
    if (val == '3'){
      Serial.print("Hufflepuff");
      Serial.println();
    }
   }
}

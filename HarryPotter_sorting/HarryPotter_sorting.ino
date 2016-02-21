#include <Adafruit_NeoPixel.h>
 
int val;
int pos;
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
  strip.setPixelColor(0, 200, 200, 200);
  strip.setPixelColor(1, 200, 200, 200);
  strip.show();
}
 
void sorting(){
    if(val == '0') {
      breath();
    }
    if (val == 'A'){
      Serial.print("Rawenclaw");
      strip.setPixelColor(0, 0, 0, 200);
      strip.setPixelColor(1, 0, 0, 200);
      strip.show();
      delay(4000);
      val = '0';
    }
    if (val == 'B'){
      Serial.print("Sytherin");
      strip.setPixelColor(0, 0, 200, 0);
      strip.setPixelColor(1, 0, 200, 0);
      strip.show();
      delay(4000);
      val = '0';
    }
    if (val == 'C'){
    Serial.print("Gryffindor");
    strip.setPixelColor(0, 200, 0, 0);
    strip.setPixelColor(1, 200, 0, 0);
    strip.show();
    delay(4000);
    val = '0';
    }
    if (val == 'D'){
      Serial.print("Hufflepuff");
      strip.setPixelColor(0, 255, 150, 0);
      strip.setPixelColor(1, 255, 150, 0);
      strip.show();
      delay(4000);
      val = '0';
    }
}
 
void breath(){
  strip.setPixelColor(0, 200, 200, 200);
  strip.setPixelColor(1, 200, 200, 200);
  strip.show();
  for (int i=10; i<200; i++) { strip.setBrightness(i); strip.show(); delay(10); }
  for (int i=200; i>10; i--) { strip.setBrightness(i); strip.show(); delay(10); }
}
 
 
void loop() {
  if (Serial.available()){
    val = Serial.read();
    sorting();
   }
   else {
   
   }
  breath();
}

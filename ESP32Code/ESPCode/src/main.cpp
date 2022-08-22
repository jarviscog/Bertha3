// /*
//   WiFiAccessPoint.ino creates a WiFi access point and provides a web server on it.

//   Steps:
//   1. Connect to the access point "yourAp"
//   2. Point your web browser to http://192.168.4.1/H to turn the LED on or http://192.168.4.1/L to turn it off
//     OR
//     Run raw TCP "GET /H" and "GET /L" on PuTTY terminal with 192.168.4.1 as IP address and 80 as port

//   Created for arduino-esp32 on 04 July, 2018
//   by Elochukwu Ifediora (fedy0)
// */


// #include <WiFi.h>
// #include <WiFiClient.h>
// #include <WiFiAP.h>

// // Control the builtin led
// #include "Freenove_WS2812_Lib_for_ESP32.h"
// #define LEDS_COUNT  8
// #define LEDS_PIN	48
// #define CHANNEL		0
// Freenove_ESP32_WS2812 rgb_led = Freenove_ESP32_WS2812(LEDS_COUNT, LEDS_PIN, CHANNEL, TYPE_GRB);
// byte m_color[5][3] = { {255, 0, 0}, {0, 255, 0}, {0, 0, 255}, {255, 255, 255}, {0, 0, 0} };

// byte RED[3] = {255,0,0};
// byte GREEN[3] = {0,255,0};
// byte BLUE[3] = {0,0,255};


// // WIFI Cridentials
// const char *ssid = "AeroBoard";
// const char *password = "esp32";

// WiFiServer server(80);

// void set_led(byte color[3]){

//     for (int i = 0; i < LEDS_COUNT; i++) {
// 			rgb_led.setLedColorData(i, color[0], color[1], color[2]);
// 			rgb_led.show();
// 			// delay(2);
// 	}


// }



// void setup() {

//     // Setup LED for debugging
//     rgb_led.begin();
//     rgb_led.setBrightness(100);

//     Serial.begin(115200);
//     Serial.println();
//     Serial.println("Configuring access point...");

//     // You can remove the password parameter if you want the AP to be open.
//     WiFi.softAP(ssid, password);
//     IPAddress myIP = WiFi.softAPIP();
//     Serial.print("AP IP address: ");
//     Serial.println(myIP);
//     server.begin();

//     Serial.println("Server started");
// }

// void loop() {
    
    
//     set_led(RED);
//     // Serial.println("Set color");


//     WiFiClient client = server.available();   // listen for incoming clients
//     if (client) {                             // if you get a client,
//     Serial.println("New Client connected");           // print a message out the serial port
//     String currentLine = "";                // make a String to hold incoming data from the client
//     while (client.connected()) {            // loop while the clWient's connected
//         // set_led(BLUE);
//         if (client.available()) {             // if there's bytes to read from the client,
//         char c = client.read();             // read a byte, then
//         Serial.write(c);                    // print it out the serial monitor
//         if (c == '\n') {                    // if the byte is a newline character

//             // if the current line is blank, you got two newline characters in a row.
//             // that's the end of the client HTTP request, so send a response:
//             if (currentLine.length() == 0) {
//             // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
//             // and a content-type so the client knows what's coming, then a blank line:
//             // client.println("HTTP/1.1 200 OK");
//             // client.println("Content-type:text/html");
//             // client.println();

//             // // the content of the HTTP response follows the header:
//             // client.print("Click <a href=\"/H\">here</a> to turn ON the LED.<br>");
//             // client.print("Click <a href=\"/L\">here</a> to turn OFF the LED.<br>");

//             // The HTTP response ends with another blank line:
//             client.println();
//             // break out of the while loop:
//             break;
//             } else {    // if you got a newline, then clear currentLine:
//             currentLine = "";
//             }
//         } else if (c != '\r') {  // if you got anything else but a carriage return character,
//             currentLine += c;      // add it to the end of the currentLine
//         }

        
//         // Serial.println("The client sent something:");
//         // Serial.println(currentLine);
//         // Serial.println("---------");
//         set_led(GREEN);
        
//         if (currentLine.endsWith("GET /Hello")) {

//           Serial.println("GOT SOME CODE!");

//         }

//       }
//     }
//     // close the connection:
//     set_led(RED);
//     client.stop();
//     Serial.println("Client Disconnected.");
//   }

// }
          
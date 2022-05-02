#include <servo.h>

servo servo1;
servo servo2;
servo servo3;
servo servo4;

void setup() {
  // put your setup code here, to run once:
  serial.begin(9600);

  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);

  servo1.writeMicroseconds(1500);
  servo2.writeMicroseconds(1500);

  delay(7000);



}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.avaliable()=0){
    string data = serial.readStringUntil('\n')
    serial.println(data);


    if(data.equals("foward")){
      servo1.writeMicroseconds(1400);
      servo2.writeMicroseconds(1400);
    }

    else if (data.equals("backward")){
      servo1.writeMicroseconds(1600);
      servo2.writeMicroseconds(1600);
    }

    else if (data.equals("zstop")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1500);
    }


    if(data.equals("right")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1400);
    }

    else if (data.equals("left")){
      servo1.writeMicroseconds(1400);
      servo2.writeMicroseconds(1500);
    }

    else if (data.equals("xstop")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1500);
    }


    if(data.equals("up")){
      servo1.writeMicroseconds(1400);
      servo2.writeMicroseconds(1400);
    }

    else if (data.equals("down")){
      servo1.writeMicroseconds(1600);
      servo2.writeMicroseconds(1600);
    }

    else if (data.equals("ystop")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1500);
    }


    if(data.equals("up1")){
      servo1.writeMicroseconds(1400);
      servo2.writeMicroseconds(1500);
    }

    else if (data.equals("up2")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1400);
    }

    else if (data.equals("ystop")){
      servo1.writeMicroseconds(1500);
      servo2.writeMicroseconds(1500);
    }


  }

}

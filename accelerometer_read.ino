int num_of_accelerometers = 2;
float time_between_measurements = 10; // in milliseconds


const int zpin1 = A1;
const int zpin2 = A2;
float calibration_value1 = 0.0;
float calibration_value2 = 0.0;
float zval1 = 0.0;
float zval2 = 0.0;

void setup() {
  // initialize the serial communications:
  Serial.begin(9600);
}


void loop() {
  while (calibration_value1 == 0.0)
  calibration_value1 = analogRead(zpin1);
  // print the sensor values:
  zval1=(analogRead(zpin1)/calibration_value1)-1.00;
  String zprint1 = String(zval1) + "a";
  Serial.println(zprint1);
  // delay before next reading:
  delay(time_between_measurements/num_of_accelerometers);


  if (num_of_accelerometers == 2)
  {
  while (calibration_value2 == 0.0)
  calibration_value2 = analogRead(zpin2);
  // print the sensor values:
  zval2=(analogRead(zpin2)/calibration_value2)-1.00;
  String zprint2 = String(zval2) + "b";
  Serial.println(zprint2);
  // delay before next reading:
  delay(time_between_measurements/num_of_accelerometers);
  }
}

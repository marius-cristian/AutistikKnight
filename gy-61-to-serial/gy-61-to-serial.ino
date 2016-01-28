const int VCCPin = A0;
const int xPin   = A1;
const int yPin   = A2;
const int zPin   = A3;
const int GNDPin = A4;

int x = 0;
int y = 0;
int z = 0;

void setup() {

pinMode(A0, OUTPUT);
pinMode(A4, OUTPUT);
digitalWrite(14, HIGH);
digitalWrite(18, LOW);

Serial.begin(9600);
} 

void loop() {
x = analogRead(xPin);
y = analogRead(yPin);
z = analogRead(zPin);




String aux=String(x)+","+String(y)+","+String(z);


Serial.println(aux);



} 

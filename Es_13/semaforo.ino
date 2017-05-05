/* 
 *  Create a traffic light with FSM on arduino
 */

const int LVpin = 9; // led verde
const int LGpin = 10; // led giallo
const int LRpin = 11; // led rosso
const int ENpin = 8; // input pin for enable

const int timeV = 4000; //time of greeen (ms)
const int timeVG = 1500; //time of verde giallo (ms)
const int timeR = 2000; //time of rosso (ms)
const int timeG =  1500; // time del lampeggiante

#define LVstate 0
#define LVGstate 1
#define LRstate 2
#define LOFFstate 3
#define LGstate 4

int thisState = LOFFstate; // this state
int nextState = LOFFstate; // next state
int stateWait = timeG; // state wait
bool inEnable = false; // enable bit

void setup() {
  // put your setup code here, to run once:
  pinMode(LVpin, OUTPUT);
  Serial.begin(9600);
  pinMode(LGpin, OUTPUT);
  pinMode(LRpin, OUTPUT);
  pinMode(ENpin, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:
  // 1. read the input
  // swith (state) 
  // 2. generate the output
  // 3. calculate the next state
  // 4. wait for this state to complete
  inEnable = readEnable();
  Serial.println(thisState);
  Serial.println(inEnable);
  switch (thisState) {
  case LVstate:
    // green state
    stateWait = timeV;
    setOutput(HIGH, LOW, LOW);
    if (inEnable) {
      nextState = LVGstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//
  case  LVGstate:
    // green-yellow state
    stateWait = timeVG;
    setOutput(HIGH, HIGH, LOW);
    if (inEnable) {
      nextState = LRstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//    
  case LRstate:
    // red state
    stateWait = timeR;
    setOutput(LOW, LOW, HIGH);
    if (inEnable) {
      nextState = LVstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//    
  case LOFFstate:
    // OFF state
    stateWait = timeG;
    setOutput(LOW, LOW, LOW);
    if (inEnable) {
      nextState = LRstate;
    } else {
      nextState = LGstate;
    }
    break;
//    
  case LGstate:
    // green-yellow state
    stateWait = timeG;
    setOutput(LOW, HIGH, LOW);
    if (inEnable) {
      nextState = LRstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//    
  default:
  // should never get here
  break;
  }
/*
 wait for the stateWait ms time
*/
  delay(stateWait);
/* 
 *  goto next state
 */
  
  thisState = nextState;
}

bool readEnable(){
  // read the value of the enable pin
  int val;
  val = digitalRead(ENpin);
  return ( val == HIGH);
}

int setOutput(int LV, int LG, int LR) {
  Serial.println("setOutput");
  Serial.print( LV);  
  Serial.print( LG);
  Serial.println( LR);
  digitalWrite(LVpin, LV);  
  digitalWrite(LGpin, LG);
  digitalWrite(LRpin, LR);
}




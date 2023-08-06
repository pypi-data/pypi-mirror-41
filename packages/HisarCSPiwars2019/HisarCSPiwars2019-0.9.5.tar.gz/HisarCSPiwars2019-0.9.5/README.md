
# PiWars Turkey 2019: Python library for the distributed robot kits by HisarCS

This python library was created for the purposes of easing the understanding between software, sensors, and movables on the robot kits designed by HisarCS for attendees of Pi Wars Turkey 2019.


## Installation

Use the following commands to install the library
```bash 
git clone https://github.com/HisarCS/PiWars2019.git
cd PiWars2019
sudo python setup.py install
```

## Usage

```python
import HisarCSPiWars2019
```

## Documentation

The library includes 5 classes as of now these are:
- OptimizedPiCam (for a simplified and optimized way to use the Pi Camera and OpenCV)
- Kumanda (for an easy way to use the pygame Joystick class with the sixaxis PS3 controller)
- MotorControl (for an easy way to use the Pololu DRV8835 motor control circuit for the Raspberry Pi with a controller)
- ServoControl (for a simple way to use servo motors on the Raspberry Pi using GPIO pins)
- UltrasonicSensor (for an easy way to use HC-SR04 ultrasonic distance sensors on the Raspberry Pi)

For the purposes of performance, some of the classes include multithtreading. This prevents some parts of the code to not have an effect on other parts of the code. Multithreading was especially implemented to OptimizedPiCam (for both grabbing and showing the frames), Controller (to get the controller values continuously), ServoControl(to prevent any sleep function in the class to affect the main thread).

OptimizedPiCam:
-
- Methods
```python
updateData()
```
Updates the data obtained from the Pi Camera.

```python
startReadingData()
```
Creates a new Thread to call ``` updateData()``` in order to update the data without slowing down the main thread.

```python
readData()
```
Returns the current data of the camera as a numpy array.

```python
updateShownFrame()
```
Creates and updates the opencv window that shows the image the Pi Camera is seeing. The "q" key can be used to close the window.

```python
showFrame()
```
Calls ``` updateShownFrame()``` in a new Thread to create a visual window without slowing down the main thread.

- Example Usage
```python
from HisarCSPiWars2019 import OptimizedPiCam

camera = OptimizedPiCam()
camera.startReadingData()
camera.showFrame()
```
The above example creates a new OptimizedPiCam object and uses it to show the image the camera is seeing until the "q" key is pressed.  

The default resolution of 640x480 for camera is set when the constructor is called. If you want a different resolution settings, for instance 1280x720 ,then set the camera object as follows:
 ``` camera = OptimizedPiCam(resolution=(1280, 720))```

Keep in mind that the data has to be received using  ``` camera.startReadingData()``` with ``` camera.readData()```  or  ``` camera.currentFrame``` , if further vision processing is wanted. ``` camera.currentFrame``` is the current frame variable in numpy array, where the function ``` camera.readData()```  returns variable ``` camera.currentFrame```. 

The below example code will grab the frame from the camera in numpy array format, grayscale it, and display the frames in the **main thread**.
```python
from HisarCSPiWars2019 import OptmizedPiCam
import cv2

camera = OptimizedPiCam()
camera.startReadingData()

while True:
	frame = camera.readData()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("gray", gray)
```
Wheras in the example below, the grayscaled frames are both grabbed and displayed in **different threads**, **not in the main thread**. This method is strongly encouraged to increase the performance as much as possible.
```python
from HisarCSPiWars2019 import OptimizedPiCam
import cv2

camera = OptimizedPiCam()
camera.startReadingData()
camera.showFrame()

while True:
	frame = camera.currentFrame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	camera.suAnkiKare = gray
```
Kumanda
-
- Methods
```python
refresh()
```
Refreshes the values obtained from the controller inside a while loop. **Not recommended** to call in the main thread since the program will stuck in this method.

```python
startListening()
```
Calls ```python refresh()``` in a new thread. Allowing the while loop of the main thread to be faster. 

```python
readLeftValues()
```
Returns the values of the left joystick of the controller as two float values, x and y.

```python
readRightValues()
```
Returns the values of the right joystick of the controller as two float values, x and y.

```python
readButtons()
```
Returns an array of the numerical values of all the buttons pressed.

```python
readData()
```
Returns all values of the controller ```(python readLeftValues(), python readRightValues(), python readButtons())```

- Example Usage
```python
import HisarCSPiWars2019

controller = HisarCSPiWars2019.Controller()
controller.startListening()

while True:
  lx, ly = controller.readLeftValues()
  rx, ry = controller.readRightValues()
  buttons = controller.readButtons()
  
  print("The left joystick values are: ", lx, ly)
  print("The right joystick values are: ", rx, ry)
  
  if(0 in buttons):
    print("Button 0 was pressed!")
```
The above code initializes a Kumanda object and prints the values from the left and right joysticks, as well as a set string when a button is pressed. Keep in mind that ```python startListening()``` has to be called once when the main code is executed, or the data won't be read from the controller.

MotorControl
-
- Methods -
```python
setSpeeds(rightSpeed, leftSpeed)
```
Sets the speeds of the motors using the pololu-drv8835-rpi library. The range for the speeds are -480 to 480 where -480 is maximum speed in reverse. The right and left speeds are for motor 1 and motor 2 depending on which side they are on.

```python
controllerDataToMotorSpeed(x, y, t)
```
Returns the speed for the motor according to the values of a joystick from the controller. x and y are the x and y values of the joystick and t is a boolean value with True for the right motor and False for the left motor.

- Example Usage
```python
import HisarCSPiWars2019
motors = HisarCSPiWars2019.MotorControl()

while True:
  motors.setSpeeds(480, 480)
```
This code initializes motors and sets both of them to max speed.

- Example Usage w/ Controller
```python
import HisarCSPiWars2019

motors = HisarCSPiWars2019.MotorControl()

controller = HisarCSPiWars2019.Controller()
controller.startListening()

while True:
  lx, ly = controller.readLeftValues()
  rightSpeed = motors.controllerDataToMotorSpeed(lx, -ly, True)
  leftSpeed = motors.controllerDataToMotorSpeed(lx, -ly, False)
  
  motors.setSpeeds(rightSpeed, leftSpeed)
```
The above code initializes the motors and the controller and goes into a while loop. Inside the loop, the ```controllerDataToMotorData()```function is used to get the speed values for the motors. The y value is set to negative because on PS3 controllers specifically forwards on the joystick returns negative values. 

ServoControl
-
- Methods -
```python
setToContinuous()
setToNotContinuous()
```
Switches the servo from continous and not continuous respectively. Continuous requires dynamic values to be provided while not continuous turns the servo between provided angles.

```python
setAngle(angle)
```
Turns the servo to the provided angle in degrees. Provides a sleep statement and a separate thread when the servo is set to not continuous. 

- Example Usage -
Continuous:
```python
servo = HisarCSPiWars2019.ServoControl()
servo.setToContinuous()

angle = 0
add = 0
while True:
  servo.setAngle(angle)
  
  if(angle == 180):
    add = -1
  elif(angle == 0):
    add = 1
  angle += add
  sleep(0.01)
```
In this case, the servo is set to continuous. A while loop is used to constantly change the angle of the servo by 1 and set the new angle.

- Example Usage -
Non-Continuous:
```python
import HisarCSPiWars2019
from time import sleep

servo = HisarCSPiWars2019.ServoControl()
servo.setToNotContinuous()

while True:
  servo.setAngle(180)
  sleep(1)
  servo.aetAngle(0)
  sleep(1)
```
In this case, the servo is set to non-continuous. A while loop is used to set the angle of servo with one minute sleeps

UltrasonicSensor
-
- Methods 
```python
getDistance()
```
Returns the distance measured by the ultrasonic sensor

- Example Usage
```python
ultra = HisarCSPiWars2019.UltrasonicSensor(38, 40)

while True:
  print(ultra.getDistance())
```
The code above prints the distance. The integers inside the initializer for the class are the pins it is attached to.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

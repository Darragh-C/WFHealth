# WFHealth: A work from home health and productivity solution
#### Student Name: *Darragh Conneely*   Student ID: *20099857*

Workers now working from home no longer benefit from the light and temperature controlled, air conditioned environment of the office which can affect employee productivity and health, notwithstanding traditional health risks of office work. This solution aims to increase home working comfort and productivity around the themes of light, temperature, air purity and humidity monitoring and control, as well as enforcing healthy habits concerning sedentariness, and nearsightedness.

| Problem                         | Solution                            |
|---------------------------------|-------------------------------------|
|Temperatures above 22℃  cause lethargy and drowsiness|SenseHat temperature sensor detects temperature rise and notifies user to open window|
|Temperatures below 22℃ cause stress and mistakes|SenseHat temperature sensor detects temperature drop and turns on heater until 22℃|
|Humidity above 50% causes drowsiness, stuffiness, and mold (eye, skin and lung irritation)|SenseHat humidity sensor detects humidity rise and turns on dehumidifier until ideal humidity|
|Humidity below 30% causes a sore throat, coughing, and skin irritation|SenseHat humidity sensor detects humidity drop and notifies worker to open window| 
|High CO2 slows workers up to 60%, causes drowsiness, drop in attention, cognition, and response times.|CO2 sensor detects CO2 above marker and notifies worker to open window until ideal level is reached.|
|Dust in the office causes allergic/asthmatic reactions, eye irritation, damage to equipment and a drop in attention, cognition, and response times|Dust sensor detect particulate matter above a certain concentration and notifies worker to vacuum clean office.|
|Poor lighting can cause eye strain and headaches, drowsiness and lack of focus, and can worsen eyesight|Photoresistor to detect low luminosity, which triggers an LED light strip, ideally relative to luminosity
|Light colour affects mood in different ways|Change LED colour for user’s desired mood|
|Sitting is the new smoking|Pressure mat on seat detects sit duration|
|Staring at a screen for prolonged periods causes nearsightedness, headaches, and burnout|After 20 min of screen time, the user is notified to focus on object 20 m away for 20 seconds.|

## Additional hardware

Raspberry Pi, Wifi sockets to control heater and dehumidifier, button or PIR motion sensor to tell the system when you are away from desk, Bluetooth speaker to give voice commands for actions outside the system’s control

## Programming languages

Python for IoT/network scripts; Javascript for web development

## Additional tools

Think Speak, Glitch

## Desired but outside project scope

Motorized blinds, water level sensor to track water consumption



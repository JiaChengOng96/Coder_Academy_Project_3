Design and perform acceptance tests using TWO test procedures and document the results. You must:

Design TWO tests which a human can follow to ensure the program conforms to the specification:

one test must verify that a modelled IoT device can be successfully controlled

- Test1: we will check if the smart baby monitor would perform the action as input


one test must verify one other behaviour of the application
- Test2: we will try drag the link device to outside of the application

Describe the procedure for each test and its expected outcome
Test 1 procedure

- Step1: Check if the server is running and if not run the ./run.sh command at the folder to run the server store in the remote server
- Step2: Boot up the client by running using `python3 main.py` within the local folder
- Step3: Link the device with the ip of 127.0.0.4 to connect the baby monitor device
- Step4: Try on and off the radio button to check if the applcation does connect with the server and the monitor is affect by the choice
- Step5: Restart the client and run step 3 and step 4 again. Check if the client have the result of step 4 because it would mean that the controller is running fine.

Test 1 Expected Outcome: The device would work fine and control the monitor

Test 2 Procedure

- Step1: First ensure that the server is running and if not then just follow the step 1 of test 1
- Step2: Same as test 1 to just run the IoT Clent
- Step3: Link any device from 127.0.0.2 to 127.0.0.4 so that the window for the device would pop out
- Step4: Drag one of the device window, move out of the main window and drop it

Test 2 Expected Outcome: The device would perform nothing and ignore that while putting the device window back to original place


Record the results of each test and describe the outcomes.

Test 1 Outcome: The device work fine just as expected outcome

Test 2 Outcome: The IoT client crash and close down with unexpected error
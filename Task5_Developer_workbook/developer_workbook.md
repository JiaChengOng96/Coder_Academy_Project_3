# Developer workbook
### ***1. Define the following terms and state why they are important in the relating to the planning phase of securing a network:***
- security model
	
	mean that organisation would secure it network by defining and enforcing security polices on to the system such as access right to different people and integrity as well as protection to data. Security policies used for the security model should be design by the organisation security team. Within security policies, step are decribe to ensure that security of the network is achieve. There is many different security model for different case such as change of access right, achieve data intregerity protection and etc. Different organisation may implement different security model depend on it organisation need.

- threat model	
	
	mean that organisation would analyse the network and system then determine what vulnerability or issues it may have. Security team would start securing the network based on its finding on the network and start provide patches, contant fixes or create countermeasure to protect its network from the attacker. For example, using threat model would mean that the security team would find potential threat such as DDOS attack or unauthorised access to the system and start mitigating the issues to prevent from happening.


### ***2	Define the following terms and state why they are important in terms of the building phase of network:***
- security policies 
	
	Security policies is a guidelines of what the security team would need to do in order to achieve security for their network. A strong security policies includes correct access right, disk encryption, strong password and others else are consider important because it build the baseline of how a secure network should have and to prevent data theft. A strong policies help to secure the network where external attacker would not be able to unauthorised access the network system.

- security templates
	
	Security templates is a templates which consist of all the specific configuration format which the network administation can follow. For example by default most of the firewall only allow for specific port such as 80 and more others to be open for incoming or outgoing connection. For an organisation, secuirty templates are important because I provide a baseline for company to setup their network or device when they setting up a new device they will have a complete secure setup while not worrying what to include during the setup phrase.

### ***3	Define the following terms relating to security and state why they are important during the managing phase:*** 
- network monitoring 
	
	mean that constant monitoring over the network and provide maintainance according to the finding. Why monitoring is important because it help to check for known vulnerabilities against the network system specification and software used. Sample network monitoring tools such as nessus and wireshark help to provide information about what is happening within the network. For example, running nessus scan will provide report about that scan it perform as well as potential vulnerabilities found within the network which provide time or information for the security team to patch or fix. Sometime, manual scan is required for better network monitoring as external attacker is in constant evolving and new exploit would be develop.

- security policy enforcement
	
	mean that policy implement should be enforce where employee or user should not stop the habit to make environment secure. For example, employee should follow the policy where they need to encrypt their new device or use a strong password. This is important because of lacking policy enforcement would cause employee to be lazy to follow the policy such as not setting a good password as their credentials which may lead to unauthorised user to access into their network. This could potential cause a huge harm to the organisation.

### ***4	Describe TWO common types of ICT networks and why they are used and identify the hardware required to implement them.	100 - 200 words***

- LAN
	
	Local Area Network is a network which is private within an organisation and every device within the organisation is connected to one server which is the central point of the whole network. Most of the LAN are only accessible within the range of organisation such as within a building and LAN provide the capabilities to share the network resources such as network storage and other resources such as printer. The required hardware for LAN is cable, wireless network, router and switch for internal LAN connection as well as network service such as Wide Area Network to connect to the organisation other's LAN network which located at another location.

- WAN
	
	WAN aka Wide area network is a network communication which communicate over a large geographical area such as between cities or even countries. The aim of WAN is to provide the capabilities to connect one user from one location with another user from another location which is unreachable with LAN. For easier understanding, internet is using the WAN technologies where every user or organisation have their own identity from the Internet Service Provider (isp) which is used to connect with each others and as well as used to connect with smaller LAN or servers across big geagraphical area. The basic hardware requirement for WAN would be having device as a base, connecting to a router then connect to a switch which connect to the internet or other LAN network. Each local area network would have switch as an access point to the internet because device usually do not communicate with each other directly but would pass through a access point such as router or switch. Wireless connection would not be able to transmit beyond a range thus having a switch which use physical connection line would be the basic requirement.

### ***5	Describe TWO auditing and TWO penetration testing techniques.	250 - 300 words***

Auditing techniques
	mean to check, analyse and monitor the health of the network as well as the potential vulnerabilities or being attack 
- network scan
	
	Network scan can be done using nmap scan or nessus which will scan the network status such as current open port as well as guess of the system OS or technologies used. Using network scan we can identify the possible vulnerable port or potential attack based on technologies found. 

- packet capturing
	
	Packet capturing would provide information of what was requested or sent through the traffic to known or unknown source. Packet capturing is the best place to monitor what information is sent through using a service such as when requesting a webpage or using a software. There may be potential risk due to poorly develop program where sensitive data is sent through the packet without encryption or protection. Packet capturing also provide the capabilities to identify the source of packet to be analyse for validity

Penetration testing
	mean that tester would actively tries exploit or attack the network the see if it is exploitable.
- automation testing
	
	Automation penetration testing is where the testing is made autonomous and would automatically run at set interval or based on the set config. For example nessus is an automation tools to scan the network for possible potential vulnarabilities and using metasploit or searchsploits tools to execute attack based on the information gather. Automations tools mostly use for daily basis scan to scan for known vulnerabilities or common exploit on huge amount of computer or device and not being manually scan one by one. However for more in depth testing of certain device that show interesting information, penetration tester often use manual testing.
- manual testing
	
	Manual testing mean that tester often perform most task manually and modify the setting based on certain OS condition or term such as different version. Scanning stage can be done by any manual or automatic tools but when at the exploiting stage, penetration tester would be using exploit that work for the technologiess that they test by may modify to accomodate the different of OS or other additional service. For example an exploit that work for splunk version 3.3 may not work for some machine splunk version of 3.3 or newer version as different environment may behave differently.

### ***6	Describe how you would approach the analysis of logs and how these could assist investigation of security related networking matters.***

Depending on the way of how developer design the log file, we should focus on what is important shown in the log such as error, unknown authentication or others that may pose a threat or issues where log such as system user login into system should just be ignore. When identifying an log file, stuff such as information that is printed should be take note as well because some sensitive information may be unintentionally logged by the developer and may be compromise by other people. 

Steps that I would approach is:
1. filter and remove all log file that is redundant or just informational
2. start viewing log that has higher severity level or might pose potential vulnerability
3. focus on what is affected such as which program, operating system, machines/server is affected as well as the scale
4. research based on the information gather from step c and simulate a virtual environment and test it out


### ***7	Describe TWO elements of network infrastructure common to all organisations from the list below:*** 

- Switches

	Switches is the hardware which filter and forward packets between LAN segments. A switch provide multiple lan port for physical connection which would connect to all different device or router. It operate on the data link layer and sometimes on the network layer (based on the 7 model of the OSI Model). Switches has a port which provide the capability to monitor all traffic that flow through the switch.

- Router

	Routers forward data packets along the networks. Most of the time, router uses wireless technology to send data to other device whih also provide physical connection capabilities if neede. Router use forwarding tables and headers to be able to determine the best path for forwarding the packets to their destination. They also make use of different protocols to communicate with the host machine and the other as well as configure the best route between any two hosts machine.


### ***8	Describe the purpose and capabilities of TWO software and TWO hardware network security solutions.	200 - 300 words***

Software network security

- Wireshark - packet capturing
	
	Is an network packet capturing software to monitor and analyse the incoming or outgoing packet from to known or unknown sources or destination. Wireshark provide the capabilities to identify and follow the packet stream to check for the information that is convey through the network. 

- Network scanning - nessus

	Is an autonomous network scanner which provide different multi scanner capbilities to perform different type of scanning such as basic network scanning, host discovery and others more. Each scanner provide result according to the severity of issues found and provide example or information based on known information on the public. This is a good scanning tools which allow organisation to scan the whole network simultanously while not using manual scan one by one.

Hardware network security
- Router with firewall installed and capable of supporting better security protection
	
	Firewall provide the capabilities to filter the incoming and outgoing packet while providing access right to specific host/source to connect with the device. Router with firewall would be able to config so that none of the unauthorised source could harm the organisation network.

- Drive and device with encryption capabilities

	Using encryption and decryption technique, unless the key is know to other, for those drive compromise, lost or hack would not be consider data compromise but only losing an asset. Encryption require hugh amount of resource to perform which most device do not come with encryption technique. However, device that have encryption capabilities would be able to secure it network and device from authorise access.

### ***9	Explain the role of the following concepts in terms of the processes and techniques of object-oriented programming:***

- Inheritance

	Mean that there is a class of object that will be the base for other object class. The children object would inherit some or all of the property of the parent class. For example, a student class would have data of name, age, id, gender. While Bob object which is a student would inherit the student class and have the name, age, id, gender, course and more. In programming term, this technique is used to promote code reusability and efficiency.

- Polymorphism

	Mean that one object that can be used or seen as another. In programming term, polymorphism would act or behave different based on the different data type. For example in a car engine, commonly there are 5 gear from 1 to 5. Each gear is doing the same thing however the difference is how fast each gear spin and how much power each gear give. When driving, same amount of input would have different result depend on the gear it use which mean same item with different data type would behave many different form.

- Abstraction

	mean that the esential part of the coding would be remain while remove all the unnessary part such that developer would remove the complexity while increase the efficiency of the software implementation by hiding everything but important part that needed to be shown. Thinking as an example of art, artist would keep the original content but remove the unwanted detail about the art. Developer would name an entite that is revelant to the class and not doing something that is extra or unnessary.

- separation of concerns

	Means that in object-oriented programming, developer would seperate code into meaning full group of code such as an object using encapsulation and Polymorphism technique for easy maintainability and reusability. Separation of concerns also mean developer would code in a cleaner way and will not violate the rule of "don't repeat the code" 

### ***10	Describe the process for developing:***

- Small-size application development
Is where the total line of code needed for the application is approximately around 500 lines. Most of the time, it can be done with only one developer and the whole application only consist of limited amount of function to perform small amount of task. Small size application would be completed by how the developer want to do it

- Large-size application development
Is where the total line of code needed for the application may exceed 10,000 lines. For this application development model, it would take a few developer to code for the application and capable of performing many task compare to small size application. In large-size application development, developer often have their own part to complete and everything would be merge into one master branch when complete and finalised


### ***11	Identify and outline the key features of a graphical user interface (GUI), for interaction with an operator.***

Graphical user interface (GUI) uses the visual effect to enhance the user interaction and experience by giving easier accessibility and functionality with much technical knowledge. The few main key features includes menu, icon, widget, window and others help to enhance and improve usability. Firstly, every software comes with a window which will store all widget such as layer with all the buttons and functional element that an operator can interact with. Window can consist of multiple widget. As for icon, icon includes graphical image, visual or movie which enhance the understability of operator and making software more attractive. Moving on to interactive element of GUI such as button, pointer, movable menu selection and others provide an operator for a more visualise action. Button is an element which all the task can be group up together and be performed with a click of the button. There is multiple different button such as normal button, radio button which only have one choice and checkboxes which can have multiple selection. For pointer commonly mean mouse or touchpad where use can point toward certain part of the screen based on the cursor and operator can perform manipulator such as drag and click. Other than that, there is also selection menu where there are normal drop down menu, selection bar for choosing, rotation menu to increase or decrease value and other. The menu help to group information of the same field into a menu for operator easier accesibility without spending time to find.

### ***12	Describe the architecture of a framework for web-enabled application development.	150 - 200 words***

Framework is a tool with collection of libraries to guide developer to develop web-enabled application with capable to interact with application interface, component and the database. The main component for the framework of web application is the web browser and client, the application server as well as the database server. Framework is designed to be the standard way of deploying web application and allow developer to develop all common web application activity through framework. Framework also include many library which help developer to access for database, session management, code reusability and others to facilitate faster and easier deployment. 

Developing with a framework provide the code into server side code and client side code. Server side code mean the code that develop and only run in server while client side code only run on browser which mean a web application have two application running concurrently. Based on the component of framework, developer will be able to do database management, configuration and maintanence, provide better security, provide web service, have more web resource and others to enhance the developing process.

### ***13	Outline the techniques for implementing inter-process communication	150 - 250 words***

In computing term, process can be of two type which is independent process and co-operating process. Independent process mean that the process are not affecting or affected by other process while co-operatin process mean that it cooperate or will affect with or by other process. Inter-process commincation mean that one process would communication or cooperate with other process to perform an action which also can be say as one of the co-operate process method. There are multiple different technique to implement inter-process communcation such as message queuing, pipes, shared memory or socket. 

- ***Message queuing*** 
	
	mean that there will be sending or recieving multiple message from different running process while the OS kernel would manages the message. This technique require a communication link. 

- ***Pipes*** 

	means that when an information is send from one process to another, it can only be sent in one direction. It will also be buffered at the memory until everything is received.

- ***Shared memory***
	
	mean that multiple process are allow to exchange information through a predefined area of memory. The area of memory has to be pre-allocate before the data is able to gain access to the allocated memory address.

- ***Socket*** 

	is a end point communication for the process to communicate with another communcation through client and server communication.


### ***14	Identify and outline testing techniques as applied to distributed application development.***	

Distributed application development mean that part of the software is distributed over different multiple computer while non-distributed application is store within a computer. Multiple testing techniques can be use to test on distributed application such as functionality testing, behaviour with destructive input, scaling testing for performance and others more. In functionallity testing, most test are to validate and determine if the function of the application works as intended. Test is run on different operating system as well as different environment to test the functionality work without issues. Some time a similar environment may not work the same and some may even cause issues. Moving on, behaviour testing coming into play when testing an unclear design of software with unhelpful documentation. The core test for this testing unit is to test what will happen if user perform this action in an unexpected way. For example, what will happen if user supply more input than the system can accept, would it crash the system or will it be vulnerable with malicious input. Testing plays an important party in the software development to create a secure software. Last but not least, the software performance scale testing. This testing focus on monitor how software work with a similar environment but with limited resource such as weaker processor, limited access and missing driver for the hardware. For example, a game can run better with better graphic card, or a software can communicate with the organisation if the access to network connection for the software is granted. 


### ***15	Identify and outline techniques for implementing third-party supplied code.	200 - 250 words***

Given any programming language, there is heap amount of library and resources available for used and help to further enhance developer software without to recode the functionality that is already available. For example, when developing a calculator developer would need to develop function that would be calculating root of a number, the power or exponantian of a number and etc which if the developer include the math library provide, he could just implement the function with just one method name than implement all the calculation code. The technique to implementing third-party code varies for different programming language. For an example in our python program, we will have to import the packages in our python script file in order to use the third party code. 

Before import the package, we will need to install the package. In python library, there is a python repository that store all the python register third party code that can be download and used. By default when python is installed, there is few python libraries that will be installed as well. However for in our peer to peer application, we have to download the pyqt packages using the `pip3 install` command to install the package into the system. 

After installing the application, we can now use `import pyqt` to use all the preprogram code to developer program with GUI. Within the coding part to develop a button, depending on how developer import the package, generally developer would need to use the method such as `button1 = QPushButton('send')` which will create a button with label of send. This will be one of the technique for python programming language. In C language, we will need to use `#include math` rather than `import` to include the package into the program and for other language may be more different.

### ***16	Describe the basic principles of database management systems.	150 - 250 words***

Database is a storage which store a collection of data in a structured way which help for future managing and maintaning. Database management system which refer as DBMS, is a software which interact with the database and manage all the data within the database. The basic principles of database management system which includes data definition and data manipulation language. Data define what information is recorded into the database which have meaning such as username, age and others. Within database, data usually store in many table where each table have relationship with another table. Each table consist of group of data which is of similar type or related and come with an unique id which identify the primary data within that table. For example a student table would have their student id as the primary key which identify each unique student. Data management language is the languaged used to create, read, update or delete table within the database also known as CRUD. Example of data management language are SQL language and noSQL. SQL is the more commonly use database language within the industry. By using the CRUD keyword of DBMS, database admin can create a table with data using CREATE keyword, read the database with SELECT keywoard, update the database with UPDATE and delete the database with the DELECT keyword. 

### ***17	Outline the software development life cycle (SDLC)	100 - 150 words***

Software development life-cycle include planning phrase, analysis phrase, design phrase, implementation phrase, maintenance phrase and evaluation phrase. Each phrase has to be completed before moving into next phrase. Our initial planning phrase would be creating use case based on the client requirement. Following into analysis phrase, we will analyse the requirement from both our client and the use case which will be design for our approach on achieving the target feature in design phrase. Moving on to implementation phrase is where we will start doing code and creating our software feature. After the feature completion, we will have maintenance phrase where we will perform debug for any issues we encounter and provide fix to any issues within the feature. Last but not least, we will do the review for completed code before moving on toward the next feature. 


### ***18	Explain the coding used to create deployment applications.	150 - 250 words***

Deployment applicaitons is also mean the installation application in our application deployment which is used to install application in victim machine. The coding technique we use for our application is a script file with command to be execute. Within our installation script, we have command that run to download the bot application from another machine into the victim machine using wget command. After getting the file using wget, we will run the chmod command to change the right of the file so that we will be able to run the script file. After changing the access right, we will run the script file on the background so that the user would not need to perform another action to get it running. In our case, the installation script is simple because of the condition however installation can be more complex depending on the situation and environment as well as the requirement.

### ***19	Describe the design pattern used to implement remote procedure calls in the application you created in Task 3.	150 - 250 words***

The design pattern we used in the application is called proxy object design pattern where the proxy object we created in the RPC client is not the real object but an proxy object link to the RPC server. Remote procedure calls, aka RPC is a technique where the code processing would be done external rather than internal. For example, when we implement the RPC for our IoT application, we will have a RPC server which will accept the code from the RPC client and process it at the RPC server then send it back to the RPC client with the result. In this case, as long as the server does not stop, the data that the user have given previously would still be store and when user restart the RPC client it will not restart everything. 

### ***20	Explain the information and communications technology (ICT) hardware, software, security protocols and standards and organisational policies relevant to deployment of applications.	150 - 250 words***

In our case of deploying a bot application, we have certain requirement for hardware, software as well as all the policies that would need to met before we can deploy the bot.

In hardware case, we would need to victim to have a computer or device that run on linux with all neccessary basic component such as network card, router that connect the device to the internet. 

Moving on to the software, the device would need to have basic software that make the computer run as well as multiple requirement such as ssh packages, wget packages and also python3 install in the machine. Ssh is an optional in our case depending on how we want to insert our installation script file however wget and python3 package is essential because we relies on those packages to download our bot and execute it.

As for the secuirty protocols and standard, there would be firewall configure to disallow connection from unknown source. In our case, we use the victim to connect back to us which is by default allow by the firewall. Other than that, there would be anti-malware is install in the system as well which we will need to allow it before running our bot program.

In the organisational policies, some of the important notes are that user do not randomly download file from unknown source and also check with the integrity before running the file. There is also the policy of constantly monitoring of the network to prevent any unauthorised connection or any malicious program running within the network.
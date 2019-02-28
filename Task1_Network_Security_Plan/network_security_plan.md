# Network Security Plan

## *Problem Scenario*

You are a security consultant who has been asked to develop a network security plan for a client who is a tech obsessive/early-adopter. The client has a high speed internet connection and both a wired and wireless network which connects many different devices throughout their home.

## *Contextual Details*

The client works in the finance sector as a senior executive and lives with their partner and two children. The dwelling is a house which has a backyard with a back fence that adjoins a public park. The distance from the dwelling to the back fence is approximately 20 metres.

The power source and internet connection for the dwelling comes from overhead powerlines at the front of the house. There is no backup source of power. The wifi router is located on the kitchen bench. The home has a basic alarm system with motion detectors, but does not have phone home capability to a response company.

# *Technical Details*
***Router***: TP-LINK AC750

***Wifi-range extenders***: N/A, extended antenna attached to router with range well onto the street frontage and park.

***Network Attached Storage***: Apple time machine.

***Mobile Devices***: 2 x Samsung Galaxy S8 Android phones, 1 x iPhone 7, 1 x iPhone X

***Computers***: 2 x 2014 HP standard laptops running Windows 8.1, 2 x 2017 Macbook Pros

***Home Security System***: basic alarm system with motion detectors, and two Grandstream products, note: imagine you have visited the client's home, visit the Grandstream website and pick TWO network connected security products other than motion detectors that the client is using.

***IoT***: Smart fridge, Google Home, baby monitor, remote access to security camera monitoring front door via web GUI

# Instructions
You must write a network security plan to present to the client:

Identify threats to network security by creating a threat model for the network described in the Problem Scenario. You must:

### ***outline the common and emerging vulnerabilities for the client (150 - 200 words)***

### Common vulnerability:

DOS attack 
- Grannstream GXP-2000 VoIP Descktop phone is vulnerable to denial of service attack. If the user DOS attack the client, the client would not be able to use the ip decktop phone.

App Provisioning Vulnerability
- Grandstream android desk phone of version 1.0.3.55 or earlier is vulnerable to app provisioning where it allow to automatically on startup setting up the configuration setting for the desk phone.

iphone 7 support up to ios 10 and apple time machine - KRACK wifi vulnerabililty
- There are many vulnerability evovle around ios 10. If the phone is updated upto 10.3.3, one of the high severity vulnerabilities is wifi vulnberability where hacker can intercept someone traffic that is not encrypted when the iphone user is search for wifi and is within the range of hacker without the need of user credential or apple id. Apple still provide support for iphone 7 however iphone would not be compatible to update to later than ios 10.

TP-LINK AC750
- Device model CISCO version reach end of life support. Vulnerability found is that if user have authenticated local access, it would run arbitary code execution or cause denial of services

Apple time machine - arbitary code execution through buffer overflow
- There is memory corruption issues existed in DNS data parsing which would cause arbitary code execution (CVE-2015-7029)

### Emerging Vulnerability:

Window 8.1 system end of main-stream support
- without the main-stream support, window 8.1 device would got some patches for critical level vulnerabilities until year of 2023 which if the vulnerability found is not critical it would not be patch. From the link below, there are more critical level vulnerability found for window 8.1.
- links: https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-26434/Microsoft-Windows-8.1.html

Samsung s8 latest android version is 8.0 
- Android 8.0 have few vulnerabilities such as android 8.0 system privilege escalation(cve-2017-13209) which would perform privilege escalated within the android phone or some latest local privilege escalation(CVE-2018-9558). There is current no further android version update for samsung s8 and version 8.0 is current latest which later version is to be announce.

### ***profile TWO potential attackers, and describe: (200 - 300 words for each profile)***

Random hacker
- Motivation: Just because they are interest to break into people network and feel the sense of achievement on breaking stuff
- Scenario: A random hacker who just thought of hacking a neighbourhood or random household and start scanning the whole area. Coincidently, our client house is also within the area and became one of the target as well. The hacker then start trying to hack into the house using social engineering technique such as scanning all nearby area wifi name and range. Incidently the client wifi range have be extended which was detected by the hacker as a chance to mimic the wifi and provide a evil twin in hoping that the client household member would accidentally connect to his evil twin wifi and start the traffic routing and reading all the credentials.
- Technical expertise: The hacker would need to be knowledgable to set up a wifi twin to trick the user to connect to. Secondly, the hacker would also need to know the necessary skill to social engineering people while also require basic skill in data or information routing.
- Severity: If the hacker get someone from the client household to connect to him, he would be able to get all the traffic and data to follow through him and also potential sensitive information. In this case, it would be severe enough and may potential cause huge damage with all the data that the hacker can retrive. If he is able to retrieve more than just customer daily data such as the client company product or credential data, it can cause unthinkable damage to the client and his organisation as well.

Physical burglar
 - Motivation: Burglar are only interest in robbing valuable items may or may not specific target for example like gold, jewellery and other else
 - Scenario: Burglar may be armed with various type of weapon or without anything. Assume that the whole family are not at home, the burglar would need to cut the only power supply which supply the power and would then disable the only basic alarm system installed. He can then enter through their backdoor and start stealing valuable stuff. In this case we say that there is only one burglar, so the amount of stuff he can carry is limited which he focus more on easy money stuff like gold bar or jewellery or even try pick lock the safe(If there is a safe) 
- Technical expertise: To rob a house would required less to no technical skill. However in our scenario there is a basic alarm system with motion detection. So one of the skill needed is to disable the motion detector or cut the power supply. Other than that he may need some simple lock picking skill to unlock the door or he can just brute force the door in a way that no one would notice it. When stealing stuff would required no technical skill but if there is a safe with lock on it, it would required high technical skill to open the lock.
- Severity: This attack can be consider medium to severe because the burglar can be armed and harm the household member if there is member staying at home. Other than that, if the burglar decide to steal device that contain data, he can sell those data if there is data that is valuable. In contrast, if the burglar only steal gold or jewelery stuff then would not cause huge amount of damage would only only lose some asset.


### ***categorise the threats/issues you have identified and provide a statement which gives them an overall qualitative assessment of their security posture. (150 - 200 words)***

The current of risk expose of the client is high based on the finding from question 1. We can see that most of the devices, or product that they use are vulnerable and there is no future support or further update to fix the issues of being unsafe. Other than that based on the assuming house floor plan layed out from scenario, we conclude that there is one that is highly catasrophic risk which is unlikely to happen yet not possible to change. The highly catasrophic risk is that the house only have one power grid which is visible to public and there is no backup power supply anywhere. If the power grid were be cut by attacker, any security feature of the house such as the alarm with motion detector or maybe the grandstream security product would not work, which then would cause a high risk to the client and his family. Besides that, since the scenario mention that the client and his family total to 4 member within the family would suggest that each of them hold one laptop. This mean that the client is using a laptop for both work and personal use which is a serious issue where anything happen to the laptop would cause potential leak of his company information due to not using encryption on laptop or others. The wireless router use within the household are not secure as it is and there is some security finding as well as it is extended toward the house area range which any people who passby would be able to search the wireless. This could lead to a mimic of same wifi name to trick the client or family member to connect to it. Last but not least, there are many IoT device within the house which may be vulnerable because most of the IoT device do not have firmware update after purchases as well as data would be store within the chipset of IoT device. If any person would retreive any of the IoT device would be able to get data or information about the house network.


## Analyse the security risks and outline the process of risk management, you must:
outline the risk management process you will undertake to assess risks in plain-English. (200 - 300 words)

In this part, we will be assessing the risk mention in question 1 using the 5 * 5 matrix to scale the risk in term of likelyhood and consequences. The rating of risk assessment total up to 25 point from 5 point of likelihood and 5 point of consequences. 1 point from likelihood mean low posibility to none of happening while 5 point of likelihood mean high chance to guarantee happening. While for 1 point of consequences means low consequences and 5 point of consequences rate means critical consequences. 

![risk-matrix](https://github.com/JiaChengOng96/Coder_Academy_Project_3/blob/master/Task1_Network_Security_Plan/matrix.png)

***image link: https://1.bp.blogspot.com/-glnMOx-KzBc/WH-mao9fMZI/AAAAAAAAARo/8Y_NqUklpVYKCIXeT5fkJuWJSjbbcWBTgCLcB/s400/5x5%2BRisk%2BMatrix.png***

***Risk 1***: Window 8.0 end-of main stream support
End of main stream support from microsoft team means that window 8.0 device would not be on the priority list of the support list and maybe would receive patches for vulnerability if the microsoft team have the capabilities. Through my research, there are many vulnerabilities found targeted window 8.0 which range from low to critical. This show that the risk have a 5 point of likelihood of happend while 4 point for consequences depend on average of vulnerability found mean total up to 20 point which conclude as a high risk to the client.

***Risk 2***: KRACK vulnerability
KRACK vulnerability is found and potential vulnerable to all device which use WPA protection in their wifi network. The vulnerability work as long as they are within range and the device network is using WPA standard, this vulnerability would have high chance of suceeding in exploiting. However, this exploit only allow the attacker to view the traffic which is not encrypted with https and nothing else. This show that this vulnerability has a 5 point in likelihood while 2 point in consequences due to the limitation of what attacker can do and total up to 10 which is a low risk finding.


## identify and categorise THREE potentially valuable assets on the network, you must (400 - 500 words):

identify the type of asset and state why it is valuable

The laptop of the client
- This is important piece of asset for the client as laptop of the client potentially consist of many data of it company such as email within organisation, product plan of company, financial detail as well as potential report for future plan and etcs. For the attacker, if the attacker is spear phishing for the company information or purely revenge of his company, this laptop maybe of high value because he can blackmail the client, destroy the client's company reputation and so on. However if the attacker is just a random hacker would don't care about data and purely like to break into other people stuff or some random burglar who even may not rob his computer will not see this laptop as valuable stuff. For both client and attacker, this laptop can cost up to millions depend on how much company data is store within the laptop storage. Thus, this device would require protection from attack. Example of protection would be to have different layer of security lock, having long password, full drive encryption and one most important security protection is to seperate personal and work laptop.

Apple Time Machine
- This may be important depending on the apple time machine is for family use or for client use to store company data. However for this scenario, we will assume that the apple time machine is for the storing client company data. Thus, this would be an important asset which potential hold many information which is yet to be publicify. For the attacker point of view, this would also be a valuable target because if he is succeed on breaking into the time machine, he could get many data from the time machine. Even if the attacker is not skilled enough to extract data, he should still able to destroy or break the apple time machine. So in this case, the appli time machine would cost a huge amount of money for both the client or attacker. This device would require protection such as adding firewall before connection to the machine with anti malware capabilities, adding strong password and credential to access the storage space as well as constantly update with the patch provided by apple support.

The router
- This may seem insignification to the client as router does not storage any company data or personal data but it actually important for the client because it is the only point of access to the internet. Router would be the only connection available within the house and there is no other backup connection. From the attacker point of view, router is always the attack start point because by exploiting the router (other than creating a new evil twin to trick member of client house to connect to it), the attacker would be able to intercept all the traffic that flow through the router as well as start inflitrate into the whole house network. Depending on the situation, router can cause to cost up to thousand of dollar or only the price on one router. It is because attacker may not be able to hack into the router which would not cost any client money but possibly cost to cover broken router. In contrast, if the attacker break into the router then it would cost more than just a router. Router should come with pre-install firewall or anti malware and also purchase another layer of physical firewall before going through the router for extra protection.


### Create a risk management plan and security controls based on your threat model and assets on the network, you must:

### ***design two policies which outline security controls and requirements to mitigate TWO threats in your threat model. (300 - 400 words per policy)***

- Window 8.0 end of main-stream support

    This is a threats to the client work environment as any company data that is stored within the laptop would have high chance of being exploit. The laptop is use for both personal and work which should not be done in the first place due to potential malicious software installation for personal use which would exploit the laptop.

Policies and requirement to mitigate:

1. Constantly perform window update with the latest patches available
2. Seperate the laptop into work use laptop and personal use laptop
3. Never installed any unnecessary software or unknown program on the work laptop
4. Perform full drive encryption of industry standard to prevent information theft
5. Using strong password to prevent bruteforce attack and not a commonly use password
6. Never connect work laptop to a home wifi that is not secure and tries to minimise connection time toward wifi
7. Install anti-malware or anti-virus to have one extra layer of security on the laptop
8. If possible, switch to a laptop which as a operating system that is still in main-stream support such as window 10 device

- Router and power grid lines

    This router do not meet industry standard for the client to perform work related task that required internet. Through nessus basic scan, I found that there is high rate vulnerability on the router and there is no layer of protection on the router. There is only one power grid line that provide power to the house and if the power line is cut would cause the house to have no electricity, this would cause the client to not be able to perform emergency work related task.

Policies and requirement to mitigate:

1. Install another internet cable and router which is only for work use and is industry level protection such as fully encrypted connection
2. Purchase another physical firewall and connect the router after the physical firewall so that there is one layer of protection before connecting to router
3. The client can also purchase a router which has firewall or anti-malware install in to router to have a more secure connection 
4. Install an extra power supply such as back-up power generator or emergency battery for short term use to prevent power supply cut and losing connect to working environment
5. Constantly check for update for the router to have the latest firmware so that there would be lesser chance of having vulnerability
6. Reduce the range of the wifi router to only within the house area so that the wifi would not be detect outside of the house compound so that public would be able to exploit the KRACK vulnerability
7. Sign contract with an external security response team to ensure that the team would take action as soon as an alert have been detected such as power grid is down
8. Change the password to a strong and longer password which also not a commonly found password


### ***create a timeline and budget for the implementation of policies (200 - 300 words)***

Most of the policies would need to be completed within the timeline of one week to ensure the best possible security around the client. The budget would be varies depend on security implementation.

In 1 day time:
- Change the password for both the router and the laptop to be more secure 
- Purchase a new laptop for work use which have main-stream support such as window 10 laptop 
- Perform update to the latest possible firmware and also latest update for any offical software for all device
- uninstall any unwanted or unnecessary software to remove any potential vulnerability and never install work-unrelated software to the work laptop
- Perform the full drive encryption using window bit locker to secure the data within the work laptop
- install one of any anti-virus such as kaspersky, norton and others to protect from virus or malware for all laptop

Within 2 to 3 day:
- contract with an external security response team for any of alert or potential risk happenly physically around the house
- Contact an external ventor to install an external power supply such as power generator or emergency power battery for emergency use when the power supply from the power grid is cut 
- request the client company to setup router for work use at home

Within a week:
- Client company security team come to perform a setup on secure cable and internet line for the client to work at home and a work router that install with a firewall or setup another 
- The security team also help to configure both work network connection range and the home network connection range not to be accesible outside of the compund
- installation of the emergency power supply is complete

Constantly follow:
- reduce amount of time for device to connect to the internet to reduce the risk
- never connect personal device to the work network and never connect work device to personal home network

Budget:
1. router installation and cable implementation would cost roughly up to 200 for the secure connection per month and around 150 for a decent router
2. Purchasing a new laptop would cost around 2000 dollar and with around 100 for a copy of anti virus software
3. Sign contract with incident response team would roughly up to 100 per month
4. request for installing emergency power supply would cost around 300 for equipment and around 100 dollar for installation fee

***Rough total*** of the money to implement would total up to around 3000 intially and around 300 per month for paying work internet and incident response team


### ***write a plain-English explanation for the client relating to the timeline and budget for implementation of the risk management plan (150 - 200 words)***

Incident response team is a must because it is like an insurance to protect the company asset that is store at the house which would need to pay regulary. This should be perform within one week is due to consideration of allocating the response team to have a check on the house and registering the necessary equipment. Besides, using only one laptop for both personal and work is a security risk as explain above and need to be done within one day time frame because of the risk. Thus, client would need to purchase a standard usable laptop with recommended security protection would cost up to around 2000 dollar with one piece of anti virus for extra layer of protection. Moving on to installing a work only network connect would be important for the client and should be complete within one week time frame because would need to call in a team to install hardware component and setting everything up. This is important for the reason being that if the client use home network to connect to the company internal network create another security issues for company because if the home network were to exploit would cause the company network to be in risk. Thus by seperating into work router and home router would prevent from additional risk to the company assuming that the client would not connect anything non-work related device to the work router.

### ***create a process for continuous review in the form of a list of steps to be followed to maintain the security controls you have designed (100 - 200 words)***

Steps or action necessary to maintain security controls:
- Constantly update the firmware of device or anything that is connect to the network to get the latest security patches.
- never connect personal device to the work network and never connect work device to personal home network
- Change the house network as well as device password every few month to prevent password bruteforce crack
- Discuss for the company security team to have a monthly house security check to identify any new potential risk arise
- Any new device or implementation would need to seek advice some security team to ensure safety of the house member
- Client would need to monitor their children to ensure that they do not install any harmful software that may harm the home network


### ***provide evidence you have received feedback from a industry expert on your risk management plan, and how you have modified your approach based on feedback (notes on feedback or written feedback from industry expert in addition to 100 - 200 words on your response to this feedback)***

![Feedback](https://github.com/JiaChengOng96/Coder_Academy_Project_3/blob/master/Task1_Network_Security_Plan/feedback.PNG)

The image above show the feedback i got from my educator. For the window part i have not only fixed the minor issues, I have also added more information as well as link to list of potential emerging vulnerability on window 8.1 laptop. On top of that, I have also format it to show the common vulnerability group as well as emerging vulnerability group to show the priority as well as to answer the question. From the feedback, I have also fix some of the part to make it more readable.


### ***Design an auditing and incident response plan to handle a security incident affecting the network described in the Problem Scenario***

Your Incident response plan must include:

### ***a description of the incident it will address (150 - 200 words)***

One day there is an incident happen around the client house.

- Someone broke into the client house through the back door. 
- Before entering the compound, the attacker have stop the camera by destroying it from afar. 
- Then he move into the house to start stealing
- He stole some of the valuable stuff such as gold bar or jewellery and also went to the client machine.
- He then start performing exploit on the 
- When the client reach home from the family day trip, he found that there is no power to his house.
- It was later that he found out about the incident where someone already broke into his house. 
- When he is trying to find out what has been stolen but it seem that he only know that stuff like gold bar, jewellery and other accessories have been stolen.
- He contact and report to the police about this case
- Few day later after responding to the case, the house issues have been fixed. But he found something out of ordinary when he is working on home.
- He then receive a blackmail email blackmailing him money for the data that suppose only he and the company have
- He then call the company security team to report of the issues and seek for advice as this is a cyber security breach

### ***an outline which states how it provides appropriate coverage for the incident which must refer to an authoritative source on incident response (100 - 200 words)***

Link: https://cyber.gov.au/infrastructure/guides/strategies-to-mitigate-cyber-security-incidents/

From the incident we know that the attacker have already hack into the router because the hacker sent an blackmail email.

Action that need to be perform:
- The client would need to switch away the router
- Request the security team to perform installation and network testing on the new router as well as set up a firewall to prevent unauthorised access
- The router would need to be constantly patch to have the latest security protection
- Sign up for a security incident response team to protect further future incident

create an auditing checklist with FIVE items which includes:

software and hardware configurations to be checked which support security controls and incident response procedures
suggested penetration tests that should be conducted to verify security controls are in place to prevent the incident

- Ensure that the exploit router have been remove and not to be use anymore 
- Request the security team to setup the new router as well as an extra router for work use only 
- Add an additional physical firewall to protect the router
- Hire penetration tester to test the network to heck for vulnarability
- Sign up for an incident response team for future incident as well as security team to monitor the network monthly

### ***create a process, a list of steps, that should be followed should the incident occur, the process must include (200 - 300 words):***

A preamble which has an allocation of responsibilities to relevant persons
specific details relating to the management, monitoring and auditing of software and hardware in the context of the incident

Allocation of responsibilities toward the incident:

- Responsible: Consultant
- Accountable: Client
- Consulted: Partner
- Informed: Work

Steps:

1. First identify the cause of the issues by contacting a security team to perform a check on the house network
2. After the check, the security team should be able to identify the problem in this incident would be the router
3. The router would need to be unplug and remove
4. Request a more secure router for the home network as well as the client should request one secure router with a more secure connection just for work use only
5. After all the setup, the client should request for an additional layer of protection by installing a physical firewall for the router
6. After all the hardware installation, the client should hire penetration tester to perform pen test on the router to check for vulnerabilities or potential issues
7. Client should also follow the instruction issues by the pen test team to mitigate any potential vulnerabilities the router may have through patches or firmware update
8. If wanted, the client could also install a dedicated system that would monitor the network using comersial software such as nessus to run daily or weekly scan for vulnerability and send a report for client as well as the security team



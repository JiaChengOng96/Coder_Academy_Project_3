


Problem Scenario
You are a security consultant who has been asked to develop a network security plan for a client who is a tech obsessive/early-adopter. The client has a high speed internet connection and both a wired and wireless network which connects many different devices throughout their home.

Contextual Details
The client works in the finance sector as a senior executive and lives with their partner and two children. The dwelling is a house which has a backyard with a back fence that adjoins a public park. The distance from the dwelling to the back fence is approximately 20 metres.

The power source and internet connection for the dwelling comes from overhead powerlines at the front of the house. There is no backup source of power. The wifi router is located on the kitchen bench. The home has a basic alarm system with motion detectors, but does not have phone home capability to a response company.

Technical Details
Router: TP-LINK AC750

Wifi-range extenders: N/A, extended antenna attached to router with range well onto the street frontage and park.

Network Attached Storage: Apple time machine.

Mobile Devices: 2 x Samsung Galaxy S8 Android phones, 1 x iPhone 7, 1 x iPhone X

Computers: 2 x 2014 HP standard laptops running Windows 8.1, 2 x 2017 Macbook Pros

Home Security System: basic alarm system with motion detectors, and two Grandstream products, note: imagine you have visited the client's home, visit the Grandstream website and pick TWO network connected security products other than motion detectors that the client is using.

IoT: Smart fridge, Google Home, baby monitor, remote access to security camera monitoring front door via web GUI

Instructions
You must write a network security plan to present to the client:

Identify threats to network security by creating a threat model for the network described in the Problem Scenario. You must:

outline the common and emerging vulnerabilities for the client (150 - 200 words)
DOS attack 
- Grannstream GXP-2000 VoIP Descktop phone is vulnerable to denial of service attack. If the user DOS attack the client, the client would not be able to use the ip decktop phone.

App Provisioning Vulnerability
- Grandstream android desk phone of version 1.0.3.55 or earlier is vulnerable to app provisioning where it allow to automatically on startup setting up the configuration setting for the desk phone.

Window 8.1 system end of main-stream support
- without the main-stream support, window 8.1 device would got some patches for critical level vulnerabilities until year of 2023 which if the vulnerability found is not critical it would not be patch.

Samsung s8 latest android version is 8.0
- Android 8.0 have few vulnerabilities such as android 8.0 system privilege escalation(cve-2017-13209) which would perform privilege escalated within the android phone. There is current no further android version update for samsung s8 and version 8.0 is current latest which later version is to be announce.

iphone 7 support up to ios 10 and apple time machine - KRACK wifi vulnerabililty
- There are many vulnerability evovle around ios 10. If the phone is updated upto 10.3.3, one of the high severity vulnerabilities is wifi vulnberability where hacker can break someone iphone when the iphone user is search for wifi and is within the range of hacker without the need of user credential or apple id. Apple still provide support for iphone 7 however iphone would not be compatible to update to later than ios 10.

TP-LINK AC750
- Device model CISCO version reach end of life support. Vulnerability found is that if user have authenticated local access, it would run arbitary code execution or cause denial of services

Apple time machine - arbitary code execution through buffer overflow
- There is memory corruption issues existed in DNS data parsing which would cause arbitary code execution (CVE-2015-7029)


profile TWO potential attackers, and describe: (200 - 300 words for each profile)

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


categorise the threats/issues you have identified and provide a statement which gives them an overall qualitative assessment of their security posture. (150 - 200 words)

The current of risk expose of the client is high based on the finding from question 1. We can see that most of the devices, or product that they use are vulnerable and there is no future support or further update to fix the issues of being unsafe. Other than that based on the assuming house floor plan layed out from scenario, we conclude that there is one that is highly catasrophic risk which is unlikely to happen yet not possible to change. The highly catasrophic risk is that the house only have one power grid which is visible to public and there is no backup power supply anywhere. If the power grid were be cut by attacker, any security feature of the house such as the alarm with motion detector or maybe the grandstream security product would not work, which then would cause a high risk to the client and his family. Besides that, since the scenario mention that the client and his family total to 4 member within the family would suggest that each of them hold one laptop. This mean that the client is using a laptop for both work and personal use which is a serious issue where anything happen to the laptop would cause potential leak of his company information due to not using encryption on laptop or others. The wireless router use within the household are not secure as it is and there is some security finding as well as it is extended toward the house area range which any people who passby would be able to search the wireless. This could lead to a mimic of same wifi name to trick the client or family member to connect to it. Last but not least, there are many IoT device within the house which may be vulnerable because most of the IoT device do not have firmware update after purchases as well as data would be store within the chipset of IoT device. If any person would retreive any of the IoT device would be able to get data or information about the house network.


Analyse the security risks and outline the process of risk management, you must:
outline the risk management process you will undertake to assess risks in plain-English. (200 - 300 words)

***************Use the 5 * 5 metric to calculate and provide the easiest way for people to understand the risk


identify and categorise THREE potentially valuable assets on the network, you must (400 - 500 words):

identify the type of asset and state why it is valuable

The laptop of the client
- This is important piece of asset for the client as laptop of the client potentially consist of many data of it company such as email within organisation, product plan of company, financial detail as well as potential report for future plan and etcs. For the attacker, if the attacker is spear phishing for the company information or purely revenge of his company, this laptop maybe of high value because he can blackmail the client, destroy the client's company reputation and so on. However if the attacker is just a random hacker would don't care about data and purely like to break into other people stuff or some random burglar who even may not rob his computer will not see this laptop as valuable stuff. For both client and attacker, this laptop can cost up to millions depend on how much company data is store within the laptop storage. Thus, this device would require protection from attack. Example of protection would be to have different layer of security lock, having long password, full drive encryption and one most important security protection is to seperate personal and work laptop.

Apple Time Machine
- This may be important depending on the apple time machine is for family use or for client use to store company data. However for this scenario, we will assume that the apple time machine is for the storing client company data. Thus, this would be an important asset which potential hold many information which is yet to be publicify. For the attacker point of view, this would also be a valuable target because if he is succeed on breaking into the time machine, he could get many data from the time machine. Even if the attacker is not skilled enough to extract data, he should still able to destroy or break the apple time machine. So in this case, the appli time machine would cost a huge amount of money for both the client or attacker. This device would require protection such as adding firewall before connection to the machine with anti malware capabilities, adding strong password and credential to access the storage space as well as constantly update with the patch provided by apple support.

The router
- This may seem insignification to the client as router does not storage any company data or personal data but it actually important for the client because it is the only point of access to the internet. Router would be the only connection available within the house and there is no other backup connection. From the attacker point of view, router is always the attack start point because by exploiting the router (other than creating a new evil twin to trick member of client house to connect to it), the attacker would be able to intercept all the traffic that flow through the router as well as start inflitrate into the whole house network. Depending on the situation, router can cause to cost up to thousand of dollar or only the price on one router. It is because attacker may not be able to hack into the router which would not cost any client money but possibly cost to cover broken router. In contrast, if the attacker break into the router then it would cost more than just a router. Router should come with pre-install firewall or anti malware and also purchase another layer of physical firewall before going through the router for extra protection.


Create a risk management plan and security controls based on your threat model and assets on the network, you must:
design two policies which outline security controls and requirements to mitigate TWO threats in your threat model. (300 - 400 words per policy)
create a timeline and budget for the implementation of policies (200 - 300 words)
write a plain-English explanation for the client relating to the timeline and budget for implementation of the risk management plan (150 - 200 words)
create a process for continuous review in the form of a list of steps to be followed to maintain the security controls you have designed (100 - 200 words)
provide evidence you have received feedback from a industry expert on your risk management plan, and how you have modified your approach based on feedback (notes on feedback or written feedback from industry expert in addition to 100 - 200 words on your response to this feedback)
Design an auditing and incident response plan to handle a security incident affecting the network described in the Problem Scenario

Your Incident response plan must include:

a description of the incident it will address (150 - 200 words)

an outline which states how it provides appropriate coverage for the incident which must refer to an authoritative source on incident response (100 - 200 words)

create an auditing checklist with FIVE items which includes:

software and hardware configurations to be checked which support security controls and incident response procedures
suggested penetration tests that should be conducted to verify security controls are in place to prevent the incident
create a process, a list of steps, that should be followed should the incident occur, the process must include (200 - 300 words):

A preamble which has an allocation of responsibilities to relevant persons
specific details relating to the management, monitoring and auditing of software and hardware in the context of the incident
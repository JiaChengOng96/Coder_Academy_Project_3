# Concept

`bot.py` is installed on the victim machine. Every so often, it wakes up
and does a standard HTTP request to a server machine. The server replies
with a file containing one instruction and an optional payload. If the
client has anything to reply with, it sends a POST request otherwise
goes back to sleep.

# Files

`test_server.py` and `command.txt` are files running on the server
(attacker) machine.

`bot.py` is a script intended to be run on the client (victim) machine.

# Command codes

See bot.py for command codes and their meaning. For example,

    write
    test.txt
    These are the contents

can be put into `command.txt`.

# TODO

* An install script
* An uninstall script added to the bot

__module_name__ = "Auto messages"
__module_version__ = "0.1"
__module_description__ = "send messages when some word appear in dialog"
__module_author__ = "Powabanga"

import xchat

    if word[1]=="!help":
        xchat.command("echo  14Open and Automessage.py with a text editor to change this message:14")
        xchat.command("say 00Message2 :")

    if word[1]=="!blabla":
        xchat.command("say  14Message3 :14 ")
        xchat.command("say 00Message4")


    return xchat.EAT_NONE


# lance les fonctions
EVENTS = [("Channel Message", 1)]
for event in EVENTS:
    xchat.hook_print(event[0], stop_mess_auto, event)

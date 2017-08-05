__module_name__ = 'Nicknameban'
__module_version__ = '0.1'
__module_description__ = 'cban user for a spécific time.'
__module_author__ = 'Powabanga !'
 
import xchat
 
c = '\x02\x0303'
help0 = 'Type /pban {0-3} [nick] ' 
 
print('%s%s has been loaded.' % (c, __module_name__))
 
def pban(word, word_eol, userdata):
    if word[1]=="0":
        xchat.command('ban %s!*@*' % (word[2]))
        xchat.command('kick %s Merci de choisir un pseudo plus addapté. :)' % (word[2]))

    if word[1]=="1":
        xchat.command('ban %s*!*@*' % (word[2]))
        xchat.command('kick %s Merci de choisir un pseudo plus addapté. :)' % (word[2]))

    if word[1]=="2":
        xchat.command('ban *%s!*@*' % (word[2]))
        xchat.command('kick %s Merci de choisir un pseudo plus addapté. :)' % (word[2]))

    if word[1]=="3":
        xchat.command('ban *%s*!*@*' % (word[2]))
        xchat.command('kick %s Merci de choisir un pseudo plus addapté. :)' % (word[2]))
	


def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))
 
xchat.hook_command('pban', pban, help=help0) 


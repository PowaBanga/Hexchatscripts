
__module_name__ = 'Chronoban'
__module_version__ = '0.1'
__module_description__ = 'ban user for a spécific time with an automatic reason.'
__module_author__ = 'Powabanga !'
 
import xchat
 
c = '\x02\x0303'
help0 = 'Type /cban{0-3} [Channel] {Seconds} [nick] [domaine] [user] [host] - to ban *!*@*.host'
help1 = 'Type /cban{0-3} [Channel] {Seconds} [nick] [domaine] [user] [host] - to kickban *!*@domain'
help2 = 'Type /cban{0-3} [Channel] {Seconds} [nick] [domaine] [user] [host] - to ban *!*user@*.host'
help3 = 'Type /cban{0-3} [Channel] {Seconds} [nick] [domaine] [user] [host] - to ban *!*user@domain'
help4 = 'Type /cban{0-3} 1=*!*@domain, 2=*!*user@*.host, 3=*!*user@domain. Type /help cban{1-2} for more help'
 
print('%s%s has been loaded.' % (c, __module_name__))
 
def cban0(word, word_eol, userdata):
        xchat.command('ban *!*@*.%s' % (word[6], word[2]))
        xchat.command('timer %s unban *!*@*.%s' % (word[2], word[4]))
 
def cban1(word, word_eol, userdata):
        xchat.command('kickban %s Vous avez été banni de ce cannal pour une durée de %s secondes' % (word[3], word[2]))
        xchat.command('timer %s unban *!*@%s' % (word[2], word[4])) 

def cban2(word, word_eol, userdata):
        xchat.command('ban *!%s@*.%s' % (word[5], word[6], word[2]))
        xchat.command('timer %s unban *!%s@*.%s' % (word[2], word[5], word[6]))

def cban3(word, word_eol, userdata):
        xchat.command('ban *!*%s@%s' % (word[5], word[4], word[2]))
        xchat.command('timer %s unban *!*%s@%s' % (word[2], word[5], word[4]))

def cban4(word, word_eol, userdata):
        print('Type /cban{0-3} 1=*!*@domain, 2=*!*user@*.host, 3=*!*user@domain. Type /help cban{1-2} for more help') 

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))
 
xchat.hook_command('cban0', cban0, help=help0) 
xchat.hook_command('cban1', cban1, help=help1) 
xchat.hook_command('cban2', cban2, help=help2)
xchat.hook_command('cban3', cban3, help=help3)
xchat.hook_command('cban', cban4, help=help4)

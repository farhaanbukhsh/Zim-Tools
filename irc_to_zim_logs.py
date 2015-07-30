###################################################################################################################
#  This script is written by Farhaan Bukhsh and is licensed under MIT license , the script can be used to backup  #
#  your irc logs to your zimwiki provided you make changes to the apt variable.                                   #
###################################################################################################################




import commands
import time
import datetime
date_list = []
date = commands.getoutput('date')
date_list = date.split()

#Replace 'source' with the log file from your irc client , For eg:/home/farhaan/.xchat2/xchatlogs/FreeNode-#dgplug.log
log_file = open('source', 'r')
start_log_line = '**** BEGIN LOGGING AT '
chats = []
log_to_zim = False
chats = log_file.readlines()

raw_input('Press Enter to Start logging >')

# Replace 'destination' with the zim folder in your zim directory, For eg: /home/farhaan/Notebooks/Notes/Dg_Plug/
file_name = 'Dgplug-'+date_list[0]+date_list[1]+date_list[2]
zim_file = open('destination'+file_name+'.txt','a')
zim_file.write('Content-Type: text/x-zim-wiki\nWiki-Format: zim 0.4\n')
ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('Creation-Date: '+'%Y-%m-%d'+'T'+'%H:%M:%S'+'+05:30')
zim_file.write(st+'\n')
zim_file.write('\n\n======'+file_name+'======\n\n')
for msg in chats:
  if msg.startswith(start_log_line) and date_list[0] in msg and date_list[1] in msg and date_list[2] in msg:
   log_to_zim = True
   print 'about to log'
  if log_to_zim :
   zim_file.write(msg)
log_file.close()
zim_file.close()
print "logging...."
print "File is created please update your index for making changes visible"

# Zim-Tools
This script is written to backup your irc logs to your zimwiki. It uses *Python 2*. It simply copies the log from irc log file and creates a zim page and writes into it.

#Usage
You just have to run the script as :

`$python irc_to_zim_logs.py`

#Tweaks

Various tweeks you need to make to utilise this script.

On line 17

`log_file = open('source', 'r')`

Replace 'source' with the log file from your irc client , For eg:/home/farhaan/.xchat2/xchatlogs/FreeNode-#dgplug.log



On line 27

`zim_file = open('destination'+file_name+'.txt','a')`

Replace 'destination' with the zim folder in your zim directory, For eg: /home/farhaan/Notebooks/Notes/Dg_Plug/

#Links

[Zim-Wiki](http://zim-wiki.org/)

Use it

#License

'Feel free to use'™ , just give credits to the author else you will be punished by your guilt in the middle of the night.

import sys, os, datetime



def gitcmd (cmd):
    os.system(cmd)

am = sys.argv

now = datetime.datetime.now()
nowtime = now.strftime('%Y.%m.%d')
no_inputmsg = "{}".format(nowtime)
inputmsg = no_inputmsg
hasmsg = len(am) >= 2

if hasmsg:
    inputmsg = am[1]
else :
    result = input("\n\n =====> Write commit message. (If you don't have anything to right, Press <<Enter>>)\n >>>>>>>>>")
    if result != '':
        inputmsg = result    
    





gitcmd("git add --all")
gitcmd("git commit -am {}".format(inputmsg))
gitcmd("git push")
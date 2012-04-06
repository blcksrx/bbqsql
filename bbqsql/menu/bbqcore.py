#
# Centralized classes, work in progress
# 
import bbqsql

import re
import os

# used to grab the true path for current working directory
class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'

    def disable(self):
        self.PURPLE = ''
        self.CYAN = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''
        self.BOLD = ''
        self.UNDERL = ''
        self.backBlack = ''
        self.backRed = ''
        self.backGreen = ''
        self.backYellow = ''
        self.backBlue = ''
        self.backMagenta = ''
        self.backCyan = ''
        self.backWhite = ''
        self.DARKCYAN = ''


#
# Class for colors
#
def ExitBBQ(exitcode=0):
    print "\n"*100
    print "\n\n Goodbye " + bcolors.RED + os.getlogin() + bcolors.ENDC+",  and enjoy a hot plate of ribs on the house.\n"
    quit()

def show_graphics():
    print bcolors.YELLOW + r"""
    _______   _______    ______    ______    ______   __       
   |       \ |       \  /      \  /      \  /      \ |  \      
   | $$$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$      
   | $$__/ $$| $$__/ $$| $$  | $$| $$___\$$| $$  | $$| $$      
   | $$    $$| $$    $$| $$  | $$ \$$    \ | $$  | $$| $$      
   | $$$$$$$\| $$$$$$$\| $$ _| $$ _\$$$$$$\| $$ _| $$| $$      
   | $$__/ $$| $$__/ $$| $$/ \ $$|  \__| $$| $$/ \ $$| $$_____ 
   | $$    $$| $$    $$ \$$ $$ $$ \$$    $$ \$$ $$ $$| $$     \
    \$$$$$$$  \$$$$$$$   \$$$$$$\  \$$$$$$   \$$$$$$\ \$$$$$$$$
                     \$$$                \$$$                  """ + bcolors.ENDC



    return

def show_banner():
    print "\n"*100
    show_graphics()
    print bcolors.BLUE + """
    bbqsql injection toolkit ("""+bcolors.YELLOW+"""bbqsql"""+bcolors.BLUE+""")         
    Lead Development: """ + bcolors.RED+"""Ben Toews"""+bcolors.BLUE+"""("""+bcolors.YELLOW+"""mastahyeti"""+bcolors.BLUE+""")         
    Development: """ + bcolors.RED+"""Scott Behrens"""+bcolors.BLUE+"""("""+bcolors.YELLOW+"""arbit"""+bcolors.BLUE+""")         
    Menu modified from code for Social Engineering Toolkit (SET) by: """ + bcolors.RED+""" David Kennedy """+bcolors.BLUE+"""("""+bcolors.YELLOW+"""ReL1K"""+bcolors.BLUE+""")    
    SET is located at: """ + bcolors.RED+""" http://www.secmaniac.com"""+bcolors.BLUE+"""("""+bcolors.YELLOW+"""SET"""+bcolors.BLUE+""")    
    Version: """+bcolors.RED+"""%s""" % (bbqsql.__version__) +bcolors.BLUE+"""               
    
  """ + bcolors.GREEN+"""  Welcome to bbqsql. 
    a tasty resturant for all of your injection fun..
    """
    print  bcolors.ENDC + '\n'

def setprompt(category=None, text=None):
    '''helper function for creating prompt text'''
    #base of prompt
    prompt =  bcolors.UNDERL + bcolors.DARKCYAN + "bbqsql"
    #if they provide a category
    if category:
            prompt += ":"+category
    prompt += ">"
    #if they provide aditional text
    if text:
        prompt += " "+ text + ":"
    prompt += bcolors.ENDC + " "
    return prompt


class CreateMenu:
    def __init__(self, text, menu):
        self.text = text
        self.menu = menu

        print text
        #print "\nType 'help' for information on this module\n"

        for i, option in enumerate(menu):

            menunum = i + 1

            # Check to see if this line has the 'return to main menu' code
            match = re.search("0D", option)

            # If it's not the return to menu line:
            if not match:
                if menunum < 10:
                    print('   %s) %s' % (menunum,option))
                else:
                    print('  %s) %s' % (menunum,option))
            else:
                print '\n  99) Return to Main Menu\n'
        return

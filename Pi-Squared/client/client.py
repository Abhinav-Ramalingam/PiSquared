#! /usr/bin/env python3

from configparser import ConfigParser
import os

config = "./config/user.conf"
parser = ConfigParser()

######################################################################
############################# configs ################################
######################################################################

def readConfigs():
    if os.path.isfile(config):
        parser.read(config)
        username = parser['general']['username']
        chat = parser['general']['chat']
        return username, chat
    return "",""


def saveConfigs(username, chat):
    clear()
    parser['general'] = {'username': username, 'chat':chat}
    with open(config, 'w') as configfile:
        parser.write(configfile)

    print("config saved!\n")

def showConfig(username, chat):
    clear()
    if username == "":
        print("username not set!")
    else:
        print("username: {}".format(username))
    if chat == "":
        print("chat not set!")
    else:
        print("chat: {}".format(chat))
    print()


######################################################################
############################## chats #################################
######################################################################

def setUsername():
    username = input("Enter your username: ")
    clear()
    return username


def setChatroom():
    chatname = input("Enter chatname: ")
    clear()
    return chatname


def enterChat():
    clear()
    print("not implemented\n")


######################################################################
############################### menu #################################
######################################################################

def menu():
    print("1 - show configuration")
    print("2 - change username")
    print("3 - change chat name")
    print("4 - enter chat")
    print("5 - save configurations")
    print("0 - exit")


def askMenu():
    menu()
    return int(input("What do you want to do? "))

def getValidInput():
    firstValid = False
    option = 0
    while not firstValid:
        try:
            option = askMenu()
            firstValid = True
        except ValueError:
            clear()
            print("Invalid input! Please enter an integer.\n")
            
    return option

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


######################################################################
############################### main #################################
######################################################################

def main():
    username = ""
    chat = ""
    username, chat = readConfigs()
    option = getValidInput()

    while True:
        if option == 1:
            showConfig(username, chat)
        if option == 2:
           username = setUsername()
        elif option == 3:
            chat = setChatroom()
        elif option == 4:
            enterChat()
        elif option == 5:
            saveConfigs(username, chat)
        elif option == 0:
            clear()
            print("Bye!\n")
            break
 
        option = getValidInput()
        


if __name__ == "__main__":
    main()




#Developers: Sharkov K(65%)
#            Ermolenko V. - 45%
import os



language = input('Change language: en, ru').lower()
if language == 'en':
    import locen as loc
elif language == 'ru':
    import locru as loc






# the checking command block
def acceptCommand():
    try:
        com = int(input())
    except ValueError:
        acceptCommand()
    if com > 7 or com < 1:
        return acceptCommand()
    else:
        return com


# counts the size of all files in the directory and subdirectories
sz = 0
def countBytes(path):
    pass

# moves a user to a parent directory
def moveUp():
    try:
        os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    except:
        acceptCommand()


# counts all the files in the directory and subdirectories
def countFiles(path):
    pass


# gives the user a list of subdirectories and after the user has chosen one - moves him to it
def moveDown():
    print('\n' + loc.movedown)
    drlst = []
    for n in range(len(os.listdir(os.getcwd()))):
        if os.path.isdir(os.getcwd() + '/' + os.listdir(os.getcwd())[n]):
            drlst.append(str(os.listdir(os.getcwd())[n]))
    for i in range(len(drlst)):
        print(str(i + 1) + '. ' + drlst[i])

    togo = input()
    os.chdir(os.getcwd() + '/' + drlst[int(togo) - 1])


findtarget = 0


# gives the list of paths to the files with the searched word in their names
def search(target, workdirect):
    try:
        global findtarget
        a = []
        b = []
        b = os.listdir(workdirect)
        for name in b:
            a.append(name.lower())
        for i in range(len(a)):
            if target in a[i]:
                print(os.path.join(workdirect, a[i]))
                findtarget += 1
            newworkdirect = os.path.join(workdirect, a[i])
            search(target, newworkdirect)

    except:
        pass


# looks for the file with the given name
def findFiles():
    direct = int(input(loc.direct))
    target = input(loc.target)
    if direct == 1:
        workdir = os.getcwd()
    else:
        workdir = input(loc.workdir)
    search(target, workdir)
    if findtarget == 0:
        print(loc.notarget, target)


# the command choosing block
def runCommand(command):
    if command == 1:
        print(os.listdir(os.getcwd()))
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown()
    elif command == 4:
        countFiles(path)
    elif command == 5:
        countBytes(path)
    elif command == 6:
        findFiles()
    elif command == 7:
        print(loc.quit)


def main():
    while True:
        print()
        print(os.getcwd())
        print(loc.MENU)
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            break


main()

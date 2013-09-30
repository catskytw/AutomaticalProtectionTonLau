def eatChiken():
    if exists("1379822749169.png"):
        click("1379822761583.png")
        wait("1379822780659.png", 3)
        click("1379822780659.png")
        wait(1)

def protection():
    if exists("1379784828302.png", 3):
        click("1379784828302.png")
        wait(2)
        # unlock Protect
        if exists("1379784985998.png"):
            wait(1)
        else:
            if exists("1379785496704.png"):
                click("1379785496704.png")
        wait(60)

def myWait(inputValue):
    a=0
    while a<inputValue:
        print(a)
        a = a+1
        wait(1)

def unlockProtection():
    if exists("1379865937421.png"):
        click("1379865950512.png")
        wait(3)
def loginGame():
    print("loginGame")
    #click("1379784587756.png")
    openApp("BlueStacks")
    wait(3)
    if exists("1379952280943.png"):
        click("1379952290815.png")
        wait("1379952311495.png", 180)
        click("1379952319422.png")
        wait(1)

def nextStep():
    print("nextStep")
    returnValue = True
    if exists("1379785615163.png"):
        click("1379785615163.png")
    elif exists("1379785915692.png"):
        click("1379785915692.png")
    elif exists("1379785955990.png"):
        click("1379785955990.png")
    elif exists("1379810380156.png"):
        click("1379810380156.png")
    elif exists("1379784900486.png"):
        click("1379784900486.png")
    elif exists("1379960592944.png"):
        click("1379960611444.png")
    else:
        returnValue = False
    wait(1)
    return returnValue
    
def enterMenu():
    print("enterMenu")
    if exists("1379783893694.png"):
        click("1379783893694.png")
        wait(1)
   
while True:
    loginGame()
    r = True
    while r:
        r=nextStep()
    enterMenu()
  # eatChiken()
    unlockProtection()
      
    protection()                  
 
#
#

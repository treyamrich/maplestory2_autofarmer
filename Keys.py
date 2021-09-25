import time
import C

#Wait Function is for the beginning of the program
def Wait(timeIn):
    time.sleep(timeIn)

def upLeft(timeIn):
    C.PressKey(0xC8)
    C.PressKey(0xCB)
    time.sleep(timeIn)
    C.ReleaseKey(0xC8)
    C.ReleaseKey(0xCB)
    time.sleep(0.1)

def upRight(timeIn):
    C.PressKey(0xC8)
    C.PressKey(0xCD)
    time.sleep(timeIn)
    C.ReleaseKey(0xC8)
    C.ReleaseKey(0xCD)
    time.sleep(0.1)

def downLeft(timeIn):
    C.PressKey(0xD0)
    C.PressKey(0xCB)
    time.sleep(timeIn)
    C.ReleaseKey(0xD0)
    C.ReleaseKey(0xCB)
    time.sleep(0.1)

def downRight(timeIn):
    C.PressKey(0xD0)
    C.PressKey(0xCD)
    time.sleep(timeIn)
    C.ReleaseKey(0xD0)
    C.ReleaseKey(0xCD)
    time.sleep(0.1)

def Up(timeIn):
    C.PressKey(0xC8)
    time.sleep(timeIn)
    C.ReleaseKey(0xC8)
    time.sleep(0.1)

def Down(timeIn):
    C.PressKey(0xD0)
    time.sleep(timeIn)
    C.ReleaseKey(0xD0)
    time.sleep(0.1)

def Right(timeIn):
    C.PressKey(0xCD)
    time.sleep(timeIn)
    C.ReleaseKey(0xCD)
    time.sleep(0.1)

def Left(timeIn):
    C.PressKey(0xCB)
    time.sleep(timeIn)
    C.ReleaseKey(0xCB)
    time.sleep(0.1)

def jumpUpRight(timeIn):
    C.PressKey(0x2E)#Key: c
    time.sleep(0.15)
    C.ReleaseKey(0x2E)
    time.sleep(0.1)
    C.PressKey(0xC8)#Up
    C.PressKey(0xCD)#Right
    time.sleep(timeIn)
    C.ReleaseKey(0xC8)
    C.ReleaseKey(0xCD)
    time.sleep(0.1)

def jumpUpLeft(timeIn):
    C.PressKey(0x2E)#Key: c
    time.sleep(0.15)
    C.ReleaseKey(0x2E)
    time.sleep(0.1)
    C.PressKey(0xC8)#Up
    C.PressKey(0xCB)#Left
    time.sleep(timeIn)
    C.ReleaseKey(0xC8)
    C.ReleaseKey(0xCB)
    time.sleep(0.1)

def jumpDownLeft(timeIn):
    C.PressKey(0x2E)#Key: c
    time.sleep(0.15)
    C.ReleaseKey(0x2E)
    time.sleep(0.1)
    C.PressKey(0xD0)#Down
    C.PressKey(0xCB)#Left
    time.sleep(timeIn)
    C.ReleaseKey(0xD0)
    C.ReleaseKey(0xCB)
    time.sleep(0.1)
    
def Spacebar(timeIn):
    C.PressKey(0x39)
    time.sleep(timeIn)
    C.ReleaseKey(0x39)
    time.sleep(3)

def Enter(timeIn):
    C.PressKey(0x1C)
    time.sleep(timeIn)
    C.ReleaseKey(0x1C)
    time.sleep(0.1)

def keyT(timeIn):
    C.PressKey(0x14)
    time.sleep(timeIn)
    C.ReleaseKey(0x14)
    time.sleep(0.1)
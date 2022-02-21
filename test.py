from caesar import *

en= open("encrypted-message.txt", "r").read()
p= open("pad.txt","r").read()
de= open("decrypted-message.txt","r").read()

#test the shiftletter function by shifter a character for n numbers
def test_shiftLetter():
    assert shiftLetter("a", 1 ) == "b"
    assert shiftLetter("H", 2) == "J"

#test the decipher function
def test_decipher():
    assert decipher(en,p) == de
    assert decipher("J", "H") == "C"
    assert decipher("y", "K") == "o"

#test the encipher function
def test_encipher():
    assert encipher(de,p) == en
    assert encipher("C", "H") == "J"
    assert encipher("o", "K") == "y"

#test the shiftMessage (a sentence) by shifting all of the charaters for n numbers
def test_shiftMessage():
    assert shiftMessage("BBBBB", 2) == "DDDDD"

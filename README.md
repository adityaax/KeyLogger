# SPYKI -

![Untitled design](https://github.com/adityaax/KeyLogger/assets/98630015/62e751c8-30ac-4166-be92-b183b354fda9)



# KeyLogger
:rocket: Keyloggers are a particularly insidious type of spyware that can record and steal consecutive keystrokes (and much more) that the user enters on a device. 

:artificial_satellite: The term keylogger, or "keystroke logger," is self-explanatory: Software that logs what you type on your keyboard.

# Disclaimer
:fire: This tool is only for educational purposes. Use it on your own risk.

:jack_o_lantern: Hacking is illegal.

# Prerequisite
:basketball: Python package `pynput` is required.

`pip install pynput`

:basketball: Create `log.txt` file in the same directory of `keyLogger.py` file.

# About the library
:flying_disc: `pynput`- This library allows you to control and monitor input devices.

:flying_disc: In this I have used `pynput.keyboard` subpackage(contains classes for controlling and monitoring the keyboard)

# smtplib module
:flying_disc: It is the module used to send mails.

# Working
1. Listen the pressed key
2. Add pressed key to the file
3. After every 10 keys pressed, send it to the researcher's email.

# NOTE
:radioactive: `sendLogs.py` file need to be configured before use. 

:radioactive: Create a seperate email id for this because it can comprise the security of the email id.

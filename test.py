# import the modules
import imaplib                             
import email
from email.header import decode_header
import webbrowser
import os
 
# establish connection with Gmail
server ="imap.gmail.com"                    
imap = imaplib.IMAP4_SSL(server)
 
# instantiate the username and the password
username ="b3gul4.infosec@gmail.com"
password ="begula@google2003"
 
# login into the gmail account
imap.login(username, password) 
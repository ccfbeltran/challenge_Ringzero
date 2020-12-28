import requests 
from requests import request



import re 
import hashlib
import sys 
import requests
import time 

#all constans used

USERNAME='username'
PASSWORD='password'


BEGINMESSAGE= '----- BEGIN MESSAGE -----<br />\r\n\t\t'
ENDMESSAGE= '<br />'
BEGGINMESSAGEFLAG='<div class="alert alert-info">'
ENDMESSAGEFLAG= '</div>'
url ="https://ringzer0ctf.com/login"
url2='https://ringzer0ctf.com/challenges/13'



#getting the current session
session = requests.session()
#getting the response of the get request
r= session.get(url)


#getting the scrf token
scrf_token= r.content.decode("utf-8").split("var _")[1][12:44]

# #filling the informations to do the post request       
login_data = {
'username': USERNAME,
'password': PASSWORD,
'csrf':scrf_token,
'check':"true"
}

# #making the post request  to be able to login    
r= session.post(url,data=login_data)


#acceding into the challenge by the link
r=session.get(url2)

#getting the message to hash (re.S is to mach the fin string with all the jump lines etc)
message_to_hash= re.findall('(?<='+BEGINMESSAGE+')(.*?)(?='+ENDMESSAGE+')',r.content.decode('utf-8'), flags=re.S)



#hashing the code 
message_hashed=hashlib.sha512(message_to_hash[0].encode('utf-8')).hexdigest()

#creating the link to return
url_response_to_send= url2+'/'+message_hashed

#getting the response  after sending the response
r3=session.get(url_response_to_send)


#getting the flag on the result
flag= re.findall('(?<='+BEGGINMESSAGEFLAG+')(.*?)(?='+ENDMESSAGEFLAG+')',r3.content.decode('utf-8'), flags=re.S)
flag=flag[0]
#printing the flag
print(flag)




  
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, wikipedia, csv, subprocess, smtplib, pafy, humanize, errno,shutil

host = 'https://wa.boteater.us/api'

togroup = '***************@g.us' #groupid
to = '**************@c.us' #chatid

headers = {
	  'apikey': 'API KEY SENDIRI',
    'userid': 'USER ID SENDIRI',
  	'username': 'USERNAME SENDIRI'
}

def getClient():
    url = host + '/client'
    a = requests.get(url, headers=headers)
    return a

def getQr():
    url = host + '/login'
    a = requests.get(url, headers=headers)
    return a.json()

def sendMessage(to, text):
    url = host + '/sendMessage'
    data = {
        'chat_id': to,
        'message': text
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def sendMention(to, text, userids=[]):
    url = host + '/sendMention'
    data = {
        'chat_id': to,
        'message': text,
        'user_ids': userids
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def sendMedia(to, path, caption=''):
    url = host + '/sendMedia'
    data = {
        'chat_id': to,
        'caption': caption
    }
    files ={'files': open(path,'rb')}
    req = requests.post(url, data=data, files=files, headers=headers)
    return req.json()

def setName(name):
    url = host + '/setMyName'
    data = {
        'name': name
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def setBio(bio):
    url = host + '/setMyStatus'
    data = {
        'status': bio
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getBio(chat_id):
    url = host + '/getBio'
    data = {
        'chat_id': chat_id
    }
    req = requests.get(url, data=data, headers=headers)
    return req.json()

def getContacts():
    url = host + '/getContacts'
    req = requests.get(url, headers=headers)
    return req.json()

def getMyContacts():
    url = host + '/getMyContacts'
    req = requests.get(url, headers=headers)
    return req.json()

def blockContact(user_id):
    url = host + '/blockContact'
    data = {
        'chat_id': user_id
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def unblockContact(user_id):
    url = host + '/unblockContact'
    data = {
        'chat_id': user_id
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getChats():
    url = host + '/getChats'
    req = requests.get(url, headers=headers)
    return req.json()

def getChat(to):
    url = host + '/getChatsinchat'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def sendSeen(to):
    url = host + '/sendSeen'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def sendReply(message_id, text):
    url = host + '/sendReply'
    data = {
        'message_id': message_id,
        'message': text
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def downloadObjMessage(message_id):
    url = host + '/messages/' + message_id + '/download'
    req = requests.get(url, headers=headers)
    return req.json()

def loadChat(to):
    url = host + '/chatLoadEarlier'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def loadAllChat(to):
    url = host + '/chatLoadAllEarlier'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def loadChatStatus(to):
    url = host + '/chatLoadStatus'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getBatteryLevel():
    url = host + '/getBatteryLevel'
    req = requests.get(url, headers=headers)
    return req.json()

def deleteChat(to):
    url = host + '/deleteChat'
    data = {
        'chat_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def unsendMessage(to, message_ids=[], _all=True):
    url = host + '/unsendMessage'
    data = {
        'chat_id': to,
        'message_ids': message_ids,
        'all': _all
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getGroupParticipantsIds(to):
    url = host + '/getGroupParticipantsIds'
    data = {
        'group_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def downloadFileWithURL(url, filename):
    files = open(filename, 'wb')
    resp  = requests.get(url, stream=True)
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, files)
    return filename

def sendMediaWithURL(to, url, filename, caption=''):
    path = downloadFileWithURL(url, filename)
    r = sendMedia(to, path, caption)
    os.remove(path)
    return r

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def getGroupParticipants(to):
    url = host + '/getGroupParticipants'
    data = {
        'group_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getGroupAdminsIds(to):
    url = host + '/getGroupAdminIds'
    data = {
        'group_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def getGroupAdmins(to):
    url = host + '/getGroupAdmins'
    data = {
        'group_id': to
    }
    req = requests.post(url, data=data, headers=headers)
    return req.json()

def mentionAll(message):
    to = message['chatId']
    if message['chat']['isGroup']:
        result = '╭───「 Mention Members 」\n'
        no = 0
        members = getGroupParticipantsIds(message['chatId'])['result']
        for member in members:
            no += 1
            result += '│ %i. @%s\n' % (no, member.replace('@c.us',''))
        result += '╰───「 Hello World 」\n'
        sendMention(to, result, members)
    else:
        sendMessage(to, 'Group only!')
                
def helpmessage():
    helpMessage ="╭─「Help Message」─" + "\n" + \
                    "│ Joox 「Search」" + "\n" + \
                    "│ Cektogel「Kode negara ALPHA2」" + "\n" + \
                    "│ Tagall" + "\n" + \
                    "╰────────────"
    return helpMessage
    
def check_m():
    print(getClient().text)
    qr = getQr()
    if 'LoggedIn' in str(qr):
        while True:
            req = requests.post(host + '/unread', headers=headers)
            if req.json()['result'] == []:
                pass
            else:
                try:
                    print(req.json()['error'])
                except:
                    pass
                for contact in req.json()['result']:
                    for message in contact['messages']:
                        
                        try:
                            cont = str(message['content'][0:25])
                        except:
                            cont = 'None'

                        print('new message - {} from {} message {}...'.format(str(message['type']), str(message['sender']['formattedName']), cont))
                        try:
                            sender_id = message['sender']['id']
                        except:
                            sender_id = "None"
                        try:
                            chat_id = message['chat_id']
                        except:
                            chat_id = sender_id
                        if message['type'] == 'chat':
                            text = message['content']
                            txt  = text.lower()
                            cmd  = text.lower()
                            to   = chat_id
                            sender = sender_id
                            msg_id = message['id']
                            if txt == 'tagall':
                                mentionAll(message)
                            elif txt == 'status':
                                sendReply(msg_id, 'Alive Gan')
                            elif txt == 'restart':
                                restartBot()
                            elif txt == 'help':
                                helpMessage = helpmessage()
                                sendReply(msg_id, str(helpMessage))
                            elif txt.startswith("cektogel"):
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("https://mnazria.herokuapp.com/api/togel?server={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                sendReply(msg_id, "{}".format(str(data["hasil"])))
                            elif txt.startswith("joox"):
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://mnazria.herokuapp.com/api/joox?search={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                babi = ""
                                if data["picture"] == babi:
                                    sendReply(msg_id,"Data Gambar Kosong")
                                else:
                                    sendMediaWithURL(togroup,data["picture"],"tai.jpg","Picture")
                                if data["lirik"] == babi:
                                    sendReply(msg_id,"Data Lirik Kosong")
                                else:
                                    sendReply(msg_id,data["lirik"])
                                if data["mp3"] == babi:
                                    sendReply(msg_id,"Data Lagu Kosong")
                                else:
                                    sendMediaWithURL(togroup,data["mp3"],"anj.mp3","Song")
                            elif txt.startswith('exec\n'):
                                sep = text.split("\n")
                                nazri = text.replace(sep[0] + "\n","")
                                try:
                                    exec(nazri)
                                except Exception as error:
                                    sendReply(msg_id, "error\n" + str(error))
    else:print(qr)
check_m()

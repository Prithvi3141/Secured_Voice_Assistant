import paho.mqtt.client as mqtt
import ssl
from time import sleep
import datetime
import requests
import sys
from control_lib import *
from word2number import w2n
import selenium.webdriver as webdriver
import json
import pymysql
import thread

state = None

print sys.path

url_base = 'http://ec2-184-72-98-174.compute-1.amazonaws.com/'

request_parameters = {
	's':'1',
}

rootca = r'/home/pi/Desktop/project/control-pi/certificates/root-CA.crt'
certificate = r'/home/pi/Desktop/project/control-pi/certificates/7812df2ed4-certificate.pem.crt'
key = r'/home/pi/Desktop/project/control-pi/certificates/7812df2ed4-private.pem.key'

while_variable = 1

sns_lambda_subscription_topic = 'projectPolicy'


def on_connect_mqtt(c, userdata, flags, rc):
    print("Successfully connected to AWS with RC", rc)
    c.subscribe("accessTopic")


def on_message_mqtt(c, userdata, msg):
    m = msg.payload.decode()
    print(m)
    parsed_m = json.loads(m)
    print(parsed_m['type'])
    if parsed_m['type'] == 'login':
        connection = pymysql.connect(host='ec2-184-72-98-174.compute-1.amazonaws.com', user='ralphie', password='buffalo', db='Book_A_MovieShow')
        cursor = connection.cursor()
        query = ''
        sql=("select password from User where username='%s'"%(parsed_m['name']))
        cursor.execute(sql)
        data=cursor.fetchall()
        data_list=list(sum(data,()))
        print(data_list)
        print(data_list[0])
        login = {
            'postUser':None,
            'postPass':None,
        }
    
        login['postUser']=parsed_m['name'],
        login['postPass']=data_list[0],
    
        print(login)

        thread.start_new_thread( begin, (c, login, ) )

    elif parsed_m['type'] == 'logout':
        global while_variable
        while_variable = 0
        

def publish_message_mqtt( message, log_type, c):
    message = {
        'Time': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
        'message': message,
        'log_type': log_type
    }
    msg = json.dumps(message)
    c.publish('projectTopic', msg, qos = 1)
    sleep(5)

def begin(c, login):
    print('Sapwn new thread')
    default_browser = webbrowser.get()
    state = 1
    request_parameters = {
	's':'1',
    }
    publish_message_mqtt( "Logged in Successfully", "login", c)

    session = requests.session()
    r = session.request('POST', url_base + 'index.php', json=None, data=login, headers=None, params=request_parameters)

    with open("results.html", "w") as f:
        f.write(r.content)
    default_browser.open("results.html", new=0)
    notification_message = '%s has just logged in '%login['postUser']
    #publish_message_mqtt(sns_lambda_subscription_topic, 'Successful login', 'login', c)


    while while_variable:
        data = recordAudio()
        lower_data = data.lower()
        if lower_data.startswith('google'):
            command = lower_data.split(' ', 1)
            if len(command) == 1:
                continue
            if state == 1:
                if command[1].startswith('movies in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName) == 2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            print "India"
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 2
                            print "India"
                    
            elif state == 2:
                if command[1].startswith('go to'):
                    theatreName = command[1].split('to ', 1)
                    if len(theatreName) == 2:                    
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 3
                elif command[1].startswith('add to'):
                    words = command[1].split(' ')
                    length = len(words)
                    if words[length-1] == 'favorites':
                        stringName = 'add to favorites'
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)

                elif command[1].startswith('remove from'):
                    words = command[1].split(' ')
                    length = len(words)
                    if words[length-1] == 'favorites':
                        stringName = 'remove from favorites'
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
            elif state == 3:
                if command[1].startswith('book tickets'):
                    speak('Which Show')
                    while 1:
                        data = recordAudio()
                        lower_data = data.lower()
                        words = lower_data.split(' ')
                        if len(words)==2:
                            if words[0] == 'show':
                                if words[1].isdigit():
                                    #number = int(words[1])
                                    className = 'show'+str(words[1])
                                    print className
                                    url = fetchPostLinkFromClassName(r.content, className)
                                    if url == 'Link Not Found':
                                        speak('There is no such show')
                                        continue
                                    print 'India'
                                    print url
                                    
                                    while 1:
                                        speak('How many tickets')
                                        data = recordAudio()
                                        lower_data = data.lower()
                                        words = lower_data.split(' ')
                                        if len(words)==2:
                                            if words[1] == 'tickets' or words[1] == 'ticket':
                                                if words[0].isdigit():
                                                    numberOfTickets = int(words[0])
                                                    print numberOfTickets
                                                    body = {
                                                        'numberofseats':numberOfTickets,
                                                    }
                                                    r = session.request('POST', url_base + url, json=None, data=None, headers=None, params=None)
                                                    url = fetchPostLinkFromClassName(r.content, 'Show')
                                                    r = session.request('POST', url_base + url, json=None, data=body, headers=None, params=None)
                                                    print r.content
                                                    with open("results.html", "w") as f:
                                                        f.write(r.content)
                                                    default_browser.open("results.html", new=0)
                                                    
                                                    
                                                    
                                                    break
                                                else:
                                                    continue
                                        else:
                                            continue
                                else:
                                    continue
                            else:
                                continue
                        elif len(words)==1:
                            if words[0].isdigit():
                                
                                className = 'show'+str(words[0])
                                print className
                                url = fetchPostLinkFromClassName(r.content, className)
                                if url == 'Link Not Found':
                                    speak('There is no such show')
                                    continue
                                print 'India'
                                print url
                                while 1:
                                    speak('How many tickets')
                                    data = recordAudio()
                                    lower_data = data.lower()
                                    words = lower_data.split(' ')
                                    print words[1]
                                    if len(words)==2:
                                        if words[1] == 'tickets' or words[1] == 'ticket':
                                            if words[0].isdigit():
                                                numberOfTickets = int(words[0])
                                                print numberOfTickets
                                                body = {
                                                    'numberofseats':numberOfTickets,
                                                }
                                                r = session.request('POST', url_base + url, json=None, data=None, headers=None, params=None)
                                                url = fetchPostLinkFromClassName(r.content, 'Show')
                                                r = session.request('POST', url_base + url, json=None, data=body, headers=None, params=None)
                                                print r.content
                                                with open("results.html", "w") as f:
                                                    f.write(r.content)
                                                default_browser.open("results.html", new=0)

                                                break
                            else:
                                continue
                        else:
                            continue
                        break

            elif state == 4:
                if command[1].startswith('theaters in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 1



            elif state == 5:
                if command[1].startswith('movies in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1]
                        print stringName
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 2

                elif command[1].startswith('go to'):
                    theatreName = command[1].split('to ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 3

                    
            if command[1] == 'go home':
                    theatreName = command[1].split(' ')
                    stringName = theatreName[1] 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 1
            elif command[1] == 'show me cities':
                    stringName = 'view theaters by location' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 4
            elif command[1] == 'show me favorite theaters':
                    stringName = 'favorite theatres' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 1
            elif command[1] == 'show me booked movie shows' or command[1] == 'show me book movie shows':
                    stringName = 'booked movie shows' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 5
            elif command[1].startswith('locate'):
                theatreName = command[1].split('locate ', 1)
                if len(theatreName) == 2:
                    stringName = theatreName[1]
                    stringName.replace(' ', '+')
                    print(stringName)
                    
                    os.system("chromium-browser https://www.google.com/maps/place/" + stringName + "/&amp;")

                    print "India"

            elif command[1].startswith('review of'):
                movieName = command[1].split('review of ', 1)
                if len(movieName) == 2:
                    stringName = movieName[1]
                    stringName.replace(' ', '+')
                    print(stringName)
                    
                    os.system("chromium-browser https://www.rottentomatoes.com/m/" + stringName)
                    print "India"

            elif command[1] == 'logout':
                    stringName = command[1] 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        exit;
    print('Logged out successfully')

if __name__ == "__main__":
    c =mqtt.Client()
    c.tls_set(rootca, certfile=certificate, keyfile = key, cert_reqs = ssl.CERT_REQUIRED,
          tls_version = ssl.PROTOCOL_TLSv1_2, ciphers = None)
    c.connect('aa1kkd852hct2.iot.us-west-2.amazonaws.com', 8883)
    c.on_connect = on_connect_mqtt
    c.on_message = on_message_mqtt
    print('India')
    c.loop_forever()


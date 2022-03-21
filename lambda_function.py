import json
import requests

def weather_info(ciudad):
    try:
        URL = 'http://api.weatherstack.com/current?access_key=5b1f5459e72ca57a1c51bc8820e5c880&query=' + ciudad
        r = requests.get(url = URL)
        data = r.json()
        print(data)
        response = 'Temperatura: ' + str(data['current']['temperature']) + " °C. Humedad: " + str(data['current']['humidity']) +"%"
        return response
    except:
        return "Weather system down"

def lambda_handler(event, context):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "PlainText"
            }
        }
    }
    print(event)
    if event["currentIntent"]["name"] == "WeatherIntent":
        response["dialogAction"]["message"]["content"] = weather_info(event["currentIntent"]["slots"]["ciudad"])
    else:
        response["dialogAction"]["message"]["content"] = "Unrecognized intent"
    return response

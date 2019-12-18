from flask import Flask, render_template
import requests

APP = Flask(__name__)
FLASK_ENV='development'

@APP.route('/')
def home():
    return render_template('home.html', title='Dog Picture', picture=randomImage())

def randomImage(number=1):
    if number == 1:
        r = requests.get('https://dog.ceo/api/breeds/image/random/')
    elif number <= 50:
        r = requests.get('https://dog.ceo/api/breeds/image/random/'+ str(number))
    else:
        raise ValueError('Max Number of Dogs Returned is 50')
    pics = r.json()['message']
    return pics

@APP.route('/breeds')
def breeds():
    return render_template('breeds.html', all_breeds=listbreeds())

def listbreeds():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    b = r.json()
    breeds = []
    for key, value in b['message'].items():
        if len(value) == 0:
            breeds.append(key)
        else:
            for breed in value:
                full = breed + " " + key
                breeds.append(full)
    return breeds

if __name__ == '__main__':
    APP.run()

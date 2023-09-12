# flask imports
from flask import Flask, request, jsonify, make_response, send_from_directory
import json

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

@app.route('/contacts', methods =['POST'])
def save():
    data = request.get_json()
    name, phone = data.get('name'), data.get('phone')

    agenda = None
    with open('agenda.json', 'r') as openfile:
        agenda = json.load(openfile)
    
    dictionary = {
        "name": name,
        "phone": phone
    }
    
    agenda.append(dictionary)
    json_agenda = json.dumps(agenda)

    with open("agenda.json", "w") as outfile:
        outfile.write(json_agenda)
  
    return make_response('Successfully registered.', 201)

@app.route('/contacts', methods =['GET'])
def get_all_contacts():
    agenda = None
    with open('agenda.json', 'r') as openfile:
        agenda = json.load(openfile)
  
    return jsonify({'contacts': agenda})

# curl -d '{"name": "xxxx", "phone", "+323 2323 434"}' -H "Content-Type: application/json" localhost:5000/contacts
# curl localhost:5000/contacts
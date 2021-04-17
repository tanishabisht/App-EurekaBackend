from flask import Flask
from flask import request
from flask import jsonify,make_response
import json
import os
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    
    return jsonify({
        'documentationUrl' : 'https://documenter.getpostman.com/view/13305175/TzJphzAS'
    })

jsonFile = open('../Clustered_Data/final_data.json',)
data = json.load(jsonFile)

@app.route('/fetchAll')
def fetchAll():
    return jsonify(data)

@app.route('/fetchbyName/<string:name>')
def fetchByName(name):
    for x in data:
        if(x['name'] == name):
            namedObject = x
            break
    
    return jsonify(namedObject)

@app.route('/fetchLabels')
def fetchlabels():
    labelList = []
    for x in data:
        labelList.append(x['label'])
    label_list = set(labelList)
    list_label = list(label_list)
    return jsonify(list_label)

@app.route('/fetchEducation')
def fetchEducation():
    educationList = []
    for x in data:
        if(x['label'] == 'education'):
            educationList.append(x)
    
    return jsonify(educationList)

@app.route('/fetchMentalHealth')
def fetchMental():
    mentalhealthList = []
    for x in data:
        if(x['label'] == 'mental health'):
            mentalhealthList.append(x)
    
    return jsonify(mentalhealthList)

@app.route('/fetchHealth')
def fetchHealth():
    healthList = []
    for x in data:
        if(x['label'] == 'health and wellness'):
            healthList.append(x)
    
    return jsonify(healthList)

@app.route('/fetchMisc')
def fetchMisc():
    miscList = []
    for x in data:
        if(x['label'] == 'miscellaneous'):
            miscList.append(x)
    
    return jsonify(miscList)

@app.route('/fetchTech')
def fetchTech():
    techList = []
    for x in data:
        if(x['label'] == 'technology'):
            techList.append(x)
    
    return jsonify(techList)

@app.route('/fetchGeneral')
def fetchGeneral():
    generalList = []
    for x in data:
        if(x['label'] == 'general wellfare'):
            generalList.append(x)
    
    return jsonify(generalList)

@app.route('/fetchScience')
def fetchScience():
    scienceList = []
    for x in data:
        if(x['label'] == 'technology'):
            scienceList.append(x)
    
    return jsonify(scienceList)

@app.route('/fetchSafety')
def fetchSafety():
    safetyList = []
    for x in data:
        if(x['label'] == 'safety and wellbeing'):
            safetyList.append(x)
    
    return jsonify(safetyList)

@app.route('/fetchSpecialMention')
def specialMention():
    specialList = []
    for x in data:
        if(len(x['special_mention'])>1):
            specialList.append(x)

    return jsonify(specialList)

@app.route('/fetchAllLabels')
def fetchAllLabels():
    array = [
        {'label' : 'safety and wellbeing','fetchUrl':'fetchSafety'},
        {'label' : 'science and research','fetchUrl':'fetchScience'},
        {'label' : 'general welfare','fetchUrl':'fetchGeneral'},
        {'label' : 'miscellaneous','fetchUrl':'fetchMisc'},    
        {'label' : 'technology','fetchUrl':'fetchTech'},
        {'label' : 'mental health','fetchUrl':'fetchMental'},
        {'label' : 'health and wellness','fetchUrl':'fetchHealth'},
        {'label' : 'education','fetchUrl':'fetchEducation'}
    ]
    return jsonify(array)
@app.route('/fetchAllNames')
def fetchAllNames():
    nameArray = []
    for x in data:
        nameArray.append(x["name"])
    return jsonify(nameArray)

if __name__ == '__main__':
    app.run(debug=True,port = int(os.environ.get('PORT',3000)))
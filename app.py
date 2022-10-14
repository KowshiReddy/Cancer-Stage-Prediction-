import flask
import pandas as pd
import prediction as m





app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        #Age=flask.request.form['Age']
        hairfall = flask.request.form['hairfall']
        fatigue = flask.request.form['fatigue']
        lump = flask.request.form['lump']
        weightloss = flask.request.form['weightloss']
        fever = flask.request.form['fever']
        skinchanges = flask.request.form['skinchanges']
        pains = flask.request.form['pains']
        bleeding = flask.request.form['bleeding']
        smoking = flask.request.form['smoking']
        alcoholuse = flask.request.form['alcoholuse']
        indigestion= flask.request.form['indigestion']

        input_variables = pd.DataFrame([[hairfall, fatigue, lump, weightloss, fever, skinchanges, pains, bleeding, smoking, alcoholuse,indigestion ]],
                                       columns=['hairfall', 'fatigue', 'lump', 'weightloss', 'fever', 'skinchanges', 'pains', 'bleeding', 'smoking',
                                        'alcoholuse','indigestion'],
                                       dtype='float',
                                       index=['input'])
        
        predictions =m.prediction(input_variables)[0]
        print('CANCER LEVEL IS:' ,predictions)

        return flask.render_template('index.html', original_input={'hairfall': hairfall, 'fatigue': fatigue, 'lump': lump, 'weightloss': weightloss, 'fever':fever, 'skinchanges': skinchanges, 'pains': pains, 'bleeding': bleeding, 'smoking': smoking, 'alcoholuse': alcoholuse,'indigestion':indigestion},
                                     level=predictions)


if __name__ == '__main__':
    
    app.run(debug=True)

    
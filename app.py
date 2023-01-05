import os

from flask import Flask, render_template, request, flash

from main import getPrediction

app = Flask(__name__)
app.secret_key = '8662747133'

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    imagefile.save(os.path.join('./static/uploads', imagefile.filename))
    getPrediction(imagefile.filename)
    answer, probability_results, filename = getPrediction(imagefile.filename)
    flash(answer)
    return render_template('index.html', answer=answer, probability_results=probability_results, filename=filename)


if __name__ == '__main__':
    app.run(debug=True)

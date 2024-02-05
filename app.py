import os

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename

from utils import file_preprocessing, llm_pipeline

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('content')
    summarization = llm_pipeline(text)
    return render_template("index.html", summary=summarization)


@app.route('/upload', methods=['POST'])
# write a function that uploads the file to a folder
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:

            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename

        if file.filename == '':

            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            summarization = llm_pipeline(os.path.join('uploads', filename))
            return jsonify({'summary': summarization})


# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    # Get data posted as a json
    file = upload_file()
    summarization = llm_pipeline(file)
    return jsonify({'summary': summarization})  # Return prediction


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

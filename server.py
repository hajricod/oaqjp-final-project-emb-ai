from flask import Flask, render_template, request, json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] != None:
        return response
    else:
        return " Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
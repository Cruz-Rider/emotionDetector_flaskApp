''' This Module detects the emotion
    in the text provided to the function
    emotion_detector(). It gives output as
    dictionary of all emotion scores and the
    dominant of all. '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index():
    ''' This function renders the Index Page. '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    ''' This function takes text from user as an argument
        and tells the emotions involved in that text. '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    response_sentence = "For the given statement, the system response is: "

    for key, value in response.items():
        if key == "dominant_emotion":
            response_sentence += f"The dominant emotion is {value}."
        else:
            response_sentence += f"'{key}': {value}, "
    return response_sentence

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

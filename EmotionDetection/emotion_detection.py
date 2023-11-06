''' This is a module to detect emotions from the
    given text and give output whenever the function
    inside this module is being called '''

import requests
import json
def emotion_detector(text_to_analyse):
    ''' In this function the text is passed
        as an argument and given as an json
        object to the Watson Library.This
        function returns the output of the 
        analyzed text as a string '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    emotions = {}

    if response.status_code == 200:
        for prediction in formatted_response['emotionPredictions']:
            anger_score = float(prediction['emotion']['anger'])
            disgust_score = float(prediction['emotion']['disgust'])
            fear_score = float(prediction['emotion']['fear'])
            joy_score = float(prediction['emotion']['joy'])
            sadness_score = float(prediction['emotion']['sadness'])    

        emotions = {"anger":anger_score, "disgust":disgust_score, "fear":fear_score, "joy":joy_score, 
                    "sadness":sadness_score}
        dominant_emotion = max(emotions, key=lambda x: emotions[x])
        emotions["dominant_emotion"] = dominant_emotion

    elif response.status_code == 400:
        emotions = {"anger":None, "disgust":None, "fear":None, "joy":None, 
                    "sadness":None}
        dominant_emotion = None
        emotions["dominant_emotion"] = dominant_emotion

    return emotions

import requests

def emotion_detector(text_to_analyze):
    # URL and headers for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON format
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Send a POST request to the Emotion Predict function
    response = requests.post(url, json=input_json, headers=headers)

    # Return the text attribute of the response object
    return response.text


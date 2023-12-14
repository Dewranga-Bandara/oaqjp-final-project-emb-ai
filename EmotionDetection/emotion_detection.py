import requests
import json

def emotion_detector(text_to_analyze):
    # URL and headers for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON format
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Send a POST request to the Emotion Predict function
    response = requests.post(url, json=input_json, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Convert response text to a dictionary
            response_dict = json.loads(response.text)

            # Extract emotions and their scores
            emotion_predictions = response_dict.get('emotionPredictions', [])

            if not emotion_predictions:
                raise ValueError("Emotion predictions not found in the response.")

            emotion_prediction = emotion_predictions[0]
            emotions = emotion_prediction.get('emotion', {})
            
            if not emotions:
                raise ValueError("Emotion not found in the response.")

            anger_score = emotions.get("anger", 0.0)
            disgust_score = emotions.get("disgust", 0.0)
            fear_score = emotions.get("fear", 0.0)
            joy_score = emotions.get("joy", 0.0)
            sadness_score = emotions.get("sadness", 0.0)

            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Return the formatted output
            output_dict = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

            return output_dict

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Error: {response.status_code}, {response.text}")


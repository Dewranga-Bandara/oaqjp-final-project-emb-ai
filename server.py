from flask import Flask, render_template, request, make_response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')

def emotion_detector_route():
    """
    Handles the emotionDetector route, processes the input, and returns the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response

@app.route("/")
def index():
    """
    Entry point for the index route.
    """
    return render_index_page()

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_entry():
    """
    Entry point for the emotionDetector route.
    """
    return emotion_detector_route()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

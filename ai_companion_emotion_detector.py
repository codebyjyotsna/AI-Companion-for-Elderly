import tensorflow as tf
import numpy as np
from microcontroller import Microphone, Speaker, WiFiModule

# Load your pre-trained TinyML model for emotion detection
model_path = "emotion_detection_model.tflite"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Initialize hardware
mic = Microphone()
speaker = Speaker()
wifi = WiFiModule()

def preprocess_audio(audio):
    """
    Preprocess the audio data for the TinyML model.
    """
    # Convert audio to spectrogram or mel-frequency cepstral coefficients (MFCC)
    # Placeholder for actual preprocessing
    return np.expand_dims(audio, axis=0)

def predict_emotion(audio_data):
    """
    Predict the emotion from audio data using the TinyML model.
    """
    processed_audio = preprocess_audio(audio_data)
    interpreter.set_tensor(input_details[0]['index'], processed_audio)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(predictions), predictions

def suggest_activity(emotion):
    """
    Suggest an activity based on the detected emotion.
    """
    activity_map = {
        0: "Play relaxing music",
        1: "Call a family member",
        2: "Suggest a short walk outside",
        3: "Tell a joke or story"
    }
    return activity_map.get(emotion, "Let's chat!")

def notify_family(emotion):
    """
    Notify family if a distress emotion is detected.
    """
    if emotion == 1:  # Example: Emotion 1 = Sadness
        wifi.send_notification("Detected sadness. Reaching out to family.")

# Main loop
while True:
    print("Listening for audio...")
    audio_data = mic.record_audio(duration=5)  # Record 5 seconds of audio
    emotion, confidence = predict_emotion(audio_data)
    print(f"Detected Emotion: {emotion}, Confidence: {confidence}")

    if confidence[emotion] > 0.8:  # Confidence threshold
        activity = suggest_activity(emotion)
        speaker.play_message(activity)
        
        if emotion == 1:  # Sadness or distress
            notify_family(emotion)

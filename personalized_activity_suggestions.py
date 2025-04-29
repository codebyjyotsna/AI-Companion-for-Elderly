class UserPreferences:
    def __init__(self):
        self.preferences = {
            "hobbies": ["listening to music", "gardening"],
            "preferred_music": ["classical", "jazz"],
            "activities": ["morning walk", "puzzle solving"],
        }

    def get_suggestion(self, emotion):
        """
        Suggest an activity based on user preferences and emotion.
        """
        if emotion == "happy":
            return f"How about enjoying your favorite hobby: {self.preferences['hobbies'][0]}?"
        elif emotion == "sad":
            return f"Would you like to listen to some {self.preferences['preferred_music'][0]} music?"
        else:
            return f"How about a {self.preferences['activities'][1]} to cheer up?"

# Example usage
user_prefs = UserPreferences()
detected_emotion = "sad"  # Replace with emotion detection output
print(user_prefs.get_suggestion(detected_emotion))

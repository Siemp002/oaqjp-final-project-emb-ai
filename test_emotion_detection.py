from EmotionDetection import emotion_detector


def test_emotion_detector(text, expected_emotion):
    response = emotion_detector(text)
    if response['dominant_emotion'] == expected_emotion:
        print("test passed!")
    else:
        print("test failed!")

test_emotion_detector("I am glad this happened", "joy")
test_emotion_detector("I am really mad about this", "anger")
test_emotion_detector("I feel disgusted just hearing about this", "disgust")
test_emotion_detector("I am so sad about this", "sadness")
test_emotion_detector("I am really afraid that this will happen", "fear")
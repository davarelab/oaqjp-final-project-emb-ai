import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotions(unittest.TestCase): 

    def test1(self): 
        text1 = 'I am glad this happened'
        text2 = 'I am really mad about this'
        text3 = 'I feel disgusted just hearing about this'
        text4 = 'I am so sad about this'
        text5 = 'I am really afraid that this will happen'

        self.assertEqual(emotion_detector(text1)['dominant_emotion'], 'joy')
        self.assertEqual(emotion_detector(text2)['dominant_emotion'], 'anger')
        self.assertEqual(emotion_detector(text3)['dominant_emotion'], 'disgust')
        self.assertEqual(emotion_detector(text4)['dominant_emotion'], 'sadness')
        self.assertEqual(emotion_detector(text5)['dominant_emotion'], 'fear')
        
        
unittest.main()

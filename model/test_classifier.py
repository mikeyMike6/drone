import unittest
import tensorflow as tf


class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.model_path = r'C:\python projects\unit_tests\classifier.tflite'
        self.num_threads = 1
        self.interpreter = tf.lite.Interpreter(model_path=self.model_path, num_threads=self.num_threads)
        pass


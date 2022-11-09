import mediapipe as mp
import tensorflow as tf
import numpy as np

def test_classifier_load():
    interpreter = tf.lite.Interpreter(model_path='model/classifier/classifier.tflite')
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()
    output_deta = interpreter.get_tensor(output_details[0]['index'])

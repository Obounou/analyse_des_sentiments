import unittest
from inference import predict

class TestInference(unittest.TestCase):
    def test_predict(self):
        pred = predict("I love this product!")
        self.assertIn(pred, [0, 1])
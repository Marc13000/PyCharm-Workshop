from unittest import TestCase

from Car import Car

class TestCar(TestCase):
    def setUp(self):
        self.car = Car()

    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_brake(self):
        self.fail()

import unittest

from Class_Task.TV1 import Tv


class TestFunction(unittest.TestCase):
    def test_tv_is_on(self):
        self.t1 = Tv()
        self.t1.turn_on()
        self.assertTrue(self.t1.isOn)

    def test_tv_is_off(self):
        self.t1 = Tv()
        self.t1.turn_off()
        self.assertFalse(self.t1.isOn)

    def test_set_channel(self):
        self.t1 = Tv()
        self.t1.turn_on()
        self.t1.set_channel(12)
        self.assertEqual(12, self.t1.get_channel())

    def test_channel_up(self):
        t1 = Tv()
        t1.turn_on()
        self.assertTrue(True)
        t1.set_channel(10)
        self.assertEqual(10, t1.get_channel())
        t1.channel_up()
        self.assertEqual(11, t1.get_channel())

    def test_channel_down(self):
        t1 = Tv()
        t1.turn_on()
        self.assertTrue(True)
        t1.set_channel(10)
        self.assertEqual(10, t1.get_channel())
        t1.channel_down()
        self.assertEqual(9, t1.get_channel())

    def test_set_volume(self):
        t1 = Tv()
        t1.turn_on()
        self.assertTrue(True)
        t1.set_volume(5)
        self.assertEqual(5, t1.get_volume())

    def test_volume_up(self):
        t1 = Tv()
        t1.turn_on()
        self.assertTrue(True)
        t1.set_volume(20)
        self.assertEqual(20, t1.get_volume())
        t1.volume_up()
        self.assertEqual(21, t1.get_volume())

    def test_volume_down(self):
        t1 = Tv()
        t1.turn_on()
        self.assertTrue(True)
        t1.set_volume(20)
        self.assertEqual(20, t1.get_volume())
        t1.volume_down()
        self.assertEqual(19, t1.get_volume())

import unittest
from datetime import datetime, timedelta

from Class_Task.MentrualCycleApplication.MenstrualCycle import MenstrualCycle


class TestMenstrualCycle(unittest.TestCase):
    def setUp(self):
        self.previous_end_date = datetime(2023, 1, 1)
        self.cycle_duration = 28
        self.period_duration = 5

    def test_period_start_date(self):
        next_period_start_date = MenstrualCycle.period_start_date(self.previous_end_date, self.cycle_duration)
        expected_date = self.previous_end_date + timedelta(days=self.cycle_duration)
        self.assertEqual(next_period_start_date, expected_date)

    def test_period_end_date(self):
        next_period_end_date = MenstrualCycle.period_end_date(self.previous_end_date, self.period_duration)
        expected_date = self.previous_end_date + timedelta(days=self.period_duration)
        self.assertEqual(next_period_end_date, expected_date)

    def test_ovulation_start_date(self):
        ovulation_start_date = MenstrualCycle.ovulation_start_date(self.previous_end_date, self.cycle_duration)
        expected_date = self.previous_end_date + timedelta(days=self.cycle_duration // 2)
        self.assertEqual(ovulation_start_date, expected_date)


if __name__ == '__main__':
    unittest.main()

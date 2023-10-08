from datetime import datetime


class MenstrualCycle:
    @staticmethod
    def period_start_date(previous_end_date, cycle_duration):
        return previous_end_date + datetime.timedelta(days=cycle_duration)

    @staticmethod
    def period_end_date(previous_end_date, period_duration):
        return previous_end_date + datetime.timedelta(days=period_duration)

    @staticmethod
    def ovulation_start_date(previous_end_date, cycle_duration):
        return previous_end_date + datetime.timedelta(days=cycle_duration // 2)

    @staticmethod
    def ovulation_end_date(previous_end_date, cycle_duration):
        return previous_end_date + datetime.timedelta(days=(cycle_duration // 2) + 1)

    @staticmethod
    def first_safe_period_start_date(previous_end_date, period_duration, cycle_duration):
        return previous_end_date + datetime.timedelta(days=period_duration + 1)

    @staticmethod
    def first_safe_period_end_date(previous_end_date, cycle_duration):
        return previous_end_date + datetime.timedelta(days=cycle_duration - 1)

    @staticmethod
    def unsafe_period_start_date(previous_end_date, period_duration, cycle_duration):
        return previous_end_date + datetime.timedelta(days=period_duration + 1)

    @staticmethod
    def unsafe_period_end_date(previous_end_date, cycle_duration):
        return previous_end_date + datetime.timedelta(days=cycle_duration - 1)

    @staticmethod
    def next_safe_period_start_date(previous_end_date, period_duration, cycle_duration):
        return previous_end_date + datetime.timedelta(days=cycle_duration)
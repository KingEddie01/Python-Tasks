import datetime

from Class_Task.MentrualCycleApplication.MenstrualCycle import MenstrualCycle

class MenstrualCheck:
    def __init__(self):
        self.cycle_duration = 0
        self.period_duration = 0
        self.previous_period_end_date = None

    def welcome_message(self):
        print(
            """
            CHEDDARS MENSTRUAL CALCULATOR 🌸!!!

            Your personalized menstrual companion!
            We're here to make your monthly journey easier, more predictable, and a little bit magical.
            Say goodbye to guessing and hello to precision.
            With Cheddars Menstrual App, you can effortlessly track your cycles, predict your next period.
            Stay ahead of your fertile days.
            We've got your back throughout your entire cycle.
            Are you Ready to take control of your body?
            Let's get started! 🌟 #PeriodPower"""
        )
        self.period_start_date()

    def period_start_date(self):
        print("GET PERIOD START DATE ")
        try:
            previous_period_end_date_str = input("Enter the date of your last period (yyyy-MM-dd): ")
            self.previous_period_end_date = datetime.datetime.strptime(previous_period_end_date_str, "%Y-%m-%d")
            self.cycle_duration = int(
                input("Enter the average duration of your menstrual cycle (in days): "))
            print(
                f"Your flow is presumed to Start on: {MenstrualCycle.period_start_date(self.previous_period_end_date, self.cycle_duration).date()}")
            print(
                """
                Menstruation begins with the shedding of the uterine lining (endometrium).
                Hormone levels, including estrogen and progesterone, are at their lowest.
                Bleeding typically lasts for 3 to 7 days.
                """
            )
            self.period_end_date()
        except ValueError:
            print("Invalid input. Please use the yyyy-MM-dd format.")
            self.period_start_date()

    def period_end_date(self):
        print(" GET PERIOD END DATE ")
        try:
            self.period_duration = int(input("Enter period Duration (in days): "))
            if self.period_duration <= 0:
                print("Invalid period Duration")
                self.period_end_date()
            else:
                print(
                    f"Your flow is presumed to end on: {MenstrualCycle.period_end_date(self.previous_period_end_date, self.period_duration).date()}")
                print(
                    """
                    The end of menstruation, often referred to as the "menstrual flow,"
                    marks the final phase of a woman's menstrual period.
                    This phase is characterized by the cessation of bleeding and other associated symptoms.
                    """
                )
                self.ovulation_start_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.period_end_date()

    def ovulation_start_date(self):
        print("GET OVULATION START DATE ")
        try:
            print(
                f"Your Ovulation is likely to start on: {MenstrualCycle.ovulation_start_date(self.previous_period_end_date, self.cycle_duration).date()}")
            print(
                """Around the middle of the cycle, a surge in Luteinizing hormone (LH) and a smaller surge in FSH 
                trigger ovulation. The mature follicle releases an egg into the fallopian tube. This is the most 
                fertile time, with the egg viable for about 12-24 hours.

                SIGNS OF OVULATION:
                Some women may experience physical and hormonal changes around the time of ovulation, including:

                * Increased cervical mucus: The mucus becomes thinner and more slippery to facilitate sperm movement.
                * A mild increase in basal body temperature: This can be tracked using a basal body temperature (BBT) chart.
                * Mittelschmerz: Some women may experience mild pelvic pain or twinges on one side of the lower abdomen.
                * Increased libido: Some women report heightened sexual desire during ovulation.
                """
            )
            self.ovulation_end_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.ovulation_start_date()

    def ovulation_end_date(self):
        print("GET OVULATION END DATE ")
        try:
            print(
                f"Your Ovulation is likely to stop on: {MenstrualCycle.ovulation_end_date(self.previous_period_end_date, self.cycle_duration).date()}")
            print(
                """Ovulation is a relatively short event in a woman's menstrual cycle, typically lasting around 12 to 
                24 hours. After ovulation, if the egg is not fertilized, the body transitions into the luteal phase 
                of the menstrual cycle. During this phase, the corpus luteum (a temporary endocrine structure formed 
                from the ovarian follicle that released the egg) produces progesterone. If pregnancy does not occur, 
                the corpus luteum eventually breaks down, and progesterone levels decline, leading to the shedding of 
                the uterine lining in menstruation. This marks the end of the menstrual cycle, and a new cycle begins.

                It's important to remember that individual variations in menstrual cycles are common, and not all 
                women have a regular {}-day cycle. If you are trying to conceive or have concerns about your 
                menstrual cycle, it's advisable to track your cycle, monitor ovulation signs, and consult a 
                healthcare provider or a fertility specialist for personalized guidance. """.format(self.cycle_duration)
            )
            self.first_safe_period_start_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.ovulation_end_date()

    def first_safe_period_start_date(self):
        print("GET FIRST SAFE WINDOW START DATE ")
        try:
            print(
                f"The first safe windows are: {MenstrualCycle.first_safe_period_start_date(self.previous_period_end_date, self.period_duration, self.cycle_duration).date()}")
            print(
                """The first safe period after menstruation, also known as the "post menstrual safe period,". It is a 
                time when a woman is less likely to conceive because it occurs shortly after her menstrual period has 
                ended. This period is generally considered one of the safer times to have unprotected intercourse if 
                a woman is using natural family planning methods for contraception. However, it's important to 
                understand that these methods are not foolproof, and there is still a risk of pregnancy."""
            )
            self.first_safe_period_end_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.first_safe_period_start_date()

    def first_safe_period_end_date(self):
        print("GET SAFE WINDOW END DATE ")
        try:
            print(
                f"The first safe window ends on: {MenstrualCycle.first_safe_period_end_date(self.previous_period_end_date, self.cycle_duration).date()}")
            print(
                """During the end of the safe period before ovulation, a woman is transitioning from the phase 
                immediately following her menstrual period to the fertile window, which is when she is most likely to 
                conceive if she has unprotected intercourse."""
            )
            self.unsafe_period_start_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.first_safe_period_end_date()

    def unsafe_period_start_date(self):
        print("GET UNSAFE WINDOW START DATE")
        try:
            print(
                f"Your unsafe window starts from: {MenstrualCycle.unsafe_period_start_date(self.previous_period_end_date, self.period_duration, self.cycle_duration).date()}")
            print(
                """"Unsafe periods" typically refer to the fertile window in a woman's menstrual cycle when she is at 
                a higher risk of becoming pregnant if she engages in unprotected sexual intercourse. During these 
                unsafe periods, ovulation has occurred or is about to occur, making it more likely for a sperm to 
                fertilize an egg."""
            )
            self.unsafe_period_end_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.unsafe_period_start_date()

    def unsafe_period_end_date(self):
        print("GET UNSAFE WINDOW END DATE ")
        try:
            print(
                f"Your unsafe window ends on: {MenstrualCycle.unsafe_period_end_date(self.previous_period_end_date, self.cycle_duration).date()}")
            print(
                """The "safe period" or "infertile period" after ovulation refers to the time during a woman's 
                menstrual cycle when the likelihood of conceiving a pregnancy is significantly reduced. This period 
                typically occurs after ovulation when the released egg is no longer viable, and the fertile window 
                has passed."""
            )
            self.next_safe_period_date()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.unsafe_period_end_date()

    def next_safe_period_date(self):
        print("GET NEXT SAFE WINDOW DATE ")
        try:
            print(
                f"Your next safe window starts from: {MenstrualCycle.next_safe_period_start_date(self.previous_period_end_date, self.cycle_duration, self.period_duration).date()}")
            print(
                """The "final safe period" before the next menstrual flow refers to the days following ovulation when 
                a woman is considered less likely to conceive before her next period begins. This phase is typically 
                seen as a lower-risk time for pregnancy because ovulation has already occurred, and the egg is no 
                longer available for fertilization. However, it's important to remember that individual variations 
                and cycle irregularities can affect the accuracy of this method."""
            )
            self.exit()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            self.next_safe_period_date()

    def exit(self):
        print("tHANKS FOR USING CHEDDAR MENSTRUAL CALCULATOR")
        option = input("""
        Select An Option
        1. Main Menu
        0. Exit
                 """)
        if option == 1:
            self.welcome_message()
        elif option == 0:
            print("GOODBYE")
        else:
            print("Invalid input")
            self.exit()


if __name__ == '__main__':
    main = MenstrualCheck()
    main.welcome_message()

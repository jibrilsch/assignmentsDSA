class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.day = day

        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7


        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


calculator = DateCalculator(2025, 4, 30)
day_of_week = calculator.calculate_day_of_week()
print(f"April 30, 2025 was a {day_of_week}.")
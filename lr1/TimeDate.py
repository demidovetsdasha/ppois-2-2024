class TimeDate:
    def __init__(self, time: str, date: str):
        self.hours, self.minutes = self.__is_valid_time(tuple(time.split(":")))
        self.day, self.month, self.year = self.__is_valid_date(tuple(date.split(".")))

    def __is_valid_time(self, time):
        hours, minutes = time
        hours, minutes = int(hours), int(minutes)

        if hours > 24 or hours < 0:
            raise ValueError("Wrong hour input")
        if minutes > 59 or minutes < 0:
            raise ValueError("Wrong minutes input")

        return hours, minutes

    def __is_valid_date(self, date):
        day, month, year = date
        day, month, year = int(day), int(month), int(year)
        if day > 31 or day < 0:
            raise ValueError("Wrong day input")
        if month > 12 or month < 1:
            raise ValueError("Wrong month output")
        if len(str(year)) != 4:
            raise ValueError("Wrong year!")
        return day, month, year
    
    def display_date(self):
        return f"{self.hours}:{self.minutes} {self.day}.{self.month}.{self.year}"

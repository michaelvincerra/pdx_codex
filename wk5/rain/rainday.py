class RainDay:
    def __init__(self, date:str, total:str, hours: list):
        self.date = date
        self.total = total
        self.hours = [int(h) for h in hours]

    def __repr__ (self):
        message = '{} Total: {}'.format(self.date, self.total)
        return message

    def max_hour(self):
        hour, value = max(enumerate(rain), key=lambda t: t[1])
        return hour





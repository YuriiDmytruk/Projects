class Library:
    def __init__(self, title=None, rent_price=None, start_rent_date=None, end_rent_date=None, user_name=None):
        self.title = title
        self.rent_price = rent_price
        self.start_rent_date = start_rent_date
        self.end_rent_date = end_rent_date
        self.user_name = user_name



class Date:
    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year
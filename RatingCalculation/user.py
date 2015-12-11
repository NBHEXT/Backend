__author__ = 'rubanenko'

class User:
    def __init__(self, rating, contestant_id, place):
        self.rating = 1500 if rating == "0" else int(rating)
        self.id     = str(contestant_id)
        self.place  = int(place)
        self.delta  = 0
        self.seed   = 0.0


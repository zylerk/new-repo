class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times= []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend ( a_times)

    def get_top3(self):
        return self[0:3]

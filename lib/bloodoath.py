from datetime import datetime


class BloodOath:
    all = []

    def __init__(self, initiation_date, follower, cult):
        if type(initiation_date) is str:
            self.initiation_date = datetime.strptime(initiation_date, '%Y-%m-%d').date().strftime('%Y-%m-%d')
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)
    
    @classmethod
    def first_oath(cls):
        first_oath = None
        earliest_date = datetime.now()
        for oath in cls.all:
            oath_date = datetime.strptime(oath.initiation_date, '%Y-%m-%d')
            if oath_date < earliest_date:
                earliest_date = oath_date
                first_oath = oath.follower
        return first_oath



# **`BloodOath`**

# DONE
# * `BloodOath.first_oath`
#   * returns the `Follower` instance for the follower that made the very first blood oath
# * `BloodOath#initiation_date`
#   * returns a `String` that is the initiation date of this blood oath in the format _YYYY-MM-DD_.
# * `BloodOath.all`
#   * returns an `List` of all the blood oaths
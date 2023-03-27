from .bloodoath import BloodOath

class Follower:
    all_followers = []
    def __init__(self, name, age, life_motto):
        if type(name) is str:
            self.name = name
        if type(age) is int:
            self.age = age
        if type(life_motto) is str:
            self.life_motto = life_motto
        Follower.all_followers.append(self)
        
    def of_a_certain_age(age):
        followers_of_a_certain_age = []
        for follower in Follower.all_followers:
            if follower.age == age:
                followers_of_a_certain_age.append(follower)
        return followers_of_a_certain_age
    
    def cult_list(self):
        cult_list = []
        for bloodoath in BloodOath.all:
            if bloodoath.follower == self:
                cult_list.append(bloodoath.cult)
        return cult_list
    
    def num_of_cults(self):
        cult_list = []
        for bloodoath in BloodOath.all:
            if bloodoath.follower == self:
                cult_list.append(bloodoath.cult)
        return len(cult_list)
        
    
    def my_cults_slogans(self):
        slogan_list = []
        cult_list = self.cult_list()
        for cult in self.cult_list():
            slogan_list.append(cult.slogan)
        return slogan_list
    

    @classmethod
    def most_active(cls):
        most_active_follower = cls.all_followers[0]
        for follower in cls.all_followers:
            if follower.num_of_cults() > most_active_follower.num_of_cults():
                most_active_follower = follower
        return most_active_follower

    @classmethod
    def follower_activity_sort(cls):
        follower_activity = []
        for follower in cls.all_followers():
            follower_activity.append({follower: len(follower.cults())})    
        sorted_follower_activity = sorted(follower_activity, key=lambda x: list(x.values())[0], reverse = True)
        return sorted_follower_activity    

    # def join_cult(self, cult):
    #     if self.age >= cult.minimum_age:
    #         BloodOath(self, cult)
    #     else:
    #         print(f"Sorry, you are not yet old enough to join the cult of {cult.name}")
    #     
    @classmethod
    def most_cults(cls):
        followers = cls.all_followers
        followers.sort(key=lambda x: x.num_of_cults(), reverse=True)
        most_cults = []
        max_cults = followers[0].num_of_cults()
        for follower in followers:
            if follower.num_of_cults() == max_cults:
                most_cults.append(follower)
            else:
                break
        return most_cults
    
    @classmethod
    def top_ten(cls):
        return cls.most_cults()[:2]
    
    def join_cult(self, cult):
        # check if follower is already a member of the cult
        for bloodoath in BloodOath.all:
            if bloodoath.follower == self and bloodoath.cult == cult:
                print(f"{self.name} is already a member of {cult.name}.")
                return
        
        # create a new blood oath for the follower and the cult
        new_bloodoath = BloodOath(self, cult)
        
        print(f"{self.name} has joined {cult.name}!")



    # def join_cult(self, cult):
    #     if self.age >= cult.minimum_age:
    #         BloodOath(self, cult)
    #     else:
    #         print(f"Sorry, you are not yet old enough to join the cult of {cult.name}")
    
# **`Follower`**

# * `Follower#join_cult`
#   * takes in an argument of a `Cult` instance and adds this follower to the cult's list of followers
# * `Follower.top_ten`
#   * returns an `List` of followers; they are the ten most active followers

# Done 
# * `Follower.most_active`
#   * returns the `Follower` instance who has joined the most cults
# * `Follower#my_cults_slogans`
#   * prints out all of the slogans for this follower's cults
# * `Follower#cults`
#   * returns an `List` of this follower's cults
# * `Follower.of_a_certain_age`
#   * takes a `Integer` argument that is an age and returns an `List` of followers who are the given age or older
# * `Follower.all`
#   * returns an `List` of all the followers
# * `Follower#name`
#   * returns a `String` that is the follower's name
# * `Follower#age`
#   * returns a `Integer` that is the age of the follower
# * `Follower#life_motto`
#   * returns a `String` that is the follower's life motto
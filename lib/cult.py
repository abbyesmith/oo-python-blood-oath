from .bloodoath import BloodOath

class Cult:
    all_cults = []

    def __init__(self, name, location, founding_year, slogan):
        if type(name) is str:
            self.name = name
        if type(location) is str:
            self.location = location
        if type(founding_year) is int:
            self.founding_year = founding_year
        if type(slogan) is str:
            self.slogan = slogan
        Cult.all_cults.append(self)
    
    @classmethod
    def find_by_name(cls, name):
        matching_cult_names = []
        for cult in Cult.all_cults:
            if cult.name == name:
                matching_cult_names.append(cult)
        return matching_cult_names

    @classmethod
    def find_by_location(cls, location):
        matching_cult_locations = []
        for cult in Cult.all_cults:
            if cult.location == location:
                matching_cult_locations.append(cult)
        return matching_cult_locations
    
    @classmethod
    def cult_locations(cls):
        locations = {}
        for cult in cls.all_cults:
            if cult.location not in locations:
                locations[cult.location] = 1
            else:
                locations[cult.location] += 1
        return locations

    @classmethod
    def most_common_location(cls):
        locations = cls.cult_locations()
        current_high_count = 0
        current_high_location = None
        for location, count in locations.items():
            if count > current_high_count:
                current_high_count = count
                current_high_location = location
        return current_high_location

    @classmethod
    def find_by_founding_year(cls, founding_year):
        matching_cult_founding_years = []
        for cult in Cult.all_cults:
            if cult.founding_year == founding_year:
                matching_cult_founding_years.append(cult)
        return matching_cult_founding_years

    def member_list(self):
        member_list = []
        for bloodoath in BloodOath.all:
            if bloodoath.cult == self:
                member_list.append(bloodoath.follower)
        return member_list
    
    def cult_population(self):
        member_list = []
        for bloodoath in BloodOath.all:
            if bloodoath.cult == self:
                member_list.append(bloodoath)
        return len(member_list)

    def average_age(self):
        member_list = self.member_list()
        if member_list:
            total_age = sum([members.age for members in member_list])
            return float(total_age / len(member_list))
        else:
            return None
    
    def my_followers_mottos(self):
        motto_list = []
        member_list = self.member_list()
        for follower in self.member_list():
            motto_list.append(follower.life_motto)
        return motto_list 

    @classmethod
    def least_common(cls):
        least_popular_cult = cls.all_cults[0]
        # cult_population = cls.cult_population
        for cult in cls.all_cults:
            if cult.cult_population() < least_popular_cult.cult_population():
                least_popular_cult = cult
        return least_popular_cult
        
# **`Cult`**



# DONE
# * `Cult.least_popular`
#   * returns the `Cult` instance who has the least number of followers :(
# * `Cult#my_followers_mottos`
#   * prints out all of the mottos for this cult's followers
# * `Cult#average_age`
#   * returns a `Float` that is the average age of this cult's followers
# * `Cult#cult_population`
#   * returns a `Integer` that is the number of followers in this cult
# * `Cult.most_common_location`
#   * returns a `String` that is the location with the most cults
# * `Cult#name`
#   * returns a `String` that is the cult's name
# * `Cult#location`
#   * returns a `String` that is the city where the cult is located
# * `Cult#founding_year`
#   * returns a `Integer` that is the year the cult was founded
# * `Cult#slogan`
#   * returns a `String` that is this cult's slogan
# * `Cult.all`
#   * returns an `List` of all the cults
# * `Cult.find_by_name`
#   * takes a `String` argument that is a name and returns a `Cult` instance whose name matches that argument
# * `Cult.find_by_location`
#   * takes a `String` argument that is a location and returns an `List` of cults that are in that location
# * `Cult.find_by_founding_year`
#   * takes a `Integer` argument that is a year and returns a list of all the cults founded in that year






    
# import ipdb
from lib.follower import Follower
from lib.cult import Cult
from lib.bloodoath import BloodOath

# test your code here
# e.g.

c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( 'Reasonablists', 'Pawnee', 1970, 'Hail Zorp')
c3 = Cult( 'Reasonablists', 'Eagleton', 1975, 'Zorp likes us better')
c4 = Cult( 'Heavens Gate', 'Pawnee', 1974, 'Human Metamorphosis')



f1 = Follower( 'Emiley', 34, 'Living the Dream' )
f2 = Follower( 'Ron Swanson', 45, 'I know more than you')
f3 = Follower( 'Gerry', 67, 'Oh Geez')
f4 = Follower( 'Leslie Knope', 34, 'Waffles!')



bo1 = BloodOath( '2019-09-16', f1, c1 )
bo2 = BloodOath( '2017-10-31', f2, c2 )
bo3 = BloodOath( '2017-10-31', f2, c4 )
bo4 = BloodOath( '2020-10-31', f3, c2 )
bo5 = BloodOath( '2019-10-31', f3, c3 )
bo6 = BloodOath( '2018-10-31', f3, c4 )
bo7 = BloodOath( '2017-10-31', f4, c2 )


# print(Cult.all_cults)
# print(c1.name)
# print(c1.founding_year)
# print(c2.name)
# print(c2.slogan)
# print(bo1.initiation_date)
# print(len(BloodOath.all))
# print(bo2.cult.name)
# ipdb.set_trace()
# print(Cult.find_by_name("Reasonablists"))
# print(Cult.find_by_location("Eagleton"))
# print(Cult.find_by_founding_year(1974))
# print(Cult.most_common_location())
# print(Follower.all_followers())
# print(f4.age)
# print(Follower.all_followers)
# print(Follower.of_a_certain_age(45))
# print(BloodOath.first_oath())
# print(c3.cult_population())
# print (c2.average_age())
# print(c2.my_followers_mottos())
# print(Cult.least_common().name)
# print(f3.cult_list())
# print(f2.my_cults_slogans())
print(Follower.join_cult(f1, c3))
# print(Follower.top_ten())
# 
# Real Word Datas 
world_population = 8021309772
afria_female = 714604047
afria_male = 718108076


male_ration = 50.42
female_ration = 100 - 50.42
total_male = int((world_population * male_ration) / 100 )
total_female = int(world_population - total_male )


print(total_male)
print(total_female)


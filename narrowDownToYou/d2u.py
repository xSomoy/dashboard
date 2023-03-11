# Real Word Data

# WORLD 
world_population = 8043437969

# AFRICA
africa_female = 714604047
africa_male = 718108076

# ASIA
asia_female = 2334380564
asia_male = 2447668416

# NORTH AMERICA
north_Amerca_female = 307257554
north_Amerca_male = 299799765

# SOUTH AMERICA
south_Amerca_female = 224509673
south_Amerca_male = 219021362

# EUROPE
europe_female = 388955288
europe_male = 362491426

# AUSTRALIA
australia_female = 13363462
australia_male = 13278336


# UNIQUENESS FUNCTION


continent = int(input('Which Continate you are belong? \n 1.AFRICA \n 2.ASIA \n 3.NORTH AMERICA \n 4.SOUTH AMERICA \n 5.EUROPE \n 6.AUSTRALIA\n >> '))
gender = int(input('Which Continate you are belong? \n 1.MALE\n 2.FEMALE\n >> '))


if continent == 1 and gender == 1:
    unique = africa_male
elif continent == 1 and gender ==2:
    unique = africa_female
elif continent == 2 and gender == 1:
    unique = asia_male
elif continent == 2 and gender ==2:
    unique = asia_female
elif continent == 3 and gender == 1:
    unique = north_Amerca_male
elif continent == 3 and gender ==2:
   unique = north_Amerca_female
elif continent == 4 and gender == 1:
    unique = south_Amerca_male
elif continent == 4 and gender ==2:
    unique = south_Amerca_female
elif continent == 5 and gender == 1:
    unique = europe_male
elif continent == 5 and gender ==2:
    unique = europe_female
elif continent == 6 and gender == 1:
    unique = australia_male
elif continent == 6 and gender ==2:
    unique = australia_female

print(unique)
                

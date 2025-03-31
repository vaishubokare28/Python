# 1) Create a Nested dictionary Movie details-
# 2 directors and 3 movies details
movie_details = {
    "Rajkumar Hirani": {
        "3 Idiots": {
            "Year": 2009,
            "Genre": "Comedy-Drama",
        },
        "PK": {
            "Year": 2014,
            "Genre": "Comedy-Drama",
        },
        "Munna Bhai M.B.B.S": {
            "Year": 2003,
            "Genre": "Comedy-Drama",
        }
    },
    "Sanjay Leela Bhansali": {
        "Padmaavat": {
            "Year": 2018,
            "Genre": "Historical Drama",
        },
        "Bajirao Mastani": {
            "Year": 2015,
            "Genre": "Historical Romance",
        },
        "Goliyon Ki Raasleela Ram-Leela": {
            "Year": 2013,
            "Genre": "Romantic Drama",
                            }
    }
}

print(movie_details)

# 2) To access featues
genre_3_idiots = movie_details["Rajkumar Hirani"]["3 Idiots"]["Genre"]
print("Genre of 3 Idiots:", genre_3_idiots)

year_padmaavat = movie_details["Sanjay Leela Bhansali"]["Padmaavat"]["Year"]
print("Year of Padmaavat:", year_padmaavat)




# 3) To add some data and update some values.
movie_details["Rajkumar Hirani"]["3 Idiots"]["Lead Actor"] = "Aamir Khan"
movie_details["Sanjay Leela Bhansali"]["Bajirao Mastani"]["Lead Actor"] = "Ranveer Singh"
print(movie_details)

movie_details["Sanjay Leela Bhansali"]["Padmaavat"]["Lead Actor"] = "Ranveer Singh"
print(movie_details)

# 4)Iteration using for loop keys(), values(), items()
for i in movie_details.keys():
    print(i)

for i in movie_details.values():
    print(i)

for i in movie_details.items():
    print(i) 



# 5)marks={'m1':45, 'm2':56, 'm3':78) to calculate sum of values 45+56+78
marks={'m1':45, 'm2':56, 'm3':78}
sum=0
for i in marks.values():
    sum+=i
print(sum)

# 6)to calculate multiplication of a values-
marks={'m1':45, 'm2':56, 'm3':78}
mul=1
for i in marks.values():
    mul*=i
print(mul)
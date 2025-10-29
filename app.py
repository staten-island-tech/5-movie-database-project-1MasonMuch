import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# for movie in data:
#     print(movie['title'])
    



# input1 = int(input("Input year after"))
# input2 = int(input("Input year before"))


# for movie in data:
#     if movie['year'] > input1 and movie['year'] < input2:
#         print (movie['title'], movie['year'])

# year = int(input('input year during movie'))

# for movie in data:
#     if movie['year'] == year:
#         print(movie['title'], movie['year'])

name = input("Input name")

for movie in data:
    if name in movie['title']:
        print(movie['title'])
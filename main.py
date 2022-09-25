from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

option = input("Please pick from the following options: \nType 1 for everything about a movie. Type 2 for everything about an actor.")
if option == "1":
    chosenmovie = input("Type movie ID from IMDb.")
    
elif option == "2":
    personinput = input("Who would you like to find?")

# get a movie
movie = ia.get_movie(chosenmovie)

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

# search for a person name
#people = ia.search_person(personinput)
#for person in people:
 #  print(person.personID, person['name'])
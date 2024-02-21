# add new movies to my collection
# list all the movies in my collection
# find a movies by using the movies title

# where the movies are
MENU_PROMPT = "\nEnter 'a' to add a movie, 's' to see your movies, 't' to find a movie by type, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie tile: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    type = input("Enter the movie type: ")


    movies.append({
        'title': title,
        'director': director,
        'year': year,
        'type': type
    })

# show the user menu

def see_movies ():
    for movie in movies:
        print_movie(movie)
    
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")
    print(f"Type: {movie['type']}")



def find_movies_by_title ():
    operation = input("Enter the name of the movie: ")
    
    for movie in movies:
        if movie["title"] == operation:
            print_movie(movie)

def find_movies_by_type ():
    operation = input("Enter the type of the movie: ")
    
    for movie in movies:
        if movie["type"] == operation:
            print_movie(movie)

user_options = {
    "a" : add_movie,
    "s" : see_movies,
    "f" : find_movies_by_title,
    "t" : find_movies_by_type
}
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Try Again.")
        
    selection = input(MENU_PROMPT)

menu()

from tkinter.font import names
class Movie:
    def __init__(self, name, duration, director):
        self.name = name
        self.duration = duration
        self.director = director

    def __repr__(self):
        return f'Movie("{self.name}, {self.duration}, "{self.director}")'

class Watchlist:
    def __init__(self):
        self.movies_to_watch = []
        self.movies_watched = []

    def add_movies(self, movie_list):
        self.movies_to_watch.extend(movie_list)

    def watch_movie(self, movie_name):
        for movie in self.movies_to_watch:
            if movie.name == movie_name:
                self.movies_to_watch.remove(movie)
                self.movies_watched.append(movie)
                return f'You have watched "{movie_name}"'
            return f'Movie "{movie_name}" not found in your to-watch list.'

    def print_status(self):
        print("Movies to watch:")
        for movie in self.movies_to_watch:
            print(movie)
        print("Movies watched:")
        for movie in self.movies_watched:
            print(movie)

    def total_duration_to_watch(self):
        return sum(movie.duration for movie in self.movies_to_watch)

    def total_duration_watched(self):
        return sum(movie.duration for movie in self.movies_watched)

    def watch_all_movies_of_director(self, movie_director):
        movies_by_director = [movie for movie in self.movies_to_watch if movie.director == movie_director]
        if movies_by_director:
            for movie in movies_by_director:
                self.movies_to_watch.remove(movie)
                self.movies_watched.append(movie)
            return f'You have watched all movies by {movie_director}.'
        return f'No movies by {movie_director} found in your to-watch list.'


watchlist = Watchlist()
watchlist.add_movies([
    Movie("Pulp Fiction", 154, "Quentin Tarantino"),
    Movie("Barry Lyndon", 185, "Stanley Kubrick"),
    Movie("Luca", 95, "Enrico Casarosa"),
    Movie("Gone with the Wind", 238, "Victor Fleming")])

watchlist.add_movies([
    Movie("Volver", 121, "Pedro Almodovar"),
    Movie("The Shining", 115, "Stanley Kubrick")
])

watchlist.watch_movie("Volver")
watchlist.watch_movie("Luca")

watchlist.print_status()

print(watchlist.watch_movie("Volver"))
print(watchlist.watch_movie("Luca"))

watchlist.print_status()

print(f"Total time left to watch: {watchlist.total_duration_to_watch()} minutes")
print(f"Total time watched: {watchlist.total_duration_watched()} minutes")

print(watchlist.watch_all_movies_of_director("Stanley Kubrick"))

watchlist.print_status()



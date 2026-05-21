import re


words = ["mystery", "brother", "aviator", "crocodile", "pearl", "orchard", "crackpot"]
words2 = ["machine", "subset", "trouble", "starting", "matter", "eating", "truth", "disobedience"]
numbers = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]
numbers2 = [2, 6, 9, 10, 7, 4, 1, 9]


movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont", "duration": "2h 22min", "genre": ["Crime", "Drama"], "score": 9.3},
    {"title": "The Godfather", "year": 1972, "director": "Francis Ford Coppola", "duration": "2h 55min", "genre": ["Crime", "Drama"], "score": 9.2},
    {"title": "Schindler's List", "year": 1993, "director": "Steven Spielberg", "duration": "3h 15min", "genre": ["Biography", "Drama", "History"], "score": 9.0},
    {"title": "The Dark Knight", "year": 2008, "director": "Christopher Nolan", "duration": "2h 32min", "genre": ["Action", "Crime", "Drama"], "score": 9.0},
    {"title": "Pulp Fiction", "year": 1994, "director": "Quentin Tarantino", "duration": "2h 34min", "genre": ["Crime", "Drama"], "score": 8.9},
    {"title": "Forrest Gump", "year": 1994, "director": "Robert Zemeckis", "duration": "2h 22min", "genre": ["Drama", "Romance"], "score": 8.8},
    {"title": "Inception", "year": 2010, "director": "Christopher Nolan", "duration": "2h 28min", "genre": ["Action", "Adventure", "Sci-Fi"], "score": 8.8},
    {"title": "The Matrix", "year": 1999, "director": "Lana Wachowski", "duration": "2h 16min", "genre": ["Action", "Sci-Fi"], "score": 8.7},
    {"title": "Goodfellas", "year": 1990, "director": "Martin Scorsese", "duration": "2h 26min", "genre": ["Biography", "Crime", "Drama"], "score": 8.7},
    {"title": "Amistad", "year": 1997, "director": "Steven Spielberg", "duration": "2h 35min", "genre": ["Biography", "Drama", "History"], "score": 7.3},
    {"title": "Interstellar", "year": 2014, "director": "Christopher Nolan", "duration": "2h 49min", "genre": ["Adventure", "Drama", "Sci-Fi"], "score": 8.7},
    {"title": "Saving Private Ryan", "year": 1998, "director": "Steven Spielberg", "duration": "2h 49min", "genre": ["Drama", "War"], "score": 8.6},
    {"title": "The Silence of the Lambs", "year": 1991, "director": "Jonathan Demme", "duration": "1h 58min", "genre": ["Crime", "Drama", "Thriller"], "score": 8.6},
    {"title": "City of God", "year": 2002, "director": "Fernando Meirelles", "duration": "2h 10min", "genre": ["Crime", "Drama"], "score": 8.6},
    {"title": "Parasite", "year": 2019, "director": "Bong Joon-ho", "duration": "2h 12min", "genre": ["Comedy", "Drama", "Thriller"], "score": 8.6},
]


def max_of_two_numbers(a, b):
    if a >= b:
        return a

    return b


def find_longest_word(words):
    if len(words) == 0:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def average_numbers(numbers):
    if len(numbers) == 0:
        return None

    return sum_numbers(numbers) / len(numbers)


def does_word_exist(words, word):
    if len(words) == 0:
        return None

    return word in words


def get_all_directors(movies):
    return [movie["director"] for movie in movies]


def get_all_directors_unique(movies):
    directors = []

    for movie in movies:
        director = movie["director"]

        if director not in directors:
            directors.append(director)

    return directors


def how_many_movies(movies):
    count = 0

    for movie in movies:
        if movie["director"] == "Steven Spielberg" and "Drama" in movie["genre"]:
            count += 1

    return count


def scores_average(movies):
    if len(movies) == 0:
        return 0

    total = 0

    for movie in movies:
        total += movie["score"]

    return round(total / len(movies), 2)


def drama_movies_score(movies):
    dramas = []

    for movie in movies:
        if "Drama" in movie["genre"]:
            dramas.append(movie)

    if len(dramas) == 0:
        return 0

    return scores_average(dramas)


def order_by_year(movies):
    return sorted(movies, key=lambda movie: (movie["year"], movie["title"]))


def order_alphabetically(movies):
    ordered_movies = sorted(movies, key=lambda movie: movie["title"])
    first_twenty = ordered_movies[:20]

    return [movie["title"] for movie in first_twenty]


def turn_hours_to_minutes(movies):
    movies_with_minutes = []

    for movie in movies:
        new_movie = movie.copy()

        match = re.search(r"(\d+)h\s*(\d*)min?", movie["duration"])

        hours = 0
        minutes = 0

        if match:
            hours = int(match.group(1))

            if match.group(2) != "":
                minutes = int(match.group(2))

        new_movie["duration"] = hours * 60 + minutes
        movies_with_minutes.append(new_movie)

    return movies_with_minutes


def best_year_avg(movies):
    if len(movies) == 0:
        return None

    by_year = {}

    for movie in movies:
        year = movie["year"]

        if year not in by_year:
            by_year[year] = []

        by_year[year].append(movie["score"])

    best_year = None
    best_avg = 0

    for year, scores in by_year.items():
        avg = sum(scores) / len(scores)

        if best_year is None or avg > best_avg or (avg == best_avg and year < best_year):
            best_avg = avg
            best_year = year

    best_avg = round(best_avg, 2)

    return f"The best year was {best_year} with an average score of {best_avg}"


if __name__ == "__main__":
    # Parte 1
    print(max_of_two_numbers(4, 7))           # 7
    print(find_longest_word(words))           # "crocodile"
    print(sum_numbers(numbers))               # 87
    print(average_numbers(numbers2))          # 6.0
    print(does_word_exist(words2, "truth"))   # True
    print(does_word_exist(words2, "coding"))  # False

    # Parte 2
    print(get_all_directors(movies))
    print(how_many_movies(movies))            # 3
    print(scores_average(movies))             # 8.79
    print(drama_movies_score(movies))         # 8.75
    print(order_by_year(movies)[0]["title"])  # "The Godfather" (1972)
    print(order_alphabetically(movies)[:3])   # primeros 3 títulos en orden A-Z
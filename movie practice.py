import requests


def query(query):
    app_key = 'db17e1165c30d0f158babbfc71a802cb'
    result = requests.get(
        'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
            app_key, query))

    data = result.json()

    return data['results']


def movie_search():
    query = input("Please enter the title of the film you would like to find:  "
                  )  # Asks user to enter the title of a film
    app_key = 'db17e1165c30d0f158babbfc71a802cb'
    result = requests.get(
        'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
            app_key, query))

    results = result.json()

    if len(results["results"]) == 0:
        print("No search results found.")
        return

    for result in results["results"]:
        title = result["title"]
        id = result["id"]
        release_date = result["release_date"]
        # Prints results of the search with every movie containing the words from the query
        print("Movie title: {}".format(title))
        print(
            "Movie release: {}".format(release_date)
        )  # Release date included to make it easier for users to find the right movie
        print("Movie id: {}".format(id))
        print()

    while True:
        try:
            movie_id = int(
                input("Please now enter the ID of the film you would like to find: "))
            break
        except ValueError:
            print("That's not a movie ID. Please enter a number.")

    # Now asks the user to enter the ID from the list they have been given.

    app_key = 'db17e1165c30d0f158babbfc71a802cb'
    result = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(
            movie_id, app_key))

    results = result.json()

    items = [
        'title', 'homepage', 'genres', 'overview', 'release_date', 'runtime',
        'production_companies', 'budget'
    ]  # creates list for text file

    genre = results["genres"]  # targets dictionary within list
    production_company = results[
        'production_companies']  # targets dictionary within list

    with open(
            'movie.txt', 'a+'
    ) as text_file:  # writes and appends text file so programme can be run multiple times
        for item in items:
            text_file.write(item + ': ' + str(results[item]) + '\n')

    # Prints results into console
    print("Movie title: {}".format(results['title']))
    print("Homepage: {}".format(results['homepage']))
    for i in genre:
        print(
            "Movie genre: {}".format(i['name'])
        )  # targets the genres 'name' key in the dictionary embedded in the list
        break
    print("Movie overview: {}".format(results['overview']))
    print("Release_date: {}".format(results['release_date']))
    print("Run time: {} minutes".format(results['runtime']))
    for i in production_company:
        print(
            "Production company: {}".format(i['name'])
        )  # targets the production company 'name' key in the dictionary embedded in the list
        break
    print("Movie budget: ${}".format(results['budget']))


movie_search()
# can be ran multiple times and information will copy into text file

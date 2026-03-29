import requests

API_KEY = "265515c01d26a1fe6ce3b15b3a74bd4d"

# Function to search movie and get ID
def search_movie(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["results"]:
            return data["results"][0]["id"]
        else:
            return None
    except:
        print("Error connecting to API")
        return None


# Function to get recommendations
def get_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        movies = []
        for movie in data["results"][:5]:
            movies.append(movie["title"])

        return movies
    except:
        print("Error fetching recommendations")
        return []


# Main CLI
def main():
    while True:
        print("\n🎬 Movie Recommendation System")
        print("1. Get Recommendations")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            movie_name = input("Enter movie name: ")

            movie_id = search_movie(movie_name)

            if movie_id:
                recs = get_recommendations(movie_id)

                if recs:
                    print("\nRecommended Movies:")
                    for movie in recs:
                        print("-", movie)
                else:
                    print("No recommendations found.")
            else:
                print("Movie not found!")

        elif choice == "2":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice! Please try again.")


# Run program
main()

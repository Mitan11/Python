''' Write a menu driven python script for managing data of Bollywood actors and
actresses, which will allow user to perform following operations:
1. Add actor/actress (Which will allow user to enter the details like name, total
movies, fees per movie, no of flop movies)
2. Display rating of actor/actress based on following formula. (Which will allow
user to enter the name and will display his/her rating)
Formula for rating:
Grade “I” Celebrities: more than 30 movies, less than 10 flop movies, fess more
than 50 lakhs
Grade “II” Celebrities: movies between 10 and 20, flow movies between 10
and 20, fees range between 30 lakhs to 50 lakhs.
Grade “III” Celebrities: less than 10 movies and more than 20 flop movies.
3. Display bottom 5 celebrities based on their fess per movie.
4. Exit'''

bollywood_celebrities = []

def add_celebrity():
    name = input("Enter Celebrity Name: ")
    total_movies = int(input("Enter Total Movies: "))
    fees_per_movie = float(input("Enter Fees per Movie (in lakhs): "))
    flop_movies = int(input("Enter Number of Flop Movies: "))
    bollywood_celebrities.append({'name': name, 'total_movies': total_movies, 'fees_per_movie': fees_per_movie, 'flop_movies': flop_movies})

def display_rating():
    name = input("Enter Celebrity Name to check rating: ")
    for celeb in bollywood_celebrities:
        if celeb['name'] == name:
            if celeb['total_movies'] > 30 and celeb['flop_movies'] < 10 and celeb['fees_per_movie'] > 50:
                rating = "Grade I"
            elif 10 <= celeb['total_movies'] <= 20 and 10 <= celeb['flop_movies'] <= 20 and 30 <= celeb['fees_per_movie'] <= 50:
                rating = "Grade II"
            elif celeb['total_movies'] < 10 and celeb['flop_movies'] > 20:
                rating = "Grade III"
            else:
                rating = "Unrated"
            print(f"Celebrity {name} has a rating of: {rating}")
            return
    print("Celebrity not found.")

def get_fees(actor):
    return actor["fees_per_movie"]

def display_bottom_5():
    sorted_actors = sorted(bollywood_celebrities, key=get_fees)
    
    bottom_5 = sorted_actors[:5]

    print("\n--- Bottom 5 Celebrities (By Fees per Movie) ---")
    for a in bottom_5:
        print(f"Name: {a['name']}, Fees per Movie: {a['fees_per_movie']} lakhs, Movies: {a['total_movies']}, Flops: {a['flop_movies']}")

while True:
    print("\nMenu:")
    print("1. Add Actor/Actress")
    print("2. Display rating of actor/actress")
    print("3. Display bottom 5 celebrities based on their fees per movie")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_celebrity()
    elif choice == '2':
        display_rating()
    elif choice == '3':
        display_bottom_5()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
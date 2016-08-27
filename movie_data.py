import movie_page
import movie

# Instance of movie Inception
inception = movie.Movie("Inception",  # Movie Title

                        "Dreams into dreams!", # Storyline

                        "https://upload.wikimedia.org/wikipedia/en/thu"       #Poster Image
                        "mb/2/2e/Inception_%282010%29_theatrical_poster.jp"
                        "g/220px-Inception_%282010%29_theatrical_poster.jpg",

                        "https://www.youtube.com/watch?v=hstBN0Qkqhc")   # Youtube trailer

# Instance of movie Hercules
hercules = movie.Movie("Hercules",  # Movie Title

                       "Story of the son of zeus who is a demi god", # Storyline

                       "https://upload.wikimedia.org/wikipedia/en/thu"       #Poster Image
                       "mb/0/09/Hercules_%282014_film%29.jpg/220px-Her"
                       "cules_%282014_film%29.jpg",

                       "https://www.youtube.com/watch?v=g0GMzQwO2l0")   # Youtube trailer

# Instance of movie Suicide Squad
suicide_squad = movie.Movie("Suicide Squad",  # Movie Title

                       "Group of metahumans and criminals fight against spiritual power to save the world", # Storyline

                       "https://upload.wikimedia.org/wikipedia/en/thu"       #Poster Image
                       "mb/5/50/Suicide_Squad_%28film%29_Poster.png/22"
                       "0px-Suicide_Squad_%28film%29_Poster.png",

                       "https://www.youtube.com/watch?v=CmRih_VtVAs")   # Youtube trailer

# All the movie instances in an array
movies = [inception, hercules, suicide_squad]

#calling open movie page function to render the movie pages
movie_page.open_movies_page(movies)

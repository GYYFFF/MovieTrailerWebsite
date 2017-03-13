import Media
import fresh_tomatoes

# Display 4 movies, click on movie's poster image will play its trailer

Avatar = Media.Movie("Avatar", "An alien story",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

Home_alone = Media.Movie("Home Alone", "One smart kid fight with burglars",
                         "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

Sully = Media.Movie("Sully", "A flight emergency landing on the Hudson River",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg",
                    "https://www.youtube.com/watch?v=mjKEXxO2KNE")

Captain_Philips = Media.Movie("Captain Philips", "A captain and his crew fight with pirates",
                              "https://upload.wikimedia.org/wikipedia/en/a/a8/Captain_Phillips_Poster.jpg",
                              "https://www.youtube.com/watch?v=pV-ptQX-75Y")

movie_list = [Avatar, Home_alone, Sully, Captain_Philips]
fresh_tomatoes.open_movies_page(movie_list)

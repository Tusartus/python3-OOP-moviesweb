import fresh_tomatoes
import media

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "https://4.imimg.com/data4/VI/DO/ANDROID-58907264/product-500x500.jpeg",
                        "https://youtu.be/PjfP2tmjtQM"
                        )

tomjerry = media.Movie("Tom and jerry",
                        "Tom and jerry playing and reading ",
                        "https://upload.wikimedia.org/wikipedia/en/5/5f/TomandJerryTitleCardc.jpg",
                        "https://youtu.be/7fcP64w7eBE"
                        )

gameoftrone = media.Movie("Game of trone",
                        "Game of Thrones - Daenerys Targaryen & The Unsullied ",
                        "https://www.emmys.com/sites/default/files/styles/show_detail/public/2013/08/GAME-of-THRONES-w0717_0.jpg?itok=1KgWSE3n",
                        "https://youtu.be/zXpHvhjUzAI"
                        )






#print(tomjerry.storyline)
#tomjerry.show_trailer()

movies = [ toy_story,tomjerry, gameoftrone]
fresh_tomatoes.open_movies_page(movies)

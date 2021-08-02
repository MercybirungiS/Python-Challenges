# 
# A movie club contains many movies. Each movie has a title and one or more directors. 
# A movie may be borrowed and returned from the club. Write a class Movie and another class MovieClub
# with appropriate instance variables and methods to implement the scenario. Also, write a method to return
#the current number of movies in the club



class Movie:
    def __init__(self,title,directors):
        self.title=title
        self.directors=directors

    def movie_title(self):
        return f"{self.title} has been added"  
    def director_name(self ,name1,name2) :
    
        return f"{name1} and {name2} are the directors of {self.title}"

class MovieClub(Movie):
    def __init__(self,title,directors,no_movies):
        Movie.__init__(self,title,directors)
        self.no_movies=no_movies

    def borrow_movies(self,total):
        if total<=0:
            return "You can not borrow zero movies"
        else :
            self.no_movies-=total
            return f"Hello ,you have borrowed {total} movies and there are {self.no_movies} movies left in the movie club "

    def return_movies(self,returned):
        if returned <=0:
            return "Invalid , return the movies you borrowed "

        else:
           self.no_movies+=returned
           return f"Hello you have returned the movies you borrowed , the new number of movies in the movie club  is now {self.no_movies}"

    
newMovies=Movie("Game of Thrones" ,"Allan Taylor")
print(newMovies.movie_title())
print(newMovies.director_name("Mark","Allan"))
movieClub=MovieClub("Mayor of Casterbridge","Mark Twain",10)
print(movieClub.borrow_movies(4))
print(movieClub.return_movies(4))






    

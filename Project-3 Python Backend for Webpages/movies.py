#Sam Yu
#Assignment 3 Talk python to mem
class Media:
    def __init__(self,title):
        
        self.title = title
    
    def slug(self):
        title_list = list(self.title)
        filtered_title_iterator = filter(help_slug, title_list)
        filtered_title_list = list(filtered_title_iterator)
        filtered_title_list = [blank.replace(' ','-') for blank in filtered_title_list]
        filtered_string ="".join(filtered_title_list)
        filtered_string = filtered_string.lower()
        return filtered_string
    
class Movie(Media):
    ############# work out how to use super for this nonsense#############
    def __init__(self,title,year,director,runtime):
        super(Movie,self).__init__(title)
        self.year = year
        self.director = director
        self.runtime = runtime
    def __str__(self):
        return("("+str(self.year)+")" + str(self.title))
        
    def __rpr__(self):
        return("<Movie:" +self.title+ ">")
    
    def abbrevation(self): 
        first_three = self.slug()
        first_three = first_three.replace("-", "")
        first_three = first_three[:3]
        return first_three
 
        
def help_slug(title_char):
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
    special_chars_list = list(special_chars)
    if(title_char in special_chars_list):
        return False
    else:
        return True


# Decorator
def wrapper(msg):
    def actual_decorator(og_func):
        def header(*args):
            print("=====\n%s\n=====" % msg)
            return og_func(*args)
        return header
    return actual_decorator
movies_data_base = []

@wrapper("Movies:")
def slugs():
    [print(movie.slug()) for movie in movies_data_base]

@wrapper("Movie Abbr:")
def abbr():
    [print(movie.abbrevation()) for movie in movies_data_base]	    

    
@wrapper("Movies before given year: ")
def before_year(year):
    [print(movie) for movie in movies_data_base if movie.year < year]
    

    
def main():
    print("Thanks for checking the Local Movie Database!")
    slugs()
    abbr()
    before_year(2004)
    print("Thank you")
    return


if __name__ == '__main__':
    movies_data_base.append(Movie("Apocalypse Now", 1979, "Francis Coppola", 153))
    movies_data_base.append(Movie("Casablanca", 1942, "Michael Potatoe", 102))
    movies_data_base.append(Movie("Guardians of the Galxy", 2014, "James Gunn", 201))
    movies_data_base.append(Movie("12 Angry Women", 1995, "Sidney Lumet", 96))
    movies_data_base.append(Movie("Black Cheetah", 2016, "Marvel Avengers", 300))
    movies_data_base.append(Movie("Make Up Club", 2077, "David Fincher", 49))
    movies_data_base.append(Movie("Poorpus 9", 1945, "Dolphin Man", 99))
    movies_data_base.append(Movie("March of Germans", 1921, "Micheal Gary Scott", 199))

    main()

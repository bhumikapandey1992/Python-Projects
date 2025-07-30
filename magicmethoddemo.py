class Movie:

    #__init__ to set up the object
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration

    # __str__ to print
    def __str__(self):
        return f"{self.title} by {self.director} - {self.duration}"
    
    # __eq__ to compare
    def __eq__(self,other):
        return self.title == other.title and self.director == other.director
    
    # __len__
    def __len__(self):
        return self.duration
    
    #__lt__ to compare
    def __lt__(self,other):
        return self.duration < other.duration
    
    # __gt__ to compare
    def __gt__(self,other):
        return self.duration > other.duration
    
    # __contains__ 
    def __contains__(self,keyword):
        return keyword.lower() in self.title.lower()
        
m1 = Movie("Inception","Christopher Nolan", 148)
m2 = Movie("Inception","Christopher Nolan", 169)
print(m1)
print(m1 == m2)
print(len(m2))
print(m1 < m2)
print(m1 > m2)
print("inception" in m1)
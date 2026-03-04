
class dad:

    def _init_(self, eyes, funny):
        self.eyes = eyes
        self.funny = funny

    def display(self):
        print("your eye color is", self.eyes)
        print("You are funny", self .funny  )

# Child son(dad):
class son(dad):

   def _init_(self, name, age- eyes, funny)
        self.name = name   
        self.age = age
    
        # invoking the _init_of perent class
        # to access its attributes
        dad._init_(self, eyes, funny)
   
# Object Creation 
obj = son("Penguin", 8, "blue", True)
   
# Calling method display
obj.display()
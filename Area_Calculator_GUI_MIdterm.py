'''I googled alot to learn some stuff I didn't know how to implement. I used w3schools to learn some things 
I also didn't know how to not use the width for the square, so it helped me with that. You have to use "None"
I used https://www.tutorialspoint.com/python/tk_toplevel.htm
and I used the geeksforgeeks website on python syntax and small issues I had
I couldn't figure out a way to make the calculation end and give the user an option to make another calculation'''

import tkinter as tk

class Shape:  #shape class that has the shapes and exit buttons
    def __init__(self, root):
        self.root = root # root represents main window
        root.title("Shape Calculator")

        self.shape = None
        self.label = tk.Label(root, text="Choose a shape:")  #label or a title
        self.label.pack()

        self.square_button = tk.Button(root, text="Square", command=self.square) #square button
        self.square_button.pack()

        self.rectangle_button = tk.Button(root, text="Rectangle", command=self.rectangle) #rectangle button
        self.rectangle_button.pack()

        self.triangle_button = tk.Button(root, text="Triangle", command=self.triangle) #triangle button
        self.triangle_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit) #quit makes it so, it ends the program 
        #ends the program if the button quit is clicked
        self.exit_button.pack()

   
   #these next three methods are called after user selects a shape
  
    def square(self): #method for square and similar ones for all the shapes
        self.shape = "Square"
        self.area_window() #opens the area window

    def rectangle(self):
        self.shape = "Rectangle"
        self.area_window()

    def triangle(self):
        self.shape = "Triangle"
        self.area_window()

    
    def area_window(self):  #area method or function, also a window
        self.area_window = tk.Toplevel(self.root)

        if self.shape == "Square":
            self.area_window.title("Square Area Calculator")
            self.label = tk.Label(self.area_window, text="Enter the length of a side:")
            self.label.pack()
            self.length_input = tk.Entry(self.area_window)  #dot Entry allows user to put an input
            self.length_input.pack()
            self.width_input = None
        elif self.shape == "Rectangle":
            self.area_window.title("Rectangle Area Calculator")
            self.label = tk.Label(self.area_window, text="Enter the length and width:") # I made it so there was 2 inputs in one window
            self.label.pack()
            self.length_input = tk.Entry(self.area_window)
            self.length_input.pack()
            self.width_input = tk.Entry(self.area_window)
            self.width_input.pack()
        elif self.shape == "Triangle":
            self.area_window.title("Triangle Area Calculator")
            self.label = tk.Label(self.area_window, text="Enter the base and height:")
            self.label.pack()
            self.length_input = tk.Entry(self.area_window)
            self.length_input.pack()
            self.width_input = tk.Entry(self.area_window)
            self.width_input.pack()

        self.calculate_button = tk.Button(self.area_window, text="Calculate", command=self.calculate_area)
        #button that starts the calculation, it used to the calculate_area method
        self.calculate_button.pack()

    def calculate_area(self): #calculations for the 
        length = float(self.length_input.get()) #all shapes have a lenght input
        if self.width_input:  #this is only for rectangle and triangle
            width = float(self.width_input.get())

        if self.shape == "Square":  #if statement to choose which calculation to do 
            area = length ** 2   #square formula. length squared
            answer = f"The area of the square is {area}"
        elif self.shape == "Rectangle":
            area = length * width
            answer = f"The area of the rectangle is {area}"
        elif self.shape == "Triangle":
            area = 0.5 * length * width
            answer = f"The area of the triangle is {area}"

        self.result_window = tk.Toplevel(self.area_window) #Toplevel is a widget that can be created on top of the main window
        self.result_window.title("Result")
        self.result_label = tk.Label(self.result_window, text=answer)  #dispays the answer of the calculation in the
                                                                        #result window
        self.result_label.pack()
        self.result_button = tk.Button(self.result_window, text="program ended", command=self.close_windows)
        self.result_button.pack()
        

    def close_windows(self):
        self.result_window.destroy() #ends result window
        self.area_window.destroy() #ends area window


root = tk.Tk()#starting point of GUI
shape = Shape(root)#shape GUI and all it's widgets
root.mainloop() #makes GUI run, without it, it won't show the pop ups

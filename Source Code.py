# Importing pakages we need
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

# The window and its Tilte,Dimensions and Background
window = Tk()
window.title('Function Plotter')
window.geometry("640x680")
window.configure(background='teal')

# Text Variables
user_minx=StringVar()
user_maxx=StringVar()
user_function = StringVar()

# Getting the function we will plot
askForfunction = Label( text="Write Your Function",font=("Noto", 18),background="teal",foreground="black")
askForfunction.place(x = 40,y = 50)
function_input = Entry(textvariable=user_function)
function_input.place(x = 280,y = 55) 

# Getting the Minimum Value for X
askForminx = Label( text="Write Minimum X",font=("Noto", 18),background="teal",foreground="black")
askForminx.place(x = 40,y = 100)
minx_input = Entry(textvariable=user_minx)
minx_input.place(x = 280,y = 105) 

# Getting the Maximum Value for X
askFormaxx = Label( text="Write Maximum X",font=("Noto", 18),background="teal",foreground="black")
askFormaxx.place(x = 40,y = 150)
maxx_input = Entry(textvariable=user_maxx)
maxx_input.place(x = 280,y =155) 

# The default empty graph
default_figure = Figure(figsize=(6.5,5), dpi=88)
default_graph = default_figure.add_subplot(111)
chart = FigureCanvasTkAgg(default_figure, window)
chart.get_tk_widget().place(x = 35,y = 200)

# Titles and labels for default graph
default_graph.set_xlabel('x', fontsize=15)
default_graph.set_ylabel('F(x)', fontsize=15)
default_graph.set_title('Graph', fontsize=15)


# The function which will process the user function and plot it
def plot():
    
        
        # Getting user input
        temp_function=user_function.get()
        min_x=user_minx.get()
        max_x=user_maxx.get()
        
        # Replacing ^ with ** to make the program can solve the equation
        function=temp_function.replace("^","**")
        
      
        
        # Checking user inputs 
        check=True
        # Checkin x values 
        try:
           x = [i for i in range(int(min_x),int(max_x))]
        except:
               messagebox.showerror("Error","Please Write Valid Values for X")
               check=False
        
        # Checking the function
        if check==True:
            try:
               y = [eval(function)for x in range(int(min_x),int(max_x))]
            except:
                messagebox.showerror("Error","Please Write Correct Function")
       
        # Clearing the default Graph to plot the user function
        default_graph.figure.clear() 
          
        # Showing The Graph
        user_figure = Figure(figsize = (6.5,5),dpi = 88)
        user_graph = user_figure.add_subplot(111)
        
        # Plotting The function
        user_graph.plot(x,y)
        
        # Using Tkinter canvas
        canvas = FigureCanvasTkAgg(user_figure,window)
        canvas.draw()
        canvas.get_tk_widget().place(x = 35,y = 200)
        #
        # Titles and labels for user graph
        user_graph.set_xlabel('x', fontsize=15)
        user_graph.set_ylabel('F(x)', fontsize=15)
        user_graph.set_title('Graph', fontsize=15)
        
# The Plot Button
plot_button = Button(command = plot,height = 2,width =10,text = "Plot")
plot_button.place(x = 480,y = 95)

# To run the program
window.mainloop()

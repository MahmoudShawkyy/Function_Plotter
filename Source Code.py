# including the libraries we need
import matplotlib.pyplot as plt
import numpy as np

# loop is for expecting and handling errors
while True:
    try:
        # Getting the function we want to plot
        temp_function=input("Enter the function you want to graph")
        # We replace ^ with ** to can solve the equation in python
        function=temp_function.replace("^","**")
        
        # Getting the maximum and minimum value of x
        x_max=int(input("Enter the Maximum Value of X"))
        x_min=int(input("Enter the Minimum Value of X"))
        
        # Generating x and y values  
        x = np.linspace(x_min,x_max, 1000)
        y = eval(function)
        
        # Plotting points and x,y axis
        plt.plot(x, y)
        plt.axhline(color='grey')
        plt.axvline(color='grey')
        
        # Putting titles 
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title("The graph of your function")
        
        # Showing the graph
        plt.show()
        break
        
    except:
        print("Syntax Error, Please enter a valid function")

'''
 Katharine Münger
 February 2nd, 2018
 Intro to Computer Science
 Creates three types of plots (random, squares, cubes) and a corresponding text file with the coordinate sets.
'''

import matplotlib.pyplot as plt
import random


def create_random_data(num_pts):
    ''' creats two lists:
    x-  [1, 2, 3, ..., num_pts]
    y- randomly drawn values between 0 and 1.
    Returns: x and y lists 
    
    '''
    x = []
    for i in range(1,num_pts+1):
        x.append(i)
    y = []
    for i in range(num_pts):
        y.append(random.random())
    return x,y

def squared_data(num_pts):
    ''' creats two lists:
    x- [1, 2, 3, ..., num_pts]
    y- [x^2, ...]
    Returns: x and y lists 
    
    '''
    x = []
    for i in range(1,num_pts+1):
        x.append(i)
    y = []
    for i in range(num_pts):
        y.append(i*i)
    return x,y

def cubed_data(num_pts):
    ''' creats two lists:
    x- [1, 2, 3, ..., num_pts]
    y- [x^3, ...]
    Returns: x and y lists 
    '''
    x = []
    for i in range(1,num_pts+1):
        x.append(i)
    y = []
    for i in range(num_pts):
        y.append(i*i*i)
    return x, y
    
def save_points(x, y, data_type_str):
    ''' Takes in x and y coordinates and saves them in a txt file.
    Parameters:
    x - a list of x-coordinates 
    y - a list of y-coordinates   
    Should be same length as x.
    filename - a string that is the name of the file you want to save
    '''
    file = open(data_type_str, 'w')
    
    #adds the string versions of the x&y coordinates to a text file
    i=0
    for num in x:
        x_str = str(x[i])
        y_str = str(y[i])
        file.write(x_str +', ' + y_str + '\n')
        i+= 1
    
    file.close()
    
def plot_points(x, y, title = None):
    '''Plots the values in lists x and y as two dimensional points. 
    Optional argument title will add a title to the graph.
    
    Parameters:
    x - a list of x-coordinates for the 2-d points.
    y - a list of y-coordinates for the 2-d points.  
    Should be same length as x.
    title - a string to use for the title of the figure.
    
    Returns: None (Displays a graph, but graph is not returned)
    '''

    plt.plot(x,y, '.')
    plt.xlabel('x values')
    plt.ylabel('y values')
    if title is not None:
        plt.title(title)
    plt.show()
    
# The main function should always be the last function
# in your module.
def main():
    ###
    # Make sure to add some useful comments here. 
    ###
    '''Asks the user 
    Returns: 
    num_pts = the number of data points to create (must be between 10-50)
    data_type_str = the type of data to be created (random, squared, cubed)
    '''
    
    #ask user for number of data points
    num_pts_str = input("Please enter a the number of data points between 10-50 that you wish to create. ")
    num_pts = int(num_pts_str)
    if num_pts >50 or num_pts <10:
        num_pts_str = input("Error: please enter a number greater than 10 and lower than 50 ")
        num_pts = int(num_pts_str)
        
    #ask user for type of data
    data_type_str = input("Which type of data would you like to be created? Please enter either 'random' or 'squares' or 'cubes'. ")
    
    '''depending on the user's input, creates the corresponding
    data plot''' 
    if data_type_str.lower() == 'random':
        print("...creating random data plot...")
        x,y = create_random_data(num_pts)
        file = save_points(x, y, data_type_str)
        plot_points(x, y, data_type_str)
        
    elif data_type_str.lower() == 'squares':
        print("...creating squares data plot...")
        x,y = squared_data(num_pts)
        file = save_points(x, y, data_type_str)
        plot_points(x, y, data_type_str)
        
    elif data_type_str.lower() == 'cubes':
        print("...creating cubes data plot...")
        x,y = cubed_data(num_pts)
        file = save_points(x, y, data_type_str)
        plot_points(x, y, data_type_str)
        
    #checks to make sure the input is correct
    else:
        data_type_str = input("error, incorrect input, press enter to redo")
        main()
    
if __name__ == '__main__':
    main()
    
"""
recursion.py

This module contains two different recursion functions.
Introduction to Computer Science
Katharine Münger
March 2018
 
"""

def num_digits(num):
    """
    This function takes a single parameter, an integer num and returns an integer that is the number of digits in the number.
     """
    #convert the num to a string
    num_str = str(num)
    
    #remove negative sign
    if '-' in num_str: 
        num_str = num_str[1:]
        print('num_str without negative =   ', num_str)
    
    #base case -- num is one digit 
    if len(num_str) == 1:
        return 1
    
    else: 
        #remove first character from string
        num_str = num_str[1:]
        print("num_str is ", num_str)
        return 1 + num_digits(num_str)
    
def permutations(s):
    """
    This function takes a string s and return a list of all possible
    permutations of characters in the given string.
    """
    #empty permutations list to collect permutations
    perm_list = []
        
    #base case-- str will return in list
    if len(s) <= 1:
        return[s]
    
    else:
        #loop through each ch in str
        for idx in range(len(s)):      
            
            ch = s[idx]
            #new string without ch
            new_str = s[:idx] + s[1+idx:]

            #recursive call
            partials_list = permutations(new_str)
            for item in partials_list:
                perm_list.append(ch + item)           
        
        return perm_list
    
    
def main():
    """
    This will test out the two recursion functions.
    """
    
    #test out num_digits with 
    print('num_digits(0) should return 1')
    print('actual num_digits(0) =   ' , num_digits(0))
    print(' \n ')
    print('num_digits(2318) should return 4')
    print('actual num_digits(2318) =   ' , num_digits(2318))
    print('\n  ')
    print('num_digits(-67) should return 2')
    print('actual num_digits(-67) =   ' , num_digits(-67))
    print(' \n ')
    
    #test out permutations
    print("permutations('abc') should return ['abc’, ’acb’, ’bca’, ’bac’, ’cba’, ’cab’]")
    print("actual permutations('abc')" , permutations('abc'))
    print(' \n ')
    print("permutations('0') should return ['0']")
    print("actual permutations('0')" , permutations('0'))
    print('\n  ')
    
if __name__ == '__main__':  #this allows us to run our module from the command line
    main()  
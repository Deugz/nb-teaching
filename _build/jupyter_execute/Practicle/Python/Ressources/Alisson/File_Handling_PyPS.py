#!/usr/bin/env python
# coding: utf-8

# # Getting Started with Python - File input and output
# 
# Version 0.2 Aug 2020
# 
# This notebook explains how you can import data from external files into a Python program or write data from a program to a file. 
# 
# For this part, you will need to download the files `file_1.txt`, `file_2.txt` and `file_3.txt` from the Resources section of the course. These files should be saved to the same folder as this notebook.
# 
# [1. Importing data from a file](#Input)
# 
# [2. Writing data to a file](#Output)
# 
# [3. Formatting text](#Format)
# 
# [Answers to Exercises](#Exercise-Answers)
# 
# **FILE:** `File_Handling_PyPS.ipnyb`
# ***

# <a id="Input"></a> 
# ## 1. Importing data from a file

# We’ve already seen (in `Functions_PyPS.ipynb`) how we can get the user to input data from the keyboard. However, it is not very practical to do so when you want to input or output thousands of lines of data or long texts. To overcome this issue, Python provides a way to access the content of files.  
# 
# The first step is to use the `open()` function to tell Python the name of the file. This is done using a statement such as:

# In[1]:


file_input = open("file_1.txt", 'r')


# Here `"file_1.txt"` is the file you want the program to to access. Note that the file needs to be in the same folder as your Jupyter Notebook.
# 
# In addition, you need an instruction that describes how Python will be working with this file:
# 
# 1. `'r'` opens the file in reading mode. This reads data from an existing file.
# 1. `'w'` opens the file in writing mode. If the file already exists, then this mode overwrites the content of the existing file. If the file does not exist then it is created by the kernel.
# 1. `'a'` opens the file in append mode. Writing in this mode will add what you write at the end of the file.
# 
# Let's trying opening and reading the input file `file_1.txt`, assuming it is located in the same folder as this notebook. Run the following:

# In[2]:


file_input_1 = open("file_1.txt", 'r')

content = file_input_1.read()
print(content)

file_input_1.close()


# In the above code cell, the file is opened under the name `file_input_1`. Then the file content is read using `read()` and stored as a string variable called `content`. The very last line of the program tidies things up by closing the file using `close()`.
# 
# In fact, `file_input_1` is what is called a *file object*. This file object can be given any name providing it follows the usual rules for naming variables. 
# 
# Note especially the way in which `read()` is called here - it is connected with a `.` to the name of the file object.  You need to be aware that in handling files, we often use special functions that are called by connecting them to name of the file object in this way (you can see that `close()` also follows this pattern). We won't say much more about this except to note that that `read()` and `close()` are more properly described as a **methods** rather than functions and we will use this terminology in what follows. 
# 
# Often we want to read files one line at a time and it is possible to do this with the `readline()` method. This instruction only reads one line at the time and repeating it will read the following line. Try running the following example:

# In[3]:


file_input_1 = open("file_1.txt", 'r')

first_line = file_input_1.readline()
print("The first line is:", first_line)

second_line = file_input_1.readline()
print("The second line is:", second_line)

file_input_1.close()


# It is also possible to use a `for` loop to iterate over the lines of a file using  `for line in (file_object):`
# 
# For example:

# In[4]:


file_input_1 = open("file_1.txt", 'r')

for line in file_input_1:
    print(line)
    
file_input_1.close()


# Lines that are extracted this way are a sequence of single strings. You will often find that you need to manipulate such strings to get at the data you want to work with, so let us show you some properties of strings and one useful method that works on `str` variables (i.e. a string method):
# 
# If `string` is a `str` type variable, then:
# 
# 1. `string[k]` is the k-th element of `string`,  i.e. the character in the k-th position. Remember that in Python, counting starts at 0.
# 1. `string[i:j]` is the part of the `string` from the i-th to the j-th characters.
# 1. `string.split('divider')`: this method allows you to divide `string` into multiple strings using the `divider` ; e.g. dividing a string using `' '` (which is the default value) would divide a phrase into words. This method returns a list of strings containing all the words in the phrase.
# 
# Let us illustrate these by running a short example:

# In[5]:


string_1 = "This is an example of a string."

print("The zero-th element of the string is:", string_1[0])

print("The 5-th element of the string is:", string_1[5])

print("The 5-th to 15-th elements of the string are:", string_1[5:15])

string_cut = string_1.split(' ')

print("The list of words in the string is:", string_cut)

print("The 4-th word of the string is:", string_cut[4])


# Let's practice file input and string handling with an exercise:

# <a id="Exercise1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
#     
# In the following code cell, write a program that will load the file `file_2.txt`. The content of this file is:
# 
# ***
# Apples 5
# 
# Pears 19
# 
# Oranges 32
# 
# Pineapples 2
# 
# Blackberries 45
# ***
# The program should read the file and print the total number of items of fruit.
# 
# </div>

# In[6]:


# Code for Exercise 1.1
# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers1.1)

# ### Importing data from a file - summary 
# 
# In this part, you learned how to load a file in Python and you saw how to read it either in its entirety or line by line.
# You saw that methods are types of functions that apply to entities (such as file objects or strings). You also gained experience in working with strings and saw how to extract data from a string that you can work with in a program.
# ***

# <a id="Output"></a> 
# ## 2. Writing data to a file

# Often, you will find it useful to store some data that your Python program has produced. Saving data in an external file allows it to be used at a later time. Python allows you to write to a text file in a way that is similar to the process of reading data.
# 
# The first step is to open the file, but this time in a *write* mode:

# In[7]:


file_output = open("output.txt", 'w')


# This will create a file named `output.txt` in the folder you are working in (likely to be the folder where is located this Notebook). Of course, you can chose any valid name for the file; however, we strongly recommend avoiding the use of spaces or any other special characters except underscores (`_`), dashes (`-`), and full stops `.`. As for opening files for reading, note that within the program, a new file object (called `file_output` in this example) is created and this file object can have any name that meets the rules of naming variables in Python. 
# 
# The second step is to write to the file with a method called `write()`. Note that this method can only take an input that is a string.
# 
# Let us try writing a few words in a new file by running the following:

# In[8]:


# Open a new file in write mode
file_output_2 = open("output_2.txt", 'w')

# A string to be written to file
text_1 = "example text to write in the file"

# Write this to file
file_output_2.write(text_1)

# Another string to be written to file
text_2 = "other text to write"

# Write this to file
file_output_2.write(text_2)

# Close the output file
file_output_2.close()


# Executing this cell has created a new file named `output_2.txt` in your folder. 
# 
# Look for this file now and inspect its contents (in Windows File Explorer, double clicking on this file should open it using the Notepad application). Is the content of the file exactly as you expect? 
# 
# You'll see that the program has written the two strings, one immediately after the other, like this:
# 
# `example text to write in the fileother text to write`
# 
# You might have been expecting there to be a separate line for each string, but this does not happen automatically - if you want a new line after a string is output, you have to explicity state this using using the special character `'\n'` (note that although it looks like this the two characters `'\'` and `'n'`, it is interpreted by Python as a single special character called *newline*).
# 
# Another special character is ``\t`` that is used to indicate a `Tab` separation. This can be useful in producing formatted output. 
# 
# For example, try running the following code cell:

# In[9]:


# A string to be written to file
text_1 = "example text to write in the file"

# Another string to be written to file
text_2 = "other text to write"

# A new string that combines these with an intervening tab 
tab_separation = text_1 + '\t' + text_2

print(tab_separation)

# A new string that combines these with an intervening newline
new_line = text_1 + '\n' + text_2

print(new_line)


# Usually, when writing to a file, you will want to write it line by line.  First put all the output information for each line in a string, then end it with a final `'\n'` before writing it with the `write()` method.

# <a id="Exercise2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
#     
# Copy and paste the code you wrote for Exercise 1.1 and modify it so that it creates a new file named `output_exercise_2.1.txt`. This output file should contain in each line the name of the fruit, the number of items of this fruit, and the cumulative sum at that point (i.e. the sum of the number of items of fruit from this and all previous lines). All these should be Tabulation or space separated.
# 
# Your program should return a file like:
# 
# ***
# Apples 5    5
# 
# Pears 19    24
# 
# Oranges 32    56
# 
# Pineapples 2    58
# 
# Blackberries 45    103
# ***
# 
# </div>

# In[10]:


# Code for Exercise 2.1
# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers2.1)

# ### Writing data to a file - summary 
# 
# In this part, you learned how a file can be created with Python and how you can write text to it. 
# 
# Now it is time to see how you can change how numbers and words are written so that you can modify the way they are printed.
# ***

# <a id="Format"></a> 
# ## 3. Formatting text

# Computers can handle numerical calculations with ease, but making it readable to humans takes a little thought and care.
# 
# Take this example – this program calculates the square root of 2.0 and prints it out. This example uses the `sqrt()` function, which is part of the `math` package. We must import the `math` package first, before we can use it.
# 
# Run the following to see how the number is output:

# In[11]:


# Printing numerical values
import math     # this is needed for the sqrt() function

x = math.sqrt(2.0) # calculate the square root of 2.0

print(x)


# You will find that the result is printed out with a long string of decimal places: 1.4142135623730951
# 
# Fortunately, the print() function allows us to control the precision displayed. This is of course important when dealing with scientific data as we want to display the values to the correct number of significant figures.
# 
# Try this:

# In[12]:


# Formatting printout
import math     # this is needed for the sqrt() function

x = math.sqrt(2.0) # calculate the square root of 2.0

print("%.2f" % x)


# This time, the result is printed with just two decimal places: 1.41.
# 
# In this example, the `%.2f` is a format specifier that says that we want to print a floating point value with two decimal places. The second % sign separates this format specifier from the variable whose value we want to print (i.e. `x`).
# 
# To control the number of significant figures rather than decimal places, we use the format `%.2g`. 
# 
# This will print the result to two significant figures 1.4. (Try it.)
# 
# Another way of controlling what is printed or written to a file is to create strings that are formatted in the way we want before they are output. To do this we use a string method called `format`. 
# 
# Let's have a look at how this works. Run the following:

# In[13]:


name = "Julius"
age = 21
city = "Singapore"

sentence_to_print = "My name is {0}, I live in {1} and I am {2} years old.".format(name, city, age)

print(sentence_to_print)


# Here we have used the `format()` method to insert the content of three variables (`name`, `city` and `age`)) into the string (`sentence_to_print`) that is printed by the kernel. Note how the position is denoted by curly braces (`{ }`), and that `{0}` is where the first variable (`name`) is inserted. 
# 
# You can specify how numbers are written by combining this with the formatting instruction you saw previously. For example if the variable at position `{2}` is to be written as a floating point number with one decimal place, we would replace `{2}` with `{2:.1f}`.
#  
# Have a look at the example below where the same number is printed but with different formatting instructions. Note that the numbers is rounded appropriately (rather than being truncated).

# In[14]:


number = 3.5902756829385638292384

print("Here is the number given to 5 decimal places : {0:.5f}".format(number))

print("Here is the number to 7 significant figures : {0:.7g}".format(number))


# Let us finish with a concluding exercise for you to practice this last point.

# <a id="Exercise3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# 
# File `file_3.txt` lists the planets in the solar system and the semi-major axes of their orbits (in metres). 
# 
# Write a program that calculates the orbital period (in seconds) for each planet. 
# 
# To find the orbital period $P$ you will need to use Kepler's third law, which can be written as:
# 
# $P^2 = K d^3$
# 
# where $P$ is the period in seconds and $d$ the semi-major axis of the planetary orbit in metres.
# 
# The constant $K$ has a value of $2.97 \times 10^{-19} \text{ s}^2 \text{ m}^{-3}$
# 
# The program should output a file which gives the name of each planet, its semi-major axis and the relevant orbital period (in seconds) to three significant figures.
# ***
# Note that the content of `file_3.txt`  is: 
# ***
# Mercury   5.79e10
# 
# Venus   1.08e11
# 
# Earth   1.50e11
# 
# Mars   2.28e11
# 
# Jupiter   7.79e11
# 
# Saturn   1.43e12
# 
# Uranus   2.87e12
# 
# Neptune   4.50e12
# ***
# 

# In[15]:


# Code for Exercise 3.1
# Type your code here


# You should attempt this exercise *before* looking at the [Exercise Answers](#ExerciseAnswers3.1)

# ### Formatting text - summary 
# 
# In this section you have seen some of the ways that you can control the format of text that is written to a file. Specifically, you have seen how to control the format of how variables are written to a string. This string can then be output (printed or written to a file).  
# 
# There are many more aspects to formatting strings, but the examples you have seen here will allow you to have some control over how to store and display numerical data from your Python programs.  
# ***

# <a id="Exercise-Answers"></a> 
# ## Exercises - Answers

# <a id="ExerciseAnswers1.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 1.1</b> <br> 
# 
# Have a look at the following example answer. You can check that your code is fine by calculating the sum of fruits yourself and compare to what the program gives.
# </div>

# In[16]:


# Code for Exercise 1.1
# First we load the file, assuming it is located in the same folder as this notebook
file_2 = open("file_2.txt", 'r')

# Initialise the total number of fruits
number_of_fruits = 0

# Then we loop on all the lines of the file
for line in file_2:
    
    # Then we divide the line into words    
    line_split = line.split(' ')

    # Take the second word and converting it into an integer
    number_in_line = int(line_split[1])
    
    # Add this number to the total number of fruits
    number_of_fruits = number_of_fruits + number_in_line
    
# Now close the file
file_2.close()
    
# Print the answer
print("The total number of items of fruit is:", number_of_fruits)


# [Back to Exercise 1.1](#Exercise1.1)

# <a id="ExerciseAnswers2.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 2.1</b> <br> 
# 
# Have a look at the following example answer. 
# </div>

# In[17]:


# Code for Exercise 2.1
# First we load the file, assuming it is located in the same folder as this notebook
file_2 = open("file_2.txt", 'r')

# Then we create the output file
output_file = open("output_exercise_2.1.txt", 'w')

# Initialise the total number of items of fruit
number_of_fruits = 0

# Then we loop on all the lines of the file
for line in file_2:
    
    # Then we divide the line into words 
    line_split = line.split(' ')

    # Take the second word and convert it into an integer
    number_in_line = int(line_split[1])
    
    # Add this number to the total number of fruits
    number_of_fruits = number_of_fruits + number_in_line
    
    # Prepare the line we are going to write. First the name of the fruit, first element of line_split
    # then the number_in_line converted in string, then the number_of_fruits converted in string
    # then the newline statement '\n'
    
    line_to_write = line_split[0] + '\t' + str(number_in_line) + '\t' + str(number_of_fruits) + '\n'
    
    output_file.write(line_to_write)
    
# Close the files
file_2.close()
output_file.close()


# [Back to Exercise 2.1](#Exercise2.1)

# <a id="ExerciseAnswers3.1"></a>
# <div class="alert alert-block alert-info">
# <b>Exercise 3.1</b> <br> 
# 
# Have a look at the following example answer. 
# </div>

# In[18]:


from math import sqrt

# First we load the file, assuming it is located in the same folder as this notebook

file_3 = open("file_3.txt", 'r')

# Then we create the output file

output_file = open("planetary_d_P.txt", 'w')

# Then we loop on all the lines of the file

for line in file_3:
    
    # Then we divide the line in words
    
    line_split = line.split(' ')

    # Then we take the second word and convert it into a float
    
    semi_major_axis = float(line_split[1])
    
    # Then we calculate the orbital period using Kepler's third law
    
    orbital_period = sqrt(2.97e-19*(semi_major_axis**3))
    
    # Then we prepare the line we are going to write ; name of the planet, semi-major axis and orbital period and end of line
    
    line_to_write = line_split[0] + '\t' + '{0:.3g}'.format(semi_major_axis) + '\t' + '{0:.3g}'.format(orbital_period)+ '\n'
    
    output_file.write(line_to_write)
    
file_3.close()
output_file.close()


# [Back to Exercise 3.1](#Exercise3.1)

# Labster

这是一个对中国的大学物理实验（尤其是DUTers）进行数据处理的小东西. 
This is a little program that to deal with data anaylsis in college Physics in China (especially for DUTers in Panjin campus).
Currently, this program is based on 'pylatex' to generate a LaTeX report and 'sympy to do symbolic calculation. 

## Getting Started

### Prerequisites

*This project is written in python.* To use this program, your computer needs to have 'python 3.8' or higher version; alternatively, 'Anaconda 3' or higher version is also agreeable. Your computer should also have installed the following packages:
'''
- 'pylatex'
- 'sympy'
- 'numpy'.
'''

### Using
First you need to download all '.py' files in the same folder, then execute labster.py and follow the instruction in GUI. 
You need to check if the final formate of report is what your university required.
The template 'database.csv' can be used to generate a template report and so you can check if the rounding method is used in your university. In practise, you can add as much as data rows you need. For the function, you need to write a function as a string. For example, if the function for the final is 

$$\frac{4m}{\pi d^2 h}$$

then you need to write 

'''
(4*m)/(pi*(d**2)*h)
'''

## About Authors & Others
This is just a product of a whim of a Math student so don't execpt too much ~ 
And there may be some bugs when the data are all in type of int, I'm now trying to fix these bugs.
In the near future I hope I can add an image recognition module in the project to actualize the automatic handwritting-data reading function, if, of course, I have enough time and fully understand group theory.

## License
 
This project is licensed under the Apache 2.0 License

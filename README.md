# Labster

这是一个对中国的大学物理实验（尤其是DUTers）进行数据处理的小东西. 
This is a little program that to deal with data anaylsis in college Physics in China (especially for DUTers in Panjin campus).
Currently, this program is based on `pylatex` to generate a LaTeX report and `sympy` to do symbolic calculation. 

## Getting Started

### Prerequisites

*This project is written in python.* To use this program, your computer needs to have `python 3.8` or higher version; alternatively, `Anaconda 3` or higher version is also agreeable. Your computer should also have installed the following packages:

- `pylatex`
- `sympy`
- `numpy`.


### Using
To begin, please follow these steps:

1. Download all `.py` files and place them in the same folder.
2. Execute `labster.py`.
3. Follow the instructions provided in the Graphical User Interface (GUI).

Ensure that the final report format complies with your university's requirements. You can use the 'database.csv' template to generate a sample report and verify if it adheres to your university's rounding methods. In practice, you can add as many data rows as needed.

When defining your function, it should be written as a string. For example, if your final function is represented as:

$\frac{4m}{\pi d^2 h}$ 

You should express it in the code as a string, like this:

```
"4m / (pi * d**2 * h)"
```

This will ensure that your function is correctly processed within the program.
## About Authors & Others
This is just a product of a whim of a Math student so don't execpt too much ~ 
And there may be some bugs when the data are all in type of int, I'm now trying to fix these bugs.
In the near future I hope I can add an image recognition module in the project to actualize the automatic handwritting-data reading function, if, of course, I have enough time and fully understand group theory.

## License
 
This project is licensed under the Apache 2.0 License 

# Labster

这是一个对中国的大学物理实验（尤其是DUTers）进行数据处理的小东西. 
This is a project designed for handling data analysis in college Physics in China, with a specific focus on Dalian University of Technology (DUT).
Currently, the program relies on the `pylatex`  for generating LaTeX reports and `sympy` for performing symbolic calculations.

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

## License
 
This project is licensed under the Apache 2.0 License 

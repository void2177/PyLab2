## **Lab 2: Python Variables, Statements, and Expressions**

### **Introduction**
In this lab, you'll explore the fundamental building blocks of Python: variables, statements, and expressions. By the end, you'll have a solid understanding of how to create variables, write statements, and perform calculations using expressions.

### **Objectives**

* Understand the concept of variables and how to assign values to them.
* Learn to use basic arithmetic operators and write expressions.
* Recognize the difference between expressions and statements.
* Explore the `print` function for displaying output.
* Practice using the `import` statement to access modules and their functions.

### **Part 1: Variables and Assignments**

1. **Create variables:** 
   * Create a new file named lab02.py and assign the following values to variables within it:
     * `name` = "Your Name"
     * `age` = 20 (or your actual age)
     * `height` = 5.7 (or your actual height in feet)
     * `favorite_color` = "Blue" (or your favorite color)
2. **Printing Techniques for variable values:**
   * **1. Print one variable at a time:**
       * Print the value of each variable individually using separate `print` statements.
   * **2. Print with one `print` statement and commas:**
       * Print the values of all variables in a single `print` statement, separating them with commas.
       * Does it add a space between the variables?
   * **3. Print with Python formats or format specifiers:**
       * Use Python's string formatting capabilities to print the variables in a more structured way.
       * Here's an example with only 2 of your variables.:
         ```python
         print(f"Hello: {name} my is {favorite_color}!")
         ```
       * Note the **"f"** at the beginning of the string tells Python to "format"
       * Try different format specifiers to control the output (e.g., `{:d}` for integers, `{:f}` for floats).
           * Interact with your friendly AI chatbot of choice to get some examples of how to do this, and add statements to your code.
   * **4. Print with format specifiers within a multi-line string:**
       * A multi-line string is a string that spans multiple lines. It is defined using triple quotes (`"""`).
       * Use format specifiers within a multi-line string to create a formatted output.
       * Here's an example with 2 of the variables you previously defined, you need to include them all:
         ```python
         print(f"""
         Name: {name}
         Age: {age}
         """)
         ```
       * Test what happens if you add extra spaces at the beginning of the lines of multi-line strings?
3. **Create a new variable:**
   * Similar to last week, calculate the area of a circle with a radius of 5, but this time store the result in a variable named `circle_area`.
   * Print the value of `circle_area` to ONLY 1 decimal place.

### **Part 2: Statements and Modules**

1. **Import the `math` module:**
    * Use the `import` statement to import the `math` module.
2. **Calculate the square root:**
    * Use the `sqrt` function from the `math` module to calculate the square root of `age`.
    * Print the result.
3. **Calculate the sine and cosine:**
    * Use the `sin` and `cos` functions from the `math` module to calculate the sine and cosine of `height`.
    * Print the results.

### **Part 3: Expressions and Operators**

1. **Arithmetic operations:**
   * Use arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`) to perform calculations.
   * Calculate the following:
     * The sum of `age` and 5.
     * The difference between `height` and 4.
     * The product of `age` and `height`.
     * The quotient of `height` and 2.
     * The remainder of `age` divided by 3.
     * `age` raised to the power of 2.
2. **Print the results:**
   * Use `print` to display the results of each calculation. Choose your preferred print formatting from the previous exercise.

### **Part 4: Temperature Conversion**
1. **Create a temperature conversion program:**
   * Write a program that converts Fahrenheit to Celsius.
   * Prompt the user to enter a temperature in Fahrenheit.
       * HINT: the `input` function will be necessary, and it takes the **prompt** string as the first argument.
   * Convert the temperature to Celsius using the formula: `Celsius = (Fahrenheit - 32) * 5/9`.
   * Print the converted temperature and see if you can print the **degree** symbol.

#### Part 5: Pushing to GitHub
1. **Create a GitHub Repository:**
   * Log in to your GitHub account.
   * Create a new repository with a suitable name (e.g., "python_lab2").
2. **Configure Git in PyCharm:**
   * Open the "Git" menu in PyCharm and initialize a Git repository for your project.
   * Add your GitHub remote repository by going to "Git" -> "Manage Remotes".
3. **Commit Changes:**
   * Stage all changes in your PyCharm project.
   * Commit the changes with a descriptive message (e.g., "Initial commit").
4. **Push to GitHub:**
   * Push the committed changes to your GitHub repository using the "Push" button in PyCharm.

### Submission
Submit the link to your GitHub repository containing the `lab02.py` file to the Canvas Lab!

### **Additional Notes**
* Remember to use proper indentation to organize your code.
* If you encounter errors, carefully read the error messages for clues.
* Experiment with different operators and functions to explore Python's capabilities.
* Use comments to explain your code and make it easier to understand.
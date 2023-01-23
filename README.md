# Introduction
Welcome to the README for the ARQSOFT project, a simple Spreadsheet management software system developed as part of the Master's subject Software Architechture.  

In this document, you will find information about the project's dependencies, the process and tools used for version management, communication, and task management within the team, as well as an overview of the updated documents stored in the "updated_assignments" folder.  

Additionally, this README includes a brief explanation of how Jupyter notebooks were utilized throughout the course.
## Libraries that have to be insalled:
In order to run our code, you will need to install this package:
- Pandas: We have used pandas in order to make more easier the implementation of cells on a spreadsheet 
install by using the following command on the terminal:   
``pip install pandas``


## Version management with GitHub

During the development of this project, we used GitHub as our version management system. GitHub is a web-based platform that provides hosting for software development and version control using Git. It allows developers to collaborate and contribute to a project by sharing and managing code in a centralized repository.

GitHub provides a number of features that made it an ideal choice for managing the development of this project. One of the key features is the ability to track changes to the code over time, allowing us to easily revert to previous versions if needed.

GitHub's powerful version control and collaboration features made it an essential tool for managing the development of this project, allowing us to work efficiently, organize our code and keep track of progress and changes.

You can check our repository page [here](https://github.com/sergi24sanchez/theSpreadsheet).

## Updated Assignments
In the "latest_assignment" folder, you will find a "Design Class Diagram UML" document.

The "Design Class Diagram UML" document has undergone some changes, with the current state to be a representation of how the code is programmed.


# Running the code

- For the testing script, simply execute the file called "TestsRunner.py" located in the root folder of the project.

    ``python TestsRunner.py``

- For the User Interface, execute the file called "main.py".

    ``python main.py``


# Tests Score
As of the time of delivering the code, the TestsRunner.py file should give this score. 

```
- Nota en clase TextContentTest: 10.00 (Porcentaje en nota final: 1.5%). Contribucion a nota final: 0.15
- Nota en clase NumberContentTest: 10.00 (Porcentaje en nota final: 1.5%). Contribucion a nota final: 0.15
- Nota en clase FormulaContentTest: 10.00 (Porcentaje en nota final: 64.5%). Contribucion a nota final: 6.45
- Nota en clase DependentCellsTest: 10.00 (Porcentaje en nota final: 12.5%). Contribucion a nota final: 1.25
- Nota en clase CircularDependenciesTest: 4.00 (Porcentaje en nota final: 7.5%). Contribucion a nota final: 0.30
- Nota en clase SaveTest: 6.27 (Porcentaje en nota final: 5%). Contribucion a nota final: 0.31
- Nota en clase LoadTest: 0.00 (Porcentaje en nota final: 5%). Contribucion a nota final: 0.00

- NOTA FINAL DE CORRECCIÓN AUTOMÁTICA: 8.61
```

If the score is different, please contact us.

# Known issues:
- We assume that the input will always be a string (since that is what the UI gave us). Later in the code this string is the one that will be converted to Numerical, Text or Formula. There is a comment in the file Spreadsheet_checker.py in the function set_cell_content(coord, str_content) of the class SpreadsheetChecker() that explains this.

- We noticed while doing the latest tests that if a cell is referenced before giving it a content and a value, it does not work. When having formulas that have dependencies, this dependencies must have a content already and its correspondent value. Is for this motive that the LoadTextTest is not working.

- Also when saving a spreadsheet we have ';' that indicate cells that are empty even after the last content introduced in the row. And also we have them if a row is completly empty. This is due a missunderstanding of the directions given in the first .pdf We assumed that the ';' indicated change of cell. this creates issues in the save test.
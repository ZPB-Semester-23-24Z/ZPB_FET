# Parameterization of the FET transistor

## Info
A repository containing scripts for determining the basic parameters of a FET transistor.

## Directory structure

* **src**  - Source Code folder
    * **Module_1** - Code for module_1
* **tests**- Tests folder
    * **Module_test_1** - Tests for module_1
* **configs** - Config File folder
* **doc**  - Documentation of project
* **res**  - Resources 
* **venv** - Virtual Enviroment Python

## Tutorials
This chapter contains rules and small tutorials

### Coding
It does not define any coding style. But... there are some rules

#### Rules
1. **Use comments**
    * for function:
        ```python
            def test_function(p1, p2, p3):
            """
            test_function does blah blah blah.

            :param p1: describe about parameter p1
            :param p2: describe about parameter p2
            :param p3: describe about parameter p3
            :return: describe what it returns
            """ 
            pass
        ```
    * for code blocks:
        ```python
             """Create a new user.
            Line 2 of comment...
            And so on... 
            """
        ```
    * for one spectial line:
        ```python
            # Make a spell (turn a Mother of your Friend into a Car)
            do_magic(spell = "Hokus Pokus Your Mother are Ford Focus!")
        ```
2. Sign the files
    * At the begin of the file:
        ```python
        __title__       = "README.md"                                                               # filen/module name
        __author__      = "Konrad Domian, Marcin Władziński, Karol Kosowski, Maciej Mikulski"       # all of us
        __copyright__   = "Copyright 2023, ZPB - Parameterization of the FET transistor team"       # copyrights
        __license__     = "for internal use only"                                                   # licence
        __version__     = "1.0.0"                                                                   # version (can be a date)
        __maintainer__  = "Konrad Domian"                                                           # Who works at that specifc file
        __status__      = "Production
        ```


### Using Virtual Enviroment Python
**shortcut**:Using Virtual Enviroment Python allows you to eliminate errors like "it works for me".

The python virtual environment is a set of previously installed libraries. This means we always have the same versions of the libraries and the same version of python. This completely eliminates the version incompatibility problem

#### Rules:
1. Before any work on the repository, you always activate the virtual environment
    * Good Tutorial: https://realpython.com/python-virtual-environments-a-primer/
2. If you need any libraries, install them using pip. And add it with version to requirement.txt
     * Example requirement.txt file:
     ```python
        package_name1 == version1
        package_name2 == version2
     ```

#### How use Virtual Enviroment Python

##### Active VENV
``` python
.\venv\Scripts\activate
```
##### Dezactive VENV
``` python
deactivate
```
##### Install new package
**Do it after Active VENV**
``` python
python -m pip install <package-name>
```


### Wrinting Tests
I Know writing tests seems pointless. But they really save a lot of time on debugging

Tests are **run automatically** after **committing** to the repository. If they end in failure, you will receive an e-mail telling you what happened

#### Rules:
1. Each module should be tested. 
2. Tests should be placed in the tests folder.
3. Each module should have a separate test file. **(1 module file = 1 test file)**
3. Tests should at least cover 90% of the code. (CodeCover)
    * We test functionalities, **NOT CODE!**
4. We use the pytest library to write tests.
    * Project WebPage: https://docs.pytest.org/en/7.4.x/
    * Good Tutorial: https://blog.qalabs.pl/pytest/pytest-pierwsze-kroki/
    * Example code :
        ``` python
        import pytest
        import random
        import calculator

        @pytest.fixture
        def numbers():
            return (random.randint(1, 10), random.randint(1, 10), random.random.randint(1, 10))

        def test_addition(numbers):
            assert calculator.add(numbers[0], numbers[1]) == numbers[0] + numbers[1]
            assert calculator.add(numbers[2], numbers[1]) == numbers[2] + numbers[1]
            assert calculator.add(numbers[2], numbers[2]) == numbers[2] + numbers[2]

        def test_subtraction(numbers):
            assert calculator.subtract(numbers[0], numbers[1]) == numbers[0] - numbers[1]
            assert calculator.subtract(numbers[2], numbers[1]) == numbers[2] - numbers[1]
            assert calculator.subtract(numbers[2], numbers[2]) == numbers[2] - numbers[2]

        def test_multiplication(numbers):
            assert calculator.multiply(numbers[0], numbers[1]) == numbers[0] * numbers[1]
            assert calculator.multiply(numbers[2], numbers[1]) == numbers[2] * numbers[1]
            assert calculator.multiply(numbers[2], numbers[2]) == numbers[2] * numbers[1]

        def test_division(numbers):
            assert calculator.divide(numbers[0], numbers[1]) == numbers[0]/numbers[1]
            assert calculator.divide(numbers[1], numbers[0]) == numbers[1]/numbers[0]
            assert calculator.divide(numbers[2], numbers[1]) == numbers[2]/numbers[1]

            # Test division by zero
            with pytest.raises(ZeroDivisionError):
                calculator.divide(numbers[2], 0)
        ```

#### HOW USE pytest?
##### run all tests
``` python
python -m pytest
```
#### Run Specific Test
``` python
pytest tests/test_file.py
```
##### Show CodeCoverage raports and print to HTML
``` python
pytest --cov --cov-report=html:coverage_re
```

### Recoment Tools

#### Consol Emulator CMDER (when u use windows)
**Link**: https://cmder.app/

#### Good IDEs
Pycharm:
**Link**: https://www.jetbrains.com/pycharm/download/

VsCode:
**Link**: https://code.visualstudio.com/download

### **Warmings!**
Remember that we use Github, so for political correctness the **Master** branch is called **Main**

Modify: 30.11.2023r by KD

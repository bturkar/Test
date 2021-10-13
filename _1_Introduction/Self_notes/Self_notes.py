"""
***********************INTRODUCTION OF PYTHON************************
------------------------------------------------------------------------------------------------------
How interpreter works in python.
 -Process the statements of your script in a sequential fashion
 -Compile the source code to an intermediate format known as bytecode.
      This bytecode is a translation of the code into a lower-level language that’s platform-independent.
      Its purpose is to optimize code execution. So, the next time the interpreter runs your code, it’ll
      bypass this compilation step.
      Strictly speaking, this code optimization is only for modules (imported files), not for executable scripts.
 -Ship off the code for execution
      At this point, something known as a Python Virtual Machine (PVM) comes into action.
      The PVM is the runtime engine of Python. It is a cycle that iterates over the instructions of your
      bytecode to run them one by one.
      The PVM is not an isolated component of Python. It’s just part of the Python system you’ve installed on your
      machine.
      Technically, the PVM is the last step of what is called the Python interpreter.
------------------------------------------------------------------------------------------------------------
Python features
  1. Easy Language
    -Easy to read, write, learn and understand.
    -simple syntax and easy to understand.
  2. Readable
    -Reading a Python code is like reading an English, best for beginners.
    -uses indentation instead of curly braces, unlike other programming languages. This makes the code look
    clean and easier to understand.
  3. Interpreted Language
    -It comes with the IDLE (Interactive Development Environment).
    -This is an interpreter and follows the REPL structure (Read-Evaluate-Print-Loop).
    -It executes and displays the output of one line at a time.
    -So it displays errors while you’re running a line and displays the entire stack trace for the error.
  4. Dynamically-Typed Language
    -You don’t need to declare data type while defining a variable.
    -The interpreter determines this at runtime based on the types of the parts of the expression.
    -This is easy for programmers but can create runtime errors.
    -Python follows duck-typing. It means, “If it looks like a duck, swims like a duck and quacks like a duck,
     it must be a duck.”
  5. Object-Oriented
    -Object-oriented but supports both functional and object-oriented programming.
    -Everything in Python is an object.
    -It has the OOP (Object-oriented programming) concepts like inheritance and polymorphism.
  6. Popular and Large Community Support
    -Python has one of the largest communities on StackOverflow and Meetup.
    -If you need help, the community will answer your questions.
  7. Open-Source
    -It is free and its source code
  8. Large Standard Library
    -Standard library is large and has many packages and modules with common and important functionality.
    -If you need something that is available in this standard library, you don’t need to write it from scratch.
    -Because of this, you can focus on more important things.
    -You can also install packages from the PyPI (Python Package Index) if you want even more functionality.
  9. Platform-Independent
    -If you write a program, it will run on different platforms like Windows, Mac and Linux.
    -You don’t need to write them separately for each platform.
  10. Extensible and Embeddable
    -Extensible. You can use code from other languages like C++ in your Python code.
    -Embeddable. You can embed your Python code in other languages like C++.
  11. GUI Support
    -You can use Python to create GUI (Graphical User Interfaces).
    -You can use tkinter, PyQt, wxPython or Pyside for this.
  12. High-level Language
    -Python is a high-level language and C++ is mid-level.
    -It is easy to understand and closer to the user.
    -You don’t need to remember system architecture or manage the memory.
--------------------------------------------------------------------------------------------------------

3.Interpreter CPython IronPython Jython
  -Cpython
    The default implementation of the Python programming language is Cpython. As the name suggests Cpython is written
    in C language. Cpython compiles the python source code into intermediate bytecode, which is executed by the Cpython
    virtual machine. CPython is distributed with a large standard library written in a mixture of C and Python.
    CPython provides the highest level of compatibility with Python packages and C extension modules.
    All versions of the Python language are implemented in C because CPython is the reference implementation.
  -IronPython
    A Python implementation written in C# targeting Microsoft’s .NET framework. Similar to Jython, it uses Net Virtual
    Machine i.e Common Language Runtime. IronPython can use the .NET Framework and Python libraries, and other .NET
    languages can use Python code very efficiently. IronPython performs better in Python programs that use threads
    or multiple cores, as it has a JIT, and also because it does not have the Global Interpreter Lock.
  -Jython
    Jython is an implementation of the Python programming language that can run on the Java platform.
    Jython programs use Java classes instead of Python modules .Jython compiles into Java byte code, which can then
    be run by Java virtual machine. Jython enables the use of Java class library functions from the Python program.
    Jython is slow as compared to Cpython and lacks compatibility with CPython libraries.
  -Pypy
    “If you want your code to run faster, you should probably just use PyPy.” — Guido van Rossum (creator of Python)
    Python is dynamic programming language. Python is said to be slow as the default CPython implementation compiles
    the python source code in bytecode which is slow as compared to machine code(native code). Here PyPy comes in.
    PyPy is an implementation of the Python programming language written in Python. The Interpreter is written in
    RPython (a subset of Python).
---------------------------------------------------------------------------------------------------------
4.Dynamically typed programming language-Answered in feature(above).
---------------------------------------------------------------------------------------------------------
5.Procedure Oriented vs Object oriented programming languages   Answered below
---------------------------------------------------------------------------------------------------------
6.Setting path in python. Importance
  -The Path variable lists the directories that will be searched for executables when you type
   a command in the command prompt. By adding the path to the Python executable, you will be able
   to access python.exe by typing the python keyword (you won't need to specify the full path to the program).
  -PATH is an environment variable on Unix-like operating systems, DOS, OS/2, and Microsoft Windows,
   specifying a set of directories where executable programs are located.The PATH variable prevents us from
   having to write out the entire path to a program on the CLI every time we run it.
---------------------------------------------------------------------------------------------------------
7.Environment variables importance in python
 -Environment variables help programs know what directory to install files in, where to store temporary files,and
  where to find user profile settings. They help shape the environment that the programs on your computer use to run.
 -PYTHONPATH, PYTHONHOME, PYTHONSTARTUP, PYTHONINSPECT, PYTHONCASEOK, PYTHONVERBOSE
---------------------------------------------------------------------------------------------------------
8.Different ways to run python program
  -Interactive Mode.
  -Command Line.
  -Text Editor (VS Code)
  -IDE (PyCharm)
---------------------------------------------------------------------------------------------------------
9.source file
  -Python source files are files that contain Python source code.
  -As Python can be used as a scripting language, Python source files can be considered as scripts.
  -A source program is a text file that contains instructions written in a high level language.
  -It can not be executed (made to run) by a processor without some additional steps.
---------------------------------------------------------------------------------------------------------
10.compiler
  -The compiler is a special program that is written in a specific programming language to convert the human-readable
   language i.e. high-level language to machine-readable language i.e. low-level language.
---------------------------------------------------------------------------------------------------------
11.interpreter
  -An interpreter is a kind of program that executes other programs. When you write Python programs ,
   it converts source code written by the developer into intermediate language which is again translated
   into the native language / machine language that is executed.
  -The Python interpreter is a bytecode interpreter: its input is instruction sets called bytecode.
  -translates code into machine code.
  -Interpreters interpret verbal communication from one language to another, and act as mediums where
   language barriers exist.
---------------------------------------------------------------------------------------------------------
12.interpreted* programming language -answered in feature(above)
---------------------------------------------------------------------------------------------------------
13.cpython vs ironpython vs jython: Answered above
---------------------------------------------------------------------------------------------------------
14.interactive
  -A programming language designed to operate in an environment in which the user and computer
   communicate as transactions are being processed.
  -Python is Interactive − You can actually sit at a Python prompt and interact with the interpreter
   directly to write your programs.
  -Interactive mode is a command line shell which gives immediate feedback for each statement,
   while running previously fed statements in active memory.
---------------------------------------------------------------------------------------------------------
15.object-oriented -answered in feature(above)
---------------------------------------------------------------------------------------------------------
16.high-level programming language-answered in feature(above)
---------------------------------------------------------------------------------------------------------
17.functional programming and structured programming
  -Functional programming (FP)
    is a programming paradigm a style of building the structure and elements
    of computer programs — that treats computation as the evaluation of mathematical functions and avoids
    changing-state and mutable data.
  -Structural programming
   is a programming paradigm aimed at improving the clarity, quality,development times of computer programs,by making
   extensive use of the selection and repetition, structured control flow creation of block structures.
   divide the program into small module, so that program becomes easy to understand, debug, maintain, test, modify.
  -Procedural programming is a programming paradigm, derived from structured programming, based upon the concept of
    the procedure call. Procedures, also known as routines, subroutines, or functions, simply contain a series of
    computational steps to be carried out.
---------------------------------------------------------------------------------------------------------
18.    procedural vs object-oriented programming
     Procedural Oriented Programming                           Object Oriented Programming
 - program is divided into small parts called functions. -program is divided into small parts called objects.
 - top down approach                                     -bottom up approach.
 -no access specifier                                    -have access specifiers like private, public, protected
 -Adding new data and function is not easy.              -Adding new data and function is easy.
 -don't have any proper way for hiding data .            -proper way for hiding data
 -so it is less secure                                   -So provides data hiding so it is more secure.
 -overloading is not possible.                           -Overloading is possible
 -function is more important than data.                  -data is more important than function.
 -based on unreal world.                                 -is based on real world.
 -Examples: C, FORTRAN, Pascal, Basic etc.               -Examples: C++, Java, Python, C# etc.




---------------------------------------------------------------------------------------------------------
19.Dynamically typed programming language  int x = 10 <==>  x = 10---answered in feature(above)
---------------------------------------------------------------------------------------------------------
Automatic garbage collection
  -Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space.
  -Python's garbage collector runs during program execution and is triggered when an object's reference count
   reaches zero. An object's reference count changes as the number of aliases that point to it changes.
  -An object's reference count increases when it is assigned a new name or placed in a container  (list, tuple,
   or dictionary).
  -The object's reference count decreases when it's deleted with del,its reference is reassigned,
   or its reference goes out of scope.
  -When an object's reference count reaches zero, Python collects it automatically.
---------------------------------------------------------------------------------------------------------

"""

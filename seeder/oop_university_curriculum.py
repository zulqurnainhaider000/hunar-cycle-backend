"""
OOP University Curriculum Seeder (CS-121L Object Oriented Programming)
100% Verbatim transcription from 'OOP Manual 2024.pdf' for Department of Computing, Faculty of Engineering Sciences & Technology, Hamdard University Islamabad Campus.
Populates all 14 University Laboratory Modules (Labs 1 to 14) with zero data loss, exact paragraphs, code listings, tables, tasks, quizzes, and flashcards.
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from prisma import Prisma

COURSE_DATA = {
    "title": "Object Oriented Programming (CS-121L)",
    "category": "University",
    "description": "Official Academic Curriculum for CS-121L Object Oriented Programming. Comprehensive university laboratory manual covering C++ programming skills, function overloading, recursion, pointer arithmetic, structures, classes & objects, constructors & destructors, operator overloading, arrays & strings, static members, single & multiple inheritance, polymorphism & virtual functions, file & exception handling, and class templates.",
    "color": "#0D9488",
    "thumbnail": "assets/images/university/oop/fest_logo.png"
}

LABS_DATA = [
    {
        "order": 1,
        "title": "Lab 1: Practice Basic Programming Skills and Functions",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nvoid starline(); // function declaration (prototype)\n\nint main() {\n    starline();\n    cout << \"Data type Range\" << endl;\n    starline();\n    cout << \"char -128 to 127\" << endl\n         << \"short -32,768 to 32,767\" << endl\n         << \"int System dependent\" << endl\n         << \"long -2,147,483,648 to 2,147,483,647\" << endl;\n    starline();\n    return 0;\n}\n\nvoid starline() {\n    for (int j = 0; j < 45; j++)\n        cout << '*';\n    cout << endl;\n}",
        "content": "# Lab#01\n\n## PRACTICE BASIC PROGRAMMING SKILLS AND FUNCTIONS\n\n### Objective\n* Function definitions and declarations\n* Overloaded functions\n* Arguments and return values\n* Default arguments\n* Reference arguments\n* Storage classes\n\n### Theory Overview\nA function groups a number of program statements into a unit and gives it a name. This unit can then be invoked from other parts of the program. Functions in C++ (and C) are similar to subroutines and procedures in various other languages.\n\nAny sequence of instructions that appears in a program more than once is a candidate for being made into a function. The function's code is stored in only one place in memory, even though the function is executed many times in the course of the program.\n\n![Figure 1.1: flow of control to function](assets/images/university/oop/fig1_1_flow_of_control.png)\n\nFigure 1.1: flow of control to function\n\n### Simple Functions\nOur first example demonstrates a simple function whose purpose is to print a line of 45 asterisks. The example program generates a table, and lines of asterisks are used to make the table more readable. Here's the listing for TABLE:\n\n```cpp\n// demonstrates simple function\n#include<iostream>\nusing namespace std;\nvoid starline(); //function declaration\n// (prototype)\nint main()\n{\nstarline(); //call to function\ncout << \"Data type Range\" << endl;\nstarline(); //call to function\ncout << \"char -128 to 127\" << endl\n<< \"short -32,768 to 32,767\" << endl\n<< \"int System dependent\" << endl\n<< \"long -2,147,483,648 to 2,147,483,647\" << endl;\nstarline(); //call to function\nreturn 0;\n}\n//--------------------------------------------------------------\n// starline()\n// function definition\nvoid starline()\n{\nfor(int j=0; j<45; j++) //function body\ncout << '*';\ncout << endl;\n}\n```\n\noutput from the program looks like this:\n```text\n*********************************************\nData type Range\n*********************************************\nchar -128 to 127\nshort -32,768 to 32,767\nSystem dependent\ndouble -2,147,483,648 to 2,147,483,647\n```\n\nprogram consists of two functions: main() and starline(). You've already seen main() alone. What other components are necessary to add a function to the program? function declaration, the calls to the function, and the function definition.\n\n### The Function Declaration\nJust as you can't use a variable without first telling the compiler what it is, you also can't use a function without telling the compiler about it. There are two ways to do this. The approach we show here is to declare the function before it is called.\n(The other approach is to define it before it's called; we'll examine that next.). In the TABLE program, the function starline() is declared in the line\n```cpp\nvoid starline();\n```\n\nThe declaration tells the compiler that at some later point we plan to present a function called starline. The keyword void specifies that the function has no return value, and the empty parentheses indicate that it takes no arguments.\n(You can also use the keyword void in parentheses to indicate that the function takes no arguments, as is often done in C, but leaving them empty is the more common practice in C++.)\nWe'll have more to say about arguments and return values soon. Notice that the function declaration is terminated with a semicolon. It is a complete statement in itself. Function declarations are also called prototypes, since they provide a model or blueprint for the function.\nThey tell the compiler, \"a function that looks like this is coming up later in the program, so it's all right if you see references to it before you see the function itself.\"\n\n### Calling the Function\nThe function is called (or invoked, or executed) three times from main(). Each of the three calls looks like this:\n```cpp\nstarline();\n```\n\nThis is all we need to call the function: the function name, followed by parentheses. The syntax of the call is very similar to that of the declaration, except that the return type is not used. The call is terminated by a semicolon.\nExecuting the call statement causes the function to execute; that is, control is transferred to the function, the statements in the function definition (which we'll examine in a moment) are executed, and then control returns to the statement following the function call.\n\n### The Function Definition\nFinally, we come to the function itself, which is referred to as the function definition. The definition contains the actual code for the function. Here's the definition for starline ():\n```cpp\nvoid starline() //declarator\n{\nfor(int j=0; j<45; j++) //function body\ncout << '*';\ncout << endl;\n}\n```\n\nThe definition consists of a line called the declarator, followed by the function body. The function body is composed of the statements that make up the function, delimited by braces.\nThe declarator must agree with the declaration:\nIt must use the same function name, have the same argument types in the same order (if there are arguments), and have the same return type.\nNotice that the declarator is not terminated by a semicolon. Figure 1.2 shows the syntax of the function declaration, function call, and function definition.\n\n![Fig 1.2: Function Syntax](assets/images/university/oop/fig1_2_function_syntax.png)\n\nFig 1.2: Function Syntax\n\nWhen the function is called, control is transferred to the first statement in the function body. The other statements in the function body are then executed, and when the closing brace is encountered, control returns to the calling program.\n\n### PASSING ARGUMENTS TO FUNCTIONS\nAn argument is a piece of data (an int value, for example) passed from a program to the function.\nArguments allow a function to operate with different values, or even to do different things, depending on the requirements of the program calling it.\n\n### Equipment:\nMicrosoft Visual Studio / Dev C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### TASK # 1\nWrite a function that takes an integer value and returns the number with its digits reversed.\nFor example, given the number 7631, the function should return 1367.\n\n#### TASK # 2\nWrite a program that asks the user to input marks of five courses and then computes the average, variance and standard deviation of them. The formula for variance is;\n$$S^2 = \\frac{\\sum (XI - X)^2}{N}$$\nWhere $S^2$ is the variance, XI is the value of the one observations and X is the average of the five scores x1, x2, x3, x4 and x5. The standard deviation is the square root of variance.\nThe program must have at least 3 functions to compute average, variance and a display function that displays these values. Your program should ask the user to exit or input the scores again.\n\n#### TASK # 3\nWrite a function that takes two Distance values as arguments and returns the larger one. Include a main () program that accepts two Distance values from the user, compares them, and displays the larger.\n",
        "quizzes": [
            {
                "question": "What is the primary syntactic difference between a function prototype (declaration) and a function definition in C++?",
                "options": [
                    "A function declaration terminates with a semicolon, whereas a function definition includes a body enclosed in curly braces without a semicolon.",
                    "A function prototype cannot specify argument types, while a definition must specify parameter names.",
                    "A function prototype must always return void, whereas a definition can return any valid data type.",
                    "A function declaration allocates executable memory for the function statements on the stack."
                ],
                "correctAnswer": "A function declaration terminates with a semicolon, whereas a function definition includes a body enclosed in curly braces without a semicolon.",
                "explanation": "A function prototype (declaration) acts as a blueprint for the compiler and terminates with a semicolon. The function definition provides the actual implementation body enclosed in braces."
            },
            {
                "question": "What is stored in memory when a function is declared and defined in a compiled C++ program?",
                "options": [
                    "The function's compiled machine code is stored in only one place in code memory, regardless of how many times it is called.",
                    "A separate duplicate copy of the function code is stored for every function invocation.",
                    "The function's code is deleted from memory immediately after its first execution.",
                    "Function code is permanently duplicated inside the calling function's stack frame."
                ],
                "correctAnswer": "The function's compiled machine code is stored in only one place in code memory, regardless of how many times it is called.",
                "explanation": "Functions prevent code redundancy by storing the executable instructions in a single place in memory, transferring control whenever the function is invoked."
            },
            {
                "question": "In Lab 1 Task 1, what mathematical algorithm is commonly used to reverse the digits of an integer (e.g. 7631 to 1367)?",
                "options": [
                    "Repeatedly taking the remainder with modulo 10 (n % 10) and dividing the number by 10 (n / 10).",
                    "Converting each number to hexadecimal and bit-shifting by 4 bits to the left.",
                    "Subtracting the integer from its ASCII code table offset.",
                    "Squaring the number and extracting the lower half of the product."
                ],
                "correctAnswer": "Repeatedly taking the remainder with modulo 10 (n % 10) and dividing the number by 10 (n / 10).",
                "explanation": "Extracting the least significant digit with (num % 10), appending it to reversed (rev = rev * 10 + digit), and updating num with (num / 10) reverses an integer mathematically."
            }
        ],
        "flashcards": [
            {
                "question": "What is a function prototype in C++?",
                "answer": "A function prototype (declaration) tells the compiler the function's name, return type, and parameter list before its actual definition, enabling forward references."
            },
            {
                "question": "Why are functions used in modular programming?",
                "answer": "Functions eliminate redundant code by grouping reusable statements into a single callable block, improving code readability, maintenance, and memory efficiency."
            },
            {
                "question": "What happens to program control during a function call?",
                "answer": "Control transfers from the caller to the function's first statement; upon reaching a return statement or the closing brace, control returns to the caller."
            },
            {
                "question": "What is the return type of a function that does not return any value?",
                "answer": "void"
            }
        ]
    },
    {
        "order": 2,
        "title": "Lab 2: Imitate Functions Overloading and Recursion",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\n// Function Overloading\nvoid print() {\n    for (int i = 1; i <= 5; i++) cout << \"*\";\n    cout << endl;\n}\n\nvoid print(int n) {\n    for (int i = 1; i <= n; i++) cout << \"*\";\n    cout << endl;\n}\n\n// Recursive Function\nint factorial(int n) {\n    if (n <= 1) return 1; // Base case\n    return n * factorial(n - 1); // Inductive step\n}\n\nint main() {\n    print();\n    print(10);\n    cout << \"Factorial of 5 is: \" << factorial(5) << endl;\n    return 0;\n}",
        "content": "# Lab#02\n\n## IMITATE FUNCTIONS OVERLOADING AND RECURSION\n\n### Objective\n* Function Overloading\n* Recursion\n\n### Theory Overview\n\n#### OVERLOADED FUNCTIONS:\nAn overloaded function appears to perform different activities depending on the kind of data sent to it. It may seem equally mysterious how an overloaded function knows what to do. It performs one operation on one kind of data but another operation on a different kind.\nNormally each function defined and used in a program has a unique name.\nIn C++, we can write more than one functions having same name, but they must differ in:\n* Number of arguments\n* Type of arguments\nBut not differ in return type.\n\nExample: Write three versions of print function, one that take no argument, second take number argument and third take student type argument.\n\n```cpp\n#include<iostream>\nusing namespace std;\n\nstruct student{\nint rollno; char sexcode; float marks;\n};\nvoid print ( )\n{\nint i ;\nfor ( i=1 ; i <= 5; i++ )\ncout<<\"*\";\ncout<<endl;\n}\nvoid print (int n )\n{\nint i ;\nfor ( i=1 ; i <= n; i++ )\ncout<<\"*\";\ncout<<endl;\n}\nstudent read_data( )\n{\nstudent s;\ncout<<\"Enter student Roll number:\"; cin>>s.rollno;\ncout<<\"Enter student sex code:\"; cin>>s.sexcode;\ncout<<\"Enter student marks:\"; cin>>s.marks;\nreturn (s);\n}\nvoid print (student st)\n{\ncout<<\"Student Roll number = \"<<st.rollno<<endl;\nif(st.sexcode=='m') cout<<\"Student is male\"<<endl;\nif(st.sexcode=='f') cout<<\"Student is female\"<<endl;\ncout<<\"Marks=\"<<st.marks<<endl;\n}\nint main ( )\n{\nint i, npass=0;\nstudent s1;\nfor (i=1; i<=30; i++)\n{\ns1=read_data( );\nif(s1.marks>=50)\nnpass ++;\nprint( );\nprint(s1);\nprint(30);\n}\ncout<<\"Total Pass students= \"<<npass<<endl;\nreturn 0;\n}\n```\n\n#### RECURSIVE FUNCTIONS:\nCalling a function within its definition is called recursion.\nIn such function, the function must decrease argument value and there is a base condition or stop condition.\n\nExample: Write a non-recursive function for factorial of a given number, and use it in main( ).\n\n```cpp\n#include <iostream>\nusing namespace std;\nint factorial(int);\nint main()\n{\nint n,fact;\ncout<<\"Enter a positive integer:\";\ncin>>n;\nfact= factorial(n);\ncout<<\"Factorial of \"<<n<<\" is \"<< fact;\nreturn 0;\n}\nint factorial(int num)\n{\nint i=1,f=1;\nwhile(i<=num)\n{\nf=f*i;\ni++;\n}\nreturn f;\n}\n```\n\nExample: Write a recursive function for factorial of a given number, and use it in main ( ).\n\n```cpp\n#include <iostream>\nusing namespace std;\nint factorial(int);\nint main()\n{\nint n,fact;\ncout<<\"Enter a positive integer: \";\ncin>>n;\nfact= factorial(n);\ncout<<\"Factorial of \"<<n<<\" is \"<< fact ;\nreturn 0;\n}\nint factorial(int n)\n{\nif (n==1) //Base case\nreturn 1;\nelse\nreturn n*factorial(n-1); // Inductive step\n}\n```\n\n### Equipment:\nMicrosoft Visual Studio / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### TASK #1:\nWrite a program to implement the cube root with the help of function overloading.\n\n#### TASK #2:\nWrite a program that reads two numbers, and uses a function order ( ) to make them in ascending order.\nFinally print them in main ( ).\n\n#### TASK #3:\nWrite a program that calls four overloaded sum( ) functions , i) one add 2 integer numbers, ii) adds three integer numbers, iii) adds two float numbers, iv) adds two distance structure variables.\n\n#### TASK #4:\nWrite a program that uses recursion to print Fibonacci series up to n numbers. Every number in Fibonacci series is sum of two previous numbers. Fab(n-1) + fab(n-2)\n",
        "quizzes": [
            {
                "question": "Which of the following conditions is required for function overloading to be valid in C++?",
                "options": [
                    "The functions must differ in the number or data types of their parameters.",
                    "The functions must differ only in their return type.",
                    "The functions must be declared with different access specifiers.",
                    "The functions must be written in separate header files."
                ],
                "correctAnswer": "The functions must differ in the number or data types of their parameters.",
                "explanation": "C++ determines which overloaded function to invoke based on its parameter list (signature). Having different return types alone causes a compiler error."
            },
            {
                "question": "What essential component must every recursive function have to prevent stack overflow?",
                "options": [
                    "A base case that stops further recursive calls.",
                    "A static variable that counts the number of invocations.",
                    "A while loop enclosing the function body.",
                    "An exception block catching segmentation faults."
                ],
                "correctAnswer": "A base case that stops further recursive calls.",
                "explanation": "Without a base case, recursive calls continue indefinitely until stack memory is exhausted, resulting in a runtime stack overflow crash."
            },
            {
                "question": "What is the return value of factorial(4) in C++ using the recursive definition return n * factorial(n - 1)?",
                "options": [
                    "24",
                    "12",
                    "16",
                    "64"
                ],
                "correctAnswer": "24",
                "explanation": "factorial(4) = 4 * factorial(3) = 4 * 3 * factorial(2) = 4 * 3 * 2 * factorial(1) = 4 * 3 * 2 * 1 = 24."
            }
        ],
        "flashcards": [
            {
                "question": "What is function overloading in C++?",
                "answer": "Function overloading allows multiple functions in the same scope to share the same name provided their parameter count or types differ."
            },
            {
                "question": "Can two C++ functions be overloaded based on return type alone?",
                "answer": "No. The compiler matches overloaded functions based solely on parameter signatures; identical parameters with different return types result in a compile error."
            },
            {
                "question": "What are the two core parts of a recursive function?",
                "answer": "1. Base case (terminating condition that returns without recursion) and 2. Inductive/recursive step (reduces problem size toward the base case)."
            },
            {
                "question": "What is the mathematical recurrence relation for Fibonacci numbers?",
                "answer": "Fib(n) = Fib(n-1) + Fib(n-2), with base cases Fib(0) = 0 and Fib(1) = 1."
            }
        ]
    },
    {
        "order": 3,
        "title": "Lab 3: Practice Program to Implement Pointer Arithmetic",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int number = 88;\n    int *pNumber = &number; // assign address of number to pointer\n\n    cout << \"Content of pNumber (address): \" << pNumber << endl;\n    cout << \"Value pointed to (*pNumber):  \" << *pNumber << endl;\n\n    *pNumber = 99; // Re-assign value through pointer\n    cout << \"Updated number via pointer:    \" << number << endl;\n    cout << \"Address of pointer itself:     \" << &pNumber << endl;\n\n    return 0;\n}",
        "content": "# Lab#03\n\n## PRACTICE PROGRAM TO IMPLEMENT POINTER ARITHMETIC\n\n### Objectives:\n* Pointers and function arguments\n* Pointers and arrays\n* Pointers and objects\n* Pointers and strings\n\n### Theory Overview\nThe ideas behind pointers are not complicated. Here's the first key concept: Every byte in the computer's memory has an address.\nAddresses are numbers, just as they are for houses on a street. The numbers start at 0 and go up from there—1, 2, 3, and so on. If you have 1MB of memory, the highest address is 1,048,575. (Of course you probably have much more.)\nYour program, when it is loaded into memory, occupies a certain range of these addresses. That means that every variable and every function in your program starts at a particular address.\n\n#### The Address-of Operator &\nYou can find the address occupied by a variable by using the address-of operator &. Here's a short program, VARADDR, that demonstrates how to do this:\n\nExample 1:\n```cpp\n// varaddr.cpp\n// addresses of variables\n#include <iostream>\nusing namespace std;\nint main()\n{\nint var1 = 11; //define and initialize\nint var2 = 22; //three variables\nint var3 = 33;\ncout << &var1 << endl //print the addresses\n<< &var2 << endl //of these variables\n<< &var3 << endl;\nreturn 0;\n}\n```\n\nThis simple program defines three integer variables and initializes them to the values 11, 22, and 33. It then prints out the addresses of these variables. The actual addresses occupied by the variables in a program depend on many factors, such as the computer the program is running on, the size of the operating system, and whether any other programs are currently in memory.\n\nThe << insertion operator interprets the addresses in hexadecimal arithmetic, as indicated by the prefix 0x before each number. This is the usual way to show memory addresses. If you aren't familiar with the hexadecimal number system, don't worry. All you really need to know is that each variable starts at a unique address.\n\nHowever, you might note in the output above that each address differs from the next by exactly 2 bytes. That's because integers occupy 2 bytes of memory (assuming it's a 16-bit system). If we had used variables of type char, they would have adjacent addresses, since a char occupies 1 byte; and if we had used type double, the addresses would have differed by 8 bytes.\n\nThe addresses appear in descending order because automatic variables are stored on the stack, which grows downward in memory. If we had used external variables, they would have ascending addresses, since external variables are stored on the heap, which grows upward.\n\nExample 2:\n```cpp\n#include <iostream>\nusing namespace std;\nint main()\n{\nint var1 = 3;\nint var2 = 24;\nint var3 = 17;\ncout << &var1 << endl;\ncout << &var2 << endl;\ncout << &var3 << endl;\nreturn 0;\n}\n```\n\nExample 3:\n```cpp\n#include <iostream>\nusing namespace std;\nint main() {\nint number = 88; // Declare an int variable and assign an initial value\nint * pNumber; // Declare a pointer variable pointing to an int (or int pointer)\npNumber = &number; // assign the address of the variable number to pointer pNumber\ncout << pNumber << endl; // Print content of pNumber (0x22ccf0)\ncout << &number << endl; // Print address of number (0x22ccf0)\ncout << *pNumber << endl; // Print value pointed to by pNumber (88)\ncout << number << endl; // Print value of number (88)\n*pNumber = 99; // Re-assign value pointed to by pNumber\ncout << pNumber << endl; // Print content of pNumber (0x22ccf0)\ncout << &number << endl; // Print address of number (0x22ccf0)\ncout << *pNumber << endl; // Print value pointed to by pNumber (99)\ncout << number << endl; // Print value of number (99)\n// The value of number changes via pointer\ncout << &pNumber << endl; // Print the address of pointer variable pNumber (0x22ccec)\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### TASK # 1\nIntroduce int variables x and y and int* pointer variables p and q. Set x to 2, y to 8, p to the address of x, and q to the address of y. Then print the following information:\n(1) The address of x and the value of x.\n(2) The value of p and the value of *p.\n(3) The address of y and the value of y.\n(4) The value of q and the value of *q.\n(5) The address of p (not its contents!).\n(6) The address of q (not its contents!).\n\n#### TASK # 2\nWrite a program to input an integer value and then to find out if given value is a prime number or not by passing the number to a function as a pointer argument.\n",
        "quizzes": [
            {
                "question": "What is the difference between *ptr and ptr in C++ when ptr is an integer pointer?",
                "options": [
                    "ptr holds the memory address of the target variable, while *ptr accesses the value stored at that address.",
                    "ptr holds the integer value, while *ptr holds the hex address.",
                    "*ptr creates a new integer on the stack, while ptr destroys the variable.",
                    "Both expressions refer to the exact same memory address."
                ],
                "correctAnswer": "ptr holds the memory address of the target variable, while *ptr accesses the value stored at that address.",
                "explanation": "ptr is a pointer storing the address; dereferencing it via *ptr (indirection operator) retrieves or modifies the data stored at that address."
            },
            {
                "question": "Why do automatic local variables allocated sequentially in C++ typically have descending memory addresses?",
                "options": [
                    "Local stack memory grows downwards towards lower addresses as frames are pushed.",
                    "Heap memory is inverted by the compiler to prevent buffer overruns.",
                    "The processor registers only store values in reverse endian order.",
                    "Hexadecimal notation requires negative offsets for integer types."
                ],
                "correctAnswer": "Local stack memory grows downwards towards lower addresses as frames are pushed.",
                "explanation": "In standard x86/x64 architecture, the program call stack grows downwards (from higher memory addresses to lower memory addresses)."
            },
            {
                "question": "What does &pNumber evaluate to if pNumber is declared as int* pNumber = &number;?",
                "options": [
                    "The memory address where the pointer variable pNumber itself is stored.",
                    "The memory address of the integer variable number.",
                    "The integer value 88.",
                    "A null pointer value 0x0."
                ],
                "correctAnswer": "The memory address where the pointer variable pNumber itself is stored.",
                "explanation": "&pNumber retrieves the address of the pointer variable itself (a pointer-to-a-pointer type int**), distinct from the address stored inside pNumber."
            }
        ],
        "flashcards": [
            {
                "question": "What does the address-of operator (&) return?",
                "answer": "It returns the hexadecimal memory address of its operand variable."
            },
            {
                "question": "What does the dereference operator (*) do when applied to a pointer?",
                "answer": "It accesses or modifies the value stored at the memory address pointed to by the pointer."
            },
            {
                "question": "In which memory segment are automatic local variables stored?",
                "answer": "On the stack, which grows downward toward lower memory addresses."
            },
            {
                "question": "How many bytes does an integer pointer occupy on a 64-bit architecture?",
                "answer": "8 bytes (64 bits)."
            }
        ]
    },
    {
        "order": 4,
        "title": "Lab 4: Practice Structures Implementation",
        "codeSnippet": "#include <iostream>\n#include <string>\nusing namespace std;\n\nstruct student {\n    int roll_no;\n    char name[30];\n    int age;\n    int marks;\n};\n\nint main() {\n    student p1 = {1, \"Brown\", 14, 78};\n    cout << \"Roll: \" << p1.roll_no << \" Name: \" << p1.name \n         << \" Age: \" << p1.age << \" Marks: \" << p1.marks << endl;\n    return 0;\n}",
        "content": "# Lab#04\n\n## PRACTICE STRUCTURES IMPLEMENTATION\n\n### Objective\n* Implement structures\n\n### Structures\nStructures (also called structs) are a way to group several related variables into one place. Each variable in the structure is known as a member of the structure.\n\n### Create a Structure\nTo create a structure, use the struct keyword and declare each of its members inside curly braces.\nAfter the declaration, specify the name of the structure variable (myStructure in the example below):\n\n```cpp\nstruct { // Structure declaration\nint myNum; // Member (int variable)\nstring myString; // Member (string variable)\n} myStructure; // Structure variable\n```\n\n### Access Structure Members\nTo access members of a structure, use the dot syntax (.):\n\nExample#1: Assign data to members of a structure and print it:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nint main() {\nstruct {\nint myNum;\nstring myString;\n}\nmyStructure;\nmyStructure.myNum =1;\nmyStructure.myString = \"Hello World!\";\ncout << myStructure.myNum << \"\\n\";\ncout << myStructure.myString << \"\\n\";\nreturn 0;\n}\n```\n\nExample#2: Write a program to store and print the roll no., name , age and marks of a student using structures.\n```cpp\n#include<iostream>\nusing namespace std;\nint main() {\nstruct student {\nint roll_no;\nchar name[30];\nint age;\nint marks;\n};\nstruct student p1 = {1,\"Brown\",14,78};\ncout << p1.roll_no << \" \" << p1.name << \" \" << p1.age << \" \" << p1.marks << \"\\n\";\nreturn 0;\n}\n```\n\n### Equipment:\nMicrosoft Visual Studio / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task#1:\nWrite a program to store the roll no. (starting from 1), name and age of 5 students and then print the details of the student with roll no. 2.\n\n#### Task#2:\nWrite a program to add two distances in inch-feet using structure. The values of the distances is to be taken from the user.\n",
        "quizzes": [
            {
                "question": "What is the primary conceptual difference between an array and a struct in C++?",
                "options": [
                    "An array stores homogeneous data (same type), while a struct can group heterogeneous data (different types).",
                    "An array is stored in RAM, whereas a struct is only stored in CPU cache.",
                    "A struct cannot hold primitive data types like integers or floats.",
                    "An array supports members accessed by name using dot syntax."
                ],
                "correctAnswer": "An array stores homogeneous data (same type), while a struct can group heterogeneous data (different types).",
                "explanation": "Arrays group elements of identical type indexed by integers; structs group fields of different data types accessed by named identifiers."
            },
            {
                "question": "Which operator is used to access members of a structure variable in C++?",
                "options": [
                    "Dot operator (.)",
                    "Arrow operator (->)",
                    "Scope resolution operator (::)",
                    "Ampersand operator (&)"
                ],
                "correctAnswer": "Dot operator (.)",
                "explanation": "The dot operator (.) is used with a direct struct variable (e.g. p1.age), while arrow (->) is used when dereferencing a struct pointer."
            },
            {
                "question": "In Lab 4 Task 2, when adding two distances represented by feet and inches, what conversion rule must be applied?",
                "options": [
                    "When total inches reach or exceed 12, divide by 12, add to feet, and keep remainder inches.",
                    "Multiply inches by 2.54 and convert directly to metric centimeters.",
                    "Discard any inches exceeding 10 as rounding errors.",
                    "Store inches as negative numbers if feet are odd."
                ],
                "correctAnswer": "When total inches reach or exceed 12, divide by 12, add to feet, and keep remainder inches.",
                "explanation": "In standard imperial units, 12 inches = 1 foot. If inches >= 12, feet += inches / 12, and inches = inches % 12."
            }
        ],
        "flashcards": [
            {
                "question": "What keyword defines a structure in C++?",
                "answer": "struct"
            },
            {
                "question": "How are members of a struct variable accessed?",
                "answer": "Using the dot member access operator (.) e.g., student.roll_no."
            },
            {
                "question": "Can a structure contain another structure as a member?",
                "answer": "Yes. This is called a nested structure."
            },
            {
                "question": "By default, what is the access specifier of members in a C++ struct?",
                "answer": "public (unlike a C++ class where members default to private)."
            }
        ]
    },
    {
        "order": 5,
        "title": "Lab 5: Practice the Classes and Objects, Class Definition & Access Specifier",
        "codeSnippet": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Cars {\npublic:\n    string car_model; // Data member\n\n    void printname() { // Member function\n        cout << \"Car name is: \" << car_model << endl;\n    }\n};\n\nint main() {\n    Cars obj1; // Object of class Cars\n    obj1.car_model = \"BMW\";\n    obj1.printname();\n    return 0;\n}",
        "content": "# Lab#05\n\n## PRACTICE THE CLASSES AND OBJECTS, CLASS DEFINITION ACCESS SPECIFIER\n\n### Objectives\n* Objects and Classes\n* Defining a class\n* Members of a class\n* Data members\n* Member Functions\n* Objects\n* Declaring objects of a class\n* Calling Member Functions\n\n### Theory Overview\nA class is a collection of data and functions. The data items and functions are defined within the class. The functions are written to work upon data items and each function has a unique relationship with the data items of the class. An object is said to be an instance of a class.\nClasses are defined to create user-defined data types. Defining a class specifies its data members and relationship between the data items through its functions.\nA class is defined in C++ using keyword class followed by the name of class.\nThe body of class is defined inside the curly brackets and terminated by a semicolon at the end.\n\nExample 1:\n```cpp\nclass className\n{\n// some data\n// some functions\n};\nclass Test\n{\nprivate:\nint data1;\nfloat data2;\npublic:\nvoid function1()\n{ data1 = 2; }\nfloat function2()\n{\ndata2 = 3.5;\nreturn data2;\n}\n};\n```\n\nExample 2:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass Cars\n{\n// Access specifier\npublic:\n// Data Members\nstring car_model;\n// Member Functions()\nvoid printname()\n{\ncout << \"Car name is: \" << car_model<< endl;\n}\n};\nint main() {\n// Declare an object of class geeks\nCars obj1;\n// accessing data member\nobj1.car_model = \"BMW\";\n// accessing member function\nobj1.printname();\nreturn 0;\n}\n```\n\n### Basic Program of Classes\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass stud\n{\npublic:\nchar name[30],clas[10];\nint rol,age;\nvoid enter()\n{\ncout<<\"Enter Student Name: \"; cin>>name;\ncout<<\"Enter Student Age: \"; cin>>age;\ncout<<\"Enter Student Roll number: \"; cin>>rol;\ncout<<\"Enter Student Class: \"; cin>>clas;\n}\nvoid display()\n{\ncout<<\"\\n Age\\tName\\tR.No.\\tClass\";\ncout<<\"\\n\"<<age<<\"\\t\"<<name<<\"\\t\"<<rol<<\"\\t\"<<clas<<endl;\n}\n};\nint main()\n{\nclass stud s;\ns.enter();\ns.display();\nreturn 0;\n}\n```\n\n### Program of Default Constructor\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass construct\n{\npublic:\nint a, b;\n// Default Constructor\nconstruct ()\n{\na = 10;\nb = 20;\n}\n};\nint main()\n{\n// Default constructor called automatically\n// when the object is created\nconstruct c;\ncout << \"a: \"<< c.a << endl << \"b: \"<< c.b << endl;\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### TASK #1\nThe following is a class called rectangle which contains two private data elements, width and height of type double and a number of member functions. Fill in the blanks and instructions to complete the class definition:\n\n```cpp\n#include <iostream>\nusing namespace std;\n\nclass rectangle {\nprivate:\ndouble width;\ndouble height;\npublic:\n//write a function set_height() that sets the Height if it is positive, otherwise Height will be zero.\nvoid set_height(double h) { if(h > 0) height = h; else height = 0; }\n//write Function set_width() that sets the Width if it is positive, otherwise Width will be zero.\nvoid set_width(double w) { if(w > 0) width = w; else width = 0; }\n//write the header of a function area that returns the area of a rectangle\ndouble area() { return width * height; }\nvoid print() {\ncout << \"Width: \" << width << \", Height: \" << height << \", Area: \" << area() << endl;\n}\n};\nint main() {\n//create an object T1 from class rectangle\nrectangle T1;\nT1.set_width(5.0);\nT1.set_height(4.0);\n//call function print\nT1.print();\n//call function area\ncout << \"Direct Area: \" << T1.area() << endl;\nreturn 0;\n}\n```\n\n#### Task #2\n* Write two classes animal and person.\n* Think of appropriate data members for both classes.(at least two members)\n* Write setter and getter functions for these classes to set and print the values of data members\n* Check the classes by creating instances(objects) of both the classes in the main method and call the print/show method of each instance separately\n",
        "quizzes": [
            {
                "question": "What is the default access specifier for members of a class in C++ if none is explicitly specified?",
                "options": [
                    "private",
                    "public",
                    "protected",
                    "internal"
                ],
                "correctAnswer": "private",
                "explanation": "In C++, class members default to private, enforcing encapsulation. In contrast, struct members default to public."
            },
            {
                "question": "What is an object in Object-Oriented Programming?",
                "options": [
                    "An identifiable run-time instance of a class that encapsulates state and behavior.",
                    "A header file that imports external C libraries.",
                    "A pointer that always points to address 0x0.",
                    "A function prototype declared inside main()."
                ],
                "correctAnswer": "An identifiable run-time instance of a class that encapsulates state and behavior.",
                "explanation": "A class is the blueprint or user-defined type; an object is an instantiated memory entity created according to that blueprint."
            },
            {
                "question": "Why are class variables commonly placed in private sections with public getters and setters?",
                "options": [
                    "To enforce data encapsulation and protect internal object state from unauthorized modification.",
                    "Because C++ compilers cannot allocate memory for public variables.",
                    "To force all member functions to be inline.",
                    "To allow external functions to bypass memory protection."
                ],
                "correctAnswer": "To enforce data encapsulation and protect internal object state from unauthorized modification.",
                "explanation": "Encapsulation hides internal implementation details and allows validation logic inside setter functions before state is updated."
            }
        ],
        "flashcards": [
            {
                "question": "What keyword declares a class in C++?",
                "answer": "class"
            },
            {
                "question": "What are the three access specifiers in C++?",
                "answer": "private (accessible only within class), public (accessible everywhere), and protected (accessible within class and derived classes)."
            },
            {
                "question": "What punctuation must terminate every C++ class definition?",
                "answer": "A semicolon (;)"
            },
            {
                "question": "What is encapsulation in OOP?",
                "answer": "The bundling of data and the methods that operate on that data into a single unit (class), restricting direct outside access."
            }
        ]
    },
    {
        "order": 6,
        "title": "Lab 6: Practice Constructors and Destructors",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nclass CRectangle {\n    int *width, *height;\npublic:\n    CRectangle(int a, int b) {\n        width = new int;\n        height = new int;\n        *width = a;\n        *height = b;\n    }\n\n    ~CRectangle() { // Destructor\n        delete width;\n        delete height;\n    }\n\n    int area() { return (*width * *height); }\n};\n\nint main() {\n    CRectangle rect(3, 4);\n    cout << \"Area: \" << rect.area() << endl;\n    return 0; // rect goes out of scope, destructor called\n}",
        "content": "# Lab#06\n\n## PRACTICE CONSTRUCTORSAND DESTRUCTORS\n\n### Objective:\n* Constructors\n* Destructors\n\n### Theory Overview\nA class constructor is a special member function of a class that is executed whenever we create new objects of that class.\nA constructor will have exact same name as the class and it does not have any return type at all, not even void. Constructors can be very useful for setting initial values for certain member variables.\n\nExample 1:\n```cpp\n#include <iostream>\nusing namespace std;\nclass Area\n{\nprivate:\nint length;\nint breadth;\npublic:\n// Constructor\nArea(): length(5), breadth(2){ }\nvoid GetLength()\n{\ncout << \"Enter length and breadth respectively: \";\ncin >> length >> breadth;\n}\nint AreaCalculation() { return (length * breadth); }\nvoid DisplayArea(int temp)\n{\ncout << \"Area: \" << temp << endl;\n}\n};\nint main()\n{\nArea A1, A2;\nint temp;\nA1.GetLength();\ntemp = A1.AreaCalculation();\nA1.DisplayArea(temp);\ncout << endl << \"Default Area when value is not taken from user\" << endl;\ntemp = A2.AreaCalculation();\nA2.DisplayArea(temp);\nreturn 0;\n}\n```\n\n### Default constructors\nA constructor that takes no parameters (or has parameters that all have default values) is called a default constructor. The default constructor is called if no user-provided initialization values are provided.\nHere is an example of a class that has a default constructor:\n```cpp\n#include <iostream>\nclass Fraction\n{\nprivate:\nint m_numerator;\nint m_denominator;\npublic:\nFraction() // default constructor\n{\nm_numerator = 0;\nm_denominator = 1;\n}\nint getNumerator() { return m_numerator; }\nint getDenominator() { return m_denominator; }\ndouble getValue() { return static_cast<double>(m_numerator) / m_denominator; }\n};\nint main()\n{\nFraction frac; // Since no arguments, calls Fraction() default constructor\nstd::cout << frac.getNumerator() << \"/\" << frac.getDenominator() << '\\n';\nreturn 0;\n}\n```\n\n### Destructors:\nDestructors are usually used to de allocate memory and do other cleanup for a class object and its class members when the object is destroyed. A destructor is called for a class object when that object passes out of scope or is explicitly deleted.\nA destructor is a member function with the same name as its class prefixed by a ~ (tilde). For example:\n```cpp\nclass X {\npublic:\n// Constructor for class X\nX();\n// Destructor for class X\n~X();\n};\n```\n\nA destructor takes no arguments and has no return type. Its address cannot be taken. Destructors cannot be declared const, volatile, const volatile or static. A destructor can be declared virtual or pure virtual.\nIf no user-defined destructor exists for a class and one is needed, the compiler implicitly declares a destructor. This implicitly declared destructor is an inline public member of its class.\nThe compiler will implicitly define an implicitly declared destructor when the compiler uses the destructor to destroy an object of the destructor's class type. Suppose a class A has an implicitly declared destructor. The following is equivalent to the function the compiler would implicitly define for A:\n```cpp\nA::~A() { }\n```\n\nExample 2:\n```cpp\n#include <iostream>\nusing namespace std;\nclass CRectangle {\nint *width, *height;\npublic:\nCRectangle (int,int);\n~CRectangle ();\nint area () {return (*width * *height);}\n};\nCRectangle::CRectangle (int a, int b) {\nwidth = new int;\nheight = new int;\n*width = a;\n*height = b;\n}\nCRectangle::~CRectangle () {\ndelete width;\ndelete height;\n}\nint main () {\nCRectangle rect (3,4), rectb (5,6);\ncout << \"rect area: \" << rect.area() << endl;\ncout << \"rectb area: \" << rectb.area() << endl;\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\nWrite a Student class in C++\nA student object should hold information about a student in your grade book and should have the Following details:\n* string name\n* int age\n* int *p\n\nWrite a default constructor that initializes name, age and p pointer dynamically points to array of size 3. Add marks in the p array for 3 quizzes.\nCreate object s1.\nCreate object s2 exactly similar to s1. (Use default copy constructor supplied by the compiler)\nPrint the values of s1 and s2 along with address of pointer p\nNow change name and marks for s1 using setter function\nPrint the values of s1 and s2 along with address of pointer p (calling the same print function again)\nChange your code and write a copy constructor for this class\nRe-run your code\n",
        "quizzes": [
            {
                "question": "What is the naming syntax of a destructor function in C++?",
                "options": [
                    "The class name preceded by a tilde (~), taking no parameters and having no return type.",
                    "The class name preceded by delete keyword.",
                    "A void function named destroy().",
                    "An overloaded operator named operator ~()."
                ],
                "correctAnswer": "The class name preceded by a tilde (~), taking no parameters and having no return type.",
                "explanation": "In C++, destructors have the exact class name preceded by ~, take zero arguments, have no return type, and cannot be overloaded."
            },
            {
                "question": "What is the critical problem with the default copy constructor when a class manages dynamic heap memory (like int *p)?",
                "options": [
                    "It performs a shallow copy, copying only the pointer address, causing double-free crashes and shared memory corruption.",
                    "It refuses to compile if any pointer variable exists inside the class.",
                    "It creates duplicate memory on the stack instead of heap.",
                    "It automatically deletes the original object when copying."
                ],
                "correctAnswer": "It performs a shallow copy, copying only the pointer address, causing double-free crashes and shared memory corruption.",
                "explanation": "Default copy constructors perform member-wise bitwise copy (shallow copy). Both objects end up pointing to the exact same heap memory, causing double-free deletion errors."
            },
            {
                "question": "When is a destructor automatically invoked in C++?",
                "options": [
                    "When an automatic local object goes out of scope or a dynamic object is freed with delete.",
                    "Only when explicitly called like obj.~ClassName().",
                    "Whenever an exception occurs inside a constructor.",
                    "At the start of main() function execution."
                ],
                "correctAnswer": "When an automatic local object goes out of scope or a dynamic object is freed with delete.",
                "explanation": "Destructors execute automatically when stack objects leave their scope or when heap-allocated objects are released via delete."
            }
        ],
        "flashcards": [
            {
                "question": "Can a C++ destructor take parameters?",
                "answer": "No. Destructors take zero arguments and therefore cannot be overloaded."
            },
            {
                "question": "What is the difference between shallow copy and deep copy?",
                "answer": "Shallow copy copies raw pointer addresses sharing memory; deep copy allocates independent new memory and copies the actual contents."
            },
            {
                "question": "What is a member initialization list in a constructor?",
                "answer": "A syntax before the constructor body (e.g. Area(): length(5), breadth(2) {}) that initializes member variables directly upon creation."
            },
            {
                "question": "What happens if a class does not define any constructor?",
                "answer": "The compiler automatically generates an implicit default constructor with an empty body."
            }
        ]
    },
    {
        "order": 7,
        "title": "Lab 7: Practice Operator Overloading Implementation",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nclass Test {\nprivate:\n    int count;\npublic:\n    Test(): count(5) {}\n\n    // Overload prefix ++ operator\n    void operator++() {\n        count = count + 1;\n    }\n\n    void Display() { cout << \"Count: \" << count << endl; }\n};\n\nint main() {\n    Test t;\n    ++t; // Calls operator++()\n    t.Display();\n    return 0;\n}",
        "content": "# Lab#07\n\n## PRACTICE OPERATOR OVERLOADING IMPLEMENTATION\n\n### Objective:\n* Operator Overloading\n* Operator Arguments\n* Operator Return value\n* Overloading Unary Operators\n* Overloading Binary Operators\n\n### Theory Overview\nOperator overloading is one of the most exciting features of Object-oriented programming that transform complex, obscure program listings into intuitively obvious. E.g.\n```cpp\nd3.addobjects(d1, d2);\n// or the similar but equally obscure\nd3 = d1.addobjects(d2);\n// can be changed to the much more readable\nd3 = d1 + d2;\n```\n\nThe rather forbidding term operator overloading refers to giving the <=, and +=, additional meanings when they are applied to user-defined\n```cpp\na = b + c;\n```\nIt works only with basic types like int and float, and attempting to apply user-defined class will cause complaints from the compiler. However, this statement legal even when a, b, and c are user-defined types.\n\nExample:\n```cpp\n#include<iostream>\n#include<string>\nusing namespace std;\nclass Test\n{\nprivate:\nint count;\npublic:\nTest(): count(5){}\nvoid operator ++()\n{\ncount = count+1;\n}\nvoid Display() { cout<<\"Count: \"<<count<<endl; }\n};\nint main()\n{\nTest t;\n// this calls \"function void operator ++()\" function\n++t;\nt.Display();\nreturn 0;\n}\n```\n\nExample 2:\n```cpp\n#include<iostream>\nusing namespace std;\nclass xyz{\nint x;\nint y;\nint z;\npublic:\nvoid get(){\ncout<<\"XYZ please\\n\";\ncin>>x>>y>>z;\n}\nvoid disp(){\ncout<<x<<y<<z<<endl;\n}\nvoid friend operator-(xyz &S);//pass by reference\n}s1;\nvoid operator-(xyz &S){\nS.x=-S.x;//object name must be used as it is a friend function\nS.y=-S.y;\nS.z=-S.z;\n}\nint main(){\ns1.get();\ncout<<\"BEFORE OVERLOADING\\n\";\ns1.disp();\ncout<<\"AFTER OVERLOADING \\n\";\n-s1;\ns1.disp();\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task # 1\nWrite a program by using a class Counter. Create two objects of class Counter c1 and c2. Use the over loaded ++ operator to increment c1 once and c2 twice. Display the resulting values.\n\n#### Task #2:\nWrite a program to add two numbers using binary operator overloading.\n\n#### Task #3:\nWrite a program to join the different strings by using the logical And (&&) operator and operator overloading.\n",
        "quizzes": [
            {
                "question": "What keyword is required in C++ to overload an operator?",
                "options": [
                    "operator",
                    "overload",
                    "virtual",
                    "friend"
                ],
                "correctAnswer": "operator",
                "explanation": "In C++, the operator keyword followed by the symbol (e.g. operator+, operator++) defines an overloaded operator function."
            },
            {
                "question": "Which of the following operators CANNOT be overloaded in C++?",
                "options": [
                    "Scope resolution (::), Member access (.), and Ternary conditional (?:)",
                    "Addition (+), Subtraction (-), and Multiplication (*)",
                    "Increment (++) and Decrement (--)",
                    "Logical AND (&&) and Logical OR (||)"
                ],
                "correctAnswer": "Scope resolution (::), Member access (.), and Ternary conditional (?:)",
                "explanation": "C++ forbids overloading the scope resolution operator (::), member selection (.), pointer to member (.*), and conditional ternary operator (?:)."
            },
            {
                "question": "When an overloaded binary operator is implemented as a member function (e.g. c3 = c1 + c2;), how many arguments does the member function take?",
                "options": [
                    "1 argument (the right operand c2; the left operand c1 is implicitly passed as the calling object this).",
                    "2 arguments (both c1 and c2).",
                    "0 arguments.",
                    "Variable number of arguments."
                ],
                "correctAnswer": "1 argument (the right operand c2; the left operand c1 is implicitly passed as the calling object this).",
                "explanation": "For member binary operators, the left-hand operand is the calling instance (*this), so only the right-hand operand is explicitly passed as an argument."
            }
        ],
        "flashcards": [
            {
                "question": "What is operator overloading?",
                "answer": "Giving standard C++ operators custom functionality when applied to user-defined class objects."
            },
            {
                "question": "What is the difference between unary and binary operator overloading?",
                "answer": "Unary operators operate on a single operand (e.g. ++x, -x); binary operators operate on two operands (e.g. a + b, x == y)."
            },
            {
                "question": "Can you create completely new operator symbols in C++ (like **)?",
                "answer": "No. You can only overload existing C++ operators; you cannot invent new operator syntax."
            },
            {
                "question": "Why use a friend function for binary operator overloading?",
                "answer": "To allow the left-hand operand to be a primitive type or non-class object (e.g. 5 + myObject)."
            }
        ]
    },
    {
        "order": 8,
        "title": "Lab 8: Operate Under Supervision Arrays and Strings Implementation",
        "codeSnippet": "#include <iostream>\n#include <cstring>\n#include <string>\nusing namespace std;\n\nint main() {\n    // 1D Array\n    int arr[5] = {10, 20, 30, 40, 50};\n    int sum = 0;\n    for (int i = 0; i < 5; i++) sum += arr[i];\n    cout << \"Array Sum = \" << sum << endl;\n\n    // C-String Functions\n    char s1[20] = \"Hello \";\n    char s2[10] = \"World\";\n    strcat(s1, s2);\n    cout << \"Concatenated: \" << s1 << \" (Length: \" << strlen(s1) << \")\" << endl;\n\n    // C++ std::string\n    string str1 = \"Hello\";\n    string str2 = \"World\";\n    string str3 = str1 + \" \" + str2;\n    cout << \"std::string:  \" << str3 << \" (Size: \" << str3.size() << \")\" << endl;\n    return 0;\n}",
        "content": "# Lab#08\n\n## OPERATE UNDER SUPERVISION ARRAYS AND STRINGS IMPLEMENTATION\n\n### Objectives\n* Arrays\n* One-dimensional Array\n* Sorting of Arrays\n* Multi-dimensional Arrays\n* Strings\n* Initializing String Variable\n* Operations on Strings\n* String Handling Functions\n\n### Theory Overview\n\n#### Arrays:\nArrays are like structures in that they both group a number of items into a larger unit. But while a structure usually groups items of different types, an array groups items of the same type. More importantly, the items in a structure are accessed by name, while those in an array are accessed by an index number.\n\nUsing an index number to specify an item allows easy access to a large number of items. Arrays exist in almost every computer language. Arrays in C++ are similar to those in other languages, and identical to those in C.\n\nExample:\n```cpp\n#include <iostream>\n#include <conio.h>\nusing namespace std;\nint main()\n{\nint arr[10],sum=0,i;\ncout<<\"Enter 10 numbers\"<<endl;\nfor(i=0;i<10;i++)\n{\ncin>>arr[i];\nsum = sum+arr[i];\n}\ncout<<\"Sum = \"<<sum;\ngetch();\nreturn 0;\n}\n```\n\nExample 2:\n```cpp\n#include<iostream>\n#include<conio.h>\nusing namespace std;\nint main()\n{\nint arr[10][10], row, col, i, j;\ncout<<\"Enter number of row for Array (max 10) : \";\ncin>>row;\ncout<<\"Enter number of column for Array (max 10) : \";\ncin>>col;\ncout<<\"Now Enter \"<<row<<\"*\"<<col<<\" Array Elements : \";\nfor(i=0; i<row; i++)\n{\nfor(j=0; j<col; j++)\n{\ncin>>arr[i][j];\n}\n}\ncout<<\"The Array is :\\n\";\nfor(i=0; i<row; i++)\n{\nfor(j=0; j<col; j++)\n{\ncout<<arr[i][j]<<\" \";\n}\ncout<<\"\\n\";\n}\ngetch();\nreturn 0;\n}\n```\n\n#### Strings:\nThe combination of characters is called a string. In the C++ programming language, the std::string class is a standard representation for a string of text. This class alleviates many of the problems introduced by C-style strings by putting the onus of memory ownership on the string class rather than on the programmer.\n\nThe class provides some typical string operations like comparison, concatenation, find and replace, and a function for obtaining substrings\n\n| Sr.No | Function & Purpose |\n|:---|:---|\n| **1** | `strcpy(s1, s2);`<br>Copies string s2 into string s1. |\n| **2** | `strcat(s1, s2);`<br>Concatenates string s2 onto the end of string s1. |\n| **3** | `strlen(s1);`<br>Returns the length of string s1. |\n| **4** | `strcmp(s1, s2);`<br>Returns 0 if s1 and s2 are the same; less than 0 if s1<s2; greater than 0 if s1>s2. |\n| **5** | `strchr(s1, ch);`<br>Returns a pointer to the first occurrence of character ch in string s1. |\n| **6** | `strstr(s1, s2);`<br>Returns a pointer to the first occurrence of string s2 in string s1. |\n\nTable 8.1 String Functions\n\nExample:\n```cpp\n#include <iostream>\nusing namespace std;\nint main()\n{\nchar str[100];\ncout << \"Enter a string: \";\ncin >> str;\ncout << \"You entered: \" << str << endl;\ncout << \"\\nEnter another string: \";\ncin >> str;\ncout << \"You entered: \"<<str<<endl;\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\nusing namespace std;\nint main()\n{\nchar str[100];\ncout << \"Enter a string: \";\ncin.get(str, 100);\ncout << \"You entered: \" << str << endl;\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\n#include <cstring>\nusing namespace std;\nint main () {\nchar str1[10] = \"Hello\";\nchar str2[10] = \"World\";\nchar str3[10];\nint len ;\n// copy str1 into str3\nstrcpy( str3, str1);\ncout << \"strcpy( str3, str1) : \" << str3 << endl;\n// concatenates str1 and str2\nstrcat( str1, str2);\ncout << \"strcat( str1, str2): \" << str1 << endl;\n// total lenghth of str1 after concatenation\nlen = strlen(str1);\ncout << \"strlen(str1) : \" << len << endl;\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nint main () {\nstring str1 = \"Hello\";\nstring str2 = \"World\";\nstring str3;\nint len ;\n// copy str1 into str3\nstr3 = str1;\ncout << \"str3 : \" << str3 << endl;\n// concatenates str1 and str2\nstr3 = str1 + str2;\ncout << \"str1 + str2 : \" << str3 << endl;\n// total length of str3 after concatenation\nlen = str3.size();\ncout << \"str3.size() : \" << len << endl;\nreturn 0;\n}\n```\n\n### Equipment:\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program to input value in an array. Find out the total number of even and odd values entered in the array.\n\n#### Task #2\nDeclare the following two-dimensional array of type integer:\n```text\n1 2 3\n2 4 6\n3 5 -7\n-1 4 8\n```\nDisplay only the negative value from the above two dim array.\n\n#### Task #3\nStart with a program that allows the user to input a number of integers, and then stores them in an int array. Write a function called maxint () that goes through the array, element by element, looking for the largest one.\nThe function should take as arguments the address of the array and the number of elements in it, and return the index number of the largest element. The program should call this function and then display the largest element and its index number.\n\n#### Task #4:\nWrite a program to input data into a string and find out its length without using any user defined function.\n\n#### Task #5:\nWrite a program that read a string and count the number of characters in it.\n",
        "quizzes": [
            {
                "question": "What is the return value of strcmp(s1, s2) when string s1 is lexicographically identical to s2?",
                "options": [
                    "0",
                    "1",
                    "-1",
                    "The length of the string"
                ],
                "correctAnswer": "0",
                "explanation": "strcmp returns 0 if both strings are equal, a negative integer if s1 < s2, and a positive integer if s1 > s2."
            },
            {
                "question": "In C++, how is a null-terminated C-style string represented in memory?",
                "options": [
                    "As a contiguous character array ending with the null terminator character '\\0'.",
                    "As a 4-byte pointer followed by an integer storing string length.",
                    "As a linked list of ASCII characters with no ending delimiter.",
                    "As a vector of unicode code points."
                ],
                "correctAnswer": "As a contiguous character array ending with the null terminator character '\\0'.",
                "explanation": "C-style strings are null-terminated character arrays where '\\0' (ASCII 0) marks the end of the text."
            },
            {
                "question": "In Lab 8 Task 2, what are the coordinates and values of the negative elements in the 4x3 array?",
                "options": [
                    "arr[2][2] = -7 and arr[3][0] = -1",
                    "arr[0][0] = -1 and arr[1][1] = -7",
                    "arr[3][2] = -7 and arr[0][3] = -1",
                    "Only arr[3][0] is negative"
                ],
                "correctAnswer": "arr[2][2] = -7 and arr[3][0] = -1",
                "explanation": "In 0-indexed matrices, row 2 column 2 contains -7, and row 3 column 0 contains -1."
            }
        ],
        "flashcards": [
            {
                "question": "What is the difference between strcpy and strcat?",
                "answer": "strcpy(dest, src) overwrites dest with src; strcat(dest, src) appends src to the end of dest."
            },
            {
                "question": "Why is std::string preferred over char[] in modern C++?",
                "answer": "std::string automatically manages dynamic memory allocation, resizing, and boundaries, preventing buffer overflow bugs."
            },
            {
                "question": "What does cin.get(str, 100) allow that cin >> str does not?",
                "answer": "cin.get reads an entire line including whitespace spaces up to 99 characters or a newline."
            },
            {
                "question": "What does strstr(s1, s2) return in C++?",
                "answer": "A pointer to the first occurrence of substring s2 in string s1, or nullptr/NULL if not found."
            }
        ]
    },
    {
        "order": 9,
        "title": "Lab 9: Imitate Static Data Members and Member Functions",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nclass SavingsAccount {\nprivate:\n    double savingsBalance;\n    static double annualInterestRate; // Shared across all instances\npublic:\n    SavingsAccount(double balance): savingsBalance(balance) {}\n\n    void calculateMonthlyInterest() {\n        savingsBalance += savingsBalance * (annualInterestRate / 12.0);\n    }\n\n    void displayBalance() const {\n        cout << \"Balance: $\" << savingsBalance << endl;\n    }\n\n    static void modifyInterestRate(double newRate) {\n        annualInterestRate = newRate;\n    }\n};\n\ndouble SavingsAccount::annualInterestRate = 0.03; // 3%\n\nint main() {\n    SavingsAccount saver1(2000.00), saver2(3000.00);\n    saver1.calculateMonthlyInterest();\n    saver2.calculateMonthlyInterest();\n    saver1.displayBalance();\n    saver2.displayBalance();\n    return 0;\n}",
        "content": "# Lab#09\n\n## IMITATE STATIC DATA MEMBERS AND MEMBER FUNCTIONS\n\n### Objectives\n* Objects and Classes\n* Defining a class\n* Members of a class\n* Data members\n* Member Functions\n* Objects\n* Declaring objects of a class\n* Calling Member Functions\n\n### Theory Overview\nA class is a collection of data and functions. The data items and functions are defined within the class. The functions are written to work upon data items and each function has a unique relationship with the data items of the class. An object is said to be an instance of a class.\nClasses are defined to create user-defined data types. Defining a class specifies its data members and relationship between the data items through its functions.\nA class is defined in C++ using keyword class followed by the name of class.\nThe body of class is defined inside the curly brackets and terminated by a semicolon at the end.\n\nExample:\n```cpp\nclass className\n{\n// some data\n// some functions\n};\nclass Test\n{\nprivate: int data1; float data2;\npublic: void function1()\n{ data1 = 2; }\nfloat function2()\n{\ndata2 = 3.5;\nreturn data2;\n}\n};\n```\n\nExample:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass Cars { // Access specifier public:\n// Data Members\nstring car_model;\n// Member Functions()\nvoid printname()\n{\ncout << \"Car name is: \" << car_model<< endl;\n} };\nint main() {\n// Declare an object of class geeks\nCars obj1;\n// accessing data member\nobj1.car_model = \"BMW\";\n// accessing member function\nobj1.printname();\nreturn 0;\n}\n```\n\n### Basic Program of Classes\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass stud\n{\npublic:\nchar name[30],clas[10];\nint rol,age;\nvoid enter()\n{\ncout<<\"Enter Student Name: \";\ncin>>name;\ncout<<\"Enter Student Age: \";\ncin>>age;\ncout<<\"Enter Student Roll number: \";\ncin>>rol;\ncout<<\"Enter Student Class: \";\ncin>>clas;\n}\nvoid display()\n{\ncout<<\"\\n Age\\tName\\tR.No.\\tClass\";\ncout<<\"\\n\"<<age<<\"\\t\"<<name<<\"\\t\"<<rol<<\"\\t\"<<clas<<endl;\n}\n};\nint main() {\nclass stud s;\ns.enter();\ns.display();\nreturn 0;\n}\n```\n\n### Program of Default Constructor\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass construct {\npublic: int a, b;\n// Default Constructor\nconstruct () { a = 10; b = 20;\n}\n};\nint main()\n{\n// Default constructor called automatically\n// when the object is created\nconstruct c;\ncout << \"a: \"<< c.a << endl << \"b: \"<< c.b << endl;\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task (in this task you will use static data members and functions)\nCreate a SavingsAccount class. Use a static data member annualInterestRate to store the annual interest rate for each of the savers. Each member of the class contains a private data member savingsBalance indicating the amount the saver currently has on deposit. Provide member function calculateMonthlyInterest that calculates the monthly interest by multiplying the savingsbalance by annualInterestRate divided by 12; this interest should be added to savingsBalance. Provide a static member function modifyInterestRate that sets the static annualInterestRate to a new value.\n\nWrite a driver program (main program) to test class SavingsAccount.\n• Instantiate two different objects of class SavingsAccount, saver1 and saver2, with balances of $2000.00 and $3000.00, respectively.\n• Set the annualInterestRate to 3 percent.\n• Then calculate the monthly interest and print the new balances for each of the savers.\nThen set the annualInterestRate to 7 percent, calculate the next month's interest and print the new balances for each of the savers\n",
        "quizzes": [
            {
                "question": "Where must a static data member of a C++ class be explicitly defined and initialized?",
                "options": [
                    "Outside the class definition at global/file scope using the scope resolution operator (::).",
                    "Inside the class's default constructor.",
                    "Inside main() before calling any methods.",
                    "Inside a header file enclosed in an anonymous namespace."
                ],
                "correctAnswer": "Outside the class definition at global/file scope using the scope resolution operator (::).",
                "explanation": "Static member variables belong to the class rather than instances, so storage must be allocated and initialized once in file scope outside the class."
            },
            {
                "question": "Which of the following restrictions applies to static member functions in C++?",
                "options": [
                    "They do not have a 'this' pointer and can only directly access other static members of the class.",
                    "They cannot accept any parameters.",
                    "They can only be called if at least one object of the class has been instantiated.",
                    "They must always return an integer value."
                ],
                "correctAnswer": "They do not have a 'this' pointer and can only directly access other static members of the class.",
                "explanation": "Because static functions are not bound to any individual object instance, they do not receive a this pointer and cannot access non-static instance fields directly."
            },
            {
                "question": "In Lab 9's SavingsAccount problem, what is saver1's balance after 1 month at 3% starting from $2000.00?",
                "options": [
                    "$2005.00",
                    "$2060.00",
                    "$2015.00",
                    "$2002.50"
                ],
                "correctAnswer": "$2005.00",
                "explanation": "Monthly interest = 2000.00 * (0.03 / 12) = 2000.00 * 0.0025 = $5.00. New balance = $2000.00 + $5.00 = $2005.00."
            }
        ],
        "flashcards": [
            {
                "question": "What is a static data member in C++?",
                "answer": "A class variable shared by all instances of the class; only one copy exists in memory throughout execution."
            },
            {
                "question": "How is a static member function called without an object?",
                "answer": "Using the class name and scope resolution operator: ClassName::staticFunction();"
            },
            {
                "question": "Can a static member function access non-static member variables?",
                "answer": "No. Non-static variables require an object instance, which static functions do not have."
            },
            {
                "question": "What happens to the static variable value when modified by one object?",
                "answer": "The updated value is immediately reflected across all existing and future objects of that class."
            }
        ]
    },
    {
        "order": 10,
        "title": "Lab 10: Practice Inheritance in Object Oriented Programming",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nclass Polygon {\nprotected:\n    int width, height;\npublic:\n    void set_values(int a, int b) { width = a; height = b; }\n};\n\nclass Rectangle: public Polygon {\npublic:\n    int area() { return width * height; }\n};\n\nclass Triangle: public Polygon {\npublic:\n    int area() { return (width * height) / 2; }\n};\n\nint main() {\n    Rectangle rect;\n    Triangle trgl;\n    rect.set_values(4, 5);\n    trgl.set_values(4, 5);\n    cout << \"Rectangle area: \" << rect.area() << endl; // 20\n    cout << \"Triangle area:  \" << trgl.area() << endl; // 10\n    return 0;\n}",
        "content": "# Lab#10\n\n## PRACTICE INHERITANCE IN OBJECT ORIENTED PROGRAMMING\n\n### Objectives\n* Inheritance\n* Derive Class\n* Base Class\n* Single Inheritance\n* Specifying the derived class\n* Accessing Base class Specifier\n* Overriding Member Functions\n\n### Theory Overview\nInheritance is probably the most powerful feature of Object-Oriented Programming, after classes themselves. Inheritance is the process of creating new classes, called derived classes, from existing or base classes. The derived class inherits all the capabilities of the base class but can add embellishments and refinements of its own. The base class is unchanged by this process. An inherited class is called a subclass of its parent class or super class. The term \"inheritance\" is loosely used for both class-based and prototype-based programming, but in narrow use is reserved for class-based programming (one class inherits from another), with the corresponding technique in prototype-based programming being instead called delegation (one object delegates to another).\n\nMany object-oriented programming languages permit a class or object to replace the implementation of an aspect—typically a behavior—that it has inherited. This process is usually called overriding. Overriding introduces a complication: which version of the behavior does an instance of the inherited class use—the one that is part of its own class, or the one from the parent (base) class? The answer varies between programming languages, and some languages provide the ability to indicate that a particular behavior is not to be overridden and should behave as defined by the base class. For instance, in C#, the base method or property can only be overridden in a subclass if it is marked with the virtual, abstract, or override modifier. An alternative to overriding is hiding the inherited code.\n\nExample:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass Person\n{\npublic:\nstring profession;\nint age;\nPerson(): profession(\"unemployed\"), age(16) { }\nvoid display()\n{\ncout << \"My profession is: \" << profession << endl;\ncout << \"My age is: \" << age << endl;\nwalk();\ntalk();\n}\nvoid walk() { cout << \"I can walk.\" << endl; }\nvoid talk() { cout << \"I can talk.\" << endl; }\n};\n// MathsTeacher class is derived from base class Person.\nclass MathsTeacher : public Person\n{\npublic:\nvoid teachMaths() { cout << \"I can teach Maths.\" << endl; }\n};\n// Footballer class is derived from base class Person.\nclass Footballer : public Person\n{\npublic:\nvoid playFootball() { cout << \"I can play Football.\" << endl; }\n};\nint main()\n{\nMathsTeacher teacher;\nteacher.profession = \"Teacher\";\nteacher.age = 23;\nteacher.display();\nteacher.teachMaths();\nFootballer footballer;\nfootballer.profession = \"Footballer\";\nfootballer.age = 19;\nfootballer.display();\nfootballer.playFootball();\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\n#include <string>\nusing namespace std;\nclass Polygon {\nprotected:\nint width, height;\npublic:\nvoid set_values (int a, int b)\n{ width=a; height=b;}\n};\nclass Rectangle: public Polygon {\npublic:\nint area ()\n{ return width * height; }\n};\nclass Triangle: public Polygon {\npublic:\nint area ()\n{ return width * height / 2; }\n};\nint main () {\nRectangle rect;\nTriangle trgl;\nrect.set_values (4,5);\ntrgl.set_values (4,5);\ncout << rect.area() << '\\n';\ncout << trgl.area() << '\\n';\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program to prepare the payroll of an employee by using the single inheritance. The base class name is \"employee\" and the derived class name is \"allowance\".\n\n#### Task #2\nWrite a program that computes the square and cube of the given number using the concept of single inheritance. Design the function for computing square in the base class and function for computing cube in the derived class.\nThe output of the program should be like:\n```text\nEnter the number for which you want to take square = 5\nEnter the number for which you want to take cube = 5\nSquare of the number = 25\nCube of the number = 125\n```\n\n#### Task #3\nCreate a base class Employee that stores name (a string) and identification number (type integer) of an employee. From this class derive three more classes:\n* Manager: that stores title and salary (string) of the manager.\n* Scientist: that stores number of articles they have published (type integer) and salary (a string) of the scientist.\n* Clerks: that stores the overtime (type int) of the clerk.\nEach of the four classes should have input () function to input data from the user, and show () function to display data. Write a main function to test the three classes by creating instances of them, asking the user to fill in data with input (), and then displaying data with show () function.\n",
        "quizzes": [
            {
                "question": "What is the purpose of the 'protected' access specifier in a C++ base class?",
                "options": [
                    "It allows derived classes to access the members directly while keeping them inaccessible to external code.",
                    "It makes variables readable but prevents writing to them.",
                    "It hides members from derived classes while making them public to main().",
                    "It stores variables in encrypted flash memory."
                ],
                "correctAnswer": "It allows derived classes to access the members directly while keeping them inaccessible to external code.",
                "explanation": "Protected members are accessible to member functions of the class and its derived classes, but private to external non-member code."
            },
            {
                "question": "In C++, what type of inheritance occurs when class B inherits from class A directly (class B : public A)?",
                "options": [
                    "Single inheritance",
                    "Multiple inheritance",
                    "Hierarchical inheritance",
                    "Hybrid inheritance"
                ],
                "correctAnswer": "Single inheritance",
                "explanation": "Single inheritance is when a derived class inherits directly from exactly one base class."
            },
            {
                "question": "When an object of derived class Rectangle is instantiated in C++, in what order are constructors executed?",
                "options": [
                    "The base class (Polygon) constructor executes first, followed by the derived class (Rectangle) constructor.",
                    "The derived class constructor executes first, followed by the base class constructor.",
                    "Only the derived class constructor executes; the base class constructor is ignored.",
                    "The order is undefined and varies at runtime."
                ],
                "correctAnswer": "The base class (Polygon) constructor executes first, followed by the derived class (Rectangle) constructor.",
                "explanation": "Constructors execute in hierarchical order starting from the root base class down to the most derived class."
            }
        ],
        "flashcards": [
            {
                "question": "What is inheritance in OOP?",
                "answer": "A mechanism where a new derived class inherits data members and member functions from an existing base class, enabling code reuse."
            },
            {
                "question": "What syntax is used to derive class Derived from Base publicly in C++?",
                "answer": "class Derived : public Base { ... };"
            },
            {
                "question": "What is member overriding?",
                "answer": "When a derived class provides its own implementation of a member function that has the same signature as a function in its base class."
            },
            {
                "question": "Can private members of a base class be accessed directly by a derived class?",
                "answer": "No. Private members are accessible only within the base class itself (use protected if derived access is needed)."
            }
        ]
    },
    {
        "order": 11,
        "title": "Lab 11: Practice Multi-level and Multiple Inheritance",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\n// Base class 1\nclass Mammal {\npublic:\n    Mammal() { cout << \"Mammals can give direct birth.\" << endl; }\n};\n\n// Base class 2\nclass WingedAnimal {\npublic:\n    WingedAnimal() { cout << \"Winged animal can flap.\" << endl; }\n};\n\n// Multiple Inheritance\nclass Bat: public Mammal, public WingedAnimal {\npublic:\n    Bat() { cout << \"Bat is both a mammal and winged animal!\" << endl; }\n};\n\nint main() {\n    Bat b1;\n    return 0;\n}",
        "content": "# Lab#11\n\n## PRACTICE MULTI-LEVEL AND MULTIPLE INHERITANCE\n\n### Objective:\n* Multiple inheritance\n\n### Theory Overview\nInheritance is the process of inheriting properties of objects of one class by objects of another class. The class which inherits the properties of another class is called Derived or Child or Sub class and the class whose properties are inherited is called Base or Parent or Super class. When a class is derived from a class which is also derived from another class, i.e. a class having more than one parent classes, such inheritance is called Multilevel Inheritance. The level of inheritance can be extended to any number of levels depending upon the relation. Multilevel inheritance is similar to relation between grandfather, father and child. In C++ programming, not only you can derive a class from the base class but you can also derive a class from the derived class. This form of inheritance is known as multilevel inheritance.\n\n![Fig 11.1 Multiple Inheritance](assets/images/university/oop/fig11_1_multiple_inheritance.png)\n\nFig 11.1 Multiple Inheritance\n\nExample\n```cpp\n#include <iostream>\nusing namespace std;\nclass A\n{\npublic:\nvoid display()\n{\ncout<<\"Base class content.\";\n}\n};\nclass B : public A\n{\n};\nclass C : public B\n{\n};\nint main()\n{\nC obj;\nobj.display();\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\nusing namespace std;\nclass Mammal {\npublic:\nMammal()\n{\ncout << \"Mammals can give direct birth.\" << endl;\n}\n};\nclass WingedAnimal {\npublic:\nWingedAnimal()\n{\ncout << \"Winged animal can flap.\" << endl;\n}\n};\nclass Bat: public Mammal, public WingedAnimal {\n};\nint main()\n{\nBat b1;\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program to input the record of a student and print on the screen by using multiple inheritance.\n\n#### Task #2\nWrite a program that consists of two classes' employee and student. Create three other classes: manager, scientist and laborer. Modify manager and scientist so that they inherit from both employee and student classes. The laborer class is inherited only from employee class. The program output should be like this:\n```text\nEnter data for manager 1\nEnter last name:\nEnter number:\nEnter title:\nEnter name of school or university:\nEnter highest degree earned\n(High school, Bachelor's, Master's, PhD):\nEnter data for scientist 1\nEnter last name:\nEnter number:\nEnter highest degree earned\n(High school, Bachelor's, Master's, PhD):\nEnter data for scientist 2\nEnter last name:\nEnter number:\nEnter highest degree earned\n(High school, Bachelor's, Master's, PhD):\nEnter data for laborer 1\nEnter last name:\nEnter number:\n```\n\n#### Task #3\nImagine a publishing company that markets both book and audiocassette versions of its works. Create a class publication that stores the title (a string) and price (type float) of a publication. From this class derive two classes: book, which adds a page count (type int); and tape, which adds a playing time in minutes (type float). Each of these three classes should have a getdata() function to get its data from the user at the keyboard, and a putdata() function to display its data. Write a main() program to test the book and tape classes by creating instances of them, asking the user to fill in data with getdata(), and then displaying the data with putdata().\n",
        "quizzes": [
            {
                "question": "What is Multiple Inheritance in C++?",
                "options": [
                    "A derived class inheriting directly from two or more base classes simultaneously.",
                    "A class having multiple member variables of the same type.",
                    "A program having multiple derived classes from a single base class.",
                    "Inheriting through three or more linear generations (A -> B -> C)."
                ],
                "correctAnswer": "A derived class inheriting directly from two or more base classes simultaneously.",
                "explanation": "Multiple inheritance occurs when a single child class inherits from multiple parent classes (e.g. class Bat : public Mammal, public WingedAnimal)."
            },
            {
                "question": "What is the Diamond Problem in C++ multiple inheritance?",
                "options": [
                    "Ambiguity caused when two base classes inherit from a common ancestor, causing duplicate subobjects in the derived class.",
                    "A syntax error caused when more than 4 classes are inherited.",
                    "A memory leak caused by virtual destructors.",
                    "Inability to overload constructors in derived classes."
                ],
                "correctAnswer": "Ambiguity caused when two base classes inherit from a common ancestor, causing duplicate subobjects in the derived class.",
                "explanation": "When class D inherits from B and C, both of which inherit from A, D contains two copies of A. C++ resolves this using virtual base classes (virtual inheritance)."
            },
            {
                "question": "In Lab 11 Task 2, which derived class inherits from only ONE base class?",
                "options": [
                    "laborer (inherits only from employee)",
                    "manager (inherits from employee and student)",
                    "scientist (inherits from employee and student)",
                    "All classes inherit from both"
                ],
                "correctAnswer": "laborer (inherits only from employee)",
                "explanation": "According to the lab specification, laborer inherits exclusively from employee, while manager and scientist inherit from both employee and student."
            }
        ],
        "flashcards": [
            {
                "question": "What is the difference between multilevel and multiple inheritance?",
                "answer": "Multilevel inheritance is linear across generations (Grandfather -> Father -> Child); multiple inheritance is lateral with multiple parents (Parent1 + Parent2 -> Child)."
            },
            {
                "question": "What is the syntax for multiple inheritance in C++?",
                "answer": "class Derived : public Base1, public Base2 { ... };"
            },
            {
                "question": "How do you solve ambiguity when both base classes share a member with the same name in multiple inheritance?",
                "answer": "Use the scope resolution operator: obj.Base1::display() or obj.Base2::display()."
            },
            {
                "question": "In multiple inheritance, in what order are base class constructors executed?",
                "answer": "In the order the base classes are listed in the derived class declaration line (left to right)."
            }
        ]
    },
    {
        "order": 12,
        "title": "Lab 12: Practice Polymorphism and Virtual Functions in Object Oriented Programming",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\nclass Shape {\nprotected:\n    int width, height;\npublic:\n    Shape(int a = 0, int b = 0): width(a), height(b) {}\n    virtual int area() { // Virtual function enables runtime polymorphism\n        cout << \"Parent class area: \" << endl;\n        return 0;\n    }\n};\n\nclass Rectangle: public Shape {\npublic:\n    Rectangle(int a = 0, int b = 0): Shape(a, b) {}\n    int area() override {\n        cout << \"Rectangle area: \" << (width * height) << endl;\n        return width * height;\n    }\n};\n\nclass Triangle: public Shape {\npublic:\n    Triangle(int a = 0, int b = 0): Shape(a, b) {}\n    int area() override {\n        cout << \"Triangle area: \" << (width * height / 2) << endl;\n        return width * height / 2;\n    }\n};\n\nint main() {\n    Shape *shape;\n    Rectangle rec(10, 7);\n    Triangle tri(10, 5);\n\n    shape = &rec;\n    shape->area(); // Calls Rectangle::area() at runtime!\n\n    shape = &tri;\n    shape->area(); // Calls Triangle::area() at runtime!\n    return 0;\n}",
        "content": "# Lab#12\n\n## PRACTICE POLYMORPHISM AND VIRTUAL FUNCTIONS IN OBJECT ORIENTED PROGRAMMING\n\n### Objectives:\n* Polymorphism\n* Virtual functions\n\n### Theory Overview\nPolymorphism is another important feature of object oriented programming. In polymorphism, the member functions with the same name are defined in each derived class and also in the base class.\nPloy means may and morphism means form. Polymorphism is therefore the ability for objects of different classes related by inheritance to response differently to the same function call.\nVirtual means existing in appearance but not in reality. When virtual functions are used, a program that appears to be calling a function of one class may in reality be calling a function of a different class. It is an amazing capability: Completely different functions are executed by the same function call.\n\nExample:\n```cpp\n#include<iostream>\n#include<string>\nusing namespace std;\nclass Addition\n{\npublic:\nvoid sum(int a, int b)\n{\ncout<<a+b;\n}\nvoid sum(int a, int b, int c)\n{\ncout<<a+b+c;\n}\n};\nint main()\n{\nAddition obj;\nobj.sum(10, 20);\ncout<<endl;\nobj.sum(10, 20, 30);\nreturn 0;\n}\n```\n\nExample:\n```cpp\n#include <iostream>\nusing namespace std;\nclass Shape {\nprotected:\nint width, height;\npublic:\nShape( int a = 0, int b = 0){\nwidth = a;\nheight = b;\n}\nint area() {\ncout << \"Parent class area :\" <<endl;\nreturn 0;\n}\n};\nclass Rectangle: public Shape {\npublic:\nRectangle( int a = 0, int b = 0):Shape(a, b) { }\nint area () {\ncout << \"Rectangle class area :\" <<endl;\nreturn (width * height);\n}\n};\nclass Triangle: public Shape {\npublic:\nTriangle( int a = 0, int b = 0):Shape(a, b) { }\nint area () {\ncout << \"Triangle class area :\" <<endl;\nreturn (width * height / 2);\n}\n};\n// Main function for the program\nint main() {\nShape *shape;\nRectangle rec(10,7);\nTriangle tri(10,5);\n// store the address of Rectangle\nshape = &rec;\n// call rectangle area.\nshape->area();\n// store the address of Triangle\nshape = &tri;\n// call triangle area.\nshape->area();\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program that consists of an abstract class \"Polygon\". This class contains two member functions:\n* set_values (pass two double type values as an argument of the function)\n* area (declare it as pure virtual function)\nDerive two classes \"Rectangle\" and \"Triangle\" from it. Calculate the area of rectangle (width*height) and triangle (width*height/2) and then display it.\n\n#### Task #2\nWrite a program using Polymorphism technique to define the class of Person as a base class and hence derive Student and Lecturer classes from it. The base class consists of two pure virtual functions: getdata and show. Override these two functions in the derive classes.\n\n#### Task #3\nWrite a program using polymorphism technique to define the class \"Main\" as base class. The base class contains two member functions: \"getdata\" to input data from the user and another function \"float result\" which is declared as virtual.\nDerive Addition, Subtraction, Multiplication and Division from the base class Main. Each of these four derive classes contain the function \"float result\". Calculate the sum, difference, product and division of the numbers entered by the user.\n\n#### Task #4\nWrite a program that contains a class \"derived\" from the base class \"base\". The \"base\" should have a virtual function func () and it should be overridden in \"derived\". Try to call fun() from the constructor of the derived class and display the result.\n",
        "quizzes": [
            {
                "question": "What is a pure virtual function in C++?",
                "options": [
                    "A virtual function declared with = 0 in the base class, having no implementation and making the class abstract.",
                    "A function that only accepts void* arguments.",
                    "A function implemented completely in assembly code.",
                    "A function that cannot be overridden by derived classes."
                ],
                "correctAnswer": "A virtual function declared with = 0 in the base class, having no implementation and making the class abstract.",
                "explanation": "A pure virtual function (virtual void func() = 0;) forces derived classes to provide an implementation and turns the containing class into an abstract class."
            },
            {
                "question": "How does C++ achieve runtime dynamic dispatch for virtual functions behind the scenes?",
                "options": [
                    "Through a Virtual Method Table (vtable) and a hidden virtual pointer (vptr) inside each object.",
                    "By recompiling the function every time it is called.",
                    "By querying the operating system kernel on every call.",
                    "By storing the source code text inside the binary file."
                ],
                "correctAnswer": "Through a Virtual Method Table (vtable) and a hidden virtual pointer (vptr) inside each object.",
                "explanation": "Compilers construct a vtable containing function pointers for each class with virtual functions. Each object has a hidden vptr pointing to its class's vtable."
            },
            {
                "question": "Why should base class destructors almost always be declared virtual?",
                "options": [
                    "To ensure the derived class destructor is properly invoked when deleting a derived object via a base class pointer.",
                    "To prevent the program from running out of stack memory.",
                    "Because non-virtual destructors cannot be called by main().",
                    "To allow destructors to take arguments."
                ],
                "correctAnswer": "To ensure the derived class destructor is properly invoked when deleting a derived object via a base class pointer.",
                "explanation": "Deleting a derived instance through a base pointer with a non-virtual destructor results in undefined behavior and resource/memory leaks."
            }
        ],
        "flashcards": [
            {
                "question": "What keyword enables runtime polymorphism in C++?",
                "answer": "virtual"
            },
            {
                "question": "What is an abstract class in C++?",
                "answer": "A class containing at least one pure virtual function (= 0); it cannot be directly instantiated."
            },
            {
                "question": "What is compile-time vs run-time polymorphism?",
                "answer": "Compile-time polymorphism is resolved at compile time via function/operator overloading; run-time polymorphism is resolved dynamically via virtual functions."
            },
            {
                "question": "What is the override keyword used for in modern C++?",
                "answer": "It explicitly tells the compiler that a member function is intended to override a virtual function from a base class, catching typo bugs."
            }
        ]
    },
    {
        "order": 13,
        "title": "Lab 13: Operate Under Supervision File Handling, Read & Write Operations and Error Handling Mechanism",
        "codeSnippet": "#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\n\ndouble division(int a, int b) {\n    if (b == 0) {\n        throw \"Division by zero condition!\";\n    }\n    return (double)a / b;\n}\n\nint main() {\n    // 1. File Writing\n    ofstream outfile(\"example.txt\");\n    if (outfile.is_open()) {\n        outfile << \"66 33 16\\n13 29 12\\n\";\n        outfile.close();\n    }\n\n    // 2. Exception Handling\n    try {\n        cout << \"10 / 2 = \" << division(10, 2) << endl;\n        cout << \"10 / 0 = \" << division(10, 0) << endl;\n    } catch (const char* msg) {\n        cerr << \"Error Caught: \" << msg << endl;\n    } catch (...) {\n        cerr << \"Catch-all handler executed!\" << endl;\n    }\n    return 0;\n}",
        "content": "# Lab#13\n\n## OPERATE UNDER SUPERVIOSION FILE HANDLING, READ & WRITE OPERATIONS AND EXCEPTION HANDLING\n\n### Objectives:\n* The stream class hierarchy\n* Exception Handling\n\n### Theory Overview\nA stream is a general name given to a flow of data. In C++ a stream is represented by an object of a particular class. We've already made extensive use of some stream classes. The extraction operator >> is a member of the istream class, and the insertion operator << is a member of the ostream class.\nBoth of these classes are derived from the ios class. The cout object, representing the standard output stream, which is usually directed to the video display, is a predefined object of the ostream_withassign class, which is derived from the ostream class. Similarly cin is an object of the istream_withassign class, which is derived from istream.\nThe classes used for input and output to the video display and keyboard are declared in the header file IOSTREAM, which we routinely included in our examples in previous chapters.\nThe classes used specifically for disk file I/O are declared in the file FSTREAM. The stream classes are arranged in a rather complex hierarchy.\n\nExample:\n```cpp\n#include <iostream>\n#include <fstream>\nusing namespace std;\nint main()\n{\nifstream fin;\nfin.open(\"out.txt\");\nchar ch;\nwhile(!fin.eof())\n{\nfin.get(ch);\ncout << ch;\n}\nfin.close();\nreturn 0;\n}\n```\n\nExample 2:\n```cpp\n// Writing on a Text File\n#include <iostream>\n#include <fstream>\nusing namespace std;\nint main () {\nofstream myfile (\"example.txt\");\nif (myfile.is_open())\n{\nmyfile << \"This is a line.\\n\";\nmyfile << \"This is another line.\\n\";\nmyfile.close();\n}\nelse cout << \"Unable to open file\";\nreturn 0;\n}\n```\n\nExample 3:\n```cpp\n// Reading on a Text File\n#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\nint main () {\nstring line;\nifstream myfile (\"example.txt\");\nif (myfile.is_open())\n{\nwhile ( getline (myfile,line) )\n{\ncout << line << '\\n';\n}\nmyfile.close();\n}\nelse cout << \"Unable to open file\";\nreturn 0;\n}\n```\n\nC++ has a mechanism for capturing and handling errors called exceptions. It uses the keywords try, throw and catch (which mean you can't use these words as variable names). In brief, it works like this: A function try's to get through a piece of code. If the code has a problem, it throws something (like a character string, number, or a class) that the calling function must catch and process. A simple example is\n\nExample 1:\n```cpp\n#include <iostream>\nusing namespace std;\nint main()\n{\nint x = -1;\n// Some code\ncout << \"Before try \\n\";\ntry {\ncout << \"Inside try \\n\";\nif (x < 0)\n{\nthrow x;\ncout << \"After throw (Never executed) \\n\";\n}\n}\ncatch (int x ) {\ncout << \"Exception Caught \\n\";\n}\ncout << \"After catch (Will be executed) \\n\";\nreturn 0;\n}\n```\n\nThere is a special catch block called 'catch all' catch(...) that can be used to catch all types of exceptions. For example, in the following program, an int is thrown as an exception, but there is no catch block for int, so catch(...) block will be executed.\n\n### Throwing Exceptions\nExceptions can be thrown anywhere within a code block using throw statement. The operand of the throw statement determines a type for the exception and can be any expression and the type of the result of the expression determines the type of exception thrown.\nFollowing is an example of throwing an exception when dividing by zero condition occurs:\n```cpp\ndouble division(int a, int b) {\nif( b == 0 ) {\nthrow \"Division by zero condition!\";\n}\nreturn (a/b);\n}\n```\n\n### Catching Exceptions\nThe catch block following the try block catches any exception. You can specify what type of exception you want to catch and this is determined by the exception declaration that appears in parentheses following the keyword catch.\n```cpp\ntry {\n// protected code\n} catch( ExceptionName e ) {\n// code to handle ExceptionName exception\n}\n```\nAbove code will catch an exception of ExceptionName type. If you want to specify that a catch block should handle any type of exception that is thrown in a try block, you must put an ellipsis, ..., between the parentheses enclosing the exception declaration as follows −\n```cpp\ntry {\n// protected code\n} catch(...) {\n// code to handle any exception\n}\n```\n\nThe following is an example, which throws a division by zero exception and we catch it in catch block.\nExample:\n```cpp\n#include <iostream>\nusing namespace std;\ndouble division(int a, int b) {\nif( b == 0 ) {\nthrow \"Division by zero condition!\";\n}\nreturn (a/b);\n}\nint main () {\nint x = 50;\nint y = 0;\ndouble z = 0;\ntry {\nz = division(x, y);\ncout << z << endl;\n} catch (const char* msg) {\ncerr << msg << endl;\n}\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program to read a text file, one character at a time, and display the contents on the screen.\n\n#### Task #2\nWrite a program to write any of the given string into a disk file.\n\n#### Task #3\nWrite a program to read data from text file, one character at a time. Find out the total number of characters into the file and print the result on the screen.\n\n#### Task #4\na) Create a text file with file name \"num.txt\" . Write three numbers in each line as shown below:\n```text\n66 33 16\n13 29 12\n```\nb) Write a program to read three numbers from each line, calculate the sum and store the result in the file \"sum.txt\" as shown below:\n```text\n66 33 16 115\n13 29 12 54\n```\n\n#### Task #5\nWrite a program which throws a division by zero exception and catch it in catch block.\n\n#### Task #6\nWrite a program for Exceptional Handling Divide by Zero\n",
        "quizzes": [
            {
                "question": "Which C++ header file must be included to work with disk file streams (ifstream and ofstream)?",
                "options": [
                    "<fstream>",
                    "<iostream>",
                    "<file.h>",
                    "<stdlib.h>"
                ],
                "correctAnswer": "<fstream>",
                "explanation": "<fstream> defines file stream classes including ifstream (file reading), ofstream (file writing), and fstream (bidirectional)."
            },
            {
                "question": "What is the purpose of the catch(...) block in C++ exception handling?",
                "options": [
                    "It acts as a catch-all block that handles any type of exception thrown within the try block.",
                    "It catches only unhandled pointers to integers.",
                    "It forces the CPU to ignore all hardware interrupts.",
                    "It rethrows the exception directly to the operating system."
                ],
                "correctAnswer": "It acts as a catch-all block that handles any type of exception thrown within the try block.",
                "explanation": "catch(...) uses the ellipsis syntax to match any uncaught exception type that was not caught by preceding catch blocks."
            },
            {
                "question": "In Lab 13 Task 4, what is the computed sum for the numbers in line 1 (66 33 16)?",
                "options": [
                    "115",
                    "105",
                    "125",
                    "99"
                ],
                "correctAnswer": "115",
                "explanation": "66 + 33 + 16 = 115. For line 2: 13 + 29 + 12 = 54."
            }
        ],
        "flashcards": [
            {
                "question": "What is the difference between ifstream and ofstream?",
                "answer": "ifstream is an input file stream used for reading data from files; ofstream is an output file stream used for writing data to files."
            },
            {
                "question": "What three keywords form the foundation of C++ exception handling?",
                "answer": "try, throw, and catch."
            },
            {
                "question": "What happens if an exception is thrown and no matching catch block is found?",
                "answer": "std::terminate() is called, aborting program execution immediately."
            },
            {
                "question": "How do you check if a file stream was successfully opened in C++?",
                "answer": "Using the myfile.is_open() member function."
            }
        ]
    },
    {
        "order": 14,
        "title": "Lab 14: Practice Designing of Class Templates",
        "codeSnippet": "#include <iostream>\nusing namespace std;\n\n// Function Template\ntemplate <class T>\nT add(T a, T b) {\n    return a + b;\n}\n\n// Class Template\ntemplate <class T>\nclass Arithmetic {\n    T a, b;\npublic:\n    Arithmetic(T x, T y): a(x), b(y) {}\n    T add() { return a + b; }\n    T subtract() { return a - b; }\n    T multiply() { return a * b; }\n    T divide() { return (b != 0) ? (a / b) : 0; }\n};\n\nint main() {\n    cout << \"add(2, 3) = \" << add(2, 3) << endl;\n    cout << \"add(2.3f, 1.2f) = \" << add(2.3f, 1.2f) << endl;\n\n    Arithmetic<float> calc(15.5f, 5.0f);\n    cout << \"Add: \" << calc.add() << \" Multiply: \" << calc.multiply() << endl;\n    return 0;\n}",
        "content": "# Lab#14\n\n## PRACTICE DESIGNING OF CLASS TEMPLATE\n\n### Objectives:\n* To understand how to develop classes without defining specific objects\n* To understand Vector in Class Templates\n* To understand Class Templates while working with Stacks\n\n### Theory Overview\nTemplates are a feature of the C++ programming language that allows functions and classes to operate with generic types. This allows a function or class to work on many different data types without being rewritten for each one.\nTemplates are of great utility to programmers in C++, especially when combined with multiple inheritance and operator overloading. The C++ Standard Library provides many useful functions within a framework of connected templates.\nA class template provides a specification for generating classes based on parameters. Class templates are generally used to implement containers. A class template is instantiated by passing a given set of types to it as template arguments. The C++ Standard Library contains many class templates, in particular the containers adapted from the Standard Template Library, such as vector.\n\n### Simple Function\nSyntax:\n```cpp\ntemplate < class Ttype> ret_type func_name(parameter_list)\n{\n// body of function.\n}\n```\n\nExample :\n```cpp\n#include <iostream>\nusing namespace std;\ntemplate<class T> T add(T &a,T &b)\n{\nT result = a+b;\nreturn result;\n}\nint main()\n{\nint i =2;\nint j =3;\nfloat m = 2.3;\nfloat n = 1.2;\ncout<<\"Addition of i and j is :\"<<add(i,j);\ncout<<'\\n';\ncout<<\"Addition of m and n is :\"<<add(m,n);\nreturn 0;\n}\n```\n\n### Function Templates with Multiple Parameters\nSyntax:\n```cpp\ntemplate<class T1, class T2,.....>\nreturn_type function_name (arguments of type T1, T2....)\n{\n// body of function.\n}\n```\n\nExample :\n```cpp\n#include <iostream>\nusing namespace std;\ntemplate<class X,class Y> void fun(X a,Y b)\n{\nstd::cout << \"Value of a is : \" <<a<< std::endl;\nstd::cout << \"Value of b is : \" <<b<< std::endl;\n}\nint main()\n{\nfun(15,12.3);\nreturn 0;\n}\n```\n\n### Class Templates\nSyntax:\n```cpp\ntemplate<class Ttype>\nclass class_name\n{\n.\n.\n}\n```\nTtype is a placeholder name which will be determined when the class is instantiated. We can define more than one generic data type using a comma-separated list. The Ttype can be used inside the class body.\nNow, we create an instance of a class\n```cpp\nclass_name<type> ob;\n```\nwhere class_name: It is the name of the class.\ntype: It is the type of the data that the class is operating on.\nob: It is the name of the object.\n\nExample :\n```cpp\n#include <iostream>\nusing namespace std;\ntemplate<class T>\nclass A\n{\npublic:\nT num1 = 5;\nT num2 = 6;\nvoid add()\n{\nstd::cout << \"Addition of num1 and num2 : \" << num1+num2<<std::endl;\n}\n};\nint main()\n{\nA<int> d;\nd.add();\nreturn 0;\n}\n```\n\n### Equipment\nMicrosoft Visual Studio 2010 / DEV C++\n\n### Discussion on Results\nStudent will discuss his/her results in lab report\n\n### Conclusion\nStudent will write in his/her lab notebook what he/she conclude from this experiment\n\n### Questions/Lab Tasks/Activities\n\n#### Task #1\nWrite a program to add, subtract, multiply and divide two numbers using class template.\n\n#### Task #2\nWrite a program to define class Stack, and implement generic methods to push and pop the elements from the stack.\n\n#### Task #3\nWrite a program for memory cell template using it with any type object.\n",
        "quizzes": [
            {
                "question": "What is the primary objective of generic programming with templates in C++?",
                "options": [
                    "To write reusable type-independent code that works with multiple data types without code duplication.",
                    "To prevent classes from using pointers.",
                    "To force all variables to be allocated in thread-local storage.",
                    "To eliminate the need for compiled binary code."
                ],
                "correctAnswer": "To write reusable type-independent code that works with multiple data types without code duplication.",
                "explanation": "Templates allow functions and classes to be written once with type parameters, instantiated for any data type at compile-time."
            },
            {
                "question": "How do you instantiate an object of a class template named Stack for type float?",
                "options": [
                    "Stack<float> myStack;",
                    "Stack(float) myStack;",
                    "template Stack float myStack;",
                    "Stack.float myStack;"
                ],
                "correctAnswer": "Stack<float> myStack;",
                "explanation": "Class template instantiation syntax specifies the concrete type inside angle brackets: ClassName<type> objectName;."
            },
            {
                "question": "When does the C++ compiler generate the concrete machine code for a template function or class?",
                "options": [
                    "At compile-time when the template is instantiated with a specific type argument.",
                    "At runtime when the user inputs data.",
                    "During operating system bootup.",
                    "Templates are interpreted and never compiled to machine code."
                ],
                "correctAnswer": "At compile-time when the template is instantiated with a specific type argument.",
                "explanation": "C++ templates are compile-time generic abstractions; the compiler generates a specialized instance for each concrete type used."
            }
        ],
        "flashcards": [
            {
                "question": "What keyword introduces a template in C++?",
                "answer": "template <class T> or template <typename T>"
            },
            {
                "question": "What is the difference between class T and typename T in template declarations?",
                "answer": "In template parameter declarations, 'class' and 'typename' are 100% equivalent and interchangeable."
            },
            {
                "question": "What happens if you use an operator inside a template that the concrete type does not support?",
                "answer": "A compile-time error occurs when the template is instantiated for that unsupported type."
            },
            {
                "question": "What is a major advantage of the C++ Standard Template Library (STL)?",
                "answer": "It provides thoroughly tested, high-performance generic algorithms and data structures (vectors, stacks, maps, lists)."
            }
        ]
    }
]

def seed_oop_curriculum(db: Optional[Prisma] = None, verbose: bool = True) -> Dict[str, Any]:
    """
    Safely seeds/updates the 'Object Oriented Programming (CS-121L)' course in Neon PostgreSQL.
    CRITICAL SAFETY:
      - Only updates the specific course with title 'Object Oriented Programming (CS-121L)' and category 'University'.
      - Cleans and regenerates steps, quizzes, and flashcards ONLY for this course ID.
      - Does NOT touch, alter, or reset any user accounts, progress records, or other course categories.
    """
    owns_connection = False
    if db is None:
        db = Prisma()
        db.connect()
        owns_connection = True

    try:
        if verbose:
            print("=" * 80)
            print("SEEDING: Object Oriented Programming (CS-121L) [University Courses]")
            print("=" * 80)

        # 1. Find or create the Lesson record
        lesson = db.lesson.find_first(
            where={
                "title": COURSE_DATA["title"],
                "category": COURSE_DATA["category"]
            }
        )

        if not lesson:
            lesson = db.lesson.create(
                data={
                    "title": COURSE_DATA["title"],
                    "category": COURSE_DATA["category"],
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[*] Created new Lesson record: ID={lesson.id}")
        else:
            lesson = db.lesson.update(
                where={"id": lesson.id},
                data={
                    "title": COURSE_DATA["title"],
                    "category": COURSE_DATA["category"],
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[*] Updated existing Lesson record: ID={lesson.id}")

        # 2. Idempotent cleanup of old steps, quizzes, and flashcards for ONLY THIS LESSON
        del_q = db.quiz.delete_many(where={"lessonId": lesson.id})
        del_f = db.flashcard.delete_many(where={"lessonId": lesson.id})
        del_s = db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"[*] Cleared previous records: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

        # 3. Insert Labs 1 to 14 LessonSteps, Quizzes, and Flashcards
        summary_rows = []
        total_quizzes = 0
        total_flashcards = 0

        for lab in LABS_DATA:
            step = db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": lab["order"],
                    "title": lab["title"],
                    "content": lab["content"],
                    "codeSnippet": lab.get("codeSnippet", "")
                }
            )

            # Insert Quizzes linked to both lessonId and lessonStepId
            for q in lab["quizzes"]:
                db.quiz.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": q["question"],
                        "options": q["options"],
                        "correctAnswer": q["correctAnswer"],
                        "explanation": q.get("explanation", "")
                    }
                )
                total_quizzes += 1

            # Insert Flashcards linked to both lessonId and lessonStepId
            for fc in lab["flashcards"]:
                db.flashcard.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": fc["question"],
                        "answer": fc["answer"]
                    }
                )
                total_flashcards += 1

            summary_rows.append({
                "lab_num": f"Lab {lab['order']}",
                "title": lab["title"][:48],
                "quizzes_count": len(lab["quizzes"]),
                "flashcards_count": len(lab["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 80)
            print("SUMMARY TABLE: UNIVERSITY OOP LABS 1 TO 14 SEEDED SUCCESSFULLY")
            print("=" * 80)
            print(f"{'Lab #':<8} | {'Title':<50} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 80)
            for row in summary_rows:
                print(f"{row['lab_num']:<8} | {row['title']:<50} | {row['quizzes_count']:<8} | {row['flashcards_count']:<10}")
            print("=" * 80)
            print(f"Total LessonSteps: {len(LABS_DATA)}")
            print(f"Total Quizzes:     {total_quizzes}")
            print(f"Total Flashcards:  {total_flashcards}")
            print(f"Category:          {COURSE_DATA['category']}")
            print("=" * 80)

        return {
            "lessonId": lesson.id,
            "title": lesson.title,
            "category": lesson.category,
            "stepsCount": len(LABS_DATA),
            "quizzesCount": total_quizzes,
            "flashcardsCount": total_flashcards
        }

    finally:
        if owns_connection and db.is_connected():
            db.disconnect()

if __name__ == "__main__":
    seed_oop_curriculum()

"""
Data Structures and Algorithms (CS-221) Curriculum Seeder
Department of Computing, Faculty of Engineering Sciences & Technology (FEST),
Hamdard University Islamabad Campus (HUIC).

100% VERBATIM transcription from "datastructures.pdf".
Includes:
- Theoretical foundations, definitions, algorithms, diagrams, and sample outputs
- Complete C++ source codes inside markdown blocks (```cpp ... ```)
- Inline diagram assets from frontend/assets/images/university/dsa/
- EXACTLY 5 high-quality Quizzes and 4 Flashcards per Lab
"""

import sys
import os
import time
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

# Ensure environment variables from backend/.env are loaded
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(backend_dir, ".env"))

from prisma import Prisma

COURSE_DATA = {
    "title": "Data Structures and Algorithms (CS-221)",
    "category": "University",
    "description": "Official Academic Curriculum for Data Structures and Algorithms (CS-221), Department of Computing, Faculty of Engineering Sciences & Technology (FEST), Hamdard University Islamabad Campus. Comprehensive laboratory curriculum covering Pointers & Dynamic Memory Allocation, Array Operations (Traversal, Insertion, Deletion), Linear & Binary Search, Bubble Sort, Selection Sort, Singly Linked Lists, Doubly Linked Lists, Stacks, Queues, Expression Parsing (Infix/Postfix), Expression Trees, Quick Sort, and Binary Search Trees (BST).",
    "color": "#0284C7",
    "thumbnail": "assets/images/university/dsa/dsa_logo.png"
}

LABS_PART1 = [   {   'codeSnippet': '// C++ Pointer Demonstration: Addresses, Values, Swapping, and Dynamic Memory\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    int x = 2, y = 8;\n'
                       '    int *p = &x;\n'
                       '    int *q = &y;\n'
                       '    cout << "Address of x: " << &x << "\\tValue of x: " << x << endl;\n'
                       '    cout << "Value of p:   " << p  << "\\tValue of *p: " << *p << endl;\n'
                       '    cout << "Address of y: " << &y << "\\tValue of y: " << y << endl;\n'
                       '    cout << "Value of q:   " << q  << "\\tValue of *q: " << *q << endl;\n'
                       '    cout << "Address of p: " << &p << endl;\n'
                       '    cout << "Address of q: " << &q << endl;\n'
                       '\n'
                       '    // Dynamic Array Allocation with new and delete[]\n'
                       '    int* a = new int[5];\n'
                       '    int z = 0;\n'
                       '    for (int i = 3; i < 20; i += 4) {\n'
                       '        a[z++] = i;\n'
                       '    }\n'
                       '    for (int f = 0; f < 5; f++) {\n'
                       '        cout << "a[" << f << "] = " << a[f] << endl;\n'
                       '    }\n'
                       '    delete[] a;\n'
                       '    return 0;\n'
                       '}',
        'content': '![FEST Hamdard University Crest](assets/images/university/dsa/dsa_logo.png)\n'
                   '\n'
                   '# LAB #: 01\n'
                   '\n'
                   '## PRACTICE PROGRAMS TO IMPLEMENT POINTER\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Objectives:-\n'
                   'The objective of this Lab is to understand the implementation of pointers in C++.\n'
                   '\n'
                   '### Software Tools:-\n'
                   '* **Dev C++**\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Theory:-\n'
                   'We have already studied pointers in our data structure & algorithms class. We would be using the '
                   'knowledge we learned there to implement the pointers.\n'
                   '\n'
                   '#### Pointers:\n'
                   'Pointers are symbolic representation of addresses.\n'
                   '\n'
                   '#### How to use a pointer?\n'
                   '* Define a pointer variable\n'
                   '* Assigning the address of a variable to a pointer using unary operator (`&`) which returns the '
                   'address of that variable.\n'
                   '* Accessing the value stored in the address using unary operator (`*`) which returns the value of '
                   'the variable located at the address specified by its operand.\n'
                   '\n'
                   '![Pointer Variable and Memory Layout '
                   'Diagram](assets/images/university/dsa/lab1_pointer_concept.png)\n'
                   '\n'
                   '*Figure 1.1: Pointer variable `ptr` holding address `0x22fe3c` pointing to variable `var` '
                   'containing value `2`.*\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Exercise 1: Address and Value Operators\n'
                   'Introduce `int` variables `x` and `y` and `int*` pointer variables `p` and `q`. Set `x` to 2, `y` '
                   'to 8, `p` to the address of `x`, and `q` to the address of `y`. Then print the following '
                   'information:\n'
                   '1. The address of `x` and the value of `x`.\n'
                   '2. The value of `p` and the value of `*p`.\n'
                   '3. The address of `y` and the value of `y`.\n'
                   '4. The value of `q` and the value of `*q`.\n'
                   '5. The address of `p` (not its contents!).\n'
                   '6. The address of `q` (not its contents!).\n'
                   '\n'
                   '#### Program:\n'
                   '```cpp\n'
                   '#include "iostream"\n'
                   '#include "conio.h"\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int x, y;\n'
                   '    int *p, *q;\n'
                   '    x = 2;\n'
                   '    y = 8;\n'
                   '    p = &x;\n'
                   '    q = &y;\n'
                   '    cout << endl << &x << " \\t\\t" << x;\n'
                   '    cout << endl << p  << " \\t\\t" << *p;\n'
                   '    cout << endl << &y << " \\t\\t" << y;\n'
                   '    cout << endl << q  << "\\t\\t" << *q;\n'
                   '    cout << endl << &p;\n'
                   '    cout << endl << &q;\n'
                   '    getch();\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Exercise 2: Pointer Values and Swapping\n'
                   'Introduce `int` variables `x, y, z` and `int*` pointer variables `p, q, r`. Set `x, y, z` to three '
                   'distinct values. Set `p, q, r` to the addresses of `x, y, z` respectively.\n'
                   '1. Print with labels the values of `x, y, z, p, q, r, *p, *q, *r`.\n'
                   '2. Print the message: `Swapping values`.\n'
                   '3. Execute the swap code: `k = x; x = y; y = z; z = k;`\n'
                   '4. Print with labels the values of `x, y, z, p, q, r, *p, *q, *r`.\n'
                   '\n'
                   '#### Program:\n'
                   '```cpp\n'
                   '#include "iostream"\n'
                   '#include "conio.h"\n'
                   '#include "stdlib.h"\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int x, y, z;\n'
                   '    int *p, *q, *r;\n'
                   '    x = 2; y = 8; z = 10;\n'
                   '    p = &x;\n'
                   '    q = &y;\n'
                   '    r = &z;\n'
                   '\n'
                   '    cout << endl << "x = " << x;\n'
                   '    cout << endl << "y = " << y;\n'
                   '    cout << endl << "z = " << z;\n'
                   '    cout << endl << "p = " << p;\n'
                   '    cout << endl << "q = " << q;\n'
                   '    cout << endl << "r = " << r;\n'
                   '    cout << endl << "*p = " << *p;\n'
                   '    cout << endl << "*q = " << *q;\n'
                   '    cout << endl << "*r = " << *r;\n'
                   '\n'
                   '    cout << endl << "Swapping Values : ";\n'
                   '    int k = x;\n'
                   '    x = y;\n'
                   '    y = z;\n'
                   '    z = k;\n'
                   '\n'
                   '    cout << endl << "x = " << x;\n'
                   '    cout << endl << "y = " << y;\n'
                   '    cout << endl << "z = " << z;\n'
                   '    cout << endl << "p = " << p;\n'
                   '    cout << endl << "q = " << q;\n'
                   '    cout << endl << "r = " << r;\n'
                   '    cout << endl << "*p = " << *p;\n'
                   '    cout << endl << "*q = " << *q;\n'
                   '    cout << endl << "*r = " << *r;\n'
                   '    getch();\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\n'
                   '\n'
                   '### Exercise 3: Dynamic Memory Allocation using `new` and `delete []`\n'
                   'Define an `int*` pointer variable `a`. Then:\n'
                   '1. Use `new` to make var `a` point to a dynamic array of 5 cells of type `int`.\n'
                   '2. Write a loop to fill `a` with values 3, 7, 11, 15, 19.\n'
                   '3. Write a loop to print the values in `a` with one cell per line.\n'
                   '4. Delete the dynamic array using `delete [] a;`.\n'
                   '\n'
                   '#### Program:\n'
                   '```cpp\n'
                   '#include "iostream"\n'
                   '#include "conio.h"\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int* a;\n'
                   '    int z = 0;\n'
                   '    a = new int[5];\n'
                   '\n'
                   '    for (int i = 3; i < 20; i = i + 4) {\n'
                   '        a[z++] = i;\n'
                   '    }\n'
                   '    for (int f = 0; f < 5; f++) {\n'
                   '        cout << endl << a[f];\n'
                   '    }\n'
                   '\n'
                   '    delete [] a;\n'
                   '    getch();\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n',
        'flashcards': [   {   'answer': 'A pointer is a symbolic representation of a memory address that points '
                                        "directly to a variable's location in memory.",
                              'question': 'What is a Pointer in C++?'},
                          {   'answer': "'&' (address-of) returns the memory address of a variable, while '*' "
                                        '(dereference) accesses the value stored at the specified address.',
                              'question': "What is the difference between operators '&' and '*'?"},
                          {   'answer': "Allocate using 'a = new int[5];' and deallocate using 'delete [] a;' to "
                                        'prevent memory leaks.',
                              'question': 'How do you allocate and deallocate a dynamic integer array of 5 elements in '
                                          'C++?'},
                          {   'answer': "'p' prints the address of the target variable stored inside the pointer, "
                                        "while '&p' prints the memory address where the pointer variable itself is "
                                        'located.',
                              'question': "What does printing '&p' display compared to printing 'p'?"}],
        'order': 1,
        'quizzes': [   {   'correctAnswer': 'Pointers are symbolic representation of addresses',
                           'explanation': "The manual states verbatim under Theory: 'Pointers: Pointers are symbolic "
                                          "representation of addresses.'",
                           'options': [   'Pointers are symbolic representation of addresses',
                                          'Pointers are data structures for storing floating point numbers',
                                          'Pointers are compiler directives used for file inclusion',
                                          'Pointers are reserved variables that store object methods'],
                           'question': 'According to the laboratory manual, what is the exact definition of a pointer '
                                       'in C++?'},
                       {   'correctAnswer': 'Unary operator &',
                           'explanation': 'Assigning the address of a variable to a pointer uses the unary operator '
                                          '(&), which returns the address of that variable.',
                           'options': [   'Unary operator &',
                                          'Unary operator *',
                                          'Binary operator ->',
                                          'Unary operator ~'],
                           'question': 'Which unary operator is used to obtain the memory address of a variable in '
                                       'C++?'},
                       {   'correctAnswer': 'It accesses the value stored at the memory address specified by its '
                                            'operand',
                           'explanation': 'Unary operator (*) accesses the value stored in the address, returning the '
                                          'value of the variable located at the address specified by its operand.',
                           'options': [   'It accesses the value stored at the memory address specified by its operand',
                                          'It allocates new heap memory for the pointer',
                                          'It returns the hexadecimal address of the pointer itself',
                                          'It multiplies the pointer by the size of the data type'],
                           'question': 'What is the function of the unary dereference operator (*) when applied to a '
                                       'pointer variable?'},
                       {   'correctAnswer': 'delete [] a;',
                           'explanation': "The manual specifies in Exercise 3: 'Delete the dynamic array using delete "
                                          "[ ]. Code: delete [] a;'.",
                           'options': ['delete [] a;', 'free(a);', 'delete a;', 'drop a[];'],
                           'question': 'In Exercise 3, which operator syntax is used to release dynamically allocated '
                                       'array memory in C++?'},
                       {   'correctAnswer': 'The addresses stored in p, q, and r remain unchanged, but *p, *q, and *r '
                                            'reflect the new swapped values',
                           'explanation': 'Pointers p, q, and r hold the fixed memory locations &x, &y, &z. Swapping '
                                          'the integer contents of x, y, z changes *p, *q, *r without changing the '
                                          'addresses p, q, and r.',
                           'options': [   'The addresses stored in p, q, and r remain unchanged, but *p, *q, and *r '
                                          'reflect the new swapped values',
                                          'The addresses stored in p, q, and r are automatically swapped by the '
                                          'runtime',
                                          'Pointers p, q, and r become NULL dangling pointers',
                                          'The compiler generates a syntax error because pointer addresses are '
                                          'immutable'],
                           'question': 'In Exercise 2, when variables x, y, and z are swapped, what happens to the '
                                       'values stored in pointers p, q, and r?'}],
        'title': 'Lab 1: Practice Programs to implement Pointer'},
    {   'codeSnippet': '// Linear Array Operations: Traversal, Insertion, and Deletion\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int main() {\n'
                       '    int arr[100] = {3, 15, 60, 45, 37};\n'
                       '    int n = 5;\n'
                       '\n'
                       '    // 1. Traversal\n'
                       '    cout << "Array elements (Traversal):\\n";\n'
                       '    for (int k = 0; k < n; k++) cout << arr[k] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    // 2. Insertion at position K (1-based)\n'
                       '    int k = 3, val = 99; // Insert 99 at position 3\n'
                       '    for (int j = n - 1; j >= k - 1; j--) {\n'
                       '        arr[j + 1] = arr[j]; // Downward shift\n'
                       '    }\n'
                       '    arr[k - 1] = val;\n'
                       '    n++;\n'
                       '    cout << "After insertion of " << val << " at position " << k << ":\\n";\n'
                       '    for (int j = 0; j < n; j++) cout << arr[j] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    // 3. Deletion at position K (1-based)\n'
                       '    int del_k = 3;\n'
                       '    for (int j = del_k - 1; j < n - 1; j++) {\n'
                       '        arr[j] = arr[j + 1]; // Upward shift\n'
                       '    }\n'
                       '    n--;\n'
                       '    cout << "After deletion at position " << del_k << ":\\n";\n'
                       '    for (int j = 0; j < n; j++) cout << arr[j] << " ";\n'
                       '    cout << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 02\n'
                   '\n'
                   '## EXECUTE ARRAYS IMPLEMENTATION AND DIFFERENT OPERATIONS\n'
                   '\n'
                   '---\\n\n'
                   '### Objective:-\n'
                   'The objective of this Lab is to understand the various operations on arrays in C++.\n'
                   '\n'
                   '### Software Tools:-\n'
                   '* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\n'
                   'We have already studied different operations that can be performed on array data structures. We '
                   'would be using the knowledge we learned there to implement different operations on arrays.\n'
                   '\n'
                   '#### Traversing Linear Arrays:-\n'
                   'Let `A` be the collection of data elements stored in the memory of the computer. Suppose we want '
                   'to print the contents of each element of `A` or suppose we want to count the number of elements of '
                   '`A` with a given property. This can be accomplished by traversing `A`, that is, by accessing and '
                   'processing each element of `A` exactly once.\n'
                   '\n'
                   'The following algorithm traverses a linear array. The simplicity of the algorithm comes from the '
                   'fact that `LA` is a linear structure. Other linear structures such as linked list can also be '
                   'easily traversed. On the other hand, the traversal of non-linear structures such as trees and '
                   'graphs is considerably more complicated.\n'
                   '\n'
                   '#### Algorithm: Traversing a Linear Array\n'
                   'Here `LA` is a linear Array with lower Bound `LB` and upper Bound `UB`. This algorithm traverses '
                   '`LA`, applying an operation `PROCESS` to each element of `LA`.\n'
                   '\n'
                   '1. **[Initialize counter]** Set `K = LB`.\n'
                   '2. Repeat Step 3 and 4 while `K <= UB`.\n'
                   '3. **[Visit element]** Apply `PROCESS` to `LA[K]`.\n'
                   '4. **[Increase Counter]** Set `K = K + 1`.\n'
                   '   *(End of Step 2 Loop)*\n'
                   '5. **Exit**\n'
                   '\n'
                   '#### Example Program (Traversal):\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int arr[5] = {3, 15, 60, 45, 37};\n'
                   '    // traversing\n'
                   '    for (int k = 0; k < 5; k++) {\n'
                   '        cout << arr[k] << endl;\n'
                   '    }\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Inserting and Deleting:-\n'
                   "Let `A` be a collection of data elements in the memory of computer. 'Inserting' refers to the "
                   "operation of adding another element to the collection `A`, and 'deleting' refers to the operation "
                   'of removing one of the elements from `A`. Here we discuss inserting and deleting when `A` is a '
                   'linear array.\n'
                   '\n'
                   "Inserting an element at the 'end' of the linear array can be easily done provided the memory space "
                   'allocated for the array is large enough to accommodate the additional element. On the other hand, '
                   'suppose we need to insert an element in the middle of the array. Then on average half of the '
                   'elements must be moved downward to the new location to accommodate the new element and keep the '
                   'order of other elements.\n'
                   '\n'
                   "Similarly, deleting the element at the 'end' of an array presents no difficulties, but deleting "
                   'the element somewhere in the middle of the array would require that each subsequent element be '
                   'moved one location upward in order to fill up the array.\n'
                   '\n'
                   '---\\n\n'
                   '#### Algorithm: Inserting into Linear Array `INSERT (LA, N, K, ITEM)`\n'
                   'Here `LA` is a linear array with `N` elements and `K` is a positive integer such that `K <= N`. '
                   'This algorithm inserts an element `ITEM` into the `K`th position in `LA`.\n'
                   '\n'
                   '1. **[Initialize Counter]** Set `J = Length` (or `N`).\n'
                   '2. Repeat Step 3 and 4 while `J >= K`.\n'
                   '3. **[Move Jth element downward]** Set `LA[J + 1] = LA[J]`.\n'
                   '4. **[Decrease Counter]** Set `J = J - 1`.\n'
                   '   *(End of Step 2 Loop)*\n'
                   '5. **[Insert element]** Set `LA[K] = ITEM`.\n'
                   '6. **[Reset N]** Set `N = N + 1`.\n'
                   '7. **Exit**\n'
                   '\n'
                   '#### Example Program (Insertion):\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int array[100], k, j, n, val;\n'
                   '    cout << "Enter number of elements in array" << endl;\n'
                   '    cin >> n;\n'
                   '    cout << "Enter the elements" << endl;\n'
                   '    for (j = 0; j < n; j++) {\n'
                   '        cin >> array[j];\n'
                   '    }\n'
                   '    cout << "Enter the location where you want to insert the new element" << endl;\n'
                   '    cin >> k;\n'
                   '    cout << "Enter the value of element to be inserted" << endl;\n'
                   '    cin >> val;\n'
                   '\n'
                   '    for (j = n - 1; j >= k - 1; j--) {\n'
                   '        array[j + 1] = array[j];\n'
                   '    }\n'
                   '    array[k - 1] = val;\n'
                   '\n'
                   '    cout << "The New array after insertion: " << endl;\n'
                   '    for (j = 0; j <= n; j++) {\n'
                   '        cout << array[j] << endl;\n'
                   '    }\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '#### Algorithm: Deletion from a Linear Array `DELETE(LA, N, K)`\n'
                   'Here `LA` is a linear array with `N` elements and `K` is a positive integer such that `K <= N`. '
                   'This algorithm deletes an element from the `K`th position in `LA`.\n'
                   '\n'
                   '1. **[Initialize Counter]** Set `J = K`.\n'
                   '2. Repeat Step 3 and 4 while `J < N - 1`.\n'
                   '3. **[Move Jth element upward]** Set `LA[J] = LA[J + 1]`.\n'
                   '4. **[Increase Counter]** Set `J = J + 1`.\n'
                   '5. *(End of Step 2 Loop)*\n'
                   '6. **[Reset N]** Set `N = N - 1`.\n'
                   '7. **Exit**\n'
                   '\n'
                   '---\\n\n'
                   '### Lab Task:-\\nWrite C++ program to implement all the above described algorithms (traversing, '
                   'insertion, and deletion) and display the output for each.\n',
        'flashcards': [   {   'answer': 'Visiting and processing each element of the array exactly once from lower '
                                        'bound LB to upper bound UB.',
                              'question': 'What is Linear Array Traversal?'},
                          {   'answer': 'Shifting existing elements from the rightmost index down to insertion index K '
                                        'by one position (LA[J+1] = LA[J]) to open a slot for the new element.',
                              'question': 'What is the downward shifting mechanism in array insertion?'},
                          {   'answer': 'Copying each subsequent element from index K upward by one position (LA[J] = '
                                        'LA[J+1]) to overwrite the deleted element and fill the gap.',
                              'question': 'What is the upward shifting mechanism in array deletion?'},
                          {   'answer': 'O(N), because inserting at the front or deleting from index 0 requires '
                                        'shifting all N elements.',
                              'question': 'What is the worst-case time complexity of inserting or deleting into a '
                                          'linear array?'}],
        'order': 2,
        'quizzes': [   {   'correctAnswer': 'Accessing and processing each element of the array exactly once',
                           'explanation': 'Traversing an array means accessing and processing each element of the '
                                          'array exactly once.',
                           'options': [   'Accessing and processing each element of the array exactly once',
                                          'Sorting the array elements in descending order',
                                          'Doubling the memory capacity of the array',
                                          'Searching for the smallest element using divide and conquer'],
                           'question': 'What is meant by traversing a linear array?'},
                       {   'correctAnswer': 'Half of the elements (N / 2)',
                           'explanation': "The manual states: 'suppose we need to insert an element in the middle of "
                                          'the array. Then on average half of the elements must be moved downward to '
                                          "the new location to accommodate the new element'.",
                           'options': [   'Half of the elements (N / 2)',
                                          'All elements (N)',
                                          'Zero elements',
                                          'Two elements'],
                           'question': 'When inserting an element in the middle of a linear array of size N, on '
                                       'average how many elements must be shifted downward?'},
                       {   'correctAnswer': 'LA[J + 1] = LA[J]',
                           'explanation': "Step 3 of INSERT states: '[Move Jth element downward] Set LA[J+1] = LA[J]'.",
                           'options': [   'LA[J + 1] = LA[J]',
                                          'LA[J] = LA[J + 1]',
                                          'LA[J] = LA[J - 1]',
                                          'LA[J + 1] = LA[K]'],
                           'question': 'In the linear array INSERT algorithm, what is the shift assignment executed '
                                       'during each iteration?'},
                       {   'correctAnswer': 'Moved one location upward: Set LA[J] = LA[J + 1]',
                           'explanation': "Step 3 of DELETE states: '[Move Jth element upward] Set LA[J] = LA[J+1]'.",
                           'options': [   'Moved one location upward: Set LA[J] = LA[J + 1]',
                                          'Moved one location downward: Set LA[J + 1] = LA[J]',
                                          'Swapped with the last element without shifting',
                                          'Overwritten with -1'],
                           'question': 'In the linear array DELETE algorithm, how are subsequent elements shifted to '
                                       'fill the gap left by the deleted element?'},
                       {   'correctAnswer': 'Because non-linear structures have multiple branches/paths and no single '
                                            'contiguous linear sequence',
                           'explanation': 'Linear structures have a direct sequential order, whereas non-linear '
                                          'structures require recursion, queues, or stacks to manage multiple '
                                          'branching paths.',
                           'options': [   'Because non-linear structures have multiple branches/paths and no single '
                                          'contiguous linear sequence',
                                          'Because non-linear structures cannot be stored in RAM',
                                          'Because C++ arrays do not support integer pointers',
                                          'Because Dev C++ does not support graph traversal'],
                           'question': 'Why is traversing non-linear structures (like trees and graphs) more '
                                       'complicated than linear arrays?'}],
        'title': 'Lab 2: Execute Arrays implementation and different operations'},
    {   'codeSnippet': '// Linear and Binary Search in C++\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int binarySearch(int arr[], int n, int item) {\n'
                       '    int beg = 0, end = n - 1;\n'
                       '    int mid = (beg + end) / 2;\n'
                       '    while (beg <= end && arr[mid] != item) {\n'
                       '        if (item < arr[mid]) end = mid - 1;\n'
                       '        else beg = mid + 1;\n'
                       '        mid = (beg + end) / 2;\n'
                       '    }\n'
                       '    if (arr[mid] == item) return mid;\n'
                       '    return -1; // Not found\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    int data[10] = {2, 6, 9, 12, 15, 18, 20, 25, 34, 45};\n'
                       '    int item = 20;\n'
                       '    int loc = binarySearch(data, 10, item);\n'
                       '    if (loc != -1) cout << "Item " << item << " found at Index: " << loc << endl;\n'
                       '    else cout << "Item not found in array" << endl;\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 03\n'
                   '\n'
                   '## PRACTICE SEARCHING ALGORITHMS\n'
                   '\n'
                   '---\\n\n'
                   '### Objectives:-\\nThe objective of this Lab is to understand the implementation of searching '
                   'algorithms in C++.\n'
                   '\n'
                   '### Software Tools:-\\n* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\\nWe will understand the searching techniques such as linear and binary search, then '
                   'implement the algorithms in C++.\n'
                   '\n'
                   '#### Linear Search Algorithm & Program:\n'
                   '```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    cout << "Enter The Size Of Array: ";\n'
                   '    int size;\n'
                   '    cin >> size;\n'
                   '    int array[size], key, i, LOC = 0;\n'
                   '\n'
                   '    for (int j = 0; j < size; j++) {\n'
                   '        cout << "Enter " << j << " Element: ";\n'
                   '        cin >> array[j];\n'
                   '    }\n'
                   '\n'
                   '    for (int a = 0; a < size; a++) {\n'
                   '        cout << "array[ " << a << " ] = " << array[a] << endl;\n'
                   '    }\n'
                   '\n'
                   '    cout << "Enter element To Search in Array: ";\n'
                   '    cin >> key;\n'
                   '\n'
                   '    for (i = 0; i < size; i++) {\n'
                   '        if (key == array[i]) {\n'
                   '            cout << "Element found at Index Number : " << i << endl;\n'
                   '            LOC = i;\n'
                   '        }\n'
                   '    }\n'
                   '    if (LOC == 0) {\n'
                   '        cout << "Element not found in the array" << endl;\n'
                   '    }\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '#### Linear Search Sample Output:\n'
                   '![Linear Search Output](assets/images/university/dsa/lab3_linear_search_output.png)\n'
                   '\n'
                   '```text\n'
                   'Enter The Size Of Array: 5\n'
                   'Enter 0 Element: 8\n'
                   'Enter 1 Element: 12\n'
                   'Enter 2 Element: 25\n'
                   'Enter 3 Element: 35\n'
                   'Enter 4 Element: 42\n'
                   'array[ 0 ] = 8\n'
                   'array[ 1 ] = 12\n'
                   'array[ 2 ] = 25\n'
                   'array[ 3 ] = 35\n'
                   'array[ 4 ] = 42\n'
                   'Enter element To Search in Array: 35\n'
                   'Element found at Index Number : 3\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Binary Search Algorithm:-\\nSuppose `DATA` is a sorted array with lower bound `LB` and upper '
                   'bound `UB` and `ITEM` is a given item of information. The variables `BEG`, `END` and `MID` denote, '
                   'respectively, the beginning, end and middle locations of a segment of elements of `DATA`. The '
                   'following algorithm finds the location `LOC` of `ITEM` in `DATA` or sets `LOC = Null`.\n'
                   '\n'
                   '1. Set `BEG = LB`, `END = UB` and `MID = INT((BEG + END)/2)`.\n'
                   '2. Repeat Steps 3 and 4 while `BEG <= END` and `DATA[MID] != ITEM`.\n'
                   '3. If `ITEM < DATA[MID]`, then:\n'
                   '       Set `END = MID - 1`\n'
                   '   Else:\n'
                   '       Set `BEG = MID + 1`\n'
                   '   *(End of If structure)*\n'
                   '4. Set `MID = INT((BEG + END)/2)`\n'
                   '   *(End of Step 2 loop)*\n'
                   '5. If `DATA[MID] = ITEM`, then:\n'
                   '       Set `LOC = MID`\n'
                   '   Else:\n'
                   '       Set `LOC = NULL`\n'
                   '   *(End of If structure)*\n'
                   '6. **Exit**\n'
                   '\n'
                   '---\\n\n'
                   '### Binary Search Step-by-Step Example Trace:-\\nConsider a sorted array `A` with 10 elements '
                   'searching for `ITEM = 20`:\n'
                   '\n'
                   '| Index | A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] | A[7] | A[8] | A[9] |\n'
                   '| :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |\n'
                   '| Value | 2 | 6 | 9 | 12 | 15 | 18 | 20 | 25 | 34 | 45 |\n'
                   '\n'
                   '![Binary Search Step-by-Step '
                   'Example](assets/images/university/dsa/lab3_binary_search_example.png)\n'
                   '\n'
                   '* **Step 1:** `BEG = 0` and `END = 9`.\n'
                   '  `MID = INT[(BEG + END) / 2] = INT[(0 + 9) / 2] = 4`.\n'
                   '  `DATA[MID] = DATA[4] = 15`.\n'
                   '  Since `ITEM (20) > DATA[MID] (15)`, set `BEG = MID + 1 = 4 + 1 = 5`.\n'
                   '\n'
                   '* **Step 2:** `BEG = 5` and `END = 9`.\n'
                   '  `MID = INT[(5 + 9) / 2] = 7`.\n'
                   '  `DATA[MID] = DATA[7] = 25`.\n'
                   '  Since `ITEM (20) < DATA[MID] (25)`, set `END = MID - 1 = 7 - 1 = 6`.\n'
                   '\n'
                   '* **Step 3:** `BEG = 5` and `END = 6`.\n'
                   '  `MID = INT[(5 + 6) / 2] = 5`.\n'
                   '  `DATA[MID] = DATA[5] = 18`.\n'
                   '  Since `ITEM (20) > DATA[MID] (18)`, set `BEG = MID + 1 = 5 + 1 = 6`.\n'
                   '\n'
                   '* **Step 4:** `BEG = 6` and `END = 6`.\n'
                   '  `MID = INT[(6 + 6) / 2] = 6`.\n'
                   '  `DATA[MID] = DATA[6] = 20`.\n'
                   '  Since `DATA[MID] == ITEM (20 == 20)`, loop terminates!\n'
                   '  **Search ITEM found at Location 6.**\n'
                   '\n'
                   '---\\n\n'
                   '### Binary Search C++ Program:-\\n```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'int main() {\n'
                   '    int DATA[10] = {2, 6, 9, 12, 15, 18, 20, 25, 34, 45};\n'
                   '    int LB = 0, UB = 9, ITEM = 20;\n'
                   '    int BEG = LB, END = UB, MID = (BEG + END) / 2;\n'
                   '    int LOC = -1;\n'
                   '\n'
                   '    while (BEG <= END && DATA[MID] != ITEM) {\n'
                   '        if (ITEM < DATA[MID]) {\n'
                   '            END = MID - 1;\n'
                   '        } else {\n'
                   '            BEG = MID + 1;\n'
                   '        }\n'
                   '        MID = (BEG + END) / 2;\n'
                   '    }\n'
                   '\n'
                   '    if (DATA[MID] == ITEM) {\n'
                   '        LOC = MID;\n'
                   '        cout << "Search ITEM found at Location: " << LOC << endl;\n'
                   '    } else {\n'
                   '        cout << "Search ITEM not found (LOC = NULL)" << endl;\n'
                   '    }\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n',
        'flashcards': [   {   'answer': 'It tests each element sequentially from index 0 to N-1 until the target is '
                                        'found or all elements are checked.',
                              'question': 'How does Linear Search find a target item in an array?'},
                          {   'answer': 'The target must lie in the right sub-array, so the lower bound is updated: '
                                        "'BEG = MID + 1'.",
                              'question': 'What happens when ITEM > DATA[MID] in Binary Search?'},
                          {   'answer': "When 'BEG > END', meaning the search interval has collapsed without matching "
                                        'DATA[MID] == ITEM.',
                              'question': 'Under what condition does Binary Search conclude that an item is NOT '
                                          'present?'},
                          {   'answer': 'O(1) for both, when the target element happens to be at index 0 (Linear '
                                        'Search) or at the initial midpoint MID (Binary Search).',
                              'question': 'What are the best-case time complexities of Linear Search and Binary '
                                          'Search?'}],
        'order': 3,
        'quizzes': [   {   'correctAnswer': 'The array elements must already be sorted in order',
                           'explanation': 'Binary search divides the search space based on relative comparison (< or '
                                          '>), which requires elements to be in sorted order.',
                           'options': [   'The array elements must already be sorted in order',
                                          'The array size must be an exact power of 2',
                                          'All array elements must be unique positive integers',
                                          'The array must be dynamically allocated with new'],
                           'question': 'What is the mandatory prerequisite for applying Binary Search to an array?'},
                       {   'correctAnswer': 'MID = INT((BEG + END) / 2)',
                           'explanation': "Step 1 and Step 4 of the Binary Search algorithm state: 'MID = INT((BEG + "
                                          "END)/2)'.",
                           'options': [   'MID = INT((BEG + END) / 2)',
                                          'MID = (END - BEG) * 2',
                                          'MID = BEG + END',
                                          'MID = INT(DATA[BEG] + DATA[END]) / 2'],
                           'question': 'How is the midpoint MID computed in the Binary Search algorithm?'},
                       {   'correctAnswer': 'Set END = MID - 1',
                           'explanation': 'If ITEM < DATA[MID], the item lies in the left half, so the upper bound END '
                                          'is moved to MID - 1.',
                           'options': ['Set END = MID - 1', 'Set BEG = MID + 1', 'Set BEG = 0', 'Set END = DATA[MID]'],
                           'question': 'If ITEM < DATA[MID] during Binary Search, how is the active search interval '
                                       'updated?'},
                       {   'correctAnswer': 'Location 6',
                           'explanation': 'In Step 4: BEG=6, END=6, MID=6, DATA[6]=20, finding the item at Location 6.',
                           'options': ['Location 6', 'Location 4', 'Location 7', 'Location 5'],
                           'question': "In the manual's step-by-step example for searching ITEM = 20 in array [2, 6, "
                                       '9, 12, 15, 18, 20, 25, 34, 45], at which index location was ITEM found?'},
                       {   'correctAnswer': 'Binary Search is O(log N) while Linear Search is O(N)',
                           'explanation': 'Binary search cuts the remaining search space in half with every iteration, '
                                          'giving logarithmic time O(log N).',
                           'options': [   'Binary Search is O(log N) while Linear Search is O(N)',
                                          'Binary Search is O(N) while Linear Search is O(1)',
                                          'Binary Search is O(N^2) while Linear Search is O(N)',
                                          'Both have identical O(N) complexity'],
                           'question': 'What is the worst-case time complexity of Binary Search compared to Linear '
                                       'Search on an array of size N?'}],
        'title': 'Lab 3: Practice Searching algorithms'},
    {   'codeSnippet': '// Bubble Sort Algorithm and Program in C++\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'void bubbleSort(int data[], int n) {\n'
                       '    for (int k = 1; k < n; k++) {\n'
                       '        for (int ptr = 0; ptr < n - k; ptr++) {\n'
                       '            if (data[ptr] > data[ptr + 1]) {\n'
                       '                int temp = data[ptr];\n'
                       '                data[ptr] = data[ptr + 1];\n'
                       '                data[ptr + 1] = temp;\n'
                       '            }\n'
                       '        }\n'
                       '    }\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    int arr[8] = {32, 51, 27, 85, 66, 23, 13, 57};\n'
                       '    int n = 8;\n'
                       '    cout << "Original Array:\\n";\n'
                       '    for (int i = 0; i < n; i++) cout << arr[i] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    bubbleSort(arr, n);\n'
                       '\n'
                       '    cout << "Sorted Array (Bubble Sort):\\n";\n'
                       '    for (int i = 0; i < n; i++) cout << arr[i] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 04\n'
                   '\n'
                   '## PRACTICE BUBBLE SORT ALGORITHM\n'
                   '\n'
                   '---\\n\n'
                   '### Objectives:-\\nThe objectives of this session are to understand the implementation of sorting '
                   'techniques i.e. Bubble sort in C++.\n'
                   '\n'
                   '### Software Tools:-\\n* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\\n#### Bubble Sorting:\n'
                   'Bubble sort is a simple sorting algorithm. This sorting algorithm is a comparison-based algorithm '
                   'in which each pair of adjacent elements is compared and the elements are swapped if they are not '
                   'in order.\n'
                   '\n'
                   '![Bubble Sort Concept](assets/images/university/dsa/lab4_bubble_sort_concept.png)\n'
                   '\n'
                   'Suppose the list of numbers `A[1], A[2], .... A[N]` is in memory. The bubble sort algorithm works '
                   'as follows:\n'
                   '\n'
                   '* **Step 1:** Compare `A[1]` and `A[2]` and arrange them in the desired order, so that `A[1] < '
                   'A[2]`. Then compare `A[2]` and `A[3]` and arrange them so that `A[2] < A[3]`. Then compare `A[3]` '
                   'and `A[4]` and arrange them so that `A[3] < A[4]`. Continue until we compare `A[N - 1]` with '
                   '`A[N]` and arrange them so that `A[N - 1] < A[N]`.\n'
                   '  *Observe that Step 1 involves `N - 1` comparisons. (During Step 1, the largest element is '
                   "'bubbled up' to the `N`th position or 'sinks' to the `N`th position.) When Step 1 is completed, "
                   '`A[N]` will contain the largest element.*\n'
                   '\n'
                   '* **Step 2:** Repeat Step 1 with one less comparison; that is, now we stop after we compare and '
                   'possibly rearrange `A[N - 2]` and `A[N - 1]`. *(Step 2 involves `N - 2` comparisons and, when Step '
                   '2 is completed, the second largest element will occupy `A[N - 1]`.)*\n'
                   '\n'
                   '* **Step 3:** Repeat Step 1 with two fewer comparisons; that is, we stop after we compare and '
                   'possibly rearrange `A[N - 3]` and `A[N - 2]`.\n'
                   '* ...\n'
                   '* **Step N - 1:** Compare `A[1]` with `A[2]` and arrange them so that `A[1] < A[2]`.\n'
                   '  *After `N - 1` steps, the list will be sorted in increasing order.*\n'
                   '\n'
                   '---\\n\n'
                   '### Example: Pass-by-Pass Trace on 8 Numbers\n'
                   'Suppose the following numbers are stored in an array `A`:\n'
                   '**`32, 51, 27, 85, 66, 23, 13, 57`**\n'
                   '\n'
                   'We apply the bubble sort to the array `A`. We discuss each pass separately:\n'
                   '\n'
                   '![Bubble Sort Pass 1](assets/images/university/dsa/lab4_bubble_pass1.png)\n'
                   '\n'
                   '#### Pass 1 Comparisons:\n'
                   '1. (a) Compare `A1` and `A2`. Since `32 < 51`, the list is not altered.\n'
                   '2. (b) Compare `A2` and `A3`. Since `51 > 27`, interchange 51 and 27: `32, (27), (51), 85, 66, 23, '
                   '13, 57`\n'
                   '3. (c) Compare `A3` and `A4`. Since `51 < 85`, the list is not altered.\n'
                   '4. (d) Compare `A4` and `A5`. Since `85 > 66`, interchange 85 and 66: `32, 27, 51, (66), (85), 23, '
                   '13, 57`\n'
                   '5. (e) Compare `A5` and `A6`. Since `85 > 23`, interchange 85 and 23: `32, 27, 51, 66, (23), (85), '
                   '13, 57`\n'
                   '6. (f) Compare `A6` and `A7`. Since `85 > 13`, interchange 85 and 13: `32, 27, 51, 66, 23, (13), '
                   '(85), 57`\n'
                   '7. (g) Compare `A7` and `A8`. Since `85 > 57`, interchange 85 and 57: `32, 27, 51, 66, 23, 13, '
                   '(57), (85)`\n'
                   '\n'
                   '*At the end of this first pass, the largest number, **85**, has moved to the last position.*\n'
                   '\n'
                   '![Bubble Sort Passes 2 to 7](assets/images/university/dsa/lab4_bubble_passes.png)\n'
                   '\n'
                   '#### Passes 2 through 7 (Interchanges Shown):\n'
                   '* **Pass 2:**\n'
                   '  * `(27), (32), 51, 66, 23, 13, 57, 85`\n'
                   '  * `27, 32, 51, (23), (66), 13, 57, 85`\n'
                   '  * `27, 32, 51, 23, (13), (66), 57, 85`\n'
                   '  * `27, 32, 51, 23, 13, (57), (66), 85`\n'
                   '  *(Second largest number 66 moved to next-to-last position)*\n'
                   '\n'
                   '* **Pass 3:**\n'
                   '  * `27, 32, (23), (51), 13, 57, 66, 85`\n'
                   '  * `27, 32, 23, (13), (51), 57, 66, 85`\n'
                   '\n'
                   '* **Pass 4:**\n'
                   '  * `27, (23), (32), 13, 51, 57, 66, 85`\n'
                   '  * `27, 23, (13), (32), 51, 57, 66, 85`\n'
                   '\n'
                   '* **Pass 5:**\n'
                   '  * `(23), (27), 13, 32, 51, 57, 66, 85`\n'
                   '  * `23, (13), (27), 32, 51, 57, 66, 85`\n'
                   '\n'
                   '* **Pass 6:**\n'
                   '  * `(13), (23), 27, 32, 51, 57, 66, 85`\n'
                   '  *(Pass 6 actually has two comparisons, A1 with A2 and A2 with A3. The second comparison does not '
                   'involve an interchange.)*\n'
                   '\n'
                   '* **Pass 7:**\n'
                   '  * Finally, `A1` is compared with `A2`. Since `13 < 23`, no interchange takes place.\n'
                   '\n'
                   '---\\n\n'
                   '### Algorithm: `BUBBLE(DATA, N)`\n'
                   '![Bubble Sort Algorithm](assets/images/university/dsa/lab4_bubble_algorithm.png)\n'
                   '\n'
                   'Here `DATA` is an array with `N` elements. This algorithm sorts the elements in `DATA`.\n'
                   '\n'
                   '1. Repeat Steps 2 and 3 for `K = 1` to `N - 1`.\n'
                   '2. **Set PTR := 1.** *[Initializes pass pointer PTR.]*\n'
                   '3. **Repeat while PTR <= N - K:** *[Executes pass.]*\n'
                   '   (a) If `DATA[PTR] > DATA[PTR + 1]`, then:\n'
                   '           Interchange `DATA[PTR]` and `DATA[PTR + 1]`.\n'
                   '       *[End of If structure.]*\n'
                   '   (b) Set `PTR := PTR + 1`.\n'
                   '   *[End of inner loop.]*\n'
                   '   *[End of Step 1 outer loop.]*\n'
                   '4. **Exit.**\n'
                   '\n'
                   '---\\n\n'
                   '### Lab Task:-\\nWrite a C++ program to implement Bubble sorting of a linear array and display the '
                   'output after each pass.\n',
        'flashcards': [   {   'answer': "Because smaller elements gradually 'bubble' up to the top while larger "
                                        "elements 'sink' to the bottom of the list.",
                              'question': "Why is Bubble Sort called 'Bubble Sort'?"},
                          {   'answer': 'N - 1 passes.',
                              'question': 'How many passes does Bubble Sort require to sort N elements in the worst '
                                          'case?'},
                          {   'answer': "'If DATA[PTR] > DATA[PTR + 1], then interchange DATA[PTR] and DATA[PTR + 1]'.",
                              'question': 'What is the inner condition for swapping in BUBBLE(DATA, N)?'},
                          {   'answer': 'O(N^2) time complexity, requiring N(N - 1) / 2 comparisons.',
                              'question': 'What is the average and worst-case time complexity of Bubble Sort?'}],
        'order': 4,
        'quizzes': [   {   'correctAnswer': 'N - 1 comparisons',
                           'explanation': 'Step 1 compares adjacent pairs from index 1 to N, requiring exactly N - 1 '
                                          'comparisons.',
                           'options': [   'N - 1 comparisons',
                                          'N comparisons',
                                          'N / 2 comparisons',
                                          '(N - 1)^2 comparisons'],
                           'question': 'How many comparisons are made during Step 1 (Pass 1) of Bubble Sort on an '
                                       'array of N elements?'},
                       {   'correctAnswer': 'The largest element has bubbled up or sunk to the final Nth position',
                           'explanation': 'During Pass 1, adjacent comparisons guarantee that the largest element '
                                          'reaches the last position A[N].',
                           'options': [   'The largest element has bubbled up or sunk to the final Nth position',
                                          'The entire array is completely sorted',
                                          'The smallest element is placed at index 0',
                                          'All even numbers are placed before odd numbers'],
                           'question': 'What is guaranteed at the completion of Pass 1 in Bubble Sort?'},
                       {   'correctAnswer': '85',
                           'explanation': '85 was the largest number and bubbled up to the 8th position at the end of '
                                          'Pass 1.',
                           'options': ['85', '66', '57', '51'],
                           'question': "In the manual's 8-element trace [32, 51, 27, 85, 66, 23, 13, 57], what number "
                                       'was placed at the end of the array after Pass 1?'},
                       {   'correctAnswer': 'PTR <= N - K',
                           'explanation': 'Because K - 1 elements are already in their final positions at the end, the '
                                          'inner loop only needs to run while PTR <= N - K.',
                           'options': ['PTR <= N - K', 'PTR < N', 'PTR <= K', 'PTR == N'],
                           'question': 'In the BUBBLE(DATA, N) algorithm, what is the termination condition for the '
                                       'inner loop pointer PTR during pass K?'},
                       {   'correctAnswer': 'N(N - 1) / 2 comparisons, resulting in O(N^2) complexity',
                           'explanation': 'The sum (N-1) + (N-2) + ... + 1 equals N(N-1)/2, giving quadratic O(N^2) '
                                          'complexity.',
                           'options': [   'N(N - 1) / 2 comparisons, resulting in O(N^2) complexity',
                                          'N comparisons, resulting in O(N) complexity',
                                          'N log N comparisons, resulting in O(N log N) complexity',
                                          '2^N comparisons, resulting in O(2^N) complexity'],
                           'question': 'What is the total number of comparisons in Bubble Sort across all N - 1 '
                                       'passes?'}],
        'title': 'Lab 4: Practice Bubble sort algorithm'},
    {   'codeSnippet': '// Selection Sort Algorithm and Program in C++\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'int minLocation(int a[], int k, int n) {\n'
                       '    int minVal = a[k], loc = k;\n'
                       '    for (int j = k + 1; j < n; j++) {\n'
                       '        if (minVal > a[j]) {\n'
                       '            minVal = a[j];\n'
                       '            loc = j;\n'
                       '        }\n'
                       '    }\n'
                       '    return loc;\n'
                       '}\n'
                       '\n'
                       'void selectionSort(int a[], int n) {\n'
                       '    for (int k = 0; k < n - 1; k++) {\n'
                       '        int loc = minLocation(a, k, n);\n'
                       '        int temp = a[k];\n'
                       '        a[k] = a[loc];\n'
                       '        a[loc] = temp;\n'
                       '    }\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    int a[8] = {77, 33, 44, 11, 88, 22, 66, 55};\n'
                       '    int n = 8;\n'
                       '    cout << "Original Array:\\n";\n'
                       '    for (int i = 0; i < n; i++) cout << a[i] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    selectionSort(a, n);\n'
                       '\n'
                       '    cout << "Sorted Array (Selection Sort):\\n";\n'
                       '    for (int i = 0; i < n; i++) cout << a[i] << " ";\n'
                       '    cout << endl;\n'
                       '\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 05\n'
                   '\n'
                   '## PRACTICE SELECTION SORT ALGORITHM\n'
                   '\n'
                   '---\\n\n'
                   '### Objectives:-\\nThe objectives of this session are to understand the implementation of sorting '
                   'techniques i.e. Selection sort in C++.\n'
                   '\n'
                   '### Software Tools:-\\n* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\\n#### Selection Sort:-\n'
                   '![Selection Sort Concept](assets/images/university/dsa/lab5_selection_sort_concept.png)\n'
                   '\n'
                   '* **Pass 1:** Find the location `LOC` of the smallest in the list of `N` elements `A[0], A[1], '
                   '..... A[N-1]`, and then interchange `A[LOC]` and `A[0]`. Then: `A[0]` is sorted.\n'
                   '\n'
                   '* **Pass 2:** Find the location `LOC` of the smallest in the sublist of `N-1` elements `A[1], '
                   'A[2], ... A[N-1]`, and interchange `A[LOC]` and `A[1]`. Then: `A[0], A[1]` is sorted. Since `A[0] '
                   '<= A[1]`.\n'
                   '* ...\n'
                   '* **Pass N-1:** Find the location `LOC` of the smallest in `A[N-2]` and `A[N-1]`, and then '
                   'interchange `A[LOC]` and `A[N-1]`. Then: `A[0], A[1], A[2], .... A[N-1]` is sorted.\n'
                   '\n'
                   '---\\n\n'
                   '### Example: Trace of 8 Elements\n'
                   'Suppose an array `A` contains 8 elements as follows:\n'
                   '**`77, 33, 44, 11, 88, 22, 66, 55`**\n'
                   '\n'
                   '![Selection Sort Trace Table](assets/images/university/dsa/lab5_selection_trace_table.png)\n'
                   '\n'
                   '| Pass | A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] | A[7] | Description |\n'
                   '| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n'
                   '| **Initial** | 77 | 33 | 44 | 11 | 88 | 22 | 66 | 55 | Initial unsorted array |\n'
                   '| **K=0, LOC=3** | **11** | 33 | 44 | **77** | 88 | 22 | 66 | 55 | Min is 11 at index 3; swap with '
                   'A[0] |\n'
                   '| **K=1, LOC=5** | 11 | **22** | 44 | 77 | 88 | **33** | 66 | 55 | Min in sublist is 22 at index '
                   '5; swap with A[1] |\n'
                   '| **K=2, LOC=5** | 11 | 22 | **33** | 77 | 88 | **44** | 66 | 55 | Min in sublist is 33 at index '
                   '5; swap with A[2] |\n'
                   '| **K=3, LOC=5** | 11 | 22 | 33 | **44** | 88 | **77** | 66 | 55 | Min in sublist is 44 at index '
                   '5; swap with A[3] |\n'
                   '| **K=4, LOC=7** | 11 | 22 | 33 | 44 | **55** | 77 | 66 | **88** | Min in sublist is 55 at index '
                   '7; swap with A[4] |\n'
                   '| **K=5, LOC=6** | 11 | 22 | 33 | 44 | 55 | **66** | **77** | 88 | Min in sublist is 66 at index '
                   '6; swap with A[5] |\n'
                   '| **K=6, LOC=6** | 11 | 22 | 33 | 44 | 55 | 66 | **77** | 88 | Min is 77 at index 6; already in '
                   'place |\n'
                   '| **Sorted** | **11** | **22** | **33** | **44** | **55** | **66** | **77** | **88** | Array '
                   'completely sorted |\n'
                   '\n'
                   '---\\n\n'
                   '### Procedure: `MIN(A, K, N, LOC)`\n'
                   '![MIN Algorithm](assets/images/university/dsa/lab5_min_algorithm.png)\n'
                   '\n'
                   'An Array `A` is in memory. This procedure finds the location `LOC` of the smallest element among '
                   '`A[K], A[K+1], ..... A[N-1]`.\n'
                   '\n'
                   '1. Set `MIN = A[K]` and `LOC = K`. *[Initializes pointers.]*\n'
                   '2. Repeat for `J = K + 1, K + 2, ..... N - 1`:\n'
                   '       If `MIN > A[J]`, then: `MIN = A[J]` and `LOC = J`.\n'
                   '3. Return `LOC`.\n'
                   '\n'
                   '---\\n\n'
                   '### Algorithm: (SELECTION SORT) `SELECTION(A, N)`\n'
                   '![Selection Sort Algorithm](assets/images/university/dsa/lab5_selection_algorithm.png)\n'
                   '\n'
                   '1. Repeat steps 2 and 3 for `K = 0, 1, 2, ...... N - 2`:\n'
                   '2. Call `MIN(A, K, N, LOC)`.\n'
                   '3. **[Interchange A[K] and A[LOC]]:**\n'
                   '   Set `TEMP = A[K]`, `A[K] = A[LOC]` and `A[LOC] = TEMP`.\n'
                   '   *[End of step 1 loop.]*\n'
                   '4. **Exit.**\n'
                   '\n'
                   '---\\n\n'
                   '### Lab Tasks:-\\nWrite a C++ program to implement Selection sorting of a linear array and display '
                   'the output after each pass.\n',
        'flashcards': [   {   'answer': 'Repeatedly finding the minimum element from the unsorted segment of the array '
                                        'and placing it at the beginning of that segment.',
                              'question': 'What is the core strategy of Selection Sort?'},
                          {   'answer': 'It initializes MIN = A[K], LOC = K, and iterates through J = K+1 to N-1, '
                                        'updating MIN and LOC whenever A[J] < MIN.',
                              'question': 'What does the procedure MIN(A, K, N, LOC) do?'},
                          {   'answer': 'At most 7 swaps (N - 1), one per pass.',
                              'question': 'How many swaps does Selection Sort execute for an array of size 8?'},
                          {   'answer': 'O(N^2) in all cases, because finding the minimum element always requires '
                                        'scanning the entire unsorted sublist.',
                              'question': 'What is the time complexity of Selection Sort in best, average, and worst '
                                          'cases?'}],
        'order': 5,
        'quizzes': [   {   'correctAnswer': 'To find the index location LOC of the smallest element in the sublist '
                                            'from K to N - 1',
                           'explanation': 'The procedure MIN scans elements A[K] to A[N-1] and returns the index LOC '
                                          'where the minimum element is located.',
                           'options': [   'To find the index location LOC of the smallest element in the sublist from '
                                          'K to N - 1',
                                          'To sort the entire array using recursion',
                                          'To delete the minimum value from the array',
                                          'To compute the median of the array'],
                           'question': 'What is the primary role of the helper procedure MIN(A, K, N, LOC) in '
                                       'Selection Sort?'},
                       {   'correctAnswer': 'A[0] (77) and A[3] (11)',
                           'explanation': 'In Pass K=0, the minimum is 11 at LOC=3, so A[0] (77) and A[3] (11) are '
                                          'interchanged.',
                           'options': [   'A[0] (77) and A[3] (11)',
                                          'A[0] (77) and A[1] (33)',
                                          'A[1] (33) and A[5] (22)',
                                          'A[4] (88) and A[7] (55)'],
                           'question': "In the manual's 8-element example [77, 33, 44, 11, 88, 22, 66, 55], which "
                                       'elements were interchanged during Pass K=0?'},
                       {   'correctAnswer': 'N - 1 swaps',
                           'explanation': 'Selection sort performs at most one swap per outer loop pass, executing at '
                                          'most N - 1 swaps total, which is O(N).',
                           'options': ['N - 1 swaps', 'N(N - 1) / 2 swaps', 'N^2 swaps', '2^N swaps'],
                           'question': 'What is the maximum number of data swaps performed by Selection Sort on an '
                                       'array of N elements?'},
                       {   'correctAnswer': 'Both require O(N^2) comparisons (specifically N(N - 1) / 2)',
                           'explanation': 'Both algorithms require comparing all unsorted pairs, yielding the same sum '
                                          'of comparisons N(N - 1) / 2.',
                           'options': [   'Both require O(N^2) comparisons (specifically N(N - 1) / 2)',
                                          'Selection sort requires only O(N) comparisons',
                                          'Bubble sort requires fewer comparisons than Selection sort',
                                          'Selection sort requires O(log N) comparisons'],
                           'question': 'How does the number of comparisons in Selection Sort compare to Bubble Sort in '
                                       'the worst case?'},
                       {   'correctAnswer': 'Because it minimizes memory writes to at most O(N) swaps',
                           'explanation': 'Since Selection Sort only writes to memory during the single swap at the '
                                          'end of each pass, it requires at most N - 1 writes.',
                           'options': [   'Because it minimizes memory writes to at most O(N) swaps',
                                          'Because it does not use any comparisons',
                                          'Because it uses dynamic stack memory',
                                          'Because it runs in O(1) space and time'],
                           'question': 'Why is Selection Sort advantageous when memory write operations are '
                                       'significantly more costly than read operations?'}],
        'title': 'Lab 5: Practice Selection sort algorithm'},
    {   'codeSnippet': '// Singly Linked List Implementation in C++\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'struct Node {\n'
                       '    int data;\n'
                       '    Node* link;\n'
                       '};\n'
                       '\n'
                       'void printList(Node* n) {\n'
                       '    while (n != NULL) {\n'
                       '        cout << n->data << " ";\n'
                       '        n = n->link;\n'
                       '    }\n'
                       '    cout << endl;\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    Node* head = new Node();\n'
                       '    Node* second = new Node();\n'
                       '    Node* third = new Node();\n'
                       '\n'
                       '    head->data = 1;\n'
                       '    head->link = second;\n'
                       '\n'
                       '    second->data = 2;\n'
                       '    second->link = third;\n'
                       '\n'
                       '    third->data = 3;\n'
                       '    third->link = NULL;\n'
                       '\n'
                       '    cout << "Linked List Elements: ";\n'
                       '    printList(head);\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 06\n'
                   '\n'
                   '## EXECUTE PROGRAMS FOR SINGLY LINKED LIST IMPLEMENTATION\n'
                   '\n'
                   '---\\n\n'
                   '### Objective:-\\nThe objective of this session is to understand the various operations on Singly '
                   'linked list in C++.\n'
                   '\n'
                   '### Software Tools:-\\n* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\\nA linked list is a collection of components, called nodes. Every node (except the '
                   'last node) contains the address of the next node. Thus, every node in a linked list has two '
                   'components: one to store the relevant information (that is, data) and one to store the address, '
                   'called the link, of the next node in the list. The address of the first node in the list is stored '
                   'in a separate location, called the `head` or `first`.\n'
                   '\n'
                   'Each node in the linked list contains:\n'
                   '1. One or more members that represent data (e.g. inventory records, customer names, addresses, '
                   'telephone numbers, etc).\n'
                   '2. A pointer that can point to another node.\n'
                   '\n'
                   '![Linked List Node](assets/images/university/dsa/lab6_singly_node.png)\n'
                   '\n'
                   '*Figure 1: Linked List Node (`data | link`).*\n'
                   '\n'
                   '**Linked list:** A list of items, called nodes, in which the order of the nodes is determined by '
                   'the address, called the link, stored in each node.\n'
                   '\n'
                   '![Linked List Chain](assets/images/university/dsa/lab6_singly_chain.png)\n'
                   '\n'
                   '*Figure 2: Singly Linked List chain (`head -> [45] -> [65] -> [34] -> [76] -> NULL`).*\n'
                   '\n'
                   'The arrow in each node indicates that the address of the node to which it is pointing is stored in '
                   'that node. The down arrow in the last node indicates that this link field is `NULL`.\n'
                   '\n'
                   '---\\n\n'
                   '### Node Declaration in C++:-\\nBecause each node of a linked list has two components, we need to '
                   'declare each node as a class or struct. The data type of each node depends on the specific '
                   'application — that is, what kind of data is being processed. However, the link component of each '
                   'node is a pointer. The data type of this pointer variable is the node type itself. For the '
                   'previous linked list, the definition of the node is as follows (supposing the data type is '
                   '`int`):\n'
                   '\n'
                   '```cpp\n'
                   'struct node {\n'
                   '    int data;\n'
                   '    node* link;\n'
                   '};\n'
                   '\n'
                   'node* head;\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Operations on Linked List:-\\nFollowing operations can be performed on a linked list:-\n'
                   '* **Traversing**\n'
                   '* **Searching**\n'
                   '* **Inserting**\n'
                   '* **Deleting**\n'
                   '\n'
                   '#### Traversing a Linked List:-\\nThe `displayList` is a member function that traverses the list, '
                   'displaying the value member of each node. The following is the algorithm:\n'
                   '1. Assign list head to node pointer.\n'
                   '2. While node pointer is not NULL:\n'
                   '   * Display the value member of the node pointed to by node pointer.\n'
                   '   * Assign node pointer to its own next/link member.\n'
                   '   * *(End While)*\n'
                   '\n'
                   '---\\n\n'
                   '### Program: Creating and Traversing a 3-Node List\n'
                   '```cpp\n'
                   '#include "iostream"\n'
                   'using namespace std;\n'
                   '\n'
                   'struct Node {\n'
                   '    int data;\n'
                   '    Node* link;\n'
                   '};\n'
                   '\n'
                   'void printList(Node* n) {\n'
                   '    while (n != NULL) {\n'
                   '        cout << n->data << " ";\n'
                   '        n = n->link;\n'
                   '    }\n'
                   '}\n'
                   '\n'
                   'int main() {\n'
                   '    Node* head = NULL;\n'
                   '    Node* second = NULL;\n'
                   '    Node* third = NULL;\n'
                   '\n'
                   '    head = new Node();\n'
                   '    second = new Node();\n'
                   '    third = new Node();\n'
                   '\n'
                   '    head->data = 1;     // assign data in first node\n'
                   '    head->link = second; // link first node with second\n'
                   '\n'
                   '    second->data = 2;   // assign data to second node\n'
                   '    second->link = third;\n'
                   '\n'
                   '    third->data = 3;    // assign data to third node\n'
                   '    third->link = NULL; // last node points to NULL\n'
                   '\n'
                   '    printList(head);\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Lab Tasks:-\\nWrite C++ program for other operations (searching, inserting, deleting) that can '
                   'be performed on singly linked list.\n',
        'flashcards': [   {   'answer': 'A self-referential structure containing data and a pointer (link) to the next '
                                        'node in the sequence.',
                              'question': 'What is a Node in a Singly Linked List?'},
                          {   'answer': 'struct Node { int data; Node* link; };',
                              'question': 'How is a singly linked list node declared in C++?'},
                          {   'answer': 'When the current node pointer becomes NULL (pointing past the last node).',
                              'question': 'What is the stop condition for traversing a linked list?'},
                          {   'answer': 'Because linked lists only require reassigning two pointers in O(1) time, '
                                        'without having to shift existing elements down in memory.',
                              'question': 'Why are insertions at the head of a linked list faster than arrays?'}],
        'order': 6,
        'quizzes': [   {   'correctAnswer': 'A data component and a link (pointer) component to the next node',
                           'explanation': 'Every node in a linked list contains data and a pointer (called link) to '
                                          'the next node.',
                           'options': [   'A data component and a link (pointer) component to the next node',
                                          'A left child pointer and a right child pointer',
                                          'A key and a hash index',
                                          'An integer data value and a priority weight'],
                           'question': 'What are the two components of every node in a singly linked list?'},
                       {   'correctAnswer': 'It indicates the end (last node) of the linked list',
                           'explanation': "The manual notes: 'The down arrow in the last node indicates that this link "
                                          "field is NULL', signifying the end of the list.",
                           'options': [   'It indicates the end (last node) of the linked list',
                                          'It indicates a memory allocation fault',
                                          'It indicates that the node contains integer zero',
                                          'It points back to the head node in a circular loop'],
                           'question': 'What does a pointer value of NULL in the link field of a node represent?'},
                       {   'correctAnswer': 'In a separate pointer variable called head or first',
                           'explanation': 'The address of the first node in the list is stored in a separate location, '
                                          'called the head or first.',
                           'options': [   'In a separate pointer variable called head or first',
                                          'At index zero of the operating system registry',
                                          'Inside the data field of the last node',
                                          'In the CPU accumulator register'],
                           'question': 'Where is the memory address of the first node of a linked list stored?'},
                       {   'correctAnswer': 'n = n->link;',
                           'explanation': 'The traversal algorithm assigns the pointer to its own next/link member: n '
                                          '= n->link.',
                           'options': ['n = n->link;', 'n = n + 1;', 'n = n * sizeof(Node);', 'n = head++;'],
                           'question': 'In the printList traversal function, how does the pointer advance through the '
                                       'list?'},
                       {   'correctAnswer': 'O(1) constant time',
                           'explanation': "Inserting at the head only requires setting the new node's link to current "
                                          'head and updating head, which takes O(1) time without shifting.',
                           'options': [   'O(1) constant time',
                                          'O(N) linear time',
                                          'O(log N) logarithmic time',
                                          'O(N^2) quadratic time'],
                           'question': 'What is the time complexity of inserting a new node at the beginning (head) of '
                                       'a singly linked list?'}],
        'title': 'Lab 6: Execute programs for Singly Linked List implementation'},
    {   'codeSnippet': '// Doubly Linked List Implementation in C++\n'
                       '#include <iostream>\n'
                       'using namespace std;\n'
                       '\n'
                       'struct Node {\n'
                       '    int data;\n'
                       '    Node* next;\n'
                       '    Node* prev;\n'
                       '};\n'
                       '\n'
                       'void printForward(Node* head) {\n'
                       '    cout << "Forward: ";\n'
                       '    while (head != NULL) {\n'
                       '        cout << head->data << " ";\n'
                       '        head = head->next;\n'
                       '    }\n'
                       '    cout << endl;\n'
                       '}\n'
                       '\n'
                       'void printBackward(Node* tail) {\n'
                       '    cout << "Backward: ";\n'
                       '    while (tail != NULL) {\n'
                       '        cout << tail->data << " ";\n'
                       '        tail = tail->prev;\n'
                       '    }\n'
                       '    cout << endl;\n'
                       '}\n'
                       '\n'
                       'int main() {\n'
                       '    Node* first = new Node();\n'
                       '    Node* second = new Node();\n'
                       '    Node* third = new Node();\n'
                       '\n'
                       '    first->data = 10;\n'
                       '    first->prev = NULL;\n'
                       '    first->next = second;\n'
                       '\n'
                       '    second->data = 20;\n'
                       '    second->prev = first;\n'
                       '    second->next = third;\n'
                       '\n'
                       '    third->data = 30;\n'
                       '    third->prev = second;\n'
                       '    third->next = NULL;\n'
                       '\n'
                       '    printForward(first);\n'
                       '    printBackward(third);\n'
                       '    return 0;\n'
                       '}',
        'content': '# LAB #: 07\n'
                   '\n'
                   '## EXECUTE PROGRAMS FOR DOUBLY LINKED LIST IMPLEMENTATION\n'
                   '\n'
                   '---\\n\n'
                   '### Objective:-\\nThe objective of this session is to understand the various operations on Doubly '
                   'linked list in C++.\n'
                   '\n'
                   '### Software Tools:-\\n* **Dev C++**\n'
                   '\n'
                   '---\\n\n'
                   '### Theory:-\\nDoubly or two way linked list is a List that can be traversed in two directions: in '
                   'the usual forward direction from the beginning of the list to the end, or in the backward '
                   'direction from end of the list to the beginning. Furthermore, given the location `LOC` of a node '
                   '`N` in the list, one now has immediate access to both the next node and the previous node in the '
                   'list.\n'
                   '\n'
                   'A two way list is a linear collection of data elements, called nodes, where each node `N` is '
                   'divided into three parts:\n'
                   '\n'
                   '1. An information field **`INFO`** which contains the data of `N`.\n'
                   '2. A pointer field **`FORW`** which contains the location of the next node in the list.\n'
                   '3. A pointer field **`BACK`** which contains the location of the previous node in the list.\n'
                   '\n'
                   '![Doubly Linked List Structure](assets/images/university/dsa/lab7_doubly_linked_list.png)\n'
                   '\n'
                   '*Figure 7.1: Two-way linked list structure showing `FIRST`, `Node N` with fields (`INFO`, `BACK`, '
                   '`FORW`), and `LAST`.*\n'
                   '\n'
                   '---\\n\n'
                   '### Deletion in Two Way List:-\\n![Doubly Linked List '
                   'Deletion](assets/images/university/dsa/lab7_doubly_deletion.png)\n'
                   '\n'
                   '*Figure 7.2: Deletion of Node N at location `LOC` in a Two-way list.*\n'
                   '\n'
                   'When deleting a node `N` at location `LOC`, the pointers of its predecessor and successor nodes '
                   'are directly rewired:\n'
                   '```text\n'
                   'Set FORW[BACK[LOC]] = FORW[LOC]\n'
                   'Set BACK[FORW[LOC]] = BACK[LOC]\n'
                   '```\n'
                   'The memory of Node `N` is then returned to the free-storage list. Notice that no search traversal '
                   'is required to locate the predecessor node because `BACK[LOC]` directly references it!\n'
                   '\n'
                   '---\\n\n'
                   '### Insertion in Two Way List:-\\n![Doubly Linked List '
                   'Insertion](assets/images/university/dsa/lab7_doubly_insertion.png)\n'
                   '\n'
                   '*Figure 7.3: Insertion of Node N between Node A and Node B in a Two-way list.*\n'
                   '\n'
                   'To insert a new node `N` containing `ITEM` between Node `A` (at `LOCA`) and Node `B` (at `LOCB`):\n'
                   '```text\n'
                   'Set FORW[LOCA] = NEW\n'
                   'Set BACK[NEW] = LOCA\n'
                   'Set FORW[NEW] = LOCB\n'
                   'Set BACK[LOCB] = NEW\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Representation of a DLL node in C++:-\\n```cpp\n'
                   '/* Node of a doubly linked list */\n'
                   'struct Node {\n'
                   '    int data;\n'
                   '    Node* next; // Pointer to next node in DLL\n'
                   '    Node* prev; // Pointer to previous node in DLL\n'
                   '};\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Complete C++ Implementation Program:-\\n```cpp\n'
                   '#include <iostream>\n'
                   'using namespace std;\n'
                   '\n'
                   'struct Node {\n'
                   '    int data;\n'
                   '    Node* next;\n'
                   '    Node* prev;\n'
                   '};\n'
                   '\n'
                   'void insertEnd(Node*& head, int val) {\n'
                   '    Node* newNode = new Node();\n'
                   '    newNode->data = val;\n'
                   '    newNode->next = NULL;\n'
                   '    if (head == NULL) {\n'
                   '        newNode->prev = NULL;\n'
                   '        head = newNode;\n'
                   '        return;\n'
                   '    }\n'
                   '    Node* temp = head;\n'
                   '    while (temp->next != NULL) temp = temp->next;\n'
                   '    temp->next = newNode;\n'
                   '    newNode->prev = temp;\n'
                   '}\n'
                   '\n'
                   'void displayList(Node* head) {\n'
                   '    Node* temp = head;\n'
                   '    cout << "Doubly Linked List: ";\n'
                   '    while (temp != NULL) {\n'
                   '        cout << temp->data << " <-> ";\n'
                   '        temp = temp->next;\n'
                   '    }\n'
                   '    cout << "NULL" << endl;\n'
                   '}\n'
                   '\n'
                   'int main() {\n'
                   '    Node* head = NULL;\n'
                   '    insertEnd(head, 10);\n'
                   '    insertEnd(head, 20);\n'
                   '    insertEnd(head, 30);\n'
                   '    displayList(head);\n'
                   '    return 0;\n'
                   '}\n'
                   '```\n'
                   '\n'
                   '---\\n\n'
                   '### Lab Tasks:-\\nWrite all of the operations on a doubly linked list as discussed in class using '
                   'separate functions for each operation:\n'
                   '1. Insert item at the end\n'
                   '2. Insert item in the beginning\n'
                   '3. Insert item at the given location\n'
                   '4. Display complete list\n'
                   '5. Delete an item\n',
        'flashcards': [   {   'answer': 'A linear data structure of nodes where each node contains data and two '
                                        "pointers: 'next' (FORW) pointing to the successor and 'prev' (BACK) pointing "
                                        'to the predecessor.',
                              'question': 'What is a Doubly Linked List?'},
                          {   'answer': 'INFO (data payload), FORW (forward pointer to next node), and BACK (backward '
                                        'pointer to previous node).',
                              'question': 'What are the three fields of a DLL node?'},
                          {   'answer': 'FORW[BACK[LOC]] = FORW[LOC] and BACK[FORW[LOC]] = BACK[LOC], bypassing node '
                                        'LOC entirely.',
                              'question': 'How are pointers rewired when deleting node LOC in a two-way list?'},
                          {   'answer': 'Both are set to NULL, indicating the beginning and end boundaries of the '
                                        'list.',
                              'question': "What are the first node's BACK pointer and last node's FORW pointer in a "
                                          'standard DLL?'}],
        'order': 7,
        'quizzes': [   {   'correctAnswer': 'It can be traversed in two directions: forward from beginning to end and '
                                            'backward from end to beginning',
                           'explanation': 'A doubly linked list has two pointer fields per node allowing traversal in '
                                          'both forward and backward directions.',
                           'options': [   'It can be traversed in two directions: forward from beginning to end and '
                                          'backward from end to beginning',
                                          'It stores elements in contiguous memory like an array',
                                          'It automatically sorts elements in descending order',
                                          'It eliminates the need for dynamic pointer memory'],
                           'question': 'What is the defining capability of a Doubly (Two-Way) Linked List compared to '
                                       'a Singly Linked List?'},
                       {   'correctAnswer': 'INFO (data), FORW (pointer to next node), and BACK (pointer to previous '
                                            'node)',
                           'explanation': "Under Theory: 'each node N is divided into three parts: 1. INFO (data), 2. "
                                          "FORW (next pointer), 3. BACK (previous pointer)'.",
                           'options': [   'INFO (data), FORW (pointer to next node), and BACK (pointer to previous '
                                          'node)',
                                          'LEFT, ROOT, and RIGHT',
                                          'DATA, KEY, and VALUE',
                                          'INDEX, DATA, and POINTER'],
                           'question': 'What are the three distinct fields comprising each node in a Two-way Linked '
                                       'List?'},
                       {   'correctAnswer': 'FORW[BACK[LOC]] = FORW[LOC] and BACK[FORW[LOC]] = BACK[LOC]',
                           'explanation': "The predecessor's forward pointer is set to LOC's successor, and the "
                                          "successor's backward pointer is set to LOC's predecessor.",
                           'options': [   'FORW[BACK[LOC]] = FORW[LOC] and BACK[FORW[LOC]] = BACK[LOC]',
                                          'FORW[LOC] = NULL and BACK[LOC] = NULL',
                                          'LOC = FORW[LOC] and LOC = BACK[LOC]',
                                          'FIRST = FORW[LOC] and LAST = BACK[LOC]'],
                           'question': 'In a two-way list, what two pointer assignments rewire the list when deleting '
                                       'node N at location LOC?'},
                       {   'correctAnswer': 'Because BACK[LOC] gives immediate direct access to the predecessor node '
                                            'without requiring a search traversal from head',
                           'explanation': 'In a singly linked list, finding the predecessor node requires traversing '
                                          'from the head. In a DLL, BACK[LOC] provides direct O(1) access to the '
                                          'predecessor.',
                           'options': [   'Because BACK[LOC] gives immediate direct access to the predecessor node '
                                          'without requiring a search traversal from head',
                                          'Because deletion in a Doubly Linked List runs in O(N^2) time',
                                          'Because DLL nodes do not require deallocation with delete',
                                          'Because the predecessor node is always at memory address 0x0'],
                           'question': 'Why is node deletion in a Doubly Linked List more efficient than in a Singly '
                                       'Linked List when given only a pointer to the target node LOC?'},
                       {   'correctAnswer': '4 pointer assignments',
                           'explanation': "Inserting between Node A and Node B requires updating Node A's forward "
                                          "pointer, Node B's back pointer, and the new node's forward and back "
                                          'pointers (4 assignments total).',
                           'options': [   '4 pointer assignments',
                                          '2 pointer assignments',
                                          '1 pointer assignment',
                                          '8 pointer assignments'],
                           'question': 'How many pointer assignments are required to insert a new node between two '
                                       'existing nodes in a Doubly Linked List?'}],
        'title': 'Lab 7: Execute programs for Doubly Linked List implementation'}]

LABS_PART2 = [
    # =========================================================================
    # LAB 8
    # =========================================================================
    {
        "order": 8,
        "title": "Lab 8: Practice Stacks using Arrays and Linked list",
        "content": """# Lab #: 08: Practice Stacks using Arrays and Linked list

## Objective:-
The objective of this session is to understand the various operations on stacks in C++.
1. Push
2. Pop

## Software Tools:-
Dev C++.

---

## Theory:-
A **Stack** is a list of elements in which an element may be inserted or deleted only at one end, called the **top** of the stack. This means, in particular, that elements are removed from a stack in the reverse order of that in which they were inserted into the stack.

A Stack operates strictly on the **LIFO (Last In, First Out)** principle.

Special terminology is used for two basic operations associated with stacks:
- **a) "Push"** is the term used to insert an element into a stack.
- **b) "Pop"** is the term used to delete an element from a stack.

---

### Array representation of stacks:
In the array representation of a stack, a linear array `STACK` of size `MAXSTK` is used along with a pointer variable `TOP` that holds the index of the top element of the stack. 
The condition `TOP = 0` (or `TOP = -1` in 0-indexed C++) indicates that the stack is **EMPTY**.

![Array representation of stack](assets/images/university/dsa/lab8_stack_array.png)

*Figure 8.1: Array representation of a stack displaying `TOP` pointer and `MAXSTK` capacity.*

---

### Algorithm for PUSH operation in Stack using Array:
```text
PUSH(STACK, TOP, MAXSTK, ITEM)
This procedure pushes an ITEM onto a stack.

1. [Stack already filled?]
   If TOP = MAXSTK, then: Print: OVERFLOW, and Return.
2. Set TOP := TOP + 1. [Increases TOP by 1.]
3. Set STACK[TOP] := ITEM. [Inserts ITEM in new TOP position.]
4. Return.
```

![PUSH operation in Stack using Array](assets/images/university/dsa/lab8_stack_push.png)

*Figure 8.2: PUSH procedure on Array Stack with OVERFLOW condition check.*

---

### Algorithm for POP operation in Stack using Array:
```text
POP(STACK, TOP, ITEM)
This procedure deletes the top element of STACK and assigns it to the variable ITEM.

1. [Stack has an item to be removed?]
   If TOP = 0, then: Print: UNDERFLOW, and Return.
2. Set ITEM := STACK[TOP]. [Assigns TOP element to ITEM.]
3. Set TOP := TOP - 1. [Decreases TOP by 1.]
4. Return.
```

![POP operation in Stack using Array](assets/images/university/dsa/lab8_stack_pop.png)

*Figure 8.3: POP procedure on Array Stack with UNDERFLOW condition check.*

---

### Linked Representation of Stacks:
The linked representation of a stack, commonly termed **linked stack**, is a stack that is implemented using a singly linked list. The `INFO` fields of the nodes hold the elements of the stack and the `LINK` field holds pointers to the neighboring element in the stack. 

The `START` pointer of the linked list behaves as the `TOP` pointer variable of the stack and the null pointer of the last node in the list signals the bottom of stack.

![Linked Representation of Stack](assets/images/university/dsa/lab8_stack_linked.png)

*Figure 8.4: Linked representation of a stack with `TOP` (START) pointing to the topmost node and `NULL` at the bottom.*

---

### Algorithm for PUSH operation in Linked Stack:
```text
PUSH_LINKSTACK(INFO, LINK, TOP, AVAIL, ITEM)
This procedure pushes an ITEM into a linked stack.

1. [Available space?] If AVAIL = NULL, then Write OVERFLOW and Exit.
2. [Remove first node from AVAIL list]
   Set NEW := AVAIL and AVAIL := LINK[AVAIL].
3. Set INFO[NEW] := ITEM. [Copies ITEM into new node]
4. Set LINK[NEW] := TOP. [New node points to the original top node in the stack]
5. Set TOP = NEW. [Reset TOP to point to the new node at the top of the stack]
6. Exit.
```

![PUSH operation in Linked Stack](assets/images/university/dsa/lab8_stack_push_linked.png)

*Figure 8.5: PUSH_LINKSTACK algorithm allocating from AVAIL list.*

---

### Algorithm for POP operation in Linked Stack:
```text
POP_LINKSTACK(INFO, LINK, TOP, AVAIL, ITEM)
This procedure deletes the top element of a linked stack and assigns it to the variable ITEM.

1. [Stack has an item to be removed?]
   IF TOP = NULL then Write: UNDERFLOW and Exit.
2. Set ITEM := INFO[TOP]. [Copies the top element of stack into ITEM]
3. Set TEMP := TOP and TOP = LINK[TOP].
   [Remember the old value of the TOP pointer in TEMP and reset TOP to point to the next element in the stack]
4. [Return deleted node to the AVAIL list]
   Set LINK[TEMP] = AVAIL and AVAIL = TEMP.
5. Exit.
```

![POP operation in Linked Stack](assets/images/university/dsa/lab8_stack_pop_linked.png)

*Figure 8.6: POP_LINKSTACK algorithm returning node to AVAIL list.*

---

## Lab Tasks:
Make C++ Programs for the following operations:
1. For PUSH operation in Stack using Array
2. For POP operation in Stack using Array
3. For PUSH operation in Linked Stack
4. For POP operation in Linked Stack
""",
        "codeSnippet": """// Complete C++ Programs for Array Stack and Linked Stack Implementation
#include <iostream>
using namespace std;

// ==========================================
// 1. ARRAY IMPLEMENTATION OF STACK
// ==========================================
#define MAXSTK 5

class ArrayStack {
private:
    int stack[MAXSTK];
    int top;

public:
    ArrayStack() {
        top = -1; // -1 represents empty stack in 0-indexed C++
    }

    void push(int item) {
        if (top == MAXSTK - 1) {
            cout << "OVERFLOW: Stack is full! Cannot push " << item << endl;
            return;
        }
        top = top + 1;
        stack[top] = item;
        cout << "Pushed " << item << " onto Array Stack. (TOP = " << top << ")" << endl;
    }

    int pop() {
        if (top == -1) {
            cout << "UNDERFLOW: Stack is empty! Cannot pop." << endl;
            return -1;
        }
        int item = stack[top];
        top = top - 1;
        cout << "Popped " << item << " from Array Stack. (TOP = " << top << ")" << endl;
        return item;
    }

    void display() {
        if (top == -1) {
            cout << "Array Stack is EMPTY." << endl;
            return;
        }
        cout << "Array Stack (top to bottom): ";
        for (int i = top; i >= 0; i--) {
            cout << stack[i] << " ";
        }
        cout << endl;
    }
};

// ==========================================
// 2. LINKED LIST IMPLEMENTATION OF STACK
// ==========================================
struct Node {
    int info;
    Node* link;
};

class LinkedStack {
private:
    Node* top;

public:
    LinkedStack() {
        top = NULL;
    }

    void push(int item) {
        Node* newNode = new Node();
        if (newNode == NULL) {
            cout << "OVERFLOW: Heap memory exhausted! Cannot push " << item << endl;
            return;
        }
        newNode->info = item;
        newNode->link = top;
        top = newNode;
        cout << "Pushed " << item << " onto Linked Stack." << endl;
    }

    int pop() {
        if (top == NULL) {
            cout << "UNDERFLOW: Linked Stack is empty! Cannot pop." << endl;
            return -1;
        }
        Node* temp = top;
        int item = temp->info;
        top = top->link;
        delete temp;
        cout << "Popped " << item << " from Linked Stack." << endl;
        return item;
    }

    void display() {
        if (top == NULL) {
            cout << "Linked Stack is EMPTY." << endl;
            return;
        }
        cout << "Linked Stack (top to bottom): ";
        Node* ptr = top;
        while (ptr != NULL) {
            cout << ptr->info << " -> ";
            ptr = ptr->link;
        }
        cout << "NULL" << endl;
    }

    ~LinkedStack() {
        while (top != NULL) {
            pop();
        }
    }
};

int main() {
    cout << "=== TESTING ARRAY STACK ===" << endl;
    ArrayStack arrStack;
    arrStack.push(10);
    arrStack.push(20);
    arrStack.push(30);
    arrStack.display();
    arrStack.pop();
    arrStack.display();

    cout << "\n=== TESTING LINKED STACK ===" << endl;
    LinkedStack lnkStack;
    lnkStack.push(100);
    lnkStack.push(200);
    lnkStack.push(300);
    lnkStack.display();
    lnkStack.pop();
    lnkStack.display();

    return 0;
}""",
        "quizzes": [
            {
                "question": "Which data processing principle does a Stack data structure follow?",
                "options": [
                    "LIFO (Last In, First Out)",
                    "FIFO (First In, First Out)",
                    "LILO (Last In, Last Out)",
                    "Random Access"
                ],
                "correctAnswer": "LIFO (Last In, First Out)",
                "explanation": "A stack is a linear collection in which insertion and deletion can occur only at one end (TOP), adhering to the Last In, First Out (LIFO) principle."
            },
            {
                "question": "What condition occurs when attempting to PUSH an element onto an array stack where TOP = MAXSTK?",
                "options": [
                    "OVERFLOW",
                    "UNDERFLOW",
                    "Memory Leak",
                    "Dangling Pointer"
                ],
                "correctAnswer": "OVERFLOW",
                "explanation": "When the stack is completely full (TOP = MAXSTK in 1-based indexing or TOP = MAXSTK - 1 in 0-based indexing), pushing another item triggers an OVERFLOW error."
            },
            {
                "question": "In the POP operation on an array stack, what is the check for an UNDERFLOW condition?",
                "options": [
                    "TOP = 0 (or TOP = -1)",
                    "TOP = MAXSTK",
                    "STACK[TOP] == 0",
                    "TOP == MAXSTK / 2"
                ],
                "correctAnswer": "TOP = 0 (or TOP = -1)",
                "explanation": "UNDERFLOW occurs when an attempt is made to pop an item from an already empty stack, signified by TOP = 0 (1-indexed) or TOP = -1 (0-indexed)."
            },
            {
                "question": "In the linked representation of a stack, which pointer acts as the TOP of the stack?",
                "options": [
                    "The START pointer of the linked list",
                    "The LAST pointer of the linked list",
                    "The AVAIL pointer",
                    "The middle node pointer"
                ],
                "correctAnswer": "The START pointer of the linked list",
                "explanation": "In a linked stack, the START pointer of the singly linked list directly behaves as the TOP pointer variable, allowing O(1) push and pop at the list head."
            },
            {
                "question": "During PUSH_LINKSTACK, when a new node is allocated from the AVAIL list, what does its LINK field point to?",
                "options": [
                    "The previous TOP node",
                    "NULL",
                    "The bottom of the stack",
                    "The next available node in AVAIL"
                ],
                "correctAnswer": "The previous TOP node",
                "explanation": "The algorithm executes `Set LINK[NEW] := TOP` so that the newly inserted node points to the former topmost node of the stack, after which `TOP = NEW`."
            }
        ],
        "flashcards": [
            {
                "question": "What is the definition of a Stack?",
                "answer": "A list of elements in which an element may be inserted or deleted only at one end, called the TOP, operating on the LIFO principle."
            },
            {
                "question": "What is the difference between OVERFLOW and UNDERFLOW in stacks?",
                "answer": "OVERFLOW occurs when pushing into a completely full stack; UNDERFLOW occurs when popping from an empty stack."
            },
            {
                "question": "How does PUSH in an array stack update TOP?",
                "answer": "It increments TOP by 1 (`TOP = TOP + 1`) and inserts ITEM at `STACK[TOP]`."
            },
            {
                "question": "What signals the bottom of a linked stack?",
                "answer": "The NULL pointer in the LINK field of the last node in the singly linked list."
            }
        ]
    },

    # =========================================================================
    # LAB 9
    # =========================================================================
    {
        "order": 9,
        "title": "Lab 9: Practice Queues using Arrays and Linked list",
        "content": """# Lab #: 09: Practice Queues using Arrays and Linked list

## Objective:-
The objective of this session is to understand the various operations on Queues in C++.

## Software Tools:-
Dev C++.

---

## THEORY:-
**Queue:** A data structure in which the elements are added at one end, called the **rear**, and deleted from the other end, called the **front**; a **First In First Out (FIFO)** data structure.

A queue is a set of elements of the same type in which the elements are added at one end, called the back or rear, and deleted from the other end, called the front. 

For example, consider a line of customers in a bank, wherein the customers are waiting to withdraw/deposit money or to conduct some other business. Each new customer gets in the line at the rear. Whenever a teller is ready for a new customer, the customer at the front of the line is served.

The rear of the queue is accessed whenever a new element is added to the queue, and the front of the queue is accessed whenever an element is deleted from the queue. As in a stack, the middle elements of the queue are inaccessible, even if the queue elements are stored in an array.

---

### QUEUES IMPLEMENTATION USING ARRAYS:-
Queues may be represented in the computer in various ways, usually by means of a one-way list or linear arrays. Unless otherwise stated or implied, each of our queues will be maintained by a linear array `QUEUE` and two pointer variables:
- **`FRONT`**: containing the location of the front element of the queue.
- **`REAR`**: containing the location of the rear element of the queue.

The condition **`FRONT = NULL`** will indicate that the queue is **empty**.

![Queue array representation](assets/images/university/dsa/lab9_queue_array.png)

*Figure 9.1: Array representation of a linear queue displaying `FRONT` and `REAR` pointers.*

![Queue operations overview](assets/images/university/dsa/lab9_queue_operations.png)

*Figure 9.2: Conceptual operations on queue.*

Whenever an element is deleted from the queue, the value of `FRONT` is increased by one:
```text
FRONT = FRONT + 1
```
Similarly, whenever an element is added to the queue, the value of `REAR` is increased by one:
```text
REAR = REAR + 1
```

---

### QUEUE INSERTION ALGORITHM (Circular Array):-
```text
QINSERT(QUEUE, N, FRONT, REAR, ITEM)
This procedure inserts an element ITEM into a queue.

1. [Queue already filled?]
   If FRONT = 1 and REAR = N, or if FRONT = REAR + 1, then:
   Write: OVERFLOW, and Return.
2. [Find new value of REAR.]
   If FRONT := NULL, then: [Queue initially empty.]
      Set FRONT := 1 and REAR := 1.
   Else if REAR = N, then:
      Set REAR := 1.
   Else:
      Set REAR := REAR + 1.
   [End of If structure.]
3. Set QUEUE[REAR] := ITEM. [This inserts new element.]
4. Return.
```

![Queue Insertion Algorithm](assets/images/university/dsa/lab9_queue_insert_array.png)

*Figure 9.3: QINSERT algorithm handling circular array boundary wrap-around and OVERFLOW.*

![Queue Enqueue Operation](assets/images/university/dsa/lab9_queue_enqueue.png)

*Figure 9.4: Enqueue operation at the REAR of the queue.*

---

### QUEUE DELETION ALGORITHM (Circular Array):-
```text
QDELETE(QUEUE, N, FRONT, REAR, ITEM)
This procedure deletes an element from a queue and assigns it to the variable ITEM.

1. [Queue already empty?]
   If FRONT := NULL, then: Write: UNDERFLOW, and Return.
2. Set ITEM := QUEUE[FRONT].
3. [Find new value of FRONT.]
   If FRONT = REAR, then: [Queue has only one element to start.]
      Set FRONT := NULL and REAR := NULL.
   Else if FRONT = N, then:
      Set FRONT := 1.
   Else:
      Set FRONT := FRONT + 1.
   [End of If structure.]
4. Return.
```

![Queue Deletion Algorithm](assets/images/university/dsa/lab9_queue_delete_array.png)

*Figure 9.5: QDELETE algorithm updating FRONT pointer and detecting UNDERFLOW.*

![Queue Dequeue Operation](assets/images/university/dsa/lab9_queue_dequeue.png)

*Figure 9.6: Dequeue operation from the FRONT of the queue.*

---

### QUEUES IMPLEMENTATION USING LINKED LIST:-
In this section we discuss the linked representation of a queue. A **linked queue** is a queue implemented as a linked list with two pointer variables `FRONT` and `REAR` pointing to the nodes which are at the FRONT and REAR of the queue. The `INFO` fields of the list hold the elements of the queue and the `LINK` fields hold pointers to the neighboring elements in the queue.

![Linked queue representation](assets/images/university/dsa/lab9_queue_linked.png)

*Figure 9.7: Linked Queue Q with Front pointing to AAA, nodes chained via pointers, and Rear pointing to DDD.*

- **Insert 'EEE' into queue Q:** Appended to the end of the list; `REAR` moves from DDD to EEE.
- **Delete from queue Q:** Node AAA is removed; `FRONT` advances from AAA to BBB.

---

### LINKED QUEUE INSERTION ALGORITHM:-
```text
LINKQ_INSERT(INFO, LINK, FRONT, REAR, AVAIL, ITEM)
This procedure inserts an ITEM into a linked queue.

1. [Available space?] If AVAIL = NULL, then Write OVERFLOW and Exit.
2. [Remove first node from AVAIL list]
   Set NEW := AVAIL and AVAIL := LINK[AVAIL].
3. Set INFO[NEW] := ITEM and LINK[NEW] := NULL.
   [Copies ITEM into new node]
4. If (FRONT = NULL) then FRONT = REAR = NEW
   [If Q is empty then ITEM is the first element in the queue Q]
   Else set LINK[REAR] := NEW and REAR = NEW.
   [REAR points to the new node appended to the end of the list]
5. Exit.
```

![Linked Queue Insertion Algorithm](assets/images/university/dsa/lab9_queue_insert_linked.png)

*Figure 9.8: LINKQ_INSERT algorithm appending new node at REAR.*

---

### LINKED QUEUE DELETION ALGORITHM:-
```text
LINKQ_DELETE(INFO, LINK, FRONT, REAR, AVAIL, ITEM)
This procedure deletes the front element of the linked queue and stores it in ITEM.

1. [Linked queue empty?] If (FRONT = NULL) then Write: UNDERFLOW and Exit.
2. Set TEMP = FRONT. [If linked queue is nonempty, remember FRONT in a temporary variable TEMP]
3. ITEM = INFO[TEMP].
4. FRONT = LINK[TEMP]. [Reset FRONT to point to the next element in the queue]
5. LINK[TEMP] = AVAIL and AVAIL = TEMP. [Return the deleted node TEMP to the AVAIL list]
6. Exit.
```

![Linked Queue Deletion Algorithm](assets/images/university/dsa/lab9_queue_delete_linked.png)

*Figure 9.9: LINKQ_DELETE algorithm advancing FRONT and reclaiming node to AVAIL.*

---

## Lab Tasks:
Make C++ Programs for the following operations:
1. For Insertion operation in Queue using Array
2. For Deletion operation in Queue using Array
3. For Insertion operation in Linked Queue
4. For Deletion operation in Linked Queue
""",
        "codeSnippet": """// Complete C++ Programs for Circular Array Queue and Linked Queue Implementation
#include <iostream>
using namespace std;

// ==========================================
// 1. CIRCULAR ARRAY IMPLEMENTATION OF QUEUE
// ==========================================
#define N 5

class CircularQueue {
private:
    int queue[N];
    int front;
    int rear;

public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    void qinsert(int item) {
        // Check Overflow
        if ((front == 0 && rear == N - 1) || (front == rear + 1)) {
            cout << "OVERFLOW: Circular Queue is full! Cannot insert " << item << endl;
            return;
        }

        // Find new value of REAR
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (rear == N - 1) {
            rear = 0;
        } else {
            rear = rear + 1;
        }

        queue[rear] = item;
        cout << "Inserted " << item << " into Circular Queue. (FRONT=" << front << ", REAR=" << rear << ")" << endl;
    }

    int qdelete() {
        // Check Underflow
        if (front == -1) {
            cout << "UNDERFLOW: Circular Queue is empty! Cannot delete." << endl;
            return -1;
        }

        int item = queue[front];

        // Find new value of FRONT
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (front == N - 1) {
            front = 0;
        } else {
            front = front + 1;
        }

        cout << "Deleted " << item << " from Circular Queue." << endl;
        return item;
    }

    void display() {
        if (front == -1) {
            cout << "Circular Queue is EMPTY." << endl;
            return;
        }
        cout << "Circular Queue elements: ";
        int i = front;
        while (true) {
            cout << queue[i] << " ";
            if (i == rear) break;
            i = (i + 1) % N;
        }
        cout << endl;
    }
};

// ==========================================
// 2. LINKED LIST IMPLEMENTATION OF QUEUE
// ==========================================
struct QNode {
    int info;
    QNode* link;
};

class LinkedQueue {
private:
    QNode* front;
    QNode* rear;

public:
    LinkedQueue() {
        front = NULL;
        rear = NULL;
    }

    void enqueue(int item) {
        QNode* newNode = new QNode();
        if (newNode == NULL) {
            cout << "OVERFLOW: Heap memory exhausted! Cannot insert " << item << endl;
            return;
        }
        newNode->info = item;
        newNode->link = NULL;

        if (front == NULL) {
            front = rear = newNode;
        } else {
            rear->link = newNode;
            rear = newNode;
        }
        cout << "Enqueued " << item << " into Linked Queue." << endl;
    }

    int dequeue() {
        if (front == NULL) {
            cout << "UNDERFLOW: Linked Queue is empty! Cannot delete." << endl;
            return -1;
        }
        QNode* temp = front;
        int item = temp->info;
        front = front->link;

        if (front == NULL) {
            rear = NULL;
        }

        delete temp;
        cout << "Dequeued " << item << " from Linked Queue." << endl;
        return item;
    }

    void display() {
        if (front == NULL) {
            cout << "Linked Queue is EMPTY." << endl;
            return;
        }
        cout << "Linked Queue (Front to Rear): ";
        QNode* ptr = front;
        while (ptr != NULL) {
            cout << ptr->info << " -> ";
            ptr = ptr->link;
        }
        cout << "NULL" << endl;
    }

    ~LinkedQueue() {
        while (front != NULL) {
            dequeue();
        }
    }
};

int main() {
    cout << "=== TESTING CIRCULAR ARRAY QUEUE ===" << endl;
    CircularQueue cq;
    cq.qinsert(10);
    cq.qinsert(20);
    cq.qinsert(30);
    cq.display();
    cq.qdelete();
    cq.display();

    cout << "\n=== TESTING LINKED QUEUE ===" << endl;
    LinkedQueue lq;
    lq.enqueue(100);
    lq.enqueue(200);
    lq.enqueue(300);
    lq.display();
    lq.dequeue();
    lq.display();

    return 0;
}""",
        "quizzes": [
            {
                "question": "What primary data processing principle does a Queue follow?",
                "options": [
                    "FIFO (First In, First Out)",
                    "LIFO (Last In, First Out)",
                    "Random Access",
                    "FILO (First In, Last Out)"
                ],
                "correctAnswer": "FIFO (First In, First Out)",
                "explanation": "A Queue follows the First In First Out (FIFO) principle, where items inserted first at the REAR are deleted first from the FRONT."
            },
            {
                "question": "In a circular array queue of size N, what condition signals OVERFLOW during insertion?",
                "options": [
                    "(FRONT = 1 and REAR = N) or (FRONT = REAR + 1)",
                    "FRONT = NULL",
                    "FRONT = REAR",
                    "REAR = N / 2"
                ],
                "correctAnswer": "(FRONT = 1 and REAR = N) or (FRONT = REAR + 1)",
                "explanation": "In a circular queue, overflow occurs when either the rear reaches the end while front is at 1, or rear wraps around to immediately precede front (FRONT = REAR + 1)."
            },
            {
                "question": "What condition indicates that a queue is completely EMPTY?",
                "options": [
                    "FRONT = NULL (or FRONT = -1)",
                    "REAR = N",
                    "FRONT = REAR + 1",
                    "FRONT = 1 and REAR = 1"
                ],
                "correctAnswer": "FRONT = NULL (or FRONT = -1)",
                "explanation": "The condition FRONT = NULL (or front == -1 in 0-indexed C++) indicates that the queue contains no elements and is empty."
            },
            {
                "question": "When deleting the final remaining element from a queue where FRONT == REAR, what do both pointers reset to?",
                "options": [
                    "Both reset to NULL (or -1)",
                    "Both reset to 1",
                    "FRONT resets to N and REAR resets to 0",
                    "Pointers remain unchanged"
                ],
                "correctAnswer": "Both reset to NULL (or -1)",
                "explanation": "When the queue contains only one element, FRONT equals REAR. Deleting that item leaves the queue empty, resetting both FRONT and REAR to NULL."
            },
            {
                "question": "In a linked queue, where are new nodes added and from where are nodes removed?",
                "options": [
                    "Added at REAR, removed from FRONT",
                    "Added at FRONT, removed from REAR",
                    "Both added and removed at FRONT",
                    "Both added and removed at REAR"
                ],
                "correctAnswer": "Added at REAR, removed from FRONT",
                "explanation": "In accordance with FIFO queue behavior, new nodes are appended at the REAR pointer and elements are dequeued from the FRONT pointer."
            }
        ],
        "flashcards": [
            {
                "question": "What is the definition of a Queue?",
                "answer": "A linear First-In First-Out (FIFO) data structure where elements are added at the rear and deleted from the front."
            },
            {
                "question": "Why is a circular array used for queue implementation?",
                "answer": "To prevent false overflow where vacant slots created by front deletions cannot be reused by a linear rear pointer."
            },
            {
                "question": "What happens to the FRONT pointer when an element is deleted from a non-empty queue?",
                "answer": "FRONT is incremented by 1 (`FRONT = FRONT + 1`, wrapping to 1 if `FRONT == N`)."
            },
            {
                "question": "In a linked queue, what pointers maintain the list?",
                "answer": "Two pointer variables: FRONT pointing to the first node and REAR pointing to the last node."
            }
        ]
    },

    # =========================================================================
    # LAB 10
    # =========================================================================
    {
        "order": 10,
        "title": "Lab 10: Execute programs for Infix to Postfix Expression",
        "content": """# Lab #: 10: Execute programs for Infix to Postfix Expression

## Objective:-
The objective of this session is to understand the transformation of Infix Expression to Postfix Expression in C++.

## Software Tools:-
Dev C++.

---

## Theory:-
### Infix to Postfix Expression Transformation:
An arithmetic expression written in standard human-readable format is in **infix notation**, where binary operators appear between their operands (e.g., `A + B`). 

In contrast, **postfix notation** (also known as **Reverse Polish Notation**) places operators immediately after their corresponding operands (e.g., `A B +`). Postfix notation eliminates the need for parentheses and operator precedence rules during computer evaluation.

#### Operator Precedence Hierarchy:
1. **Exponentiation (`^` or `↑`)**: Highest precedence.
2. **Multiplication and Division (`*`, `/`)**: Intermediate precedence.
3. **Addition and Subtraction (`+`, `-`)**: Lowest precedence.

---

### Step-by-Step Simulation:
Consider the following arithmetic infix expression `Q`:
```text
Q: A + ( B * C - ( D / E ↑ F ) * G ) * H
```
We simulate the algorithm to transform `Q` into its equivalent postfix expression `P`.

First, we push `"("` onto `STACK`, and then we add `")"` to the end of `Q` to obtain:
```text
Q: A + ( B * C - ( D / E ↑ F ) * G ) * H )
  (1)(2)(3)(4)(5)(6)(7)(8)(9)(10)(11)(12)(13)(14)(15)(16)(17)(18)(19)(20)
```
The elements of `Q` have now been labeled from `(1)` to `(20)` from left to right for easy reference.

#### Rules Observed During Scanning:
1. Each operand is simply added to `P` and does not change `STACK`.
2. The subtraction operator (`-`) in row 7 sends `*` from `STACK` to `P` before it (`-`) is pushed onto `STACK`.
3. The right parenthesis in row 14 sends `↑` and then `/` from `STACK` to `P`, and then removes the left parenthesis from the top of `STACK`.
4. The right parenthesis in row 20 sends `*` and then `+` from `STACK` to `P`, and then removes the left parenthesis from the top of `STACK`.

After Step 20 is executed, the `STACK` is empty and:
```text
P: A B C * D E F ↑ / G * - H * +
```
which is the required postfix equivalent of `Q`.

---

### 20-Step Trace Table:
![Trace table for Infix to Postfix](assets/images/university/dsa/lab10_infix_postfix_table.png)

*Figure 10.1: Complete 20-step tracing table showing scanned symbol, STACK status, and Postfix String P.*

| Step | Symbol Scanned | STACK | Expression P |
| :--- | :--- | :--- | :--- |
| **(1)** | `A` | `(` | `A` |
| **(2)** | `+` | `( +` | `A` |
| **(3)** | `(` | `( + (` | `A` |
| **(4)** | `B` | `( + (` | `A B` |
| **(5)** | `*` | `( + ( *` | `A B` |
| **(6)** | `C` | `( + ( *` | `A B C` |
| **(7)** | `-` | `( + ( -` | `A B C *` |
| **(8)** | `(` | `( + ( - (` | `A B C *` |
| **(9)** | `D` | `( + ( - (` | `A B C * D` |
| **(10)** | `/` | `( + ( - ( /` | `A B C * D` |
| **(11)** | `E` | `( + ( - ( /` | `A B C * D E` |
| **(12)** | `↑` | `( + ( - ( / ↑` | `A B C * D E` |
| **(13)** | `F` | `( + ( - ( / ↑` | `A B C * D E F` |
| **(14)** | `)` | `( + ( -` | `A B C * D E F ↑ /` |
| **(15)** | `*` | `( + ( - *` | `A B C * D E F ↑ /` |
| **(16)** | `G` | `( + ( - *` | `A B C * D E F ↑ / G` |
| **(17)** | `)` | `( +` | `A B C * D E F ↑ / G * -` |
| **(18)** | `*` | `( + *` | `A B C * D E F ↑ / G * -` |
| **(19)** | `H` | `( + *` | `A B C * D E F ↑ / G * - H` |
| **(20)** | `)` | *[empty]* | `A B C * D E F ↑ / G * - H * +` |

---

### Algorithm: POLISH(Q, P)
```text
Algorithm: POLISH(Q, P)
Suppose Q is an arithmetic expression written in infix notation. This algorithm finds the equivalent postfix expression P.

1. Push "(" onto STACK, and add ")" to the end of Q.
2. Scan Q from left to right and repeat Steps 3 to 6 for each element of Q until the STACK is empty:
3.    If an operand is encountered, add it to P.
4.    If a left parenthesis is encountered, push it onto STACK.
5.    If an operator ⊗ is encountered, then:
      (a) Repeatedly pop from STACK and add to P each operator (on the top of STACK)
          which has the same precedence as or higher precedence than ⊗.
      (b) Add ⊗ to STACK.
      [End of If structure.]
6.    If a right parenthesis is encountered, then:
      (a) Repeatedly pop from STACK and add to P each operator (on the top of STACK)
          until a left parenthesis is encountered.
      (b) Remove the left parenthesis. [Do not add the left parenthesis to P.]
      [End of If structure.]
   [End of Step 2 loop.]
7. Exit.
```

![Algorithm POLISH](assets/images/university/dsa/lab10_polish_algorithm.png)

*Figure 10.2: Algorithm POLISH(Q, P) for infix to postfix conversion.*

---

## Lab Tasks:
Make C++ Programs for the following operations:
1. For Transforming the Infix Expression to Postfix Expression
""",
        "codeSnippet": """// Complete C++ Program for Transforming Infix Expression to Postfix Expression
#include <iostream>
#include <stack>
#include <string>
#include <cctype>

using namespace std;

// Function to return precedence of operators
int precedence(char op) {
    if (op == '^' || op == '$')
        return 3;
    if (op == '*' || op == '/')
        return 2;
    if (op == '+' || op == '-')
        return 1;
    return 0; // for '('
}

// Function to implement POLISH(Q, P)
string infixToPostfix(string Q) {
    stack<char> st;
    string P = "";

    // Step 1: Push '(' onto STACK, add ')' to end of Q
    st.push('(');
    Q += ')';

    // Step 2: Scan Q from left to right
    for (int i = 0; i < Q.length(); i++) {
        char ch = Q[i];

        // Skip whitespace
        if (ch == ' ') continue;

        // Step 3: If operand is encountered, add it to P
        if (isalnum(ch)) {
            P += ch;
            P += ' ';
        }
        // Step 4: If left parenthesis is encountered, push onto STACK
        else if (ch == '(') {
            st.push(ch);
        }
        // Step 6: If right parenthesis is encountered
        else if (ch == ')') {
            while (!st.empty() && st.top() != '(') {
                P += st.top();
                P += ' ';
                st.pop();
            }
            if (!st.empty() && st.top() == '(') {
                st.pop(); // Remove '(' without adding to P
            }
        }
        // Step 5: If operator is encountered
        else {
            while (!st.empty() && st.top() != '(' && precedence(st.top()) >= precedence(ch)) {
                P += st.top();
                P += ' ';
                st.pop();
            }
            st.push(ch);
        }
    }

    return P;
}

int main() {
    cout << "=== INFIX TO POSTFIX CONVERTER (POLISH ALGORITHM) ===" << endl;
    
    // Test manual example: A + ( B * C - ( D / E ^ F ) * G ) * H
    string infix = "A + ( B * C - ( D / E ^ F ) * G ) * H";
    cout << "Infix Expression Q:   " << infix << endl;

    string postfix = infixToPostfix(infix);
    cout << "Postfix Expression P: " << postfix << endl;
    cout << "Expected Output:      A B C * D E F ^ / G * - H * +" << endl;

    return 0;
}""",
        "quizzes": [
            {
                "question": "What is the primary advantage of Postfix (Reverse Polish) notation over Infix notation?",
                "options": [
                    "It can be evaluated unambiguously without parentheses or precedence rules",
                    "It uses fewer memory bytes than infix",
                    "It requires recursive algorithms to parse",
                    "It only supports single-digit numbers"
                ],
                "correctAnswer": "It can be evaluated unambiguously without parentheses or precedence rules",
                "explanation": "In postfix notation, the order of operations is strictly dictated by the position of operators relative to operands, eliminating ambiguity and parentheses."
            },
            {
                "question": "In the POLISH(Q, P) algorithm, what initial action is performed before scanning begins?",
                "options": [
                    "Push '(' onto STACK and append ')' to the end of Q",
                    "Reverse the string Q",
                    "Push all operators to STACK",
                    "Clear both STACK and P"
                ],
                "correctAnswer": "Push '(' onto STACK and append ')' to the end of Q",
                "explanation": "Step 1 of POLISH(Q, P) states: Push '(' onto STACK, and add ')' to the end of Q to create boundary delimiters that flush the stack upon completion."
            },
            {
                "question": "What action is taken when an incoming operator has lower or equal precedence than the operator on top of the STACK?",
                "options": [
                    "Pop operators from STACK and add them to P until top has lower precedence",
                    "Push the incoming operator immediately",
                    "Discard the incoming operator",
                    "Clear the STACK entirely"
                ],
                "correctAnswer": "Pop operators from STACK and add them to P until top has lower precedence",
                "explanation": "If an operator on top of the STACK has higher or equal precedence than the incoming operator, it must be popped and added to P before pushing the incoming operator."
            },
            {
                "question": "When a right parenthesis ')' is encountered during the scan, what happens?",
                "options": [
                    "Repeatedly pop operators to P until '(' is reached, then discard '('",
                    "Push ')' onto STACK",
                    "Append ')' directly to P",
                    "Terminate the algorithm immediately"
                ],
                "correctAnswer": "Repeatedly pop operators to P until '(' is reached, then discard '('",
                "explanation": "Encountering ')' flushes all stacked operators within that scope into string P until the matching '(' is popped and discarded."
            },
            {
                "question": "What is the postfix conversion of the sub-expression (D / E ^ F)?",
                "options": [
                    "D E F ^ /",
                    "D E / F ^",
                    "/ D ^ E F",
                    "D E F / ^"
                ],
                "correctAnswer": "D E F ^ /",
                "explanation": "Because exponentiation (^) has higher precedence than division (/), E ^ F is evaluated first (E F ^), followed by division (D E F ^ /)."
            }
        ],
        "flashcards": [
            {
                "question": "What is Infix notation?",
                "answer": "An arithmetic notation where binary operators are written between their operands, e.g., A + B."
            },
            {
                "question": "What is Postfix (Reverse Polish) notation?",
                "answer": "A parenthesis-free notation where operators are written immediately following their operands, e.g., A B +."
            },
            {
                "question": "What is the precedence order of standard arithmetic operators?",
                "answer": "1. Exponentiation (^), 2. Multiplication and Division (*, /), 3. Addition and Subtraction (+, -)."
            },
            {
                "question": "How are operands handled during Infix to Postfix conversion?",
                "answer": "Operands are appended directly to the output postfix string P without modifying the STACK."
            }
        ]
    },

    # =========================================================================
    # LAB 11
    # =========================================================================
    {
        "order": 11,
        "title": "Lab 11: Execute programs for Postfix Expressions",
        "content": """# Lab #: 11: Execute programs for Postfix Expressions

## Objective:-
The objective of this session is to understand the evaluation of Postfix Expression in C++.

## Software Tools:-
Dev C++.

---

## Theory:-
### Evaluation of a Postfix Expression:
Suppose `P` is an arithmetic expression written in postfix notation. Evaluating `P` requires an operand **`STACK`**. 

Unlike infix expressions, postfix expressions do not require parentheses to determine the order of operations. During evaluation, each operand is placed on `STACK`. When an operator is encountered, the top two operands are removed from `STACK`, the operation is performed, and the resulting value is pushed back onto `STACK`.

---

### Step-by-Step Simulation:
Consider the following arithmetic expression `P` written in postfix notation:
```text
P: 5, 6, 2, +, *, 12, 4, /, -
```
*(Commas are used to separate the elements of P so that 5, 6, 2 is not interpreted as the number 562.)*

The equivalent infix expression `Q` follows:
```text
Q: 5 * ( 6 + 2 ) - 12 / 4
```
Note that parentheses are necessary for the infix expression `Q` but not for the postfix expression `P`.

We evaluate `P` by simulating the algorithm. First, we add a right parenthesis at the end of `P` to obtain:
```text
P: 5, 6, 2, +, *, 12, 4, /, -, )
  (1)(2)(3)(4)(5)(6)(7)(8)(9)(10)
```

---

### Step-by-Step Evaluation Table:
![Postfix Evaluation Table](assets/images/university/dsa/lab11_postfix_eval_table.png)

*Figure 11.1: 10-step trace table evaluating `P: 5, 6, 2, +, *, 12, 4, /, -` using STACK.*

| Step | Symbol Scanned | STACK Status | Operation & Value Calculation |
| :--- | :--- | :--- | :--- |
| **(1)** | `5` | `5` | Push operand `5` |
| **(2)** | `6` | `5, 6` | Push operand `6` |
| **(3)** | `2` | `5, 6, 2` | Push operand `2` |
| **(4)** | `+` | `5, 8` | Pop `A=2`, `B=6`; compute `B + A = 6 + 2 = 8`; push `8` |
| **(5)** | `*` | `40` | Pop `A=8`, `B=5`; compute `B * A = 5 * 8 = 40`; push `40` |
| **(6)** | `12` | `40, 12` | Push operand `12` |
| **(7)** | `4` | `40, 12, 4` | Push operand `4` |
| **(8)** | `/` | `40, 3` | Pop `A=4`, `B=12`; compute `B / A = 12 / 4 = 3`; push `3` |
| **(9)** | `-` | `37` | Pop `A=3`, `B=40`; compute `B - A = 40 - 3 = 37`; push `37` |
| **(10)** | `)` | `37` | Right parenthesis reached; Final VALUE = **37** |

---

### Algorithm for Evaluation of a Postfix Expression:
```text
Suppose P is an arithmetic expression written in postfix notation.
The following algorithm, which uses a STACK to hold operands, evaluates P.

Algorithm: This algorithm finds the VALUE of an arithmetic expression P written in postfix notation.

1. Add a right parenthesis ")" at the end of P.
2. Scan P from left to right and repeat Steps 3 and 4 for each element of P
   until the ")" is encountered.
3. If an operand is encountered, put it on STACK.
4. If an operator ⊗ is encountered, then:
   (a) Remove the two top elements of STACK, where A is the top element
       and B is the next-to-top element.
   (b) Evaluate B ⊗ A.
   (c) Place the result of (b) back on STACK.
   [End of If structure.]
   [End of Step 2 loop.]
5. Set VALUE equal to the top element on STACK.
6. Exit.
```

![Algorithm for Evaluation of Postfix Expression](assets/images/university/dsa/lab11_postfix_eval_algorithm.png)

*Figure 11.2: Standard postfix evaluation algorithm using operand STACK.*

---

## Lab Tasks:
Make C++ Programs for the following operations:
1. For Evaluation of Postfix Expression
""",
        "codeSnippet": """// Complete C++ Program for Evaluation of Postfix Expression
#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <cctype>
#include <cmath>

using namespace std;

// Function to evaluate postfix expression
double evaluatePostfix(string exp) {
    stack<double> st;
    stringstream ss(exp);
    string token;

    // Scan tokens separated by space or commas
    while (ss >> token) {
        // If comma, continue
        if (token == ",") continue;

        // Check if token is an operator
        if (token == "+" || token == "-" || token == "*" || token == "/" || token == "^") {
            if (st.size() < 2) {
                cout << "Error: Invalid postfix expression!" << endl;
                return -1;
            }
            double A = st.top(); st.pop(); // Top element
            double B = st.top(); st.pop(); // Next-to-top element
            double result = 0;

            if (token == "+") result = B + A;
            else if (token == "-") result = B - A;
            else if (token == "*") result = B * A;
            else if (token == "/") {
                if (A == 0) {
                    cout << "Error: Division by zero!" << endl;
                    return -1;
                }
                result = B / A;
            }
            else if (token == "^") result = pow(B, A);

            st.push(result);
        } else {
            // Token is an operand number
            double num = stod(token);
            st.push(num);
        }
    }

    if (!st.empty()) {
        return st.top();
    }
    return 0;
}

int main() {
    cout << "=== EVALUATION OF POSTFIX EXPRESSION ===" << endl;

    // Manual example: P: 5, 6, 2, +, *, 12, 4, /, -
    string postfix = "5 6 2 + * 12 4 / -";
    cout << "Postfix Expression: " << postfix << endl;

    double value = evaluatePostfix(postfix);
    cout << "Evaluated Result:   " << value << endl;
    cout << "Expected Result:    37" << endl;

    return 0;
}""",
        "quizzes": [
            {
                "question": "What data structure is used to evaluate a postfix expression?",
                "options": [
                    "Stack",
                    "Queue",
                    "Binary Tree",
                    "Hash Table"
                ],
                "correctAnswer": "Stack",
                "explanation": "A stack is used during postfix evaluation to hold numerical operands until an operator is encountered."
            },
            {
                "question": "When an operator ⊗ is encountered in postfix evaluation and two top elements are popped (A then B), how is the operation evaluated?",
                "options": [
                    "B ⊗ A",
                    "A ⊗ B",
                    "A ⊗ A",
                    "B ⊗ B"
                ],
                "correctAnswer": "B ⊗ A",
                "explanation": "Because the stack is LIFO, the top element A was pushed second, making B the first operand. Thus non-commutative operations like division or subtraction require B ⊗ A (e.g., B / A)."
            },
            {
                "question": "In the manual's example '5, 6, 2, +, *, 12, 4, /, -', what is the state of the STACK immediately after evaluating '+'?",
                "options": [
                    "5, 8",
                    "8",
                    "40",
                    "5, 6, 2"
                ],
                "correctAnswer": "5, 8",
                "explanation": "Operands 6 and 2 are popped and added (6 + 2 = 8). The result 8 is pushed back onto the stack above 5, giving [5, 8]."
            },
            {
                "question": "What is the final calculated value of the postfix expression '5, 6, 2, +, *, 12, 4, /, -'?",
                "options": [
                    "37",
                    "40",
                    "33",
                    "52"
                ],
                "correctAnswer": "37",
                "explanation": "5 * (6 + 2) - 12 / 4 = 5 * 8 - 3 = 40 - 3 = 37."
            },
            {
                "question": "What happens when an operand is encountered during postfix evaluation?",
                "options": [
                    "It is placed directly onto the STACK",
                    "It is added to the output string",
                    "It is multiplied by the top of STACK",
                    "It triggers a stack pop operation"
                ],
                "correctAnswer": "It is placed directly onto the STACK",
                "explanation": "Step 3 of the postfix evaluation algorithm specifies: If an operand is encountered, put it on STACK."
            }
        ],
        "flashcards": [
            {
                "question": "How are operands processed in Postfix evaluation?",
                "answer": "Operands are pushed onto the operand STACK as they are scanned from left to right."
            },
            {
                "question": "Why is operand order critical when popping for subtraction or division?",
                "answer": "Because the top item is A and the second item is B, the operation must be evaluated as B - A or B / A."
            },
            {
                "question": "Where does the final result reside after evaluating a postfix expression?",
                "answer": "As the single remaining element on the top of the STACK."
            },
            {
                "question": "What is the equivalent infix expression of '5 6 2 + * 12 4 / -'?",
                "answer": "5 * (6 + 2) - 12 / 4, which equals 37."
            }
        ]
    },

    # =========================================================================
    # LAB 12
    # =========================================================================
    {
        "order": 12,
        "title": "Lab 12: Practice Quick Sort technique",
        "content": """# Lab #: 12: Practice Quick Sort technique

## Objective:-
The objective of this session is to understand the implementation of Quick sort technique in C++.

## Software Tools:-
Dev C++.

---

## Theory:-
**Quicksort** is an algorithm of the **divide-and-conquer** type. That is, the problem of sorting a set is reduced to the problem of sorting two smaller sets. We illustrate this **"reduction step"** by means of a specific example.

### Reduction Step Illustration:
Suppose `A` is the following list of 12 numbers:
```text
(44), 33, 11, 55, 77, 90, 40, 60, 99, 22, 88, (66)
```
The reduction step of the quicksort algorithm finds the final sorted position of one of the numbers; in this illustration, we use the first number, **44** (the pivot).

This is accomplished as follows:
1. Beginning with the last number, `66`, scan the list from **right to left**, comparing each number with `44` and stopping at the first number less than `44`. The number is `22`. Interchange `44` and `22` to obtain the list:
   ```text
   (22), 33, 11, 55, 77, 90, 40, 60, 99, (44), 88, 66
   ```
   *(Observe that the numbers 88 and 66 to the right of 44 are each greater than 44.)*

2. Beginning with `22`, next scan the list in the opposite direction, from **left to right**, comparing each number with `44` and stopping at the first number greater than `44`. The number is `55`. Interchange `44` and `55` to obtain the list:
   ```text
   22, 33, 11, (44), 77, 90, 40, 60, 99, (55), 88, 66
   ```
   *(Observe that the numbers 22, 33 and 11 to the left of 44 are each less than 44.)*

3. Beginning this time with `55`, now scan the list in the original direction, from **right to left**, until meeting the first number less than `44`. It is `40`. Interchange `44` and `40` to obtain the list:
   ```text
   22, 33, 11, (40), 77, 90, (44), 60, 99, 55, 88, 66
   ```
   *(Again, the numbers to the right of 44 are each greater than 44.)*

4. Beginning with `40`, scan the list from **left to right**. The first number greater than `44` is `77`. Interchange `44` and `77` to obtain the list:
   ```text
   22, 33, 11, 40, (44), 90, (77), 60, 99, 55, 88, 66
   ```
   *(Again, the numbers to the left of 44 are each less than 44.)*

5. Beginning with `77`, scan the list from **right to left** seeking a number less than `44`. We do not meet such a number before meeting `44`. This means all numbers have been scanned and compared with `44`. 

Furthermore, all numbers less than `44` now form the sublist of numbers to the left of `44`, and all numbers greater than `44` now form the sublist of numbers to the right of `44`, as shown below:
```text
[22, 33, 11, 40]   (44)   [90, 77, 60, 99, 55, 88, 66]
-----------------         ----------------------------
  First sublist                  Second sublist
```

![Quick Sort Partitioning](assets/images/university/dsa/lab12_quicksort_partition.png)

*Figure 12.1: Division into first sublist, placed pivot 44, and second sublist.*

Thus `44` is correctly placed in its final position, and the task of sorting the original list `A` has now been reduced to the task of sorting each of the above sublists.

---

### Algorithm: QUICK(A, N, BEG, END, LOC)
```text
QUICK(A, N, BEG, END, LOC)
Here A is an array with N elements. Parameters BEG and END contain the boundary values
of the sublist of A to which this procedure applies. LOC keeps track of the position
of the first element A[BEG] of the sublist during the procedure. The local variables
LEFT and RIGHT will contain the boundary values of the list of elements that have not been scanned.

1. [Initialize.] Set LEFT := BEG, RIGHT := END and LOC := BEG.
2. [Scan from right to left.]
   (a) Repeat while A[LOC] <= A[RIGHT] and LOC != RIGHT:
       RIGHT := RIGHT - 1.
       [End of loop.]
   (b) If LOC = RIGHT, then: Return.
   (c) If A[LOC] > A[RIGHT], then:
       (i) [Interchange A[LOC] and A[RIGHT].]
           TEMP := A[LOC], A[LOC] := A[RIGHT], A[RIGHT] := TEMP.
       (ii) Set LOC := RIGHT.
       (iii) Go to Step 3.
       [End of If structure.]
3. [Scan from left to right.]
   (a) Repeat while A[LEFT] <= A[LOC] and LEFT != LOC:
       LEFT := LEFT + 1.
       [End of loop.]
   (b) If LOC = LEFT, then: Return.
   (c) If A[LEFT] > A[LOC], then:
       (i) [Interchange A[LEFT] and A[LOC].]
           TEMP := A[LOC], A[LOC] := A[LEFT], A[LEFT] := TEMP.
       (ii) Set LOC := LEFT.
       (iii) Go to Step 2.
       [End of If structure.]
```

![Algorithm QUICK](assets/images/university/dsa/lab12_quicksort_algorithm.png)

*Figure 12.2: Procedure QUICK(A, N, BEG, END, LOC) for sublist reduction.*

---

## Lab Tasks:
Make C++ Program codes for Quick sorting algorithm and verify its working by taking an array of 10 numbers as input.
""",
        "codeSnippet": """// Complete C++ Program for Quick Sort Algorithm verified on 10 numbers
#include <iostream>
using namespace std;

// Procedure to partition the array using pivot
int partition(int A[], int beg, int end) {
    int left = beg;
    int right = end;
    int loc = beg;

    while (true) {
        // Scan right to left
        while (A[loc] <= A[right] && loc != right) {
            right--;
        }
        if (loc == right) {
            return loc;
        }
        if (A[loc] > A[right]) {
            int temp = A[loc];
            A[loc] = A[right];
            A[right] = temp;
            loc = right;
        }

        // Scan left to right
        while (A[left] <= A[loc] && left != loc) {
            left++;
        }
        if (loc == left) {
            return loc;
        }
        if (A[left] > A[loc]) {
            int temp = A[loc];
            A[loc] = A[left];
            A[left] = temp;
            loc = left;
        }
    }
}

// Recursive QuickSort function
void quickSort(int A[], int beg, int end) {
    if (beg < end) {
        int loc = partition(A, beg, end);
        quickSort(A, beg, loc - 1); // Sort left sublist
        quickSort(A, loc + 1, end); // Sort right sublist
    }
}

void printArray(int A[], int n) {
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main() {
    cout << "=== QUICK SORT DEMONSTRATION ===" << endl;
    
    // Testing with an array of 10 numbers as requested in Lab Tasks
    const int N = 10;
    int A[N] = {44, 33, 11, 55, 77, 90, 40, 60, 99, 22};

    cout << "Original Array (10 numbers): ";
    printArray(A, N);

    quickSort(A, 0, N - 1);

    cout << "Sorted Array:                ";
    printArray(A, N);

    return 0;
}""",
        "quizzes": [
            {
                "question": "What algorithmic paradigm does Quick Sort employ?",
                "options": [
                    "Divide-and-Conquer",
                    "Dynamic Programming",
                    "Greedy Approach",
                    "Brute Force"
                ],
                "correctAnswer": "Divide-and-Conquer",
                "explanation": "Quick Sort is a divide-and-conquer algorithm that divides an array into two sublists around a pivot element and recursively sorts each sublist."
            },
            {
                "question": "In the reduction step on list [44, 33, 11, 55, 77, 90, 40, 60, 99, 22, 88, 66], what is the first number swapped with pivot 44 during the right-to-left scan?",
                "options": [
                    "22",
                    "66",
                    "33",
                    "40"
                ],
                "correctAnswer": "22",
                "explanation": "Scanning from 66 leftward, 22 is the first element found that is less than 44, so 44 and 22 are interchanged."
            },
            {
                "question": "What is the average-case time complexity of Quick Sort?",
                "options": [
                    "O(N log N)",
                    "O(N^2)",
                    "O(N)",
                    "O(log N)"
                ],
                "correctAnswer": "O(N log N)",
                "explanation": "On average, the partitioning step divides the array approximately in half, yielding O(N log N) time complexity."
            },
            {
                "question": "When does Quick Sort exhibit its worst-case performance of O(N^2)?",
                "options": [
                    "When the array is already sorted and the smallest or largest element is consistently picked as the pivot",
                    "When the pivot divides the array into two equal halves",
                    "When the array elements are randomly shuffled",
                    "When the array size is a power of 2"
                ],
                "correctAnswer": "When the array is already sorted and the smallest or largest element is consistently picked as the pivot",
                "explanation": "If the selected pivot creates severely unbalanced sublists (e.g. 0 elements on one side and N-1 elements on the other), recursion depth reaches N, leading to O(N^2) complexity."
            },
            {
                "question": "In the QUICK algorithm, what condition terminates the reduction step and indicates that the pivot is in its final position?",
                "options": [
                    "LOC = RIGHT (or LOC = LEFT)",
                    "LEFT > RIGHT",
                    "A[LOC] == 0",
                    "LOC == N"
                ],
                "correctAnswer": "LOC = RIGHT (or LOC = LEFT)",
                "explanation": "When the scan converges such that LOC equals the boundary index (RIGHT or LEFT), all elements have been verified and the pivot is in its final sorted position."
            }
        ],
        "flashcards": [
            {
                "question": "What is the core idea of the reduction step in Quick Sort?",
                "answer": "To place one element (the pivot) in its final sorted position such that all smaller elements are to its left and all larger elements are to its right."
            },
            {
                "question": "What are the two scans performed in the QUICK partition procedure?",
                "answer": "A right-to-left scan seeking elements smaller than the pivot, followed by a left-to-right scan seeking elements greater than the pivot."
            },
            {
                "question": "What is the average time complexity of Quick Sort?",
                "answer": "O(N log N)."
            },
            {
                "question": "What is the worst-case time complexity of Quick Sort?",
                "answer": "O(N^2), occurring when partitions are maximally unbalanced."
            }
        ]
    },

    # =========================================================================
    # LAB 13
    # =========================================================================
    {
        "order": 13,
        "title": "Lab 13: Execute Expression Tree implementation",
        "content": """# Lab #: 13: Execute Expression Tree implementation

## Objective:-
To understand the implementation of Expression Trees and learn different traversal orders of expression trees (inorder, postorder, preorder).

## Software Tools:-
1. Dev C++.

---

## Theory:-
### Introduction: Expression Trees
An **Expression Tree** is a binary tree in which each **internal node corresponds to an operator** and each **leaf node corresponds to an operand**.

For example, let `E` denote the following algebraic expression:
```text
[a + (b - c)] * [(d - e) / (f + g - h)]
```

The corresponding binary tree `T` appears in Figure 13.1.

![Expression Tree](assets/images/university/dsa/lab13_expression_tree.png)

*Figure 13.1: Binary Expression Tree T for `[a + (b - c)] * [(d - e) / (f + g - h)]`.*

The reader can verify by inspection that the preorder and postorder traversals of `T` are as follows:
- **(Preorder / Prefix):**
  ```text
  * + a - b c / - d e - + f g h
  ```
- **(Postorder / Postfix):**
  ```text
  a b c - + d e - f g + h - / *
  ```
- **(Inorder / Infix):**
  Yields the original infix expression (with appropriate parenthesization):
  ```text
  (a + (b - c)) * ((d - e) / ((f + g) - h))
  ```

---

### Notations Comparison:
| Infix | Prefix | Postfix |
| :--- | :--- | :--- |
| `A + B` | `+ A B` | `A B +` |
| `A + B * C` | `+ A * B C` | `A B C * +` |

---

### Traversal Techniques:
The three tree traversal techniques are:
1. **Preorder:**
   - (1) Process the root `R`.
   - (2) Traverse the left subtree of `R` in preorder.
   - (3) Traverse the right subtree of `R` in preorder.
2. **Inorder:**
   - (1) Traverse the left subtree of `R` in inorder.
   - (2) Process the root `R`.
   - (3) Traverse the right subtree of `R` in inorder.
3. **Postorder:**
   - (1) Traverse the left subtree of `R` in postorder.
   - (2) Traverse the right subtree of `R` in postorder.
   - (3) Process the root `R`.

---

### Construction of Expression Tree:
For constructing an expression tree we use a **stack**. We loop through the input postfix expression and do following for every character:
1. **If character is operand:** create a node and push that into stack.
2. **If character is operator:** pop two values from stack, make them its children (first popped is right child, second popped is left child), and push the current operator node again.

At the end, the only remaining element of the stack will be the **root of the expression tree**.

---

## Lab Task: -
Make C++ program for Expression Tree. The program should be able to get a postfix expression and output the infix expression.
""",
        "codeSnippet": """// Complete C++ Program for Expression Tree Construction from Postfix and Traversals
#include <iostream>
#include <stack>
#include <string>
#include <cctype>

using namespace std;

// Node structure for Expression Tree
struct TreeNode {
    char data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(char val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Check if character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^');
}

// Construction of Expression Tree from Postfix expression
TreeNode* constructTree(string postfix) {
    stack<TreeNode*> st;

    for (int i = 0; i < postfix.length(); i++) {
        char ch = postfix[i];

        if (ch == ' ') continue;

        // If operand, push node to stack
        if (isalnum(ch)) {
            st.push(new TreeNode(ch));
        }
        // If operator, pop two nodes and make them children
        else if (isOperator(ch)) {
            TreeNode* opNode = new TreeNode(ch);

            TreeNode* rightChild = st.top(); st.pop();
            TreeNode* leftChild = st.top(); st.pop();

            opNode->left = leftChild;
            opNode->right = rightChild;

            st.push(opNode);
        }
    }

    return st.top(); // Root of the expression tree
}

// Inorder traversal produces Infix expression
void inorder(TreeNode* root) {
    if (root != NULL) {
        if (isOperator(root->data)) cout << "(";
        inorder(root->left);
        cout << root->data;
        inorder(root->right);
        if (isOperator(root->data)) cout << ")";
    }
}

// Preorder traversal produces Prefix expression
void preorder(TreeNode* root) {
    if (root != NULL) {
        cout << root->data << " ";
        preorder(root->left);
        preorder(root->right);
    }
}

// Postorder traversal produces Postfix expression
void postorder(TreeNode* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        cout << root->data << " ";
    }
}

int main() {
    cout << "=== EXPRESSION TREE IMPLEMENTATION ===" << endl;

    // Test postfix input: a b c - + d e - f g + h - / *
    string postfix = "ab+c*";
    cout << "Postfix Expression Input: " << postfix << endl;

    TreeNode* root = constructTree(postfix);

    cout << "\nInfix Expression (Inorder):   ";
    inorder(root);
    cout << endl;

    cout << "Prefix Expression (Preorder): ";
    preorder(root);
    cout << endl;

    cout << "Postfix Expression (Postorder): ";
    postorder(root);
    cout << endl;

    return 0;
}""",
        "quizzes": [
            {
                "question": "In an Expression Tree, what do the internal nodes and leaf nodes represent?",
                "options": [
                    "Internal nodes represent operators; leaf nodes represent operands",
                    "Internal nodes represent operands; leaf nodes represent operators",
                    "All nodes represent operands",
                    "Root is always an operand and leaves are operators"
                ],
                "correctAnswer": "Internal nodes represent operators; leaf nodes represent operands",
                "explanation": "In binary expression trees, leaf nodes have no children and store operands, while internal nodes represent binary operators whose children are the operands or sub-expressions."
            },
            {
                "question": "Which tree traversal order yields the standard Infix representation of an expression tree?",
                "options": [
                    "Inorder traversal",
                    "Preorder traversal",
                    "Postorder traversal",
                    "Level-order traversal"
                ],
                "correctAnswer": "Inorder traversal",
                "explanation": "Inorder traversal visits (Left Subtree, Root, Right Subtree), placing the operator between its two operands to yield the infix expression."
            },
            {
                "question": "During the stack-based construction of an expression tree from a postfix expression, what happens when an operator is encountered?",
                "options": [
                    "Pop two nodes from stack, attach them as children of the operator node, and push the operator node back",
                    "Push the operator directly onto the stack",
                    "Pop all operands and discard them",
                    "Clear the stack and print the tree"
                ],
                "correctAnswer": "Pop two nodes from stack, attach them as children of the operator node, and push the operator node back",
                "explanation": "When an operator is encountered, the top node becomes its right child and the next-to-top node becomes its left child; the operator node is then pushed back onto the stack."
            },
            {
                "question": "What does a Preorder traversal of an expression tree yield?",
                "options": [
                    "Prefix (Polish) notation",
                    "Postfix notation",
                    "Infix notation",
                    "Alphabetical order"
                ],
                "correctAnswer": "Prefix (Polish) notation",
                "explanation": "Preorder traversal visits (Root, Left Subtree, Right Subtree), which visits the operator before its operands, yielding prefix notation."
            },
            {
                "question": "In the manual's algebraic expression `[a + (b - c)] * [(d - e) / (f + g - h)]`, what is the root node of the binary tree?",
                "options": [
                    "The multiplication operator `*`",
                    "The addition operator `+`",
                    "The division operator `/`",
                    "The operand `a`"
                ],
                "correctAnswer": "The multiplication operator `*`",
                "explanation": "The expression consists of two major sub-expressions multiplied together: `[a + (b - c)]` and `[...]`, making `*` the main operator at the root node of the tree."
            }
        ],
        "flashcards": [
            {
                "question": "What is an Expression Tree?",
                "answer": "A binary tree where internal nodes correspond to operators and leaf nodes correspond to operands."
            },
            {
                "question": "What notation does Inorder traversal of an expression tree produce?",
                "answer": "Infix notation (when parenthesized)."
            },
            {
                "question": "What notation does Postorder traversal of an expression tree produce?",
                "answer": "Postfix notation (Reverse Polish notation)."
            },
            {
                "question": "How are operands handled when constructing an expression tree from postfix?",
                "answer": "Each operand is instantiated as a standalone tree node and pushed onto the stack."
            }
        ]
    },

    # =========================================================================
    # LAB 14
    # =========================================================================
    {
        "order": 14,
        "title": "Lab 14: Practice Binary Search Tree Implementation",
        "content": """# Lab #: 14: Practice Binary Search Tree Implementation

## OBJECTIVE :-
To understand the Binary Search Tree and implementation of its basic insertion, deletion and traversal operations.

## Software Tools:-
1. Dev C++.

---

## Theory:-
### Introduction: BINARY SEARCH TREES
A **Binary Search Tree (BST)** is a tree in which all the nodes follow the below mentioned properties:
- The left sub-tree of a node has a value less than or equal to its parent node's value.
- The right sub-tree of a node has a value greater than to its parent node's value.

### REPRESENTATION
A BST is a collection of nodes arranged in a way where they maintain BST properties. Each node has a value. While searching, the desired value is compared to the values in BST and if found, `true` is returned.

Following is a pictorial representation of BST −

![Binary Search Tree Representation](assets/images/university/dsa/lab14_bst_tree.png)

*Figure 14.1: Binary Search Tree with root node value (27), all smaller values on the left subtree (14, 10, 19), and higher values on the right subtree (35, 31, 42).*

We observe that the root node value (`27`) has all less-values on the left sub-tree and the higher values on the right sub-tree.

---

### BASIC OPERATIONS
Following are the basic operations of a tree:
- **Search** − Searches an element in a tree.
- **Insert** − Inserts an element in a tree.
- **Pre-order Traversal** − Traverses a tree in a pre-order manner.
- **In-order Traversal** − Traverses a tree in an in-order manner.
- **Post-order Traversal** − Traverses a tree in a post-order manner.
- **Delete** − Deletes an element in a tree.

---

### IMPLEMENTATION: Class and Node
Define a class `BST` with a `struct TreeNode` having some data, references to its left and right child nodes:
```cpp
class BST {
    struct TreeNode {
        int data;
        TreeNode *right;
        TreeNode *left;
    };
    TreeNode *root;
public:
    // Methods for search, insert, traversals, and deletion
};
```

---

### INSERT OPERATION & SEARCH ALGORITHM
Whenever an element is to be inserted, first locate its proper location. Start searching from the root node, then if the data is less than the key value, search for the empty location in the left subtree and insert the data. Otherwise, search for the empty location in the right subtree and insert the data.

#### Searching and Inserting in BST:
Suppose an `ITEM` of information is given. The following algorithm finds the location of `ITEM` in the binary search tree `T`, or inserts `ITEM` as a new node in its appropriate place in the tree:
- **(a)** Compare `ITEM` with the root node `N` of the tree:
  - (i) If `ITEM < N`, proceed to the left child of `N`.
  - (ii) If `ITEM > N`, proceed to the right child of `N`.
- **(b)** Repeat Step (a) until one of the following occurs:
  - (i) We meet a node `N` such that `ITEM = N`. In this case the search is successful.
  - (ii) We meet an empty subtree, which indicates that the search is unsuccessful, and we insert `ITEM` in place of the empty subtree.

*In other words, proceed from the root `R` down through the tree `T` until finding `ITEM` in `T` or inserting `ITEM` as a terminal node in `T`.*

---

### BST Traversals:
- **1-Inorder:** The ordering is: the left subtree, the current node, the right subtree. *(Produces keys in strictly ascending sorted order!)*
- **2-Preorder:** The ordering is: the current node, the left subtree, the right subtree.
- **3-Postorder:** The ordering is: the left subtree, the right subtree, the current node.

![BST Traversal Curves](assets/images/university/dsa/lab14_bst_traversals.png)

*Figure 14.2: Traversal paths across binary tree.*

#### Example Tree Traversals:
For the binary tree shown with root `F`:
- **In-order:** `A, B, C, D, E, F, G, H, I`
- **Pre-order:** `F, B, A, D, C, E, G, I, H`
- **Post-order:** `A, C, E, D, B, H, I, G, F`

---

### BST Deletion:
While deleting a node in BST, we want to delete the node, but preserve the sub-trees that the node links to.

There are 3 possible situations to be faced when deleting a node:
1. **The node is a leaf (no children):** Simply remove the node and update its parent's pointer to `NULL`.
2. **The node has one child:** The child node takes the place of the deleted node by directly connecting to the deleted node's parent.

![BST Deletion with One Child](assets/images/university/dsa/lab14_bst_deletion.png)

*Figure 14.3: Deletion of a node with one child.*

3. **The node has two children:** We cannot attach both of the node's subtrees to its parent. **The inorder successor will take the place of the deleted node in case 2.** The inorder successor is the node with the smallest value in the right subtree. After copying its value into the target node, the inorder successor is deleted from the right subtree.

![BST Deletion with Inorder Successor](assets/images/university/dsa/lab14_bst_deletion_rewire.png)

*Figure 14.4: Deletion of a node with two children by substituting its Inorder Successor.*

---

## LAB TASK: -
Make C++ program to create a Binary Search Tree. Your code must be able to perform:
- a. Search
- b. Insertion
- c. Traversal (Inorder, Preorder, Postorder)
- d. Deletion
""",
        "codeSnippet": """// Complete C++ Program for Binary Search Tree Implementation
#include <iostream>
using namespace std;

class BST {
private:
    struct TreeNode {
        int data;
        TreeNode* left;
        TreeNode* right;

        TreeNode(int val) {
            data = val;
            left = NULL;
            right = NULL;
        }
    };

    TreeNode* root;

    // Helper: Insert recursive
    TreeNode* insertHelper(TreeNode* node, int val) {
        if (node == NULL) {
            return new TreeNode(val);
        }
        if (val < node->data) {
            node->left = insertHelper(node->left, val);
        } else if (val > node->data) {
            node->right = insertHelper(node->right, val);
        }
        return node;
    }

    // Helper: Search recursive
    bool searchHelper(TreeNode* node, int key) {
        if (node == NULL) return false;
        if (node->data == key) return true;
        if (key < node->data) return searchHelper(node->left, key);
        return searchHelper(node->right, key);
    }

    // Helper: Find Minimum Node (Inorder Successor)
    TreeNode* findMin(TreeNode* node) {
        while (node->left != NULL) {
            node = node->left;
        }
        return node;
    }

    // Helper: Delete recursive
    TreeNode* deleteHelper(TreeNode* node, int key) {
        if (node == NULL) return NULL;

        if (key < node->data) {
            node->left = deleteHelper(node->left, key);
        } else if (key > node->data) {
            node->right = deleteHelper(node->right, key);
        } else {
            // Node found!
            // Case 1: Leaf node
            if (node->left == NULL && node->right == NULL) {
                delete node;
                return NULL;
            }
            // Case 2: One child (right only)
            else if (node->left == NULL) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            }
            // Case 2: One child (left only)
            else if (node->right == NULL) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }
            // Case 3: Two children
            else {
                TreeNode* successor = findMin(node->right);
                node->data = successor->data;
                node->right = deleteHelper(node->right, successor->data);
            }
        }
        return node;
    }

    // Traversals
    void inorderHelper(TreeNode* node) {
        if (node != NULL) {
            inorderHelper(node->left);
            cout << node->data << " ";
            inorderHelper(node->right);
        }
    }

    void preorderHelper(TreeNode* node) {
        if (node != NULL) {
            cout << node->data << " ";
            preorderHelper(node->left);
            preorderHelper(node->right);
        }
    }

    void postorderHelper(TreeNode* node) {
        if (node != NULL) {
            postorderHelper(node->left);
            postorderHelper(node->right);
            cout << node->data << " ";
        }
    }

public:
    BST() {
        root = NULL;
    }

    void insert(int val) {
        root = insertHelper(root, val);
        cout << "Inserted " << val << " into BST." << endl;
    }

    bool search(int key) {
        return searchHelper(root, key);
    }

    void remove(int key) {
        root = deleteHelper(root, key);
        cout << "Deleted " << key << " from BST." << endl;
    }

    void inorder() {
        cout << "In-order Traversal:   ";
        inorderHelper(root);
        cout << endl;
    }

    void preorder() {
        cout << "Pre-order Traversal:  ";
        preorderHelper(root);
        cout << endl;
    }

    void postorder() {
        cout << "Post-order Traversal: ";
        postorderHelper(root);
        cout << endl;
    }
};

int main() {
    cout << "=== BINARY SEARCH TREE (BST) DEMONSTRATION ===" << endl;
    BST tree;

    // Building manual example tree: root 27, children 14, 35, 10, 19, 31, 42
    tree.insert(27);
    tree.insert(14);
    tree.insert(35);
    tree.insert(10);
    tree.insert(19);
    tree.insert(31);
    tree.insert(42);

    cout << endl;
    tree.inorder();
    tree.preorder();
    tree.postorder();

    cout << "\nSearch 19: " << (tree.search(19) ? "FOUND" : "NOT FOUND") << endl;
    cout << "Search 99: " << (tree.search(99) ? "FOUND" : "NOT FOUND") << endl;

    cout << "\nDeleting node with one child (leaf/single) or two children..." << endl;
    tree.remove(14); // Node 14 has two children (10 and 19)
    tree.inorder();

    return 0;
}""",
        "quizzes": [
            {
                "question": "What is the defining property of a Binary Search Tree (BST)?",
                "options": [
                    "Left subtree values <= parent value, and Right subtree values > parent value",
                    "All nodes must have exactly two children",
                    "Left subtree values > parent value, and Right subtree values < parent value",
                    "Root value is always the average of all nodes"
                ],
                "correctAnswer": "Left subtree values <= parent value, and Right subtree values > parent value",
                "explanation": "In a BST, every node satisfies the ordering condition that keys in the left subtree are smaller than or equal to the parent key, and keys in the right subtree are greater."
            },
            {
                "question": "Which traversal of a Binary Search Tree always outputs the node keys in strictly ascending sorted order?",
                "options": [
                    "In-order Traversal",
                    "Pre-order Traversal",
                    "Post-order Traversal",
                    "Level-order Traversal"
                ],
                "correctAnswer": "In-order Traversal",
                "explanation": "Because In-order visits (Left Subtree, Current Node, Right Subtree), it processes all smaller keys first, then the parent, then all larger keys, yielding sorted order."
            },
            {
                "question": "When deleting a node that has TWO children in a BST, which node takes its place?",
                "options": [
                    "The in-order successor (or in-order predecessor)",
                    "The parent node",
                    "The root of the tree",
                    "A newly allocated null node"
                ],
                "correctAnswer": "The in-order successor (or in-order predecessor)",
                "explanation": "When deleting a node with two children, its in-order successor (the smallest value in its right subtree) replaces its value, preserving the BST ordering property."
            },
            {
                "question": "What is the order of visit in Post-order tree traversal?",
                "options": [
                    "Left subtree, Right subtree, Current node",
                    "Current node, Left subtree, Right subtree",
                    "Left subtree, Current node, Right subtree",
                    "Right subtree, Current node, Left subtree"
                ],
                "correctAnswer": "Left subtree, Right subtree, Current node",
                "explanation": "Post-order traversal recursively visits the left subtree, then the right subtree, and finally processes the current node."
            },
            {
                "question": "What is the average time complexity for searching an element in a balanced BST containing N nodes?",
                "options": [
                    "O(log N)",
                    "O(N)",
                    "O(N log N)",
                    "O(1)"
                ],
                "correctAnswer": "O(log N)",
                "explanation": "In a balanced BST, each comparison eliminates approximately half of the remaining nodes, leading to logarithmic O(log N) search complexity."
            }
        ],
        "flashcards": [
            {
                "question": "What is the BST property?",
                "answer": "All keys in the left subtree are <= parent key, and all keys in the right subtree are > parent key."
            },
            {
                "question": "Why is In-order traversal special for a BST?",
                "answer": "It visits the keys in strictly ascending numerical/alphabetical sorted order."
            },
            {
                "question": "How is a BST node with two children deleted?",
                "answer": "Its value is replaced by its in-order successor (minimum value in right subtree), and the successor is then removed."
            },
            {
                "question": "What are the three main tree traversals?",
                "answer": "1. In-order (Left, Root, Right), 2. Pre-order (Root, Left, Right), 3. Post-order (Left, Right, Root)."
            }
        ]
    }
]

LABS_DATA = LABS_PART1 + LABS_PART2

def seed_dsa_curriculum(verbose: bool = True) -> Dict[str, Any]:
    """
    Seeds the Data Structures and Algorithms (CS-221) curriculum into Neon PostgreSQL.
    Non-destructive: Touches only the CS-221 course, preserving all other courses and user accounts.
    """
    db = Prisma()
    owns_connection = False

    try:
        for attempt in range(5):
            try:
                if not db.is_connected():
                    db.connect()
                    owns_connection = True
                break
            except Exception as e:
                print(f"[!] Connection attempt {attempt + 1} failed: {e}. Retrying in 2 seconds...", flush=True)
                time.sleep(2)
        else:
            raise RuntimeError("Failed to connect to Neon PostgreSQL after 5 attempts.")

        if verbose:
            print("=" * 85)
            print("[*] Connected to Neon PostgreSQL Database via Prisma.")
            print(f"[*] Target Course: '{COURSE_DATA['title']}' (Category: {COURSE_DATA['category']})")
            print("=" * 85)

        # 1. Non-destructive lookup or creation of Course/Lesson record
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
                print(f"[+] Created Course record: ID={lesson.id} | Title='{lesson.title}'")
        else:
            lesson = db.lesson.update(
                where={"id": lesson.id},
                data={
                    "description": COURSE_DATA["description"],
                    "color": COURSE_DATA["color"]
                }
            )
            if verbose:
                print(f"[*] Found existing Course record: ID={lesson.id} | Title='{lesson.title}'")

        # 2. Idempotent cleanup of old steps, quizzes, and flashcards for ONLY THIS COURSE
        del_q = db.quiz.delete_many(where={"lessonId": lesson.id})
        del_f = db.flashcard.delete_many(where={"lessonId": lesson.id})
        del_s = db.lessonstep.delete_many(where={"lessonId": lesson.id})
        if verbose:
            print(f"[*] Cleared previous records for DSA course: {del_s} steps, {del_q} quizzes, {del_f} flashcards.")

        # 3. Insert Labs LessonSteps, Quizzes, and Flashcards
        summary_rows = []
        total_quizzes = 0
        total_flashcards = 0

        def safe_op(op_func, max_retries=5, delay=0.8):
            for attempt in range(max_retries):
                try:
                    return op_func()
                except Exception as ex:
                    if attempt == max_retries - 1:
                        raise ex
                    time.sleep(delay)

        for lab in LABS_DATA:
            step = safe_op(lambda: db.lessonstep.create(
                data={
                    "lessonId": lesson.id,
                    "order": lab["order"],
                    "title": lab["title"],
                    "content": lab["content"],
                    "codeSnippet": lab.get("codeSnippet", "")
                }
            ))
            time.sleep(0.05)

            # Insert Quizzes linked to both lessonId and lessonStepId
            for q in lab["quizzes"]:
                safe_op(lambda q=q: db.quiz.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": q["question"],
                        "options": q["options"],
                        "correctAnswer": q["correctAnswer"],
                        "explanation": q.get("explanation", "")
                    }
                ))
                total_quizzes += 1
                time.sleep(0.05)

            # Insert Flashcards linked to both lessonId and lessonStepId
            for fc in lab["flashcards"]:
                safe_op(lambda fc=fc: db.flashcard.create(
                    data={
                        "lessonId": lesson.id,
                        "lessonStepId": step.id,
                        "question": fc["question"],
                        "answer": fc["answer"]
                    }
                ))
                total_flashcards += 1
                time.sleep(0.05)

            summary_rows.append({
                "lab_num": f"Lab {lab['order']}",
                "title": lab["title"][:50],
                "quizzes_count": len(lab["quizzes"]),
                "flashcards_count": len(lab["flashcards"])
            })

        if verbose:
            print("\n" + "=" * 85)
            print("SUMMARY TABLE: UNIVERSITY DSA (CS-221) ALL 14 LABS SEEDED")
            print("=" * 85)
            print(f"{'Lab #':<8} | {'Title':<52} | {'Quizzes':<8} | {'Flashcards':<10}")
            print("-" * 85)
            for row in summary_rows:
                print(f"{row['lab_num']:<8} | {row['title']:<52} | {row['quizzes_count']:<8} | {row['flashcards_count']:<10}")
            print("=" * 85)
            print(f"Total LessonSteps: {len(LABS_DATA)}")
            print(f"Total Quizzes:     {total_quizzes}")
            print(f"Total Flashcards:  {total_flashcards}")
            print(f"Category:          {COURSE_DATA['category']}")
            print("=" * 85)

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
    seed_dsa_curriculum()

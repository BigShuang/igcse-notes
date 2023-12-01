## 2 Types of programming language, translators and IDEs
Programmers use many different programming languages to communicate with computers. Computers only ‘understand’ their own language, called machine code. 
A program needs to be translated into machine code before it can be ‘understood’ by a computer.

A computer program is a list of instructions that enable a computer to perform a specific task. 
Computer programs can be written in high-level languages and low-level languages depending on the task to be performed and the computer to be used. 
Most programmers write programs in high-level languages.

### 1 High-level languages and low-level languages

#### High-level languages
High-level languages enable a programmer to focus on the problem to be solved and require no knowledge of the hardware and instruction set of the computer that will use the program. 
Many high-level programming languages are portable and can be used on different types of computer.

- read and understand as the language used is closer to English
- write in a shorter time
- debug at the development stage
- maintain once in use.

Examples:
C++, Delphi, Java, Pascal, Python, Visual Basic and many more.

#### Low-level languages
Low-level languages relate to the specific architecture and hardware of a particular type of computer. 
Low-level languages can refer to machine code, the binary instructions that a computer understands, or assembly language that needs to be translated into machine code

难写难读

### 2 Assembly languages
汇编语言

Fewer programmers write programs in an assembly language. Those programmers 
who do, do so for the following reasons:
- to make use of special hardware
- to make use of special machine-dependent instructions
- to write code that doesn’t take up much space in primary memory
- to write code that performs a task very quickly

### 3 Translators
A program must be translated into binary before a computer can use it; this is done by a utility program called a translator. 
There are several types of translator program in use; each one performs a different task.

#### Compilers
A compiler is a computer program that translates an entire program written in a high-level language (HLL) into machine code all in one go so that it can be directly used by a computer to perform a required task. 
编译器是一种计算机程序，它将用高级语言（HLL）编写的整个程序一次性翻译成机器代码，以便计算机可以直接使用它来执行所需的任务。
Once a program is compiled the machine code can be used again and again to perform the same task without re-compilation. 
一旦程序被编译，机器代码就可以一次又一次地使用来执行相同的任务，而无需重新编译。
If errors are detected, then an error report is produced instead of a compiled program.
如果检测到错误，则会生成错误报告而不是编译的程序。

#### Interpreters
An interpreter is a computer program that reads a statement from a program written in a high-level language, translates it, performs the action specified and then does the same with the next statement and so on. 
解释器是一种计算机程序，它从用高级语言编写的程序中读取语句，对其进行翻译，执行指定的操作，然后对下一条语句执行相同的操作，依此类推。
If there is an error in the statement then execution ceases and an error message is output, sometimes with a suggested correction.
如果语句中存在错误，则执行将停止并输出错误消息，有时会显示建议的更正。
A program needs to be interpreted again each time it is run.
程序每次运行时都需要重新解释。

#### Assemblers
An assembler is a computer program that translates a program written in an assembly language into machine code so that it can be directly used by a computer to perform a required task. 
汇编程序是一种计算机程序，它将用汇编语言编写的程序翻译成机器代码，以便计算机可以直接使用它来执行所需的任务。
Once a program is assembled the machine code can be used again and again to perform the same task without re-assembly.
一旦程序被汇编，机器代码就可以一次又一次地使用来执行相同的任务，而无需重新汇编。

### 4 Advantages and disadvantages of compilers and interpreters
#### Interpreter
**Advantages**
- easier and quicker to debug and test programs during development
- easier to edit programs during development
**Disadvantages**
- programs cannot be run without the interpreter
- programs can take longer to execute
#### Compiler
**Advantages**
- a compiled program can be stored ready for use
- a compiled program can be executed without the compiler
- a compiled program takes up less space in memory when it is executed
- a compiled program is executed in a shorter time

**Disadvantages**
- it takes a longer time to write, test and debug programs during development

### 5 Integrated Development Environment (IDE)

An Integrated Development Environment (IDE) is used by programmers to aid the writing and development of programs. 
There are many different IDEs available; some just support one programming language, others can be used for several different programming languages.
程序员使用集成开发环境（IDE）来帮助编写和开发程序。
有许多不同的 IDE 可供使用； 有些只支持一种编程语言，有些可以用于多种不同的编程语言。

IDEs usually have these features:
- code editors 
- a translator
- a runtime environment with a debugger
- error diagnostics
- auto-completion
- auto-correction
- an auto-documenter and prettyprinting.
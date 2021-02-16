We can implement c extension in python.

1. Write C functions in *.c file(test.c) and write one structure for those functions. Initialise the our module in the same file.

2. Create setup.py file(python3 setup.py build_ext --inplace) and mention the *.c extension file in that with and module name that you want to use.

3. Create on python file which will use the module created in step 2 and call the functions writen in *.c file.

4. Run the python file created in step 3.


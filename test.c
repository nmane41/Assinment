#include <Python.h>


int fib(int n)
{
    if (n < 2)
        return n;
    else
        return fib(n-1)+fib(n-2);
}
int addC(int a, int b)
{
    return a+b;
}
static PyObject* Cfib(PyObject* self, PyObject* args)
{
    int n;
    // if our `n` value
    if(!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    // return our computed fib number
    return Py_BuildValue("i", fib(n));
}
static PyObject* helloworld(PyObject* self, PyObject* args)
{
    //printf("Hello World\n");
    return Py_BuildValue("s","Hello World\n");
}
static PyObject* add(PyObject* self, PyObject* args)
{
     int x,y;
     if(!PyArg_ParseTuple(args, "ii", &x,&y))
        return NULL;

     return Py_BuildValue("i", addC(x,y));
}
// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition
static PyMethodDef myMethods[] = {
    {"Cfib" , Cfib, METH_VARARGS,"Calculate fibonacci" },
    { "helloworld", helloworld, METH_NOARGS, "Prints Hello World" },
    {"addC" , add, METH_VARARGS,"Addition" },
    { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",
    "Test Module",
    -1,
    myMethods
};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}
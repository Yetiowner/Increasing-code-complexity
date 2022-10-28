#include <Python.h>
#include <stdio.h>

static PyObject* c_helloworld(PyObject* self, PyObject* args)
{
   char *strtoprint;
   PyArg_ParseTuple(args, "s", &strtoprint);
   printf("%s", strtoprint);
   printf("\n");
   return Py_BuildValue("i", 1);
}


static char c_helloworld_docs[] =
   "c_helloworld( ): Lol you think we write documentation?\n";

static PyMethodDef myMethods[] = {
    { "c_helloworld", (PyCFunction)c_helloworld, METH_VARARGS, c_helloworld_docs },
    {NULL}
};

static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "helloworld",
    "No documentation for you!",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_helloworld(void)
{
    return PyModule_Create(&myModule);
}

#include <Python.h>

#include "Lyra2RE.h"

static PyObject *lyra2rec0ban_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    lyra2rec0ban_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    lyra2rec0ban_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef Lyra2REc0banMethods[] = {
    { "getPoWHash", lyra2rec0ban_getpowhash, METH_VARARGS, "Returns the proof of work hash using Lyra2REc0ban hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef Lyra2REc0banModule = {
    PyModuleDef_HEAD_INIT,
    "lyra2rec0ban_hash",
    "...",
    -1,
    Lyra2REc0banMethods
};

PyMODINIT_FUNC PyInit_lyra2rec0ban_hash(void) {
    return PyModule_Create(&Lyra2REc0banModule);
}

#else

PyMODINIT_FUNC initlyra2rec0ban_hash(void) {
    (void) Py_InitModule("lyra2rec0ban_hash", Lyra2REc0banMethods);
}
#endif

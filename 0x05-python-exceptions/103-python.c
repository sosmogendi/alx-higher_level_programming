#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, x;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (x = 0; x < size; x++)
    {
        item = PyList_GetItem(p, x);
        printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, x;
    unsigned char *str;

    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);
    for (x = 0; x < size && x < 10; x++)
        printf(" %02x", str[x]);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    PyObject *str;

    if (!PyFloat_Check(p))
    {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    str = PyObject_Str(p);
    printf("[.] float object info\n");
    printf("  value: %s\n", PyUnicode_AsUTF8(str));
    Py_DECREF(str);
}

int main(void)
{
    PyObject *p;

    Py_Initialize();
    p = Py_BuildValue("[bI]", "Hello", 42);
    print_python_list(p);
    p = Py_BuildValue("y", "Holberton");
    print_python_bytes(p);
    p = Py_BuildValue("d", 3.14159);
    print_python_float(p);
    Py_Finalize();

    return (0);
}

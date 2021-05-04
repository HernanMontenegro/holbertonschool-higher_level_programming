#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: py list pointer
 * ------------------------------------------------
*/
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list_obj = (PyListObject *)p;
	size_t i = 0, size =  PyList_Size(p);

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", py_list_obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %lu: %s\n", i, Py_TYPE(py_list_obj->ob_item[i])->tp_name);
}

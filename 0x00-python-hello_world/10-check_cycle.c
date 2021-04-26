#include "lists.h"

/**
 * check_cycle - checks if the list has cycles
 * @list: head node
 * -------------------------------------
 * Return: 1 if has a cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
	int n = 0, head_n = list->n, iteration = 0;

	while (list != NULL)
	{
		n = list->n;
		if (head_n == n)
			iteration++;
		if (iteration == 2)
			return (1);

		list = list->next;
	}

	return (0);
}

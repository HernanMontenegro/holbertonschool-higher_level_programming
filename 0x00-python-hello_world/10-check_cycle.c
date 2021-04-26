#include "lists.h"

/**
 * check_cycle - checks if the list has cycles
 * @list: head node
 * -------------------------------------
 * Return: 1 if has a cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	int n = 0, head_n = list->n, iteration = 0;

	while (current != NULL)
	{
		n = current->n;
		if (head_n == n)
			iteration++;
		if (iteration == 2)
			return (1);

		current = current->next;
	}

	return (0);
}

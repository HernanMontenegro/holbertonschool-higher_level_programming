#include "lists.h"

/**
 * check_cycle - checks if the list has cycles
 * @list: head node
 * -------------------------------------
 * Return: 1 if has a cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *aux = NULL;

	if (!list)
		return (0);

	aux = list;
	while (aux)
	{
		list = aux;
		aux = aux->next;

		if (list <= aux)
			return (1);
	}

	return (0);
}

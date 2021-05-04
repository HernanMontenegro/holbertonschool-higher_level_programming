#include "lists.h"

/**
* get_nodeint_at_index - search by index
* @head: the head node
* @index: the index to search
* --------------------------------------------
* Return: the node index
*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int count = 0;
	listint_t *pos;

	pos = head;
	while (pos && count != index)
	{
		pos = pos->next;
		count++;
	}

	return (pos);
}

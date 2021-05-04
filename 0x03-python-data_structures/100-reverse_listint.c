#include "lists.h"
#include "7-get_nodeint.c"

/**
* listint_count - counts the list length
* @h: a node given
* ------------------------
* Return: the length of a list
*/
unsigned int listint_count(const listint_t *h)
{
	unsigned int count = 0;
	listint_t *current_h = (listint_t *) h;

	if (!h)
		return (count);

	while (current_h)
	{
		count++;
		current_h = current_h->next;
	}

	return (count);
}

/**
* reverse_listint - reverse a list
* @head: the head node
* -------------------------------
* Return: a pointer to the first node of the reversed list
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current;
	long int idx;

	if (!head || !*head)
		return (NULL);

	idx = listint_count(*head) - 1;
	current = get_nodeint_at_index(*head, idx);

	for (idx--; idx > listint_count(*head); idx--)
	{
		if (idx == 0)
		{
			*head = current;
			break;
		}
		current->next = get_nodeint_at_index(*head, idx);
		current = current->next;
	}

	return (*head);
}

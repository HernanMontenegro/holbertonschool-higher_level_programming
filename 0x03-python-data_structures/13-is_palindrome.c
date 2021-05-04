#include "lists.h"
#include <stdlib.h>
unsigned int listint_count(const listint_t *h);
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);

/**
 * is_palindrome - Check if a list is palindrome
 * @head: the head node
 * --------------------------------------------
 * Return: 1 if is polindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *aux = NULL, *aux2 = NULL;
	int polindrome = 1;
	unsigned int list_len, i, j;

	if (!head || !(*head))
		return (polindrome);

	list_len = listint_count(*head);

	for (i = 0, j = (list_len - 1); i < list_len; i++, j--)
	{
		aux = get_nodeint_at_index(*head, i);
		aux2 = get_nodeint_at_index(*head, j);
		if (aux->n != aux2->n)
		{
			polindrome = 0;
			return (polindrome);
		}
	}

	return (polindrome);
}

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

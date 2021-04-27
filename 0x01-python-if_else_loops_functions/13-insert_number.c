#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node in correct place
 * @head: head node
 * @number: number to insert
 * ---------------------------------------
 * Return: new element
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *new_element = NULL;

	current = *head;
	while (current != NULL)
	{
		/* Iteramos hasta encontrar nuestro hueco en el mundo... */
		if (number > current->n && number <= current->next->n)
			break;

		current = current->next;
	}
	if (current == *head)
	{
		new_element = add_nodeint_end(head, number);
		return (new_element);
	}
	new_element = malloc(sizeof(listint_t));
	if (!new_element)
		return (NULL);
	new_element->n = number;
	new_element->next = current->next;

	current->next = new_element;
	return (new_element);
}

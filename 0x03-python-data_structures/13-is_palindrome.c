#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include "100-reverse_listint.c"

/**
 * is_palindrome - Check if a list is polindrome
 * @head: the head node
 * --------------------------------------------
 * Return: 1 if is polindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev = NULL, *aux = NULL, *aux2 = NULL;
	int polindrome = 1;

	if (!(*head))
		return (polindrome);

	/* Copy every node*/
	aux = *head;
	while (aux)
	{
		add_nodeint_end(&rev, aux->n);
		aux = aux->next;
	}
	/* Revert the copy */
	reverse_listint(&rev);

	/* Compare if reverted list is equal to the original */
	aux = *head;
	aux2 = rev;
	while (aux && aux2)
	{
		/* If a single number is different, isn't a polindrome */
		if (aux->n != aux2->n)
			polindrome = 0;

		aux = aux->next;
		aux2 = aux2->next;
	}

	return (polindrome);
}

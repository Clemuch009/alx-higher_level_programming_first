#include "lists.h"

/**
 * insert_node - inserts a node at the end of a linked list
 * @head: start of linked list
 * @number: value of node to be added
 *
 * Return: address of new node, or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *ptr = *head;
	listint_t *tmp;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}

	if (ptr->n > number)
	{
		new_node->next = ptr;
		*head = new_node;
		return (*head);
	}

	while (ptr->next != NULL && ptr->next->n < new_node->n)
		ptr = ptr->next;

	tmp = ptr->next;
	ptr->next = new_node;
	new_node->next = tmp;

	return (new_node);
}

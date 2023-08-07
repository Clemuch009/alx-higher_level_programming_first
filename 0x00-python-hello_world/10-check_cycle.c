#include "lists.h"

/**
 * check_cycle - checks if a single linked list has a cycle in it
 * @list: list to be checked
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);
	
	if (list->next == list)
		return (1);

	while (fast != NULL)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
		else
			return (0);

		if (slow == fast)
			return (1);
	}

	return (0);
}

#include "lists.h"

/**
 * check_cycle - checks if singly linked list has
 * a cycle in it
 * @list: pointer to the list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *pptr;
	listint_t *prev;

	pptr = list;
	prev = list;
	while (list && pptr && pptr->next)
	{
		list = list->next;
		pptr = pptr->next->next;

		if (list == pptr)
		{
			list = prev;
			prev =  pptr;
			while (1)
			{
				pptr = prev;
				while (pptr->next != list && pptr->next != prev)
				{
					pptr = pptr->next;
				}
				if (pptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

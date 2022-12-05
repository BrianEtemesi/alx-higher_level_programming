#ifndef _LIST_H
#define _LIST_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

#endif /* LIST_H */

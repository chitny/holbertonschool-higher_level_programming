#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if theres a cycle
 * @list: linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list) 
{
	listint_t *pre = list;
	listint_t *post = list;

	if (!list)
		return (0);

	while (pre && post && post->next)
	{
		pre = pre->next;
		post = post->next->next;
		if (pre == post)
			return (1);
	}

	return (0);
}

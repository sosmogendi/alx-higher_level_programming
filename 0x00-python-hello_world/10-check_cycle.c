#include "lists.h"

/**
 * check_cycle - this function checks if a
 * singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *kobe, *swara;

	kobe = list;
	swara = list;
	while (swara && swara->next)
	{
		kobe = kobe->next;
		swara = swara->next->next;
		if (kobe == swara)
			return (1);
	}
	return (0);
}

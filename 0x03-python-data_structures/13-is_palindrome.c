#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowly = *head;
	listint_t *fast1 = *head;
	listint_t *prev = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (fast1 && fast1->next)
	{
		fast1 = fast1->next->next;
		temp = slowly->next;
		slowly->next = prev;
		prev = slowly;
		slowly = temp;
	}
	if (fast1)
		slowly = slowly->next;
	while (prev)
	{
		if (prev->n != slowly->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slowly = slowly->next;
	}
	return (is_palindrome);
}


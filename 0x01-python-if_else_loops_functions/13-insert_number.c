#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to a pointer to the head of the linked list
 * @number: Number to be inserted
 *
 * Return: Address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node2 = malloc(sizeof(listint_t));
	listint_t *cur = *head;

	if (new_node2 == NULL)
		return (NULL);
	new_node2->n = number;
	new_node2->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node2->next = *head;
		*head = new_node2;
	}
	else
	{
		while (cur->next != NULL && cur->next->n < number)
		{
			cur = cur->next;
		}
		new_node2->next = cur->next;
		curr->next = new_node2;
	}
	return (new_node);
}

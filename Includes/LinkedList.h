/*
	Title:  LinkedList.h
	Author: Jevin Evans
	Date:  3/19/2018
	Purpose: Singly- LinkedList for Program 6
*/
#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <cstddef>
#include <iostream>
using namespace std;

template<typename Type> 
class LinkedList
{
	private:
		struct ListNode
		{
			Type value;
			struct ListNode *next;
		};
		
		ListNode* head;
		ListNode* tail;
		int numNodes;

		//Index is 1 based not 0 based
		
		ListNode* getNode(int position)
			{
				ListNode* node;
				 if(position == 1)
					return head;
				
				else if(position <= numNodes)
				{
					node = head;
					
					int current = 1;
					
					while(position >= current)
					{
						if(position == current)
							return node;
						 
						current++;
						node = node->next;
					}
				}
			}
	public:
			LinkedList()
			{
				head = NULL;
				tail = NULL;
				numNodes = 0;
			}
			
			~LinkedList() //THis needs work
			{
				cout << "Starting List Deletion...";
				ListNode* delNode, *next;
				
				delNode = head;
				while(numNodes != 0)
				{					
					next = delNode->next; 
					delete delNode;
					--numNodes;
					delNode = next;
				}
				delete head, tail;
				cout << "Done" << endl;
			}
			
			int getLength()
			{
				return numNodes; 				
			}
				
			Type getNodeValue(int position)
			{
				ListNode* node;
				 if(position == 1)
					return head->value;
				
				else if(position <= numNodes)
				{
					node = head;
					
					int current = 1;
					
					while(position >= current)
					{
						if(position == current)
							return node->value;
						 
						current++;
						node = node->next;
					}
				}
			}
						
			void appendNode(Type object)
			{
				ListNode* node;
				
				node = new ListNode;
				node->value = object;
				node->next = NULL;
				
				if(!head)
				{
					head = node;
					tail = node;
					numNodes++;
				}
				else
				{
						tail->next = node;
						tail = node;
						numNodes++;
				}
			}
			
			void deleteNode(int position)
			{
				
				ListNode* now;
				ListNode* prev;
				
				if(!head)
					return;
				
				if(position == 1)
				{
					now = head->next;
					delete head;
					head = now;
					numNodes--;
				}
				else
				{
					now = head;
					prev = now;
					int cur = 1;
					
					while(position >= cur)
					{
						if(position == numNodes)
						{
							tail = prev;
						}
						if(position==cur)
						{
							prev->next = now->next;
							delete now;
							numNodes--;
						}
						cur++;
						prev = now;
						now = now->next;
					}
				}
				
			}

			void swap(int num1, int num2)
			{
				ListNode* node1 = getNode(num1);
				ListNode* node2 = getNode(num2);
				
				Type temp;
				temp = node1->value;
				node1->value = node2->value;
				node2->value = temp;
			}
			
};

#endif

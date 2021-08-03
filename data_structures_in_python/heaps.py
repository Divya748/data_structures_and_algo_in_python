"""
Heap : It is a specialized tree based data structure

Types of heaps:
    -> Binary heap
    -> Binomial heap
    -> Fibonacci heap

Binary Heap:
        It is a complete binary tree which satisfies the heap property
        a)complete binary tree:
            The tree in which all the level except last level is completely filled with nodes 
            and last level can be completely filled from left to right.
                        example:
                                67
                               / \
                              56   87
                             / \
                            43
        b)Heap property:
        Property of a node in which key of every parent node need to be <= or >= the child node's key.
    
    Min heap/Min binary heap:
            complete binary tree where the key of every parent node need to be <= the child node's key.
    
    Max heap/Max binary heap:
            complete binary tree where the key of every parent node need to be >= the child node's key.

            max heap example:                               Min heap example:
                  100                                                1
                  / \                                              /  \
                50  70                                            4    10
               / \                                               / \  /  \
              30 20                                             7  9  45 90
    
    Applications of Binary heap:
            -> To implement priority queue.
            -> In heap sort algo.
            -> To find kth largest or smallest elements in a list of numbers.
    
    Heap operations:
            1.Heapify->2 types:(heapify_up,heapify_down):
                it is a process to rearrange the elements of the heap in order to maintain the heap property.
                    a)Insertion operation
                    b)Deletion    "
                    c)while creating a binary heap from given array
    
    Array representation:
                  100                                               
                  / \                          array=[100,50,70,30,20]                    
                50  70                              ith element= array[i]              
               / \                                  parent node of ith element = (i-1)//2         
              30 20                                 lchild node of ith element = (2*i)+1
                                                    rchild node of ith element = (2*i)+2
"""

import heapq
arr=[]
heapq.heappush(arr,9)
heapq.heappush(arr,0)
heapq.heappop(arr)
print(arr)
list=[67,98,0,5,3]
heapq.heapify(list)
print(list)
heapq.heappushpop(list,76)
print(list)
heapq.heapreplace(list,54)
print(list)
min_values=heapq.nsmallest(3,list)
print(min_values)
max_values=heapq.nlargest(3,list)
print(max_values)
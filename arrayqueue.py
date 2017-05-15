"""
File: arrayqueue.py
Project 8.3

Include a remove(index) method for queues.
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._front
        while cursor != self._rear:
            yield self._items[cursor]
            if cursor == len(self._items) - 1:
                cursor = 0
            else:
                cursor += 1
        if cursor == self._rear and cursor != -1:
            yield self._items[cursor]

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        print("!!!",len(self),len(self) - 1)
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._front = self._rear = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)

    def add(self, item):
        """Inserts item at rear of the queue."""
        # Resize array if full
        if len(self) == len(self._items):
            print("!!!!!!!", len(self))
            temp = Array(len(self._items) * 2)
            # Copy so that front is at 0 and rear is at len(self) - 1
            i = 0
            # Copy data from position front through the end of the array

            for j in range(self._front, len(self)):
                print('&&&&&', self._items[j])
                temp[i] = self._items[j]
                i += 1
            if self._rear < len(self) - 1:
                print('&&&&&', self._rear, len(self))
                # Copy data from position 0 through the rear
                for j in range(0, self._rear + 1):
                    temp[i] = self._items[j]
                    i += 1
            self._items = temp
            # Normalize front and rear
            self._front = 0
            self._rear = len(self) - 1            
        if self.isEmpty():
            self._front = self._rear = 0
        elif self._rear == len(self._items) - 1:
            self._rear = 0
        else:
            self._rear += 1
        self._items[self._rear] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        data = self._items[self._front]
        self._size -= 1
        if self.isEmpty(): self._front = self._rear = -1                  
        elif self._front == len(self._items) - 1:
            self._front = 0
        else:
            self._front += 1
        if len(self) <= .25 * len(self._items) and \
           ArrayQueue.DEFAULT_CAPACITY <= len(self._items) // 2:
            tempArray = Array(len(self._items) // 2)
            i = 0
            for item in self:
                tempArray[i] = item
                i += 1
            self._items = tempArray
            if not self.isEmpty():
                self._front = 0
                self._rear = len(self) - 1
        return data

    def remove(self, index):
        """Removes and returns the item at index,
        where index ranges from 0 (the front) to size - 1 (the rear).
        Precondition: 0 <= index < size of queue"""
        if index < 0 or index >= len(self):
            raise AttributeError("i must be >= 0 and < size of queue")
        # Compute the position in the queue and save the item
        oldPos = (self._front + index) % len(self._items)
        oldItem = self._items[oldPos]
        self._size -= 1
        if self.isEmpty():
            # Empty queue, so reset pointers to initial state
            self._rear = self._front = -1
        elif oldPos <= self._rear:
            # oldPos is before rear in the array, so close hole
            # from oldPos down to rear
            for probe in range(oldPos, self._rear):
                self._items[probe] = self._items[probe + 1]
            self._rear -= 1
        else:
            # rear has wrapped around the array and oldPos is
            # between front and the end of the array, so close
            # hole from front to oldPos
            for probe in range(oldPos, self._front, -1):
                self._items[probe] = self._items[probe - 1]
            self._front += 1
        return oldItem

        
         

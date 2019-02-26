'''
In this script I define a Queue_class, in line with the queue-datastructure. This means first in first out.
The queue should be a predefined list.
'''


class Queue:

    def __init__(self, queue=[], size=0):

        if size == 0:
            self.size = queue.__len__()
            self.free_places = 0
        elif size > queue.__len__():
            self.size = size
            self.free_places = size - queue.__len__()
        else:
            print("Size of given list is larger than the given size.")

        self.queue = queue

    def goes_in(self, value):

        if self.free_places == 0:
            print(f"Sorry, the queue is full!")
        else:
            self.queue.append(value)
            self.free_places -= 1

    def goes_out(self):

        if self.free_places == self.size:
            print("The queue is empty!")
        else:
            out = self.queue[0]
            self.queue = self.queue[1:]
            self.free_places += 1
            return out

    def resize(self, value = 0):
        if value < 0 and self.free_places + value < 0:
            print(f"You can not make it so much smaller. You would delete data, or make a negative queue. "
                  f"You can only remove {self.free_places} places.")
        else:
            self.free_places += value
            self.size += value




if __name__ == '__main__':


    a = Queue([1, 2, 3, 4], 10)
    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(5)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(6)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(7)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(8)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(9)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(10)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(11)

    print(a.queue)
    print(a.size)
    print(a.free_places)


    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)
    a = Queue([1, 2, 3, 4], 10)
    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(5)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(6)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(7)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(8)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(9)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(10)

    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.goes_in(11)

    print(a.queue)
    print(a.size)
    print(a.free_places)


    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)

    out = a.goes_out()
    print(a.queue)
    print(out)
    print(a.free_places)


    a.resize(10)
    print(a.queue)
    print(a.size)
    print(a.free_places)

    a.resize(-50)
    print(a.queue)
    print(a.size)
    print(a.free_places)

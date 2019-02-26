class Stack:

    def __init__(self, stack=[], size=0):

        if size == 0:
            self.size = stack.__len__()
            self.free_places = 0
        elif size > stack.__len__():
            self.size = size
            self.free_places = size - stack.__len__()
        else:
            print("Error: Size of given list is larger than the given size.")

        self.stack = stack

    def goes_in(self, value):

        if self.free_places == 0:
            print(f"Sorry, the stack is full!")
        else:
            self.stack.append(value)
            self.free_places -= 1

    def goes_out(self):

        if self.free_places == self.size:
            print("The stack is empty!")
        else:
            self.free_places += 1
            self.stack.pop(self.stack.__len__() -1)

    def resize(self, value = 0):
        if value < 0 and self.free_places + value < 0:
            print(f"You can not make it so much smaller. You would delete data, or make a negative stack. "
                  f"You can only remove {self.free_places} places.")
        else:
            self.free_places += value
            self.size += value




if __name__ == '__main__':

    stack_list = [1,2,3,4,5]

    stack1 = Stack(stack_list, 10)

    print(stack1.stack)
    stack1.goes_out()
    print(stack1.stack)
    stack1.goes_in(1)
    print(stack1.stack)
    stack1.goes_out()
    print(stack1.stack)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)
    stack1.goes_in(1)




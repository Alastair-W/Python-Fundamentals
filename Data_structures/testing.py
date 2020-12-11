# Singly Linked List
import re
#class to create a new node
class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#class to create a new list
class SLList:
    def __init__(self):
        self.head = None
    def addToFront(self, val):
        #create a node with the given value
        new_node = SLNode(val)
        # Since the only node we have a reference to in our list is the head, 
        # if we replace it right away, we'll lose our reference to the current head
        current_head = self.head
        #set the new node's next to the list's current head
        new_node.next = current_head
        #set the list's head to the new node
        self.head = new_node
    def print_values(self):
        #as self.head is going to repeated throughout the code block set it as a variable called 'runner'
        #self.head is also the first node which is where we want to start
        runner = self.head
        #create while loop stops when the runner variable is no longer pointing to a node
        while (runner != None):
            #print the value attribute of the node
            print(runner.value)
            #move to the next node by setting the current node (self.head) to the node it is 'pointing' to - it's neighbor
            runner = runner.next
        return self
    def addToBack(self, val):
        #if the list is empty just add the new node to the front of the list using the addToFront method
        if self.head == None:
            self.addToFront(val)
            return self
        #create a new class instance to add to the list
        new_node = SLNode(val)
        #start at the head and create a variable
        runner = self.head
        #run a while loop that stops when it finds the last item, determined by the runner.next having no value and therefor no neighbor
        while (runner.next != None):
            runner = runner.next
        #When the loop has finished running, runner will be pointing to the last node. Now we make the next value of this last node the new node
        runner.next = new_node
        return self
    def remove_from_front(self):
        current_head = self.head
        self.head = self.head.next
        removedValue = current_head.value
        # print("You have just removed {} from the list".format(removedValue))
        print(f"You have just removed {removedValue} from the list")
        # current_head = None






my_list = SLList()
my_list.addToFront('Jim')
my_list.addToFront('Dwight')
my_list.addToFront('Andy')
#print out all of the 'value' attributes for each instance of the class added to the list (my_list)
my_list.print_values()
# print(my_list.head.next)
my_list.remove_from_front()
my_list.print_values()

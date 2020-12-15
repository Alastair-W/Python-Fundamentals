# Singly Linked List
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
        return self
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
        self.print_values()
        return self
    def remove_from_back(self):
        runner = self.head
        while runner.next != None:
            previous = runner
            runner = runner.next
        previous.next = None
        removedValue = runner.value
        print(f"You have just removed {removedValue} from the list")
        self.print_values()
        return self
    def remove_val(self, val):
        if self.head.value == val:
            self.remove_from_front()
        else:
            runner = self.head
            while runner.value != val:
                previous = runner
                runner = runner.next
            if runner.next == None:
                    self.remove_from_back()
            elif runner.next != None:
                previous.next = runner.next
                runner.next = None
                removedValue = runner.value
                print(f"You have just removed {removedValue} from the list")
            self.print_values()
        return self
    def insert_at(self, val, n):
        if n == 0:
            self.addToFront(val)
        elif n < 0:
            print('Only positive integers are accepted')
        else:
            count = 1
            runner = self.head
            while runner.next != None:
                if n == count:
                    # print(runner.value)
                    # print(runner.next.value)
                    new_node = SLNode(val)
                    current_next = runner.next
                    runner.next = new_node
                    new_node.next = current_next
                    print(f'{new_node.value} has been added to index {count}')
                    self.print_values()
                    break
                else:
                    count += 1
                    runner = runner.next
            if count < n:
                print(f'The list only has {count} items so this index is out of range')
                self.print_values()
        return self






my_list = SLList()
my_list.addToFront('Jim').addToFront('Dwight').addToFront('Andy').addToFront('Pam').addToFront('Michael').addToBack('Kelly')
# my_list.addToFront('Dwight')
# my_list.addToFront('Andy')
# my_list.addToFront('Pam')
# my_list.addToFront('Michael')
# my_list.addToBack('Kelly')
# # Print full list
my_list.print_values()
# Remove first in list (Michael), left with Pam, Andy, Dwight, Jim, Kelly
my_list.remove_from_front()
# Remove last in list (Kelly), left with Pam, Andy, Dwight, Jim
my_list.remove_from_back()
# Remove node with value of 'Andy', left with Pam, Andy, Jim
my_list.remove_val('Dwight')
# Add a new node with value of 'Stanley' to index 1, left with Pam, Stanley, Andy, Jim
my_list.insert_at('Stanley', 1)
# Add a new node with value of 'Erin' to the last index (3), left with Pam, Stanley, Andy, Jim, Erin
my_list.insert_at('Erin', 3)

# my_list.print_values()

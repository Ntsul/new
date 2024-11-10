###
#task1
##################

# Node კლასი წარმოადგენს სიაში დაკავშირებულ ცალკეულ ელემენტს
class Node:
    def __init__(self, data=None):
        # ინიციალიზაცია: ქმნის ახალ ნოდს მითითებული მონაცემებით და შემდეგი ნოდის საწყისი მდგომარეობა None
        self.data = data
        self.next = None  # მიუთითებს შემდეგ ნოდზე, საწყისი მნიშვნელობა არ აქვს მიცემული

# LinkedList კლასი მართავს ნოდების ჯგუფს და შეიცავს მეთოდებს მათი დამატებისა, წაშლისა და ჩვენებისთვის
class LinkedList:
    def __init__(self):
        # სიის შექმნა, რომელსაც საწყისად არ აქვს სათავე
        self.head = None

    def append(self, data):
        # ვქმნით ახალ ნოდს  გადმოცემული მონაცემებით
        new_node = Node(data)
        #  თუ სია ცარიელია (head = None), და ამ დროს ახალი ნოდი ხდება სათავე
        if self.head is None:
            #  სათავეს იქმნება ახალ ნოდზე, რადგან ეს არის სიის პირველი ელემენტი
            self.head = new_node
            return

        #  სიაში გადადის ბოლო ნოდის საპოვნელად
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # გადადის შემდეგ ნოდზე, სანამ ბოლო ნოდი არ მოიძებნება

        #  ბოლო ნოდის შემდეგი მითითებას აძლევს ახალ ნოდზე,რომ დაემქატოს სიის ბოლოში
        last_node.next = new_node

    def remove_at(self, index):
        # თუ სია ცარიელია ან ინდექსი არაა მოქმედი ამას ამოწმებს
        if index < 0 or self.head is None:
            return  # არაფერს აკეთებს იმ შემთღვევაში თუ ინდექსი ვალიდურიი არარის(ანუ არასწორი თუა) ან სია ცარიელია

        #  თუ ინექსი უდრის 0ს, ვშლით სიის საწყის ნოდს
        if index == 0:
            # საწყისი გადადის შემდეგ ნოდზე,  პირველი ნოდი წაშლილია
            self.head = self.head.next
            return

        # სიაში გადადის, რო გადავიდეს შემდეფგ ნოდზე, რომელიც არის წასაშლელის წინ
        current_node = self.head
        current_position = 0

        # გადადის მანამ, სანამ მივა იმ პოზიციამდე, რომელიც საჭიროა წასაშლელი ინდექსის წინ
        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        #  თუ შემდეგი ნოდი არსებობს, გამოტოვებს და წაშლის სიიდან
        if current_node.next:
            current_node.next = current_node.next.next  # გამოტოვებს შემდეგ ნოდს

    def display(self):
        #  სიის სათავიდან იწყებს და აჩვენებს თითოეულო ნოდის მონაცემს
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')  # მონაცემის აჩვენებს და მითითებაა შემდეგ ნოდზე
            current_node = current_node.next  # გადადის შემდეგ ნოდზე

        print()  # აჩვენებს მონაცემებს და ამატებს ცატრიელ ხაზს


linked_list = LinkedList()

# სიისთვის ნოდების დამატება
linked_list.append(50)  # ნოდი ინდექსზე 0
linked_list.append(15)  # ნოდი ინდექსზე 1
linked_list.append(20)  # ნოდი ინდექსზე 2
linked_list.append(11)  # ნოდი ინდექსზე 3
linked_list.append(5)   # ნოდი ინდექსზე 4
linked_list.append(25)  # ნოდი ინდექსზე 5

# საწყისი სიის ჩვენება
linked_list.display()  #  შედეგი იქნეა: 50 -> 15 -> 20 -> 11 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 2 (მონაცემები 20) და განახლებული სიის ჩვენება
linked_list.remove_at(2)
linked_list.display()  # შედეგი იქნება: 50 -> 15 -> 11 -> 5 -> 25 ->

# ისევ ნოდის წაშლა ინდექსზე 2 (მონაცემები 11) და განახლებული სიის ჩვენება
linked_list.remove_at(2)
linked_list.display()  # შედეგი იქნება: 50 -> 15 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 0 (მონაცემები 50) და განახლებული სიის ჩვენება
linked_list.remove_at(0)
linked_list.display()  # შედეგი იქნება: 15 -> 5 -> 25 ->

# ნოდის წაშლა ინდექსზე 2 (მონაცემები 25) და განახლებული სიის ჩვენება
linked_list.remove_at(2)
linked_list.display()  # შედეგი იქნება: 15 -> 5 ->


############task2'
####

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def remove_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def add_at_index(self, index, data):
        if index < 0:
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print()

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()
linked_list.remove_value(20)
linked_list.display()
linked_list.add_at_index(1, 25)
linked_list.display()


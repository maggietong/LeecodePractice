"""
HashTable implementation
For example, a simple employee information management system

class HashTable is a represent of linkedlistArr
class linkedList is a list of employees
class Employee: list basic information of an employee
"""
class Employee():
    def __init__(self, id=None, name='', age=None):
        self.id = id
        self.name = name
        self.age = age

class LinkedList():
    def __init__(self, emp=None):
        self.next = None
        self.item = emp

    def add(self, lk):
        cur = self
        while cur.next!= None:
            cur = cur.next
        cur.next = lk

    def list(self):
        cur = self
        while cur.next != None:
            cur = cur.next
            print('{0} {1} {2}'.format(cur.item.id, cur.item.name, cur.item.age))

class HashTable():
    def __init__(self, size=7):
        self.size = size
        self.arr = list()
        for i in range(self.size):
            ll = LinkedList()
            self.arr.append(ll)

    def add(self, emp):
        cur_head = self.hash_func(emp.id)
        lk = LinkedList(emp)
        cur_head.add(lk)

    def list(self):
        for i in range(self.size):
            cur_head = self.arr[i]
            cur_head.list()

    def hash_func(self, emp_id):
        id = emp_id % self.size
        return self.arr[id]


if __name__ == "__main__":
    emp1 = Employee(id=0, name='TOM', age=18)
    emp2 = Employee(id=1, name='Mary', age=20)
    emp3 = Employee(id=2, name='Jack', age=30)
    emp4 = Employee(id=3, name='Lisa', age=40)
    emp5 = Employee(id=4, name='Mandy', age=50)
    emp6 = Employee(id=5, name='Peter', age=42)
    import pdb; pdb.set_trace()
    ht = HashTable(size=3)
    ht.add(emp1)
    ht.add(emp2)
    ht.add(emp3)
    ht.add(emp4)
    ht.add(emp5)
    ht.add(emp6)
    ht.list()

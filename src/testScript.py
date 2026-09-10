

class A:
    def __init__(self):
        self.a = []
        self.b = []
        self.c = self.a + self.b

    def update(self):
        self.c = self.a + self.b

    def add_to_a(self, item):
        self.a.append(item)
        self.update()

    def add_to_b(self, item):
        self.b.append(item)
        self.update()

    def remove_from_a(self, item):
        if item in self.a:
            self.a.remove(item)
            self.update()

    def remove_from_b(self, item):
        if item in self.b:
            self.b.remove(item)
            self.update()

    def print_lists(self):
        print("List A:", self.a)
        print("List B:", self.b)
        print("List C (contains A and B):", self.c)

thing = A()
thing.add_to_a(1)
thing.add_to_b(2)
thing.add_to_a(3)
thing.add_to_b(4)
thing.print_lists()
thing.remove_from_b(2)
thing.print_lists()
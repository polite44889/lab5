def get_input(text):
    return input(text)
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def edit(self):
        print(self.items)
        print("Виберіть елемент для редагування від 0 до", self.size() - 1)
        element = int(get_input())
        print("Запис: ", self.items[int(element)])
        print("Відредагуйте запис")
        self.items[int(element)] = get_input()
        print(self.items)










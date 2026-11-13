class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        if not title.strip():
            raise ValueError("제목이 비어 있습니다")
        self.items.append({"title": title.strip(), "done": False})

    def complete(self, index):
        self.items[index]["done"] = True

    def remaining(self):
        return sum(1 for item in self.items if not item["done"])

    def clear_done(self):
        self.items = [item for item in self.items if not item["done"]]

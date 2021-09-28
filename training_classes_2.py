class Title():
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(f"{self.title} - не отоброжаеться")
    def show(self):
        self.appearance = True
        print(f"{self.title} - отоброжаеться")
    def print_info(self):
        print(self.x)
        print(self.y)
        print(self.title)
        print(self.appearance)

t = Title('Test', 90, 32)
t.print_info()
t.hide()
t.print_info()

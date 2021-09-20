class Test:
    def __init__(self):
        self.x: int = 3

    def multiply(self):
        self.x = self.x ** 2

    def get_result(self):
        self.multiply()
        # return self.x

    def print_res(self):
        print(self.x)


x = Test().print_res()

print(x)

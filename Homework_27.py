import time
class GeomProgress:
    n = -1
    start_1 = -2
    step_1 = -5
    # start_2 = 10
    # step_2 = 3

    def __next__(self):
        self.n += 1
        return self.start_1 * ((self.step_1) ** self.n)
        # return self.start_2 * ((self.step_2) ** self.n)

    def __iter__(self):
        return self

my_list = GeomProgress()

for item in my_list:
    print(item)
    time.sleep(1)


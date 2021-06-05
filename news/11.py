class Rate:
    def __init__(self):
        self.rating_sum = 0
        self.users_count = 0

    def set_rate(self, user, score):
        self.rating_sum += score
        self.users_count += 1

    def get_rate(self):
        print(self.rating_sum / self.users_count)


if __name__ == '__main__':
    r = Rate()
    r.set_rate(1, 5)
    r.get_rate()
    r.set_rate(1, 7)
    r.get_rate()
    r.set_rate(1, 2)
    r.get_rate()
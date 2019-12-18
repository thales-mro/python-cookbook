from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def main():
    users = [User(23), User(3), User(99)]
    print(sorted(users, key=lambda u: u.user_id))
    # or (faster):
    print(sorted(users, key=attrgetter('user_id')))

if __name__ == "__main__":
    main()
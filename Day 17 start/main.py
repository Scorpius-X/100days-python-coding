class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follows(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Angela")
user2 = User("002", "Jack")

user1.follows(user2)


print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
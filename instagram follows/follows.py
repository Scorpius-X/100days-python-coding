class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

new_user1 = User("001", "omowole")
new_user2 = User("002", "otiteh")

new_user1.follow(new_user2)
print(new_user2.followers)
print(new_user2.following)
print(new_user1.followers)
print(new_user1.following)
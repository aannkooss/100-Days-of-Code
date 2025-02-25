class User:
    def __init__(self, id, username): #constructor with parameters (parameterized constructor in C)
        self.id = id
        self.username = username
        self.followers = 0 #kind of like a default constructor in C - also dont need a parameter when creating object
        self.following = 0
    def follow(self, user): #user parameter is the *account* we are following
        user.followers += 1 #increments that user's account by 1 to increase their followers
        self.following += 1 #increments our following by 1 as well

user1 = User("001", "ankush") #intializing an object of class User with parameters filled in to create user
user2 = User("002", "Jae")

user1.follow(user2)
print(f"{user1.username} is following: {user1.following} people")
print(f"{user2.username} now has {user2.followers} follower(s)")

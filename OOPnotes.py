class AWS_Student:

    def __init__(self, n, tc, a, sl):
        self.name = n
        self.tie_color = tc
        self.age = a
        self.stress_level = sl

    def getName(self):
        return self.name

    def getTC(self):
        return self.tie_color

    def getAge(self):
        return self.age

    def getSL(self):
        return self.stress_level

    # introduce method should have the student say everything about them
    def introduce(self):
        intro = "Hello, my name is " + self.name
        intro = intro + ". I am " + str(self.age) + " years old."
        intro = intro + " I am a " + self.tie_color + "-tie at AWS."
        return intro

    def birthday(self):
        self.age = self.age + 1

    def hasTest(self):
        if self.stress_level < 8:
            self.stress_level = self.stress_level + 2
        print("I have a test! I am so stressed")
        print("My level of stress is at a " + str(self.stress_level) + " out of ten")

def main():


    t = AWS_Student("Trinity", "red", 18, 5.5)
    print(t.introduce())
    t.birthday()
    t.birthday()
    t.birthday()
    print(t.introduce())

    t.hasTest()
    t.hasTest()
    t.hasTest()
    t.hasTest()

if __name__ == "__main__":
    main()

        

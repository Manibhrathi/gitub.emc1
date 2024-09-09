import random
import turtle

Screen = turtle.Screen()


Screen.bgcolor("white")

greeting_turtle = turtle.Turtle()
greeting_turtle.speed(1)
greeting_turtle.hideturtle()
greeting_turtle.penup()

def write_greeting(message, x, y, font_size, color):
    greeting_turtle.goto(x, y)
    greeting_turtle.pendown()
    greeting_turtle.color(color)
    greeting_turtle.write(message, align="center", font=("arial", font_size, "bold"))


write_greeting("welcome to the banking system!...", 0, 100, 24, "blue")


Screen.delay(3000)


Screen.bye()


class ATM:
    def __init__(self, account_number, pin, balance, old_pins):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.old_pins = old_pins

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful, your new balance is", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful, your new balance is", self.balance)

    def generate_otp(self):
        otp = random.randrange(0, 1000)
        print("Your OTP is"+ str(otp))
        return (otp)

    def verify_otp(self, otp, generated_otp):
        if otp == generated_otp:
            return True
        else:
            return False

    def change_pin(self):
        generated_otp = self.generate_otp()
        verify = input("Enter the OTP sent to your registered mobile number: ")
        if self.verify_otp(int(verify), generated_otp):
            new_pin = input("Enter your new PIN: ")
            if new_pin in self.old_pins:
                print("You have used this PIN already, please choose another one.")
            else:
                confirm_pin = input("Enter your new PIN again: ")
                if new_pin == confirm_pin:
                    self.pin = new_pin
                    self.old_pins.append(self.pin)
                    print("PIN changed successfully")
                else:
                    print("PIN mismatch")
        else:
            print("Invalid OTP")


class User(ATM):
    def __init__(self, name, account_number, pin, balance,old_pins):
        super().__init__(account_number, pin, balance,old_pins)
        self.name = name

    def login(self):
        pin = input("Enter your PIN: ")
        if self.check_pin(pin):
            print("Login successful")
            return True
        else:
            print("Invalid PIN")
            return False

    def perform_transaction(self):
        if self.login():
            while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Change PIN")
                print("5. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter the amount to be deposited: "))
                    self.deposit(amount)
                elif choice == 2:
                    amount = int(input("Enter the amount to be withdrawn: "))
                    self.withdraw(amount)
                elif choice == 3:
                    print("Your balance is", self.balance)
                elif choice == 4:
                    self.change_pin()
                elif choice == 5:
                    print("thankyou")
                    break
                else:
                    print("Invalid choice")


user = User("Mani Bharathi", "1814170000002644", "2101", 0,"2003")
user.perform_transaction()


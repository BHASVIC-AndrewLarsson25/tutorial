# rock, paper adn scissors

# rps variables and functions

player_name = "sam"
game_active = True


def greet_player():
    print("welcome to rps")


# rps calling functions

greet_player()


# rps dictionaries

moves = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

# rps user input

player_choice = input("choose r, p, or s: ")

# rps libraries, lists and methods

import random

computer_options = ["r", "p", "s"]
computer_choice = random.choice(computer_options)

print(computer_options.count("r"))

# rps function arguments

def show_choice(player, choice):
    print(player + " picked " + moves[choice])


show_choice(player_name, player_choice)
show_choice("computer", computer_choice)

# rps if statements

if player_choice == computer_choice:
    print("tie game")

# rps concatenating strings

print("you chose " + moves[player_choice])

# rps f strings

print(f"computer chose {moves[computer_choice]}")

# rps else and elif statements

if player_choice == computer_choice:
    print("draw")
elif player_choice == "r" and computer_choice == "s":
    print("you win")
elif player_choice == "p" and computer_choice == "r":
    print("you win")
elif player_choice == "s" and computer_choice == "p":
    print("you win")
else:
    print("computer wins")

# rps refactoring and nested if

winning_combos = {
    "r": "s",
    "p": "r",
    "s": "p"
}

if player_choice in winning_combos:
    if winning_combos[player_choice] == computer_choice:
        print("player wins after refactor")
    else:
        print("player loses after refactor")

# rps accessing dictionary values

print(winning_combos["r"])
print(moves.get("p"))

# rps testing game

for test_choice in computer_options:
    print(f"testing against {test_choice}")


# fundamentals of python

# setup python locally

print("install python from python.org")

# creating new repl

print("open a new repl and start coding")

# variables

age = 17
height = 5.9

# expressions and statements

total = age + 3
print(total)

# data types

username = "mike"
score = 99
is_online = True

# operators

result = 10 + 5

# arithmetic operators

print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 % 3)

# comparison operators

print(10 > 5)
print(10 == 5)

# boolean operators

print(True and False)
print(True or False)
print(not True)

# bitwise operators

print(5 & 3)
print(5 | 3)

# is and in operators

numbers = [1, 2, 3]

print(2 in numbers)
print(numbers is numbers)

# ternary operator

message = "adult" if age >= 18 else "teen"
print(message)

# strings

course = "python basics"

# string methods

print(course.upper())
print(course.replace("python", "java"))

# escaping characters

quote = "he said \"hello\""

# string characters and slicing

print(course[0])
print(course[0:6])

# booleans

logged_in = False

# number data types

whole_number = 10
decimal_number = 10.5
complex_number = 2 + 3j

# built in functions

print(len(course))
print(abs(-20))
print(round(4.7))

# enums

from enum import Enum


class State(Enum):
    ACTIVE = 1
    INACTIVE = 0


print(State.ACTIVE)

# user input

favorite_color = input("enter your favorite color: ")

# control statements

if favorite_color == "blue":
    print("cool color")
else:
    print("nice choice")

# lists

fruits = ["apple", "banana", "orange"]

fruits.append("grape")
fruits.remove("banana")

print(fruits)

# sorting lists

numbers = [5, 2, 9, 1]
numbers.sort()

print(numbers)

# tuples

coordinates = (10, 20)

# dictionaries

student = {
    "name": "lisa",
    "grade": "a"
}

print(student["name"])

# sets

unique_numbers = {1, 2, 2, 3}

print(unique_numbers)

# functions

def add(a, b):
    return a + b


print(add(5, 3))

# variable scope

global_var = "outside"


def check_scope():
    local_var = "inside"
    print(global_var)
    print(local_var)


check_scope()

# nested functions

def outer():
    def inner():
        print("inside inner function")

    inner()


outer()

# closures

def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)
print(double(5))

# objects

car = {
    "brand": "toyota",
    "year": 2020
}

# loops

for fruit in fruits:
    print(fruit)

count = 0

while count < 3:
    print(count)
    count += 1

# break and continue

for number in range(5):
    if number == 2:
        continue

    if number == 4:
        break

    print(number)

# classes

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")


dog1 = Dog("max")
dog1.bark()

# modules

import math

print(math.sqrt(25))

# arguments from command line

import sys

print(sys.argv)

# lambda functions

square = lambda x: x * x

print(square(4))

# map, filter and reduce

from functools import reduce

nums = [1, 2, 3, 4]

mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
reduced = reduce(lambda a, b: a + b, nums)

print(mapped)
print(filtered)
print(reduced)

# recursion

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# decorators

def decorator_function(func):
    def wrapper():
        print("before function")
        func()
        print("after function")

    return wrapper


@decorator_function
def say_hello():
    print("hello")


say_hello()

# docstrings

def greet():
    """prints a greeting"""
    print("hi")


# annotations

def multiply(a: int, b: int) -> int:
    return a * b


# exceptions

try:
    value = int(input("enter a number: "))
    print(value)
except ValueError:
    print("invalid number")

# with

with open("sample.txt", "w") as file:
    file.write("python is fun")

# installing packages with pip

print("pip install requests")

# list comprehension

squares = [x * x for x in range(5)]

print(squares)

# polymorphism

class Cat:
    def speak(self):
        print("meow")


class Bird:
    def speak(self):
        print("tweet")


animals = [Cat(), Bird()]

for animal in animals:
    animal.speak()

# operator overloading

class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __str__(self):
        return str(self.x)


v1 = Vector(5)
v2 = Vector(10)

print(v1 + v2)


# blackjack card game

# blackjack start

print("starting blackjack game")

# blackjack deck class

import random

class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"] * 4
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# blackjack card class

class Card:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"card: {self.value}")


# blackjack hand class

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_hand(self):
        for card in self.cards:
            card.show()


# blackjack game class

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()

    def start(self):
        for _ in range(2):
            dealt_card = Card(self.deck.deal())
            self.player_hand.add_card(dealt_card)

        self.player_hand.show_hand()


# blackjack testing

game = Game()
game.start()
# Python program that performs a “random walk” stock market simulation.
# Farzan Khoobchehr    Spring 2020 -- HW1

import csv
import random
repeat = "yes"
with open("randomwalk.csv","w") as file:   #export the simulation in a csv file called randomwalk
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["Initial price", "Number of days simulated", "Final price"])
    # the while loop below asks whether the user wants to simulate the stock price again
    while repeat.lower() == "yes":
        initial_price = float(input("What is the initial price of the stock? "))
        num_days = input("How many days would you like to simulate? ")
        original_price = initial_price  #we create this variable only to have the correct initial price on the csv file
        increase_counter = 0  # number of days the stock price has increase
        decrease_counter = 0  # number of days the stock price has decrease
        stay_same_counter = 0  # number of days the stock price didn't change
        for i in range(0,int(num_days),1):
            tracker = initial_price  #tracker is a new variable which help us to compare the price of tow consecutive days
            random_value = round(random.uniform(0.98,1.02),3)  # we could also use random_value = random.randint(-2,2)/100
            initial_price = initial_price * random_value  #multiplying a random number within the range (-2% to 2%) with the initial price
            if tracker < initial_price:
                increase_counter = increase_counter + 1
            elif tracker == initial_price:
                stay_same_counter = stay_same_counter + 1
            else:
                decrease_counter = decrease_counter + 1
       
        print ( "after",num_days,"days,", initial_price, "is the new stock price.")
        print ("The stock price increased", increase_counter, "times.", "decreased",decrease_counter, "times and stayed the same", stay_same_counter,"times")
        repeat = input("Would you like to simulate another time? (yes/no)? ")
        row2 = [original_price,num_days,initial_price]
        writer.writerow(row2)




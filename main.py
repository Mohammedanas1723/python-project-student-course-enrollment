

# 1. User Registration System
# A user enters their name during registration. Store the name and display a welcome message.
# Output Example
# Welcome Arunwe
# a = input("Enter a name:

# print("hello " + a)

# 2. Employee Information
# Store an employee's name and age and display them.
# Output Example
# Employee Name : Arun
# Employee Age  : 25
# employee_name = input("Enter employee name: ")
# employee_age = int(input("Enter employee age: "))
# print("Employee Name:", employee_name)
# print("Employee Age:", employee_age)

# 3. Grocery Billing System
# A customer buys 2 products.
# Store the prices and calculate the total bill.
# Example
# Rice  = 500
# Oil   = 250
# Total Bill = 750
# rice_price=int(input("Enter price of Rice: "))
# oil_price=int(input("Enter price of Oil: "))
# total_bill=rice_price+oil_price
# print("Total Bill:", total_bill)

# 4. Mobile Shop
# A customer buys a phone and a charger.
# Find the total purchase amount.
# phone_price = 15000
# charger_price = 2000
# total_purchase = phone_price + charger_price
# print("Total Purchase Amount:", total_purchase)

# 5. E-Commerce Discount
# An online store gives a flat ₹100 discount.
# Store product price and calculate final payable amount.
# Example
# Price = 1200
# Discount = 100
# Final Amount = 1100
# discount = 100
# product_price = int(input("Enter product price: "))
# final_amount = product_price - discount
# print("Final Amount:", final_amount)

# 6. Cricket Scoring App
# A player hits 4 boundaries.
# Calculate total runs.
# Boundary = 4 runs
# Number of Boundaries = 4
# Total Runs = 16
# boundary_runs = 17
# number_of_boundaries = 4
# total_runs = boundary_runs * number_of_boundaries
# print("Total Runs:", total_runs)





# 7. OTP Verification System
# OTP received from API is stored as string.
# Convert it into integer.
# otp = "456789"

# otp = "456789"
# otp_integer = int(otp)
# print("OTP:", otp_integer)


# 8. Chat Application
# Take username from user and display:
# Hello Arun, Welcome to Chat App
# user = input("Enter your username: ")
# print("Hello " + user + ", Welcome to Chat App")

# 9. Food Delivery App
# Calculate remaining amount after splitting bill among friends.
# Use modulus operator.
# Bill = 1000
# Friends = 3
# Remaining Amount = ?
# frds = 3
# bill = 1000
# remaining_amount = bill % frds
# print("Remaining Amount:", remaining_amount)

# 10. Social Media Growth
# A page doubles followers every month.
# Find followers after 5 months using power operator
# Initial Followers = 100
# initial_followers = 100
# after_5_months = initial_followers * (2 ** 5)
# print("Followers after 5 months:", after_5_months)

# 11. Bank Simple Interest Calculator
# Customer deposits money in bank.
# Calculate simple interest.
# Inputs:
# Principal
# Rate
# Time


# 12. House Painting Cost
# A painter charges per square meter.
# Find area of wall.
# Length = 20
# Width = 15
# area = 20 * 15
# print("Area of Wall:", area)

# 13. Land Measurement System
# A land surveyor wants area of circular park.
# Calculate area.
# Radius = 25 meter


# 14. Weather App
# User enters temperature in Celsius.
# Convert to Fahrenheit.
# Example:
# 32°C → 89.6°F



# 15. Logistics Company
# Truck travels 25 kilometers.
# Convert distance into meters.
# one_km_in_meters = 1000
# distance_in_meters = 25 * one_km_in_meters
# print("Distance in Meters:", distance_in_meters)

# 16. Student Performance Dashboard
# Store marks of 5 subjects.
# Calculate average marks.
# Example:
# Math
# Science
# English
# Physics
# Chemistry
# math_marks = 85
# science_marks = 90
# english_marks = 78
# physics_marks = 92
# chemistry_marks = 88
# average_marks = (math_marks + science_marks + english_marks + physics_marks + chemistry_marks) / 5
# print("Average Marks:", average_marks)

# 17. Wallet Transfer
# User A transfers money to User B.
# Swap balances using third variable.
# Wallet A = 500
# Wallet B = 1000



from itertools import product


wallet_a = 500
wallet_b = 1000
temp = wallet_a
wallet_a = wallet_b
wallet_b = temp
# print("Wallet A Balance:", wallet_a)
# print("Wallet B Balance:", wallet_b)


# 18. Game Character Position Swap
# Two players exchange positions.
# Swap values without using third variable.
# player1_position = 10
# player2_position = 20
# player1_position, player2_position = player2_position, player1_position
# print("Player 1 Position:", player1_position)
# print("Player 2 Position:", player2_position)

# 19. School Result Management System
# Store marks of 5 subjects.
# Calculate:
# Total Marks
# Percentage
# Average
# Display result card.
# Total Marks = ?
# Percentage = ?


# 20. Video Streaming Platform
# Convert total video duration from seconds into:
# Hours
# Minutes
# Seconds
# Example:
# Video Length = 7384 seconds
# Output:
# 2 Hours
# 3 Minutes
# 4 Seconds
# video_length_seconds = 12500
# hours = video_length_seconds // 3600
# minutes = (video_length_seconds % 3600) // 60
# seconds = video_length_seconds % 60
# print("Video Length:")
# print(hours, "Hours")
# print(minutes, "Minutes")
# print(seconds, "Seconds")

        #  if and else statements
# age=23
# if age >=18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
# num=5
# if num>=0:
#     print("The number is positive.")
# elif num==0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")
# age=20
# has_id=True 
# if age>=18:
#     if has_id:
#         print("entry allowed.")
#     else:
#         print("entry not allowed.")
# else:
#         print("You are to young.")

# age=12
# has_license=True
# if age>=18 and has_license:
#     print("You can drive.")
# else:
#     print("You cannot drive.")
# age = 12
# can_love = True
# if age >= 18 and  can_love:
#     print("You can love.")
# else:
#     print("You cannot love.")
# for i in range(1, 11):
#     print(i)

# 1. Login System
# Store username and password.
# If both are correct:
# Plain text
# Login Successful
# Else:
# Plain text
# Invalid Credentials
# username = "anas"
# password = "password13"
# if(username == "anas" and password == "password123"):
#     print("Login Successful")   
# else:
#     print("Invalid Credentials")


# 2. ATM Withdrawal
# Balance = 5000
# User enters withdrawal amount.
# Check:
# Amount should be less than balance
# Output:
# Plain text
# Transaction Successful
# or
# Plain text
# Insufficient Balance
# balance = 5000
# withdrawal_amount = int(input("Enter withdrawal amount: "))     
# if withdrawal_amount <= balance:
#     print("Transaction Successful")
# else:
#     print("Insufficient Balance")    
# 3. Voting Eligibility
# Input Age
# If age >= 18
# Plain text
# Eligible for Voting
# Else
# Plain text
# Not Eligible
# age = int(input("Enter your age: "))
# if age>=18:
#     print("Eligible for Voting")
# else:
#     print("Not Eligible")
# 4. Online Shopping Free Delivery
# Order Amount = 1500
# Rule:
# Above 1000 → Free Delivery
# Otherwise → Delivery Charge ₹100
# Output final payable amount.
# order_amount = 1500

# if order_amount > 1000:
#     print("Free Delivery")
# else:
#     print("Delivery Charge :"+str(order_amount + 100))    
# 5. Employee Bonus
# Salary = Input
# Rules:
# Salary > 50000
# Plain text
# Bonus = 10000
# Else
# Plain text
# Bonus = 5000
# salary = int(input("Enter your salary: "))
# if salary > 50000:
#     print("Bonus = 10000")
# else:
#     print("Bonus = 5000")
# 6. Cricket Match
# Target = 180
# Current Score = Input
# Check:
# Plain text
# Target Achieved
# or
# Plain text
# Need More Runs
# target = 200
# current_score = int(input("Enter current score: "))
# if current_score >= target:
#     print("Target Achieved")
# else:
#     print("Need More Runs")
# 7. Fuel Warning System
# Fuel Level = Input
# Rules:
# Less than 10 litres
# Plain text
# Low Fuel Warning
# Else
# Plain text
# Fuel Sufficient
# fuel_level = int(input("Enter fuel level in litres: "))
# if fuel_level < 10:
#     print("Low Fuel Warning")
# else:
#     print("Fuel Sufficient")
    
# 8. Student Pass/Fail
# Input Marks
# Rules:
# Marks >= 35
# Plain text
# Pass
# Else
# Plain text
# Fail
# marks = int(input("Enter marks: "))
# if marks>=35:
#     print("Pass")
# else:
#     print("Fail")
# 9. Bank Loan Eligibility
# Salary = Input
# Rules:
# Salary >= 30000
# Plain text
# Loan Approved
# Else
# Plain text
# Loan Rejected
# salary = int(input("Enter your salary: "))
# if salary >= 30000:
#     print("Loan Approved")
# else:
#     print("Loan Rejected")    
# 10. Mobile Unlock System
# Store PIN
# User enters PIN
# If matched
# Plain text
# Phone Unlocked
# Else
# Plain text
# Wrong PIN
# pin = "1234"
# user_pin = input("Enter your PIN: ")
# if user_pin == pin:
#     print("Phone Unlocked")
# else:
#     print("Wrong PIN")    

# 11. Largest of Two Numbers
# Input:
# Python
# a
# b
# Display largest number.
# 12. Largest of Three Numbers
# Find highest salary among 3 employees.
# 13. Even or Odd Checker
# Check whether order ID is even or odd.
# order_id = int(input("Enter order ID: "))
# if order_id % 2 == 0:
#     print("Order ID is Even")
# else:
# print("Order ID is Odd")
        
# 14. Positive, Negative, Zero
# Bank transaction amount.
# Determine:
# Plain text
# Credit
# Debit
# No Transaction
# 15. Grade Calculator
# 90+ → A
# 80+ → B
# 70+ → C
# 60+ → D
# Below → Fail
# marks = int(input("Enter marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: Fail")

# 16. Electricity Bill Category
# Units:
# 0-100 → Domestic
# 101-300 → Medium
# 301+ → High Usage
# units = int(input("Enter electricity units consumed: "))
# if units <= 100:
#     print("Category: Domestic") 
# elif units <= 300:
#     print("Category: Medium")
# else:
#     print("Category: High Usage")

# 17. Movie Ticket Eligibility
# Age:
# Below 13 → Child
# 13-59 → Adult
# 60+ → Senior Citizen
# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior Citizen")

# 18. E-commerce Coupon Check
# Order Amount:
# Above 2000 → Coupon Applied
# Otherwise → Not Eligible
# order_amount = int(input("Enter order amount: "))
# if order_amount > 2000:
#     print("Coupon Applied")
# else:
#     print("Not Eligible")    
# 19. Temperature Alert System
# Temperature:
# Above 40
# Plain text
# Heat Warning
# Below 10
# Plain text
# Cold Warning
# Else
# Plain text
# Normal Weather
# temperature = int(input("Enter temperature in Celsius: "))
# if temperature > 40:
#         print("Heat Warning")
# elif temperature < 10:
#         print("Cold Warning")
# else:
#         print("Normal Weather")

# 20. Smart Door Security
# Conditions:
# Face Detected = True
# OTP Verified = True
# Only then:
# Plain text
# Door Opened
# Else
# Plain text
# Access Denied
# face_detected = True
# otp_verified = True
# if face_detected and otp_verified:
#     print("Door Opened")
# else:
#     print("Access Denied")


# 1.Print numbers from 1 to N
# n=int(input("Enter a number N: "))
# for i in range(1,n+1):
#         print(i)
# 2.Print numbers from 1 to N
# 3.Print numbers from N to 1

#  4.Print even numbers from 1 to 20
# count = 1
# while count<=20:
#         if count%2==0:
#                 print(count)
#         count+=1         

# 5.Print odd numbers from 1 to N
# count = 0
# while count<=20:
#     if count%2!=0:
#              print(count)
#     count+=1 
# 6.Print multiples of 3 up to 30
# count = 1
# while count<=30:
#     if count%3==0:
#         print(count)
#     count+=1
# 7.Print first N multiples of 7
# n=int(input("Enter a number N: "))
# for i in range(1,n+1):
#         print(i*7)

# 8.Print squares from 1 to N
# n=int(input("Enter a number N: "))
# for i in range(1,n+1):
#         print(i*i)
        

# 9.Print cubes from 1 to N
# n=int(input("Enter a number N: "))
# for i in range(1,n+1):
#         print(i*i*i)




# 10.Print table of a number




# 11.Print numbers from 1 to N skipping multiples of 3
# 12.Print numbers from 1 to N divisible by 4
# 13.Print numbers from 1 to N where square is < 100
# 14.Print numbers from N to 1 skipping even numbers
# 15.Print first N triangular numbers









# ---------------  Accumulation  ------------

# 1.Find sum of numbers from 1 to N
# def func(n):
   
#     total = 0

#     for i in range(1, n + 1):
#         total += i

#     print("Sum:", total)

# func(5)          
    



# 2.Find sum of even numbers from 1 to N
# def func(n):
  
#   for i in range(1,n+1):
#     if i%2==0:
#      print(i)
  
# func(10)
# func(20)

# 3.Find sum of odd numbers from 1 to N


# def func(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             print(i)
# func(10)
# func(20)

# 4.Find sum of multiples of 3 up to N
# def func(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 3 == 0:
#             total += i


#     print(total)       
     
# func(10)
    

# 5.Find sum of squares from 1 to N
# def func(n):
#     total=0
#     for i in range(1,n+1):
#         total=i**2
#         print("sum of square",n,total)
# func(10)



# 6.Find sum of cubeGitHub Copilot: Enable Completions from 1 to N
# def func(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i**3
#     print("sum of cubes",total)
# func(10)

# 7.Find product of numbers from 






# write a function to find the product of numbers from 1 to n



# 8.Compute fac
# 9.Find sum of first N multiples of 5
# 10.Find sum of numbers divisible by 7 up to N
# 11.Find sum of numbers from 1 to N that are not divisible by 3
# 12.Find sum of squares of even numbers up to N
# 13.Compute:1 + 3 + 5 + 7 + ... (first N odd numbers)
# 14.Compute:1² + 2² + 3² + ... + N²
# 15.Compute:1×2 + 2×3 + 3×4 + ... + N×(N+1)

# Recursion----------------->
# Print Hello 5 times
# for i in range(5):
#     print("hello")

# Print numbers from 1 to N
# def fun(n):
#     for i in range(1,n+1):
#      print(i)
# fun(5)     

# Print numbers from N to 1
# def fun(n):
#     for i in range(n,0,-1):
#         print(i)
# fun(5)        

# Print even numbers from 1 to N
# def fun(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
# fun(10)
# fun(30)
# Print odd numbers from 1 to N
# def fun(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             print(i)
# fun(10)
# fun(100)



# 1.Count digits
# n = int(input("Enter a number: "))

# count = 0

# while n > 0:
#     n = n // 10
#     count += 1

# print("Number of digits:", count)

# # 2.Sum of digits
# def fun(n):
#     total=0
#     while n>0 :
#         digit=n%10
#         total+=digit
#         n//10
#         print(total)
     


# fun(10) 
# 1.Create a list of fruits.
# fruit=["banana","apple","orange"]
# print(fruit)


# numbers = [10,20,30,40,50,60,70,80]
# 2.Print first element.
# print(numbers[0])
# 3.Print last element.
# print(numbers[-1])
# 4.Print middle element.
# print(numbers[4])
# 5.Print first 3 elements.
# print(numbers[0:3])
# 6.Print last 2 elements.
# print(numbers[-3:])
# 7.Print alternate elements.
# print(numbers[:-4])
# 8.Print reverse list.
# print(numbers[::-1])
# 9.Print first half.
# print(numbers[:-4])
# 10.Print second half.
# print(numbers[4:])
# 11.Print elements from index 2 to 5.
# print(numbers[2:5])


# 12.Update first student name.
# students = ["Ram", "Sam", "Arun", "Ravi", "Kumar"]
# students[0]="anas"
# print(students)

# 13.Change last city
# cities = ["Chennai", "Madurai", "Salem"]
# cities[-1]="madurai"
# print(cities)
# 14.Replace middle value of N length of list.
# player_position=[1,2,4,5]
# for i in range(len(player_position)):
#     if i==len(player_position)//2:
#        player_position[i]=3
#        print(player_position)


# 15.Double all salaries.
# salaries = [20000, 30000, 40000, 50000]
# for i in range(len(salaries)):
#   salaries[i]=salaries[i]*2
#   print(salaries)
# 16.Increase marks by 5.
# marks = [70, 80, 90, 60]
# for i in range (len(marks)):
#    marks[i]=marks[i]*5
# print(marks)
# 17.Replace all negative values with 0.
# numbers = [10, -5, 30, -8, 20, -1]
# for i in range(len(numbers)):
#     numbers[i]=0
# print(numbers)    
# 18.Change all "Pending" to "Completed".
# for i in range(len(status)):
#     if status[i] == "Pending":
#         status[i] = "Completed"

# print(status)     

      

# 19.Replace zeros with 100
# numbers = [10, 0, 20, 0, 30]

# 20.Delete first item.
# numbers = [10, 20, 30, 40, 50]
# numbers.pop(0)
# print(numbers)

# 21.Delete last item.
# numbers = [10, 20, 30, 40, 50]
# numbers.pop(-1)
# print(numbers)
# 22.Remove student by name = Ram
# students = ["Ram", "Sam", "Ajay", "Ravi"]
# students.remove("Ram")
# print(students)
# 23.Remove all zeros.
# numbers = [10, 0, 20, 0, 30, 0, 40]
# print(numbers)
# 24.Remove all negatives.
# numbers = [10, -5, 20, -8, 30, -1]
# for i in range(len(numbers)):
#     numbers[i]=abs(numbers[i])
# print(numbers)

# 25.Empty list clear all.
# numbers = [10, 20, 30, 40]
# for i in range (len(numbers)):
#     numbers.clear()
# print(numbers)    

# 26.Search student Ram if found print found else not found
# students = ["Ram", "Sam", "Ajay", "Ravi"]
# if "Ram"in students:
#     print("founded",)
# else:
#     print("not found")

# 27.Count occurrences of 20.
# numbers = [10, 20, 30, 20, 40, 20]
# Count=numbers.count(20)
# print(Count)
# 28.Find index of first occurrence 20.

# numbers = [10, 20, 30, 20, 40]
# 29.Find index of last occurrence 20.
# numbers = [10, 20, 30, 20, 40, 20]
# 30.Check 20 is duplicate if print duplicate exists or not duplicate exits.
# numbers = [10, 20, 30, 20]

# 31.Add student Arun in list
# students = ["Ram", "Sam", "Ajay"]
# students.append("arun")
# print(students)

# 32.Insert city
# cities = ["Chennai", "Madurai", "Salem"]
# # ex:['Chennai', 'Trichy', 'Madurai', 'Salem']
# cities.insert(1,"triChy")
# print(cities)


# 33.Merge two classes
# class1 = ["Ram", "Sam", "Ajay"]
# class2 = ["Ravi", "Kumar", "Arun"]
# add=class1+class2
# print(add)

# 34.Build list dynamically
# students=[]
# n=int(input("how many students"))
# for i in range(n):
#      name = input("ENTER NAMES")
#      students.append(name)
# print(students)     

# 35.print highest mark
# marks = [75, 90, 65, 80, 85]
# high =marks[0]
# for i in range(len(marks)):
#   if  marks[i]> high:
#     high=marks[i]
  
# print(marks)


# 36.Sort students
# students = ["Ram", "Ajay", "Sam", "Ravi"]


# 37.Sort by length
# names = ["Ajay", "Christopher", "Sam", "Ram", "Vijay"]
# 38.Descending order of marks
# marks = [75, 90, 65, 80, 85]
# 39.Second highest
# marks = [75, 90, 65, 80, 85]
# 40.Third smallest
# numbers = [45, 12, 78, 30, 20, 5]
# -----------------  digit extraction ---------------------
# 1.Find sum of digits of a number
# num=736
# total=0
# while num >0:
#     digit=num%10
#     total=total+digit
#     num=num//10
# print(total)

# 2.Count digits of a number
# num =235
# Count=0
# while num >0:
#     Count+=1
#     num=num//10
# print(Count)
    
# 3.Print digits of a number
# num =12345
# while num >0:
#     digit=num%10
#     print(digit)
#     num=num//10

# 4.Find product of digits
num=12345

# 5.Find largest digit
# 6.Reverse a number
# 7.Check if number is palindrome
# 8.Find smallest digit
# 9.Count even digits
# 10.Count odd digits
# 11.Find sum of squares of digits
# 12.Check Armstrong number
# 13.Check if digit sum is divisible by 3
# 14.Build number using even digits only
# 15.Find difference between largest and smallest digit



# 1.Print prime numbers
# numbers = [10, -5, 25, 16, 7, 20, 9, 36, 15, -8]
# for num in  numbers:
#     if num >1:
#        is_prime=True
#        for i in range(2,num):
#            if num%i==0:
#                is_prime=False
#                break
#        if is_prime:
#           print(num)

# 2.Count duplicates
# numbers = [10, -5, 25, 16, 7, 20, 9, 36, 15, -8, 20, 0, 7]
# duplicates=0
# for num in numbers:
#     if numbers.count(num)>1:
#         duplicates+=1
# print(duplicates)
# 3.Sum of second half
# numbers = [10, -5, 25, 16, 7, 20, 9, 36, 15, -8]
# half=len(numbers)//2
# total=sum(numbers[half:])
# print(total)
# 4.Second Largest
# numbers = [10, 45, 23, 78, 56, 91, 12, 34, 67, 5]
# numbers.sort()
# print("second largest",numbers[-2])

# 5.Rotate Left by One
# numbers = [10, 20, 30, 40, 50]
# numbers=numbers[1:]+numbers[:1]
# print(numbers)
# 6.Rotate Left by K
# numbers = [10, 20, 30, 40, 50]
# name = "hello world"
# print(name.replace("world","anas"))
# student={
#     "name":"anas",
#     "age":23
# }
# print(student.keys())
# print(student.values())
# print(student.get("age"))
# a={1,2,3,4}
# b={4,5,6,7}
# print(b.union(a))
# numbers = [10, 20, 5, 40]

# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))



# 1.Multiply by 100
# o/p : [100,200,300,400]
# numbers = [1, 2, 3, 4]
# print(list(map(lambda n: n* 100, numbers)))

# 2.Find length of every word
# words = ["apple", "python", "java"]
# print(list(map(lambda word: len(word), words)))
# o/p : [5,6,4]

# 3.Get first character
# words = ["apple", "banana", "mango"]
 # Output: ['a', 'b', 'm']
# print(list(map(lambda word:word[0],words)))

# 4.Add "Mr. " before every name

# Output: ['Mr. Ajay', 'Mr. Ravi', 'Mr. Kumar']
# names = ["Ajay", "Ravi", "Kumar"]
# print(list(map(lambda name: "Mr. " + name, names)))     


# 5.Add 18% GST to product prices
# prices = [100, 500, 1000]
# Output: [108, 540, 1080]
# prices = [100, 500, 1000]
# print(list(map(lambda price: price + (price * 0.18), prices)))

# 6.Calculate student result — Pass or Fail
# marks = [80, 30, 65, 25, 90]
# Output: ['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
# marks = [80, 30, 65, 25, 90]
# print(list(map(lambda mark:"pass" if mark>=35 else "fail",marks)))
# 7.Append " kg"
# weights = [10, 20, 30]
# Output: ['10 kg', '20 kg', '30 kg']
# weights = [10, 20, 30]
# print(list(map(lambda weigth: str(weigth)+"kg",weights)))
# 8.Remove empty strings
# values = ["Python", "", "Java", ""]
# Output: ['Python', 'Java']

# values = ["Python", "", "Java", ""]
# print(list(filter(lambda value:value !="",values)))
# 9.. Filter positive numbers
# numbers = [-10, 5, -3, 0, 8, 12]
# print(list(filter(lambda number:number >= 0, numbers)))
# Output: [5, 8, 12]

# 10.Words longer than 5 characters
# words = ["apple", "banana", "cat", "python"]
# print(list(filter(lambda word:len(word) > 5, words)))
# Output: ['banana', 'python']

# 11.Numeric strings
# values = ["123", "abc", "456", "a12"]
# print(list(filter(lambda value:value .isdigit(),values)))
# Output: ['123', '456']

# 12.Emails containing "@"
# emails = [
#     "arun@gmail.com",
#     "invalidemail.com",
#     "ravi@yahoo.com"
# ]
# print(list(filter(lambda email: email !="@" in email,emails)))
# Output: ['arun@gmail.com', 'ravi@yahoo.com']

# 13.Positive bank transactions
# transactions = [-500, 1000, -200, 3000, 500]
# print(list(filter(lambda transaction:transaction >=0,transactions)))
# Output: [1000, 3000, 500]

# 14.Digit sum greater than 10
# numbers = [12, 29, 123, 99, 45]
# Output: [29, 99]

# 15.Filter expensive products and apply a 10% discount
# Assume products above ₹1000 are expensive.
# prices = [500, 1500, 800, 2000, 3000]
# expensive = list(filter(lambda price: price > 1000, prices))
# discount = list(map(lambda price: price * 0.90, expensive))
# print(discount)
# Output: [1350.0, 1800.0, 2700.0]

# 16.Find total cricket score
# scores = [45, 60, 10, 80, 25]
# total=sum(scores)
# print(total)
# Output: 195

# 17.Find difference by reducing left to right
# numbers = [100, 20, 10, 5]
# Output: 65

# 18.Join words with -
# words = ["python", "java", "react"]
# word='-'.join(words)
# print(word)
# Output: 'python-java-react'

# 19.Find final balance after applying transaction values
# initial_balance = 10000
# transactions = [2000, -500, 3000, -1000]
# final_balance=initial_balance+sum(transactions)
# Output: 13500
# print(final_balance)

# 20.Filter salaries above ₹30,000 → increase by 10% → find payroll total
# salaries = [20000, 35000, 50000, 25000, 60000]
# Output: 145000

# 21.Filter available product prices → discount them → find cheapest
# Assume prices greater than 0 are available and discount is 10%.
# prices = [500, 0, 1500, -100, 800]
# Output: 450.0   


# 1.Create a list of fruits.
# fruits = ["apple", "banana", "orange", "grape"]
# print(fruits)

numbers = [10,20,30,40,50,60,70,80]
# 2.Print first element.
# print (numbers[0])

# 3.Print last element.
# print(numbers[-1])
# 4.Print middle element.
# print(numbers[5])
# 5.Print first 3 elements.
# print(numbers[:3])
# 6.Print last 2 elements.
# print(numbers[-2:])
# 7.Print alternate elements.
# print(numbers[::2])

# 8.Print reverse list.
# print(numbers[::-1])
# 9.Print first half.
# print(numbers[:4])
# 10.Print second half.
# print(numbers[4:])
# 11.Print elements from index 2 to 5.
# print(numbers[2:5])
# 12.Update first student name.
# students = ["Ram", "Sam", "Arun", "Ravi", "Kumar"]
# students[0]="anas"
# print(students)
# 13.Change last city
# cities = ["Chennai", "Madurai", "Salem"]
# cities[-1]="japan"
# print(cities)
# 14.Replace middle value of N length of list.
# 15.Double all salaries.
# salaries = [20000, 30000, 40000, 50000]
# double = [salary * 2 for salary in salaries]
# print(double)
# 16.Increase marks by 5.
# marks = [70, 80, 90, 60]
# new_mark=[mark*5 for mark in marks]
# print(new_mark)
# 17.Replace all negative values with 0.
# numbers = [10, -5, 30, -8, 20, -1]
# numbers = [num if num >=  0 else 0 for num in numbers]
# print(numbers)

# 18.Change all "Pending" to "Completed".

# status = ["Pending", "Completed", "Pending", "Pending"]
# status=["Completed" if s == "Pending" else s for s in status]
# print(status)
# 19.Replace zeros with 100
# numbers = [10, 0, 20, 0, 30]
# numbers=[100 if num ==0 else num for num in numbers]
# print(numbers)
# 20.Delete first item.
# numbers = [10, 20, 30, 40, 50]
# numbers.pop(0)
# print(numbers)
# 21.Delete last item.
# numbers.pop(-1)
# print(numbers)
# numbers = [10, 20, 30, 40, 50]
# 22.Remove student by name = Ram
# students = ["Ram", "Sam", "Ajay", "Ravi"]
# students=[student for student in students if student != "Ram"]
# print(students)

# 23.Remove all zeros.
# numbers = [10, 0, 20, 0, 30, 0, 40]
# numbers=[num for num in numbers if num !=0]
# print(numbers)
# 24.Remove all negatives.
# numbers = [10, -5, 20, -8, 30, -1]
# numbers=[num  for num in numbers if num>=0]
# print(numbers)

# 25.Empty list clear all.
# numbers = [10, 20, 30, 40]
# numbers.clear()
# print(numbers)

# 26.Search student Ram if found print found else not found
# students = ["Ram", "Sam", "Ajay", "Ravi"]
# print("found" if "Ram" in students else "not found")

# 27.Count occurrences of 20.
# numbers = [10, 20, 30, 20, 40, 20]
# count=numbers.count(20)
# print(count)
# 28.Find index of first occurrence 20.

# numbers = [10, 20, 30, 20, 40]
# first=numbers.index(20)
# print(first)

# 29.Find index of last occurrence 20.

# numbers = [10, 20, 30, 20, 40, 20]
# last=len(numbers)-1-numbers[::-1].index(20)
# print(last)


# 30.Check 20 is duplicate if print duplicate exists or not duplicate exits.
# numbers = [10, 20, 30, 20]
# if numbers.count(20)>1:
#         print("duplicate exists")
# else:
#         print("not duplicate exists")
# 31.Add student Arun in list
# students = ["Ram", "Sam", "Ajay"]
# students.append("arun")
# print(students)
# 32.Insert city
# cities = ["Chennai", "Madurai", "Salem"]
# cities.insert(3,"tambaram")
# print(cities)
# ex:['Chennai', 'Trichy', 'Madurai', 'Salem']
# 33.Merge two classes
# class1 = ["Ram", "Sam", "Ajay"]
# class2 = ["Ravi", "Kumar", "Arun"]
# class_3=class1+class2
# print(class_3)
# 34.Build list dynamically
# new_list=[]
# for i in range(4):
#         name=input("enter names:")
#         new_list.append(name)
#         print(new_list)

# 35.print highest mark
# marks = [75, 90, 65, 80, 85]
# 36.Sort students
# students = ["Ram", "Ajay", "Sam", "Ravi"]
# 37.Sort by length
# names = ["Ajay", "Christopher", "Sam", "Ram", "Vijay"]
# 38.Descending order of marks
# marks = [75, 90, 65, 80, 85]
# marks.sort(reverse=True)
# print(marks)
# 39.Second highest
# marks = [75, 90, 65, 80, 85]
# marks.sort(reverse=True)
# print("second higest",marks[1])
        
# 40.Third smallest
# numbers = [45, 12, 78, 30, 20, 5]
# for n in numbers:
#         if n==sorted(numbers)[2]:
#                 print(n)

# 1.Two Sum Existence Check Using a Set
# numbers = [2, 7, 11, 15]
# target = 9
# set_numbers=set(numbers)
# for num in numbers:
#     if target-num in set_numbers:
#         print("true:", num, "and", target-num)
#         break
#     set_numbers.add(num)
# else:
#         print("false")


# Check whether any two numbers produce 9.
# 2.Find the Longest Consecutive Sequence
# Example:
# [100, 4, 200, 1, 3, 2]
# Longest consecutive sequence:
# 1, 2, 3, 4
# Length:4
# set_num=set(numbers)
# longest=0
# for num in set_num: 
    



# 3.Find Missing Numbers from a Range
# numbers = [1, 2, 4, 6, 7]
# start = 1
# end = 7
# set_num=set(numbers)
# miss_num=set()
# for n in range(start,end+1) :
#     if n not in set_num:
#         miss_num.add(n)
# print(miss_num)
# Output :{3, 5}
# 4.Find Intersection of Multiple Arrays
# array1 = [10, 20, 30, 40]
# array2 = [20, 30, 40, 50]
# array3 = [30, 40, 60]
# intersection=set(array1)&set(array2)&set(array3)
# print(intersection)

# Output :{30, 40}
# numbers = [10, 20, 10, 30, 20, 40]
# numbers=set(numbers)
# print(numbers)

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common=set(a)&set(b)
# print(common)


# numbers = [10, 20, 30, 40]
# set_num=set(numbers)
# for num in numbers:
#     if 30 in set_num:
#         print("exist")
#         break
# else:
#     print("not exists")
# numbers = [1, 2, 4, 6, 7]
# start = 1
# end = 7
# set_num=set(numbers)
# miss=set()
# for i in range(start,end+1):
#     if i not in set_num:
#         miss.add(i)
        
# print(miss)
# a = [10, 20, 30, 40]
# b = [20, 30, 40, 50]
# c = [30, 40, 60]
# common=set(a)&set(b)&set(c)
# print(common)

    
#  1.Multiply Corresponding Numbers
# numbers1 = [10, 20, 30]
# numbers2 = [2, 3, 4]
# result=list(map(lambda x,y:x*y,numbers1,numbers2))
# print(result)
# output: 20 60 120

# 2.Compare Corresponding Values
# numbers1 = [10, 50, 30]
# numbers2 = [20, 40, 30]
# for a,b in zip(numbers1,numbers2):
#         if a>b:
#                 print(a,"is larger")
#         elif a<b:
#                 print(b,"is larger")
#         else:
#                 print("both are equal")
# output:
# 20 is larger
# 50 is larger
# Both are equal
# 3.Count Pairs Whose Sum Is Even
# numbers1 = [10, 15, 20, 25]
# numbers2 = [2, 3, 5, 7]
# count=0
# for a,b in zip(numbers1,numbers2):
#         if (a+b)%2==0:
#                    count+1
#                    print("count of pairs whose sum is even:",count)

# 4.Create a List of Pair Products
# numbers1 = [10, 20, 30]
# numbers2 = [2, 3, 4]
# products=[a*b for a,b in zip(numbers1,numbers2)]
# print(products)

# 4.Pair IDs Generated with Names
# names = ["Ram", "Sam", "Arun", "Ravi"]
# id=[101,102,103,104]
# res=list(zip(id,names))
# print(res)
# Output
# [
#     (101, 'Ram'),
#     (102, 'Sam'),
#     (103, 'Ajay'),
#     (104, 'Ravi')
# ]
# 5.Calculate Total Price from Product, Price, and Quantity
# products = ["Laptop", "Mouse", "Keyboard"]
# prices = [50000, 500, 1500]
# quantities = [2, 3, 4]
# for product,prices,quantities in zip(products,prices,quantities):
#         total_price=prices*quantities
#         print(f"product:{product},total price:{total_price}")
# 6.Print Available Products Using Stock
# products = ["Laptop", "Mouse", "Keyboard"]
# prices = [50000, 500, 1500]
# stocks = [10, 0, 5]
# 7.Create Dictionaries from Three Related Lists as Nested Values
# names = ["Ram", "Sam", "Arun"]
# marks = [80, 70, 95]
# grades = ["A", "B", "A+"]
# 8.Separate Products and Prices
# data = [
#     ("Laptop", 50000),
#     ("Mouse", 500),
#     ("Keyboard", 1500)
# ]
# Output:
# ('Laptop', 'Mouse', 'Keyboard')
# (50000, 500, 1500)
# 9.Convert Unzipped Tuples Back to Lists
# data = [
#     ("Ram", 80),
#     ("Sam", 70),
#     ("Arun", 95)
# ]
# 10.Transport — Match Bus Numbers with Routes
# bus_numbers = ["21G", "27D", "70"]
# routes = [
#     "Tambaram - Broadway",
#     "Anna Nagar - T Nagar",
#     "Guindy - Avadi"
# ]  


# number1=int(input("enter number:"))
# number2=int(input("enter number2:"))

# numbers3=number1/number2
# print(numbers3)
# try:
#         print(numbers3)


# except:
#         print("number can be zero")        

# else:
#         print("try again") 
# .Create a Product class and store the details of one product.
# Input
# iPhone
# 80000
# Output
# Product = iPhone
# Price = 80000

# class student:
#     def display (self):
#         print("wlecome anas")




# s1=student()  
# s1.display()  

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)

# s1=student("anas",19)
# s2=student("ramu",22)

# s1.display()
# s2.display()

numbers = [10, 50, 20, 80, 30]
# for i in numbers:
#     if i %2==0:
#         print(i,"is even")

# find large 3 number
large=sorted(numbers)[-3:]
print("large 3 numbers:",large)


        
        

     




     
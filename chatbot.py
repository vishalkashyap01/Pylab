# doc = {1 : 'HTML', 2 : 'CSS', 3 : 'JavaScript', 4 : 'Python', 5 : 'Java'}
# print(doc)

# for key in doc:
#     print(key, ":", doc[key])
    
# name = input("please, enter your name her: ") 
# marks1 = int(input("please, enter your marks1 her: "))
# marks2 = int(input("please, enter your marks1 her: "))
# marks3 = int(input("please, enter your marks1 her: "))
   
# total_marks = marks1 + marks2 + marks3

# if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
#     print("Congratulations", name, "you are passed and your total marks is", total_marks)
# else:
#     print("Sorry", name, "you are failed and your total marks is", total_marks)
    

    
# item1 = int(input("please, enter your item1 here: "))
# item2 = int(input("please, enter your item2 here: "))
# item3 = int(input("please, enter your item3 here: "))
# item4 = int(input("please, enter your item4 here: "))

# total_item = item1 + item2 + item3 + item4
# print("Total Amount: ", total_item, " RS/-")


# if total_item >= 2000:
#     new_price = total_item - (total_item * 0.10)
#     print("Congratulations, you got 10% discount and your total price is", new_price, "RS/-")
# else:
#     print("Total Amount: ", total_item, " RS/-")



# account = {
#     'name' : "Suman",
#     'account_number' : 123456789,
#     'balance' : 7125073.90
# }

# while True:
#     print("\n1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
#     user_input = int(input("Please enter your choice: "))
#     if user_input == 1:
#         print("Account Holder Name: ", account['name'])
#         print("Your current balance is: ", account['balance'])
#     elif user_input == 2:
#         deposit_amount = float(input("Enter the amount to deposit: "))
#         account['balance'] += deposit_amount
#         print("Deposit successful! Your new balance is: ", account['balance'])    
#     elif user_input == 3:
#         withdraw_amount = float(input("Enter the amount to withdraw: "))
#         if withdraw_amount <= account['balance']:
#             account['balance'] -= withdraw_amount
#             print("Withdrawal successful! Your new balance is: ", account['balance'])
#         else:
#             print("Insufficient balance!")    
#     elif user_input == 4:
#         print("Thank you for using our services!")
#         break        
#     else:
#         print("Network Error! Please try again later.")        



# employee_name = input("Please enter your name: ")
# employee_id = input("Please enter your employee ID: ")
# salary = float(input("Please enter your salary: "))

# final_salary = salary + (salary * 0.10) + (salary * 0.20)
# hra = salary * 0.10
# da = salary * 0.20
# print("\nEmployee Name: ", employee_name)
# print("Employee ID: ", employee_id)
# print("Basic Salary: ", salary)
# print("HRA (10%): ", hra)
# print("DA (20%): ", da)
# print("Final Salary: ", final_salary)




# roll_no = int(input("Please, enter your roll number here: "))
# attendance = int(input("Please, enter your attendance here: "))         
# if attendance >= 75:
#     registered = True
#     print("Congratulations! You are eligible to register for the exam.")
# else:
#     registered = False
#     print("Sorry! You are not eligible to register for the exam due to low attendance.")    







# wheel = int(input("Please, show vehicle wheels : "))
# fine = 0

# drink = False

# if wheel == 2:
#     drink = input("\nAre you drinking alcohol? (yes/no): ")
#     if drink:
#         fine = 5000
#         print("You are fined Rs.", fine, "for drinking and driving on a two-wheeler.")
#     else:
#         print("No fine for drinking & driving: ", 0)
#     helmet = input("please check, here helmet or not? (yes/no): ")
#     if helmet == "no":
#         fine += 1000
#         print("You are fined Rs.", fine, "for not wearing a helmet while riding a two-wheeler.\n")
#     else:
#         print("No fine for wearing a helmet : ", 0)
#     print("Total fine for two-wheeler: Rs.", fine)
# elif wheel == 4:
#     drink = input("Are you drinking alcohol? (yes/no): ")
#     if drink:
#         fine = 10000
#         print("You are fined Rs.", fine, "for drinking and driving on a four-wheeler.")
#     else:
#         print("No fine for drinking & driving: ", 0)
#     seatbelt = input("please check, here seatbelt or not? (yes/no): ")
#     if seatbelt == "no":
#         fine += 2000
#         print("You are fined Rs.", fine, "for not wearing a seatbelt while driving a four-wheeler.")
#     else:
#         print("No fine for wearing a seatbelt: ", 0)
#     print("Total fine for four-wheeler: Rs.", fine)
#     print("Please, drive safely and follow traffic rules.")
# elif wheel >= 6 and wheel <= 18:
#     drink = input("Are you drinking alcohol? (yes/no): ")
#     if drink:
#         fine = 20000
#         print("You are fined Rs.", fine, "for drinking and driving on a heavy vehicle.")
#     else:
#         print("You are not fined for drinking and driving on a heavy vehicle.")
#     print("Total fine for heavy vehicle: Rs.", fine)
#     print("Please, drive safely and follow traffic rules.")
# else:
#     print("Invalid input....")    


                                                    # PROJECT 1: Result Management System - LAB
# WAP to create a simple result management system using in Python. 
# The program should allow the user to input student names and their corresponding marks, 
# and then display the results in a formatted manner.
# 1. Accept details of multiple students.
# 2. Take 5 subjects marks for each student.
# 3. Calculate total marks and percentage for each student.
# 4. Determine the grade based on the percentage (e.g., A, B, C, D, F).
# 5. Check whether the student has passed or failed.
# 6. Find the class topper and give prize.
# 7. Display the results in a formatted manner for each student.
# 8. Use for if/elif/else/nexted if/continue/break.

import requests

# =========================
# OPENWEATHER CONFIGURATION
# =========================

API_KEY = "9b69c3079fceac7d23c5bb2be2c1e9c8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# =========================
# GET WEATHER
# =========================

def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Convert response to JSON
        data = response.json()

        # API key error
        if response.status_code == 401:
            return "Error: Your OpenWeather API key is invalid."

        # City not found
        if response.status_code == 404:
            return f"Error: I couldn't find the city '{city}'."

        # Other HTTP errors
        if response.status_code != 200:
            return f"Weather API error: {data.get('message', 'Unknown error')}"

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        return (
            f"\nWeather in {city_name}, {country}\n"
            f"-----------------------------\n"
            f"Condition   : {description.title()}\n"
            f"Temperature : {temperature}°C\n"
            f"Feels Like  : {feels_like}°C\n"
            f"Humidity    : {humidity}%\n"
            f"Wind Speed  : {wind_speed} m/s\n"
        )

    except requests.exceptions.Timeout:
        return "Error: Weather server took too long to respond."

    except requests.exceptions.ConnectionError:
        return "Error: Please check your internet connection."

    except requests.exceptions.RequestException as error:
        return f"Request error: {error}"

    except ValueError:
        return "Error: Invalid response received from weather server."

    except KeyError as error:
        return f"Error: Weather data format changed. Missing: {error}"


# =========================
# CHATBOT
# =========================
def chatbot_response(message):

    message = message.strip()

    if not message:
        return "Please type something."

    lower_message = message.lower()

    # =========================
    # GREETINGS
    # =========================

    if lower_message in [
        "hello",
        "hi",
        "hey",
        "hii",
        "hola"
    ]:
        return (
            "Hello! I am PyBot.\n"
            "I can provide weather information.\n"
            "Try asking: 'Kanpur weather'"
        )

    # =========================
    # HELP
    # =========================

    if lower_message == "help":

        return (
            "\nYou can ask me things like:\n"
            "- Hello\n"
            "- Kanpur weather\n"
            "- Weather in Mumbai\n"
            "- Delhi temperature\n"
            "- Weather India\n"
            "- Temperature in London\n"
            "- Help\n"
            "- Bye\n"
        )

    # =========================
    # EXIT
    # =========================

    if lower_message in [
        "bye",
        "exit",
        "quit"
    ]:
        return "Goodbye! Have a great day!"

    # =========================
    # WEATHER KEYWORDS
    # =========================

    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "climate",
        "hot",
        "cold",
        "rain",
        "raining"
    ]

    # =========================
    # DETECT WEATHER REQUEST
    # =========================

    if any(word in lower_message for word in weather_keywords):

        city = None

        # ---------------------------------
        # Example:
        # weather in Kanpur
        # ---------------------------------

        if " in " in lower_message:

            city = lower_message.split(" in ", 1)[1]

        # ---------------------------------
        # Example:
        # Kanpur weather
        # ---------------------------------

        elif " weather" in lower_message:

            city = lower_message.split(" weather")[0]

        # ---------------------------------
        # Example:
        # Mumbai temperature
        # ---------------------------------

        elif " temperature" in lower_message:

            city = lower_message.split(" temperature")[0]

        # ---------------------------------
        # Example:
        # Delhi forecast
        # ---------------------------------

        elif " forecast" in lower_message:

            city = lower_message.split(" forecast")[0]

        # ---------------------------------
        # Example:
        # weather Kanpur
        # ---------------------------------

        elif lower_message.startswith("weather "):

            city = lower_message.replace(
                "weather ",
                "",
                1
            )

        # ---------------------------------
        # Clean city name
        # ---------------------------------

        if city:

            city = city.strip()

            city = city.replace("today", "")
            city = city.replace("now", "")
            city = city.replace("please", "")

            city = city.strip()

            if city:
                return get_weather(city)

        return (
            "Please specify a city.\n"
            "Examples:\n"
            "- Kanpur weather\n"
            "- Weather in Mumbai\n"
            "- Delhi temperature"
        )

    # =========================
    # DEFAULT RESPONSE
    # =========================

    return (
        "I don't understand that yet.\n"
        "Try:\n"
        "'Kanpur weather'\n"
        "'Weather in Mumbai'\n"
        "or type 'help'."
    )
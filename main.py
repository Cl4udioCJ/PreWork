#Code Foundation Is From School Assigment Where I Had Made Most Of A Chatbot

print("Hi, Welcome To The La La Restaurant! How can I help you today?")

while True:

  print("")
  user_input = input("(Reservations, Menu, Hours, Order) or (Quit) to end the conversation: ")
  print("")
  
  if user_input.lower() == "reservations":
      time = input("What time would you like to make a reservation for? ")
      date = input("What date would you like to make a reservation for? ")
      party_size = input("How many people are in your party? ")
      print("Okay, I have made a reservation for you at", time, "on", date, "for a party of", party_size)


  elif user_input.lower() == "menu":
    
    print("Our menu options are: Steak, Chicken, Fish, Pasta, Salad")

  elif user_input.lower() == "hours":
    
    print("Our business hours are from 9:00 AM to 10:00 PM Monday-Friday and 8:00 AM to 8:00 PM  on Weekends.")


  elif user_input.lower() == "order":
    
    print("Our menu options are: Steak, Chicken, Fish, Pasta, Salad")
    order_choice = input("What would you like to order? ")
    
    print("Okay, I have added a", order_choice, "to your order")
    order_confirm = input("Is there anything else you would like to add to your order? (Yes/No) ")
    
    while order_confirm.lower() == "yes":
        
        print("Our menu options are: Steak, Chicken, Fish, Pasta, Salad")
        additional_order = input("What would you like to add to your order? ")
        print("Okay, I have added a", additional_order, "to your order")
        order_confirm = input("Is there anything else you would like to add to your order? (Yes/No) ")
    
    print("Thank you for your order!")


  elif user_input.lower() == "quit":
    print("Thank you for chatting with me. Have a great day!")
  

  else:
    print("I'm sorry, I didn't understand that. Could you please try again?")
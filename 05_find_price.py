# Component 05 - Find the selling price from information given by user


# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)

        # If response is blank, question is repeated (loop starts over)
        if response == "":
            print(error)
            continue

        # if response is not blank, program continues
        else:
            return response


# Number Checking Function goes here
def num_check(question):

    error = "Please enter a number that is more than zero"
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:

                print(error)
            else:
                return response
        except ValueError:

            print(error)


# get goal function
def get_goal():
    valid = False
    while not valid:
        profit_var = not_blank("Would you like to enter your profit goal by percentage or cost? ",
                               "Please fill in this field").lower()

        if profit_var == "$":
            goal = num_check("What is your goal amount to raise for charity? $")
            print("$", goal)
            break

        elif profit_var == "%":
            goal = num_check("What percentage do you want to raise for charity? ")
            print(goal, "%")
            break

        else:
            print("Please enter '%' or '$'")

        return profit_var


# main routine

# set up empty list
printout = []
total_list = []
type_goal = ""

# Get the users charity goal
what_goal = get_goal()

# start of loop - get item info
stop = ""
while stop != "xxx":
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'xxx' to quit")

    if get_product == "xxx":
        break

    fixed = not_blank("Do you buy this product once? ",
                      "Please enter <yes> or <no>").lower()
    if fixed == "yes":
        get_cost = num_check("Cost: $")
        get_amount = 1

    else:
        get_cost = num_check("Cost: $")

        get_amount = num_check("Amount: ")

    printout.append("{:.0f} {}, ${:.2f} ".format(get_amount, get_product, get_cost))

    if get_cost > 0:
        total = get_cost * get_amount
    else:
        continue

    total_list.append(total)

total_cost = sum(total_list)

# print out list of information on items and the total cost
print()
print("Amount , Item, Cost")
for item in printout:
    print(item)
print()
print("Total Cost: ")
print("${:.2f}".format(total_cost))

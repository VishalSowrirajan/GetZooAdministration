from ExpenseManager.ExpenseCalculator import FoodExpenseCalculator, ZooKeeperExpenseCalculator
from HTTPController.HTTPHandler import HTTPRequestHandler, HTTPPostHandler
from Utils.StaticConstants import *
from Utils.Utilities import total_cost, convert_to_df, return_dict


def main():
    # Create Objects for reading Animal, Food and Zookeeper Path class
    animal_data_reader = HTTPRequestHandler(ANIMAL_EXT)
    food_data_reader = HTTPRequestHandler(FOOD_EXT)
    zookeeper_data_reader = HTTPRequestHandler(ZOOKEEPER_EXT)

    # Data Parser
    animal_data = animal_data_reader.response()
    print('Animal URL data parsed successfully')
    food_data = food_data_reader.response()
    print('Food URL data parsed successfully')
    zookeeper_data = zookeeper_data_reader.response()
    print('Zookeeper URL data parsed successfully')

    # Convert to DataFrame
    animal_df = convert_to_df(animal_data)
    food_df = convert_to_df(food_data)
    zookeeper_df = convert_to_df(zookeeper_data)

    # Food Expense Calculator
    food_expense = FoodExpenseCalculator(animal_df, food_df)
    total_food_cost = food_expense.calculate_expense()

    # ZooKeeper Expense Calculator
    zookeeper_daily_expense = ZooKeeperExpenseCalculator(animal_df, zookeeper_df)
    total_zookeeper_expense, costly_compound = zookeeper_daily_expense.calculate_expense()

    # Compute the Total Expenses
    total_expenses = total_cost(total_food_cost, total_zookeeper_expense)

    # POST Expense data request
    expense_dict = return_dict(RESULT, total_expenses)
    post_data = HTTPPostHandler(expense_dict, ADMINISTRATION_EXT)
    response_status = post_data.post_data_to_URL()
    print("The response status for Post_Expense_Data is: {}".format(response_status))

    # POST costly compound to the respected director
    expense_compound_dict = return_dict(COMPOUND, costly_compound)
    post_data = HTTPPostHandler(expense_compound_dict, DIRECTOR_EXT)
    response_status = post_data.post_data_to_URL()
    print("The response status for Post_Costly_Compound is: {}".format(response_status))


if __name__ == '__main__':
    main()

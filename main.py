from ExpenseManager.ExpenseCalculator import FoodExpenseCalculator, ZooKeeperExpenseCalculator
from HTTPController.HTTPRequestHandler import HTTPRequestHandler, HTTPPostHandler
from Utils.StaticConstants import *
from Utils.utilities import total_cost, convert_to_df


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
    post_data = HTTPPostHandler(total_expenses, ADMINISTRATION)
    response_status = post_data.post_data_to_URL()
    print(response_status)

    # POST costly compound to the respected director
    post_data = HTTPPostHandler(costly_compound, DIRECTOR)
    response_status = post_data.post_data_to_URL()
    print(response_status)


if __name__ == '__main__':
    main()

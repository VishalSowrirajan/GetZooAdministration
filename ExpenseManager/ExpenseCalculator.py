from Utils.StaticConstants import WEEK_TO_DAY_CONVERSION


class FoodExpenseCalculator:
    """This class is responsible for calculating the per day food expenses for each animal"""
    def __init__(self, animal_data, food_data):
        self.animal_data = animal_data
        self.food_data = food_data

    def calculate_expense(self):
        animal_food_type = self.extract_animal_food_type()
        total_cost = self.calculate_food_expense(animal_food_type)
        return total_cost

    def extract_animal_food_type(self):
        # Calculate the total animals and the amount of required food
        self.animal_data['total_required_food'] = self.animal_data['number_of_animals'] * self.animal_data['amount_of_food_per_day']
        # Sorting the values to enable precise multiplication of food and its related cost
        animal_food_count = self.animal_data.groupby('type_of_food').sum().reset_index().sort_values('type_of_food')
        return animal_food_count[['type_of_food', 'total_required_food']]

    def calculate_food_expense(self, animal_food_type):
        food_sorted = self.food_data.sort_values('type_of_food').reset_index(drop=True)
        cost_per_food = animal_food_type['total_required_food'] * food_sorted['price_per_kg']
        return cost_per_food.sum()


class ZooKeeperExpenseCalculator:
    """This class is responsible for calculating the per day expenses for the zookeeper w.r.t the animal compound"""
    def __init__(self, animal_data, zookeeper_data):
        self.animal_data = animal_data
        self.zookeeper_data = zookeeper_data

    def calculate_expense(self):
        animal_compound_type = self.extract_animal_compound_type()
        total_zookeeper_expense, costly_compound = self.calculate_zookeeper_expense(animal_compound_type)
        return total_zookeeper_expense, costly_compound

    def extract_animal_compound_type(self):
        # Calculate the total animal care
        self.animal_data['total_animal_care_in_hours_per_week'] = self.animal_data['hours_of_care_per_week'] * self.animal_data['number_of_animals']
        compound_wise_hours_of_care = self.animal_data.groupby('compound').sum().reset_index().sort_values('compound')
        # Return only the compound name and total hours required
        return compound_wise_hours_of_care[['compound', 'total_animal_care_in_hours_per_week']]

    def calculate_zookeeper_expense(self, animal_food_type):
        compound_sorted = self.zookeeper_data.sort_values('compound').reset_index(drop=True)
        # WEEK TO DAY CONVERSION
        animal_food_type['total_animal_care_in_hours_per_week'] = animal_food_type['total_animal_care_in_hours_per_week'] / WEEK_TO_DAY_CONVERSION
        cost_of_zookeeper_per_day = animal_food_type['total_animal_care_in_hours_per_week'] * compound_sorted['hourly_rate']
        # Get the index of the max value and slice the compound_sorted df to get the expensive compound
        expensive_compound_data = compound_sorted.iloc[cost_of_zookeeper_per_day.idxmax()]
        return cost_of_zookeeper_per_day.sum(), expensive_compound_data['compound']



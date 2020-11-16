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
        self.animal_data['total_animals'] = self.animal_data['number_of_animals'] * self.animal_data['amount_of_food_per_day']
        # Sorting the values to enable precise multiplication of food and its related cost
        animal_food_count = self.animal_data.groupby('type_of_food').sum().reset_index().sort_values('type_of_food')
        return animal_food_count[['type_of_food', 'total_animals']]

    def calculate_food_expense(self, animal_food_type):
        food_sorted = self.food_data.sort_values('type_of_food').reset_index(drop=True)
        cost_per_food = animal_food_type['total_animals'] * food_sorted['price_per_kg']
        return cost_per_food.sum()


class ZooKeeperExpenseCalculator:
    """This class is responsible for calculating the per day expenses for the zookeeper w.r.t the animal compound"""
    def __init__(self, animal_data, zookeeper_data):
        self.animal_data = animal_data
        self.zookeeper_data = zookeeper_data

    def calculate_expense(self):
        animal_compound_type = self.extract_animal_compound_type()
        total_zookeeper_expense = self.calculate_zookeeper_expense(animal_compound_type)
        return total_zookeeper_expense

    def extract_animal_compound_type(self):
        unique_compounds = self.animal_data.compound.value_counts().reset_index().sort_values('index')
        return unique_compounds.reset_index(drop=True)

    def calculate_zookeeper_expense(self, animal_food_type):
        compound_sorted = self.zookeeper_data.sort_values('compound').reset_index(drop=True)
        cost_of_zookeeper_per_day = animal_food_type['compound'] * compound_sorted['hourly_rate']
        return cost_of_zookeeper_per_day.sum()



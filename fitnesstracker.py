# 7. Fitness Tracker
# • Description: Create a console application that tracks fitness activities. Implement classes for User, Workout, and DietPlan. Include features for logging workouts and meals, as well as monitoring progress.
# • OOP Concepts: Inheritance (different user types), Composition (workouts consist of exercises), and Encapsulation (user data management).

from abc import ABC,abstractmethod
import datetime
class User(ABC):

    user_count=1
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.user_id='U-1234'+str(User.user_count)
        User.user_count+=1
        self.workouts={}
        self.diet={}
    
    @abstractmethod
    def user_type(self):
        pass
    
    def workout_log(self, workout):
        if workout.workout_name not in self.workouts:
            self.workouts[workout.workout_name] = [(datetime.datetime.now(), workout.calories_lost)]
        else:
            self.workouts[workout.workout_name].append((datetime.datetime.now(), workout.calories_lost))
    
    def meal(self, meal):
        if meal.diet_name not in self.diet:
            self.diet[meal.diet_name] = [(datetime.datetime.now(), meal.calories)]
        else:
            self.diet[meal.diet_name].append((datetime.datetime.now(), meal.calories))

    def bmi(self):
        height_in_m=self.height/100
        bmi=self.weight/(height_in_m**2)
        return round(bmi,2)
    def total_calories_burned(self):
        total_calories = 0
        for workout_sessions in self.workouts.values():
            for _, calories in workout_sessions:
                total_calories += calories
        return total_calories
    def total_calories_intake(self):
        total_calories = 0
        for diet_taken in self.diet.values():
            for _, calories in diet_taken:
                total_calories += calories
        return total_calories
    
    def show_progress(self):
        print("*"*20)
        print(f'Name:{self.name}')
        print(f'Weight: {self.weight}')
        print(f'Height: {self.height}')
        print(f'BMI: {self.bmi()}')
        
        if self.workouts:
            print("\nWorkouts Logged:")
            for workout_name, sessions in self.workouts.items():
                print(f'{workout_name}: {len(sessions)} times')
                for timestamp, calories in sessions:
                    print(f'  - {timestamp.strftime("%Y-%m-%d %H:%M:%S")} (Calories burned: {calories} kcal)')
        else:
            print("\nNo workouts logged yet.")
        
        if self.diet:
            print("\nMeals Logged:")
            for meal_name, sessions in self.diet.items():
                print(f'{meal_name}: {len(sessions)} times')
                for timestamp, calories in sessions:
                    print(f'  - {timestamp.strftime("%Y-%m-%d %H:%M:%S")} (Calories: {calories} kcal)')
        else:
            print("\nNo meals logged yet.")
        
        print("Total calories burned: ",self.total_calories_burned())
        print("Total calories intake:",self.total_calories_intake())
        print("*"*20)
        print()
        

    def setHeight(self,height):
        self.height=height
    
    def setWeight(self,weight):
        self.weight=weight
class GymGuy(User):
    def user_type(self):
        self.user_type='Gym Freak'

class Athlete(User):
    def user_type(self):
        self.user_type='Athlete'

class Workout:
    def __init__(self,name,level,calories_lost):
        self.workout_name=name
        self.level=level
        self.calories_lost=calories_lost
    def getCalories_burned(self):
        return self.calories_lost
    def __str__(self):
        return f'Workout name: {self.workout_name}\nLevel: {self.level}\n'
class DietPlan:
    def __init__(self,meal_name,diet_type,calories):
        self.diet_name=meal_name
        self.diet_type=diet_type
        self.calories=calories
    def __str__(self):
        return f'Diet:{self.diet_name}\nCalories: {self.calories}\nType: {self.diet_type}\n'

user1=GymGuy("Pragyan",23,65,165)
user2=Athlete("Nita",18,45,150)
workout1=Workout("Jogging","Beginner",40)
workout2=Workout("Stretching",'Beginner',30)
workout3=Workout('Push-up','Intermediate',50)

diet1=DietPlan('Morning Combo-2','Breakfast',35)
diet2=DietPlan('Dhal-Bhat','Lunch',100)
diet3=DietPlan('Roti-Tarkari','Dinner',100)
user1.workout_log(workout1)
user2.workout_log(workout1)
user2.workout_log(workout2)
user1.workout_log(workout3)
user2.workout_log(workout3)
user1.meal(diet1)
user1.meal(diet2)
user2.meal(diet1)
user2.meal(diet3)

user1.show_progress()
user2.show_progress()
# 3. Task Management System
# • Description: Create a console-based task manager that allows users to manage tasks and projects. Include classes for Task, Project, and User. Implement methods for adding, updating, and completing tasks.
# • OOP Concepts: Composition (projects contain tasks), Inheritance (user roles), and Polymorphism (task priorities).

class Task:
    task_id=1

    def __init__(self,name,due,priority="Low"):
        self.name=name
        self.due=due
        self.priority=priority
        self.finished=False
        self.task_id=Task.task_id
        Task.task_id+=1
    
    def completed(self):
        self.finished=True
        print(f'{self.name} finished {self.name} task of {self.task_id}.')
    
    def add_description(self,description=''):
        self.description=description
    def update_name(self,name):
        self.name=name
    def update_due(self,due):
        self.due=due
    def update_priority(self,priority):
        self.priority=priority
    
    def __str__(self):
        status="Completed" if self.finished else "Pending"
        return f'{self.task_id}\t\t{self.name}\t\tDue:{self.due}\t\t{status}\t\tPriority:{self.priority}'
    
class Project:
    project_id=1
    def __init__(self, name):
        self.name=name
        self.tasks = []
        self.p_id = Project.project_id
        Project.project_id += 1
    def add_description(self,description=''):
        self.description=description
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task.name} has been removed from {self.name}.")
                return
        print(f"Task with ID {task_id} not found in project '{self.name}'.")
    def show_tasks(self):
        if not self.tasks:
            print(f"No tasks in project {self.name}.")
        else:
            print(f"Tasks in project {self.name}:")
            for task in self.tasks:
                print(task)
    
    def __str__(self):
        return f"NAME: {self.name} ID:{self.p_id}"

class User:
    user_id=1
    def __init__(self,name,role):
        self.name=name
        self.role=role
        self.projects=[]
        self.u_id=User.user_id
        User.user_id+=1
    
    def add_Project(self,project):
        self.projects.append(project)
        
    
    def remove_project(self,project_id):
        for project in self.projects:
            if project.p_id==project_id:
                self.projects.remove(project)
                print(f"{project.name} removed for {self.name}")
                return
        print(f'Project with {project_id} not found.')
    
    def show_projects(self):
        if not self.projects:
            print(f'No any projects of {self.name}.')
        else:
            print(f"Projects of {self.name}:")
            for project in self.projects:
                print(project)
    
    def __str__(self):
        return f'Name: {self.name} ID: {self.u_id}'
    
task1=Task("Assignment","11/11/2024","Medium")
task2=Task("Major Project","06/4/2025","High")
task3=Task("App development","06/2/2025","Low")
task1.add_description("Some assignment are available to do.")
task2.add_description("Given project as major project should be done.")
task3.add_description('App development should be given to client in time.')

p1=Project("My task")
p1.add_description('These are some of my task that need to be done.')
p1.add_task(task1)
p1.add_task(task2)

p2=Project("Website")
p2.add_description("Task for Website design")
p2.add_task(task1)
p2.add_task(task3)

p1.show_tasks()
p1.remove_task(1)

user1=User("Pragyan","Designer")
user1.add_Project(p1)
user1.add_Project(p2)
print(user1)
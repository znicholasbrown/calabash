from prefect import Flow, task

@task
def Green_Teas():
    print("List of Green Teas")

@task
def Black_Teas():
    print("List of Black Teas")

@task
def Chai_Teas():
    print("List of Chai Teas")

@task
def Herbal_Teas():
    print("List of Herbal Teas")
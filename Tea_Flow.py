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

with Flow("List of Teas") as List_Teas:
    green_tea_result = Green_Teas()
    black_tea_result = Black_Teas()
    chai_tea_result = Chai_Teas()
    herbal_tea_result = Herbal_Teas()
 
list_teas_state = List_Teas.run()

assert list_teas_state.is_successful()
from prefect import Flow, task
from prefect.environments.storage import Docker

storage = Docker(
    base_image="python:3.7",
    python_dependencies=[],
    image_name="tea-flow",
    image_tag="tea-flow",
)

@task
def Green_Teas():
    print("Getting Green Teas")
    
    from Green_Tea_Tasks import AllGreenTeas
    AllGreenTeas()

@task
def Black_Teas():
    print("Getting Black Teas")

@task
def Chai_Teas():
    print("Getting Chai Teas")

@task
def Herbal_Teas():
    print("Getting Herbal Teas")

with Flow("List of Teas", storage=storage) as List_Teas:
    green_tea_result = Green_Teas()
    black_tea_result = Black_Teas()
    chai_tea_result = Chai_Teas()
    herbal_tea_result = Herbal_Teas()
 
list_teas_state = List_Teas.run()

assert list_teas_state.is_successful()
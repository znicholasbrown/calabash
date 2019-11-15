import pyfiglet
import prefect
from prefect import Flow, task
from Green_Tea_Tasks import AllGreenTeas


@task
def Green_Teas():
    print()
    pyfiglet.figlet_format("Getting Green Teas")
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

with Flow("List of Teas") as List_Teas:
    green_tea_result = Green_Teas()
    black_tea_result = Black_Teas()
    chai_tea_result = Chai_Teas()
    herbal_tea_result = Herbal_Teas()
 
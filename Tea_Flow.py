import prefect
import Green_Tea_Tasks
from prefect import Flow, task


@task
def Green_Teas():
    print("Getting Green Teas") 
    Green_Tea_Tasks.List_Teas.run()

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
    green_teas = Green_Teas()
    genmaicha = Green_Tea_Tasks.Genmaicha(upstream_tasks=[green_teas])
    Green_Tea_Tasks.GenmaichaDescription(upstream_tasks=[genmaicha])

    fridalicious = Green_Tea_Tasks.Fridalicious(upstream_tasks=[green_teas])
    Green_Tea_Tasks.FridaliciousDescription(upstream_tasks=[fridalicious])

    jasmineRose = Green_Tea_Tasks.JasmineRose(upstream_tasks=[green_teas])
    Green_Tea_Tasks.JasmineRoseDescription(upstream_tasks=[jasmineRose])
    
    raspberryBeret = Green_Tea_Tasks.RaspberryBeret(upstream_tasks=[green_teas])
    Green_Tea_Tasks.RaspberryBeretDescription(upstream_tasks=[raspberryBeret])
    
    rockinMoroccan = Green_Tea_Tasks.RockinMoroccan(upstream_tasks=[green_teas])
    Green_Tea_Tasks.RockinMoroccanDescription(upstream_tasks=[rockinMoroccan])

    templeofHeavenGunpowderGreenTea = Green_Tea_Tasks.TempleofHeavenGunpowderGreenTea(upstream_tasks=[green_teas])
    Green_Tea_Tasks.TempleofHeavenGunpowderGreenTeaDescription(upstream_tasks=[templeofHeavenGunpowderGreenTea])

    kashmiriGingerSpice = Green_Tea_Tasks.KashmiriGingerSpice(upstream_tasks=[green_teas])
    Green_Tea_Tasks.KashmiriGingerSpiceDescription(upstream_tasks=[kashmiriGingerSpice])

    chunMeiGreenTea = Green_Tea_Tasks.ChunMeiGreenTea(upstream_tasks=[green_teas])
    Green_Tea_Tasks.ChunMeiGreenTeaDescription(upstream_tasks=[chunMeiGreenTea])

    black_tea_result = Black_Teas()


    chai_tea_result = Chai_Teas()


    herbal_tea_result = Herbal_Teas()

List_Teas.run()
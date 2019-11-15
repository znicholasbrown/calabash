import prefect
import Green_Tea_Tasks
import Black_Tea_Tasks
import Chai_Tea_Tasks
import Herbal_Tea_Tasks
from prefect import Flow, task


@task
def Green_Teas():
    print("Getting Green Teas") 

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
    # Start Green Teas
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
    # End Green Teas

    # Start Black Teas
    black_tea_result = Black_Teas()

    blackMagicWoman = Black_Tea_Tasks.BlackMagicWoman(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.BlackMagicWomanDescription(upstream_tasks=[blackMagicWoman])
    blueVelvet = Black_Tea_Tasks.BlueVelvet(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.BlueVelvetDescription(upstream_tasks=[blueVelvet])
    desertRose = Black_Tea_Tasks.DesertRose(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.DesertRoseDescription(upstream_tasks=[desertRose])
    fridalicious = Black_Tea_Tasks.Fridalicious(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.FridaliciousDescription(upstream_tasks=[fridalicious])
    lapsangSouchong = Black_Tea_Tasks.LapsangSouchong(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.LapsangSouchongDescription(upstream_tasks=[lapsangSouchong])
    myJamaicanGuy = Black_Tea_Tasks.MyJamaicanGuy(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.MyJamaicanGuyDescription(upstream_tasks=[myJamaicanGuy])
    organicEarlGrey = Black_Tea_Tasks.OrganicEarlGrey(upstream_tasks=[black_tea_result])
    Black_Tea_Tasks.OrganicEarlGreyDescription(upstream_tasks=[organicEarlGrey])
    # End Black Teas

    # Start Chai Teas
    chai_tea_result = Chai_Teas()

    idrisHotChocolateInfusedChai = Chai_Tea_Tasks.IdrisHotChocolateInfusedChai(upstream_tasks=[chai_tea_result])
    Chai_Tea_Tasks.IdrisHotChocolateInfusedChaiDescription(upstream_tasks=[idrisHotChocolateInfusedChai])
    lovePotion = Chai_Tea_Tasks.LovePotion(upstream_tasks=[chai_tea_result])
    Chai_Tea_Tasks.LovePotionDescription(upstream_tasks=[lovePotion])
    mandelasMasalaChai = Chai_Tea_Tasks.MandelasMasalaChai(upstream_tasks=[chai_tea_result])
    Chai_Tea_Tasks.MandelasMasalaChaiDescription(upstream_tasks=[mandelasMasalaChai])
    mandingoChai = Chai_Tea_Tasks.MandingoChai(upstream_tasks=[chai_tea_result])
    Chai_Tea_Tasks.MandingoChaiDescription(upstream_tasks=[mandingoChai])
    yogiChai = Chai_Tea_Tasks.YogiChai(upstream_tasks=[chai_tea_result])
    Chai_Tea_Tasks.YogiChaiDescription(upstream_tasks=[yogiChai])
    # End Chai Teas

    # Start Herbal Teas
    herbal_tea_result = Herbal_Teas()

    bABYLOVE = Herbal_Tea_Tasks.BABYLOVE(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.BABYLOVEDescription(upstream_tasks=[bABYLOVE])
    fatBlackPussyCat = Herbal_Tea_Tasks.FatBlackPussyCat(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.FatBlackPussyCatDescription(upstream_tasks=[fatBlackPussyCat])
    getMyMindRight = Herbal_Tea_Tasks.GetMyMindRight(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.GetMyMindRightDescription(upstream_tasks=[getMyMindRight])
    goGoGoji = Herbal_Tea_Tasks.GoGoGoji(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.GoGoGojiDescription(upstream_tasks=[goGoGoji])
    iLovetoMoveIt = Herbal_Tea_Tasks.ILovetoMoveIt(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.ILovetoMoveItDescription(upstream_tasks=[iLovetoMoveIt])
    jamaicanGingerSorrel = Herbal_Tea_Tasks.JamaicanGingerSorrel(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.JamaicanGingerSorrelDescription(upstream_tasks=[jamaicanGingerSorrel])
    kwanYinCompassion = Herbal_Tea_Tasks.KwanYinCompassion(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.KwanYinCompassionDescription(upstream_tasks=[kwanYinCompassion])
    myLastGoodNerve = Herbal_Tea_Tasks.MyLastGoodNerve(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.MyLastGoodNerveDescription(upstream_tasks=[myLastGoodNerve])
    oshunsKiss = Herbal_Tea_Tasks.OshunsKiss(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.OshunsKissDescription(upstream_tasks=[oshunsKiss])
    rescueMeAllergyColdFluSupport = Herbal_Tea_Tasks.RescueMeAllergyColdFluSupport(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.RescueMeAllergyColdFluSupportDescription(upstream_tasks=[rescueMeAllergyColdFluSupport])
    rootChakraTea = Herbal_Tea_Tasks.RootChakraTea(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.RootChakraTeaDescription(upstream_tasks=[rootChakraTea])
    simplyIrresistible = Herbal_Tea_Tasks.SimplyIrresistible(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.SimplyIrresistibleDescription(upstream_tasks=[simplyIrresistible])
    tEATOXTEA = Herbal_Tea_Tasks.TEATOXTEA(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.TEATOXTEADescription(upstream_tasks=[tEATOXTEA])
    sweetDreamsAreMadeofTeas = Herbal_Tea_Tasks.SweetDreamsAreMadeofTeas(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.SweetDreamsAreMadeofTeasDescription(upstream_tasks=[sweetDreamsAreMadeofTeas])
    heartChakra = Herbal_Tea_Tasks.HeartChakra(upstream_tasks=[herbal_tea_result])
    Herbal_Tea_Tasks.HeartChakraDescription(upstream_tasks=[heartChakra])
    # End Herbal Teas

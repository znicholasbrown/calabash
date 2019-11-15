from prefect import task

@task
def AllGreenTeas():
    print("List of Green Teas")
    Genmaicha()
    Fridalicious()
    JasmineRose()
    RaspberryBeret()
    RockinMoroccan()
    TempleofHeavenGunpowderGreenTea()
    KashmiriGingerSpice()
    ChunMeiGreenTea()


@task
def Genmaicha():
    print("Genmaicha")
    GenmaichaDescription()

@task
def GenmaichaDescription():
    print("Green, tea, mixed, with, roasted, popped, brown, rice.")

@task
def Fridalicious():
    print("Frida-licious")
    FridaliciousDescription()

@task
def FridaliciousDescription():
    print("The iconic Mexican painter Frida Kahlo was also an amazing chef who enjoyed hosting fiery dinner parties. In a tea as complex and spicy as the artist, we crafted Frida-Luscious to honor her flamboyance-- through accents of tropical fruit, warm cinnamon, and tangy hibiscus. ")

@task
def JasmineRose():
    print("Jasmine Rose")
    JasmineRoseDescription()

@task
def JasmineRoseDescription():
    print("Green, tea, mixed, with, roasted, popped, brown, rice.")

@task
def RaspberryBeret():
    print("Raspberry Beret")
    RaspberryBeretDescription()

@task
def RaspberryBeretDescription():
    print("Our liquid love letter to His Purple Royalness features high-grade, handrolled Chunmei green tea and real raspberries for tartness. ")

@task
def RockinMoroccan():
    print("Rockin' Moroccan")
    RockinMoroccanDescription()

@task
def RockinMoroccanDescription():
    print("Amazing hot or over ice!")

@task
def TempleofHeavenGunpowderGreenTea():
    print("Temple of Heaven Gunpowder Green Tea")
    TempleofHeavenGunpowderGreenTeaDescription()

@task
def TempleofHeavenGunpowderGreenTeaDescription():
    print("This very traditional tea is named for the finely-crafted tiny hand-rolled young tea leaves. Each leaf is tightly twisted into a small bullet like shape. Mouthfeel: Green yet earthy and grounded.")

@task
def KashmiriGingerSpice():
    print("Kashmiri Ginger Spice")
    KashmiriGingerSpiceDescription()

@task
def KashmiriGingerSpiceDescription():
    print("Ingredients: chun mei, chai and spices")

@task
def ChunMeiGreenTea():
    print("Chun Mei Green Tea")
    ChunMeiGreenTeaDescription()

@task
def ChunMeiGreenTeaDescription():
    print("First-pluck, hand-twisted Chinese green tea")


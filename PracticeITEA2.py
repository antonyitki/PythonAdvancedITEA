#1.
class Auto:
    def __init__(self, color, kreslo, motor, maximspeed):
        self.color = color
        self.kreslo = kreslo
        self.motor = motor
        self.maximspeed = maximspeed
        self.__minimspeed = 0


class Light(Auto):
    def __init__(self, color, kreslo, motor, maximspeed,  vaditel, cab):
        super().__init__(color, kreslo, motor, maximspeed)
        self.vaditel = vaditel
        self. cab = cab

    def show_car(self):
        print(self.color, " ", self.kreslo, " ", self.motor, self.maximspeed,
              " ", self.vaditel, " ", self.cab)


class Heavy(Auto):
    def __init__(self, color, kreslo, motor, maximspeed, kilos):
        super().__init__(color, kreslo, motor, maximspeed)
        self.kilos = kilos
        self.kalisov = 16

    def otdijat_rabota(self, peririva):
        self.peririva = peririva
        return (f'Kamas otdijaet {self.peririva} minut')



vw = Light("white", 5, 1900, 250, "man", "no")
bmw = Light("black", 4, 3000, 360, "man", "no")
kamas = Heavy("orange", 3, 2000, 70, 300000000)
vijadnoi = kamas.otdijat_rabota(100.55)
print(vw.show_car())
bww1 = bmw.show_car()
print(vijadnoi)
#-----------------------------------------------------------------------------------------

#2.
class Magasini:
    def __init__(self, name_magasin, total_sales):
        self.name_magasin = name_magasin
        self.total_sales = total_sales

    def t_sold(self, item, items, million_items):
        item += 1
        items += 10
        million_items += 1000000
        t = self.total_sales = item + items + million_items
        return t



novus1 = Magasini("Novus_Leviybereg", 0, 6, 45)
novus55 = Magasini("Novus Obolon", 300300, 5, 3)


#TOXKI-----------------------------------------------------------------------------
class Toxki:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def change_x(self):
        pass
    def change_y(self):
        pass
    def change_z(self):
        pass
    def information_coord(self,newx, newy, newz):
        self.newx =
        self.newy =
        self.newz =






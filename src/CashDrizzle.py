from pathlib import Path
from random import randint, choice
import pygame

from player import Pelaaja
from coin import Kolikko
from monster import Hirvio

class RahasadeV2:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RahasadeV2")
        self.leveys = 640
        self.korkeus = 480
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        self.kello = pygame.time.Clock()

        graphics_path = Path(__file__).parents[1] / "graphics"
        font_file = graphics_path / "PressStart2P-vaV7.ttf"
        self.pelaaja = pygame.sprite.GroupSingle()
        self.pelaaja.add(Pelaaja(self.leveys, self.korkeus))
        self.kolikot = pygame.sprite.Group()
        self.hirviot = pygame.sprite.Group()
        self.fontti = pygame.font.Font(font_file, 30)
        self.pieni_fontti = pygame.font.Font(font_file, 13)
        self.peli_paalla = False
        self.alkuvalikko = True
        self.pisteet = 0
        self.sky = pygame.image.load(graphics_path / "sky.png")
        self.sky = pygame.transform.scale(self.sky, (640,int(100*6.4)))
        self.ground = pygame.image.load(graphics_path / "ground.png")
        self.ground = pygame.transform.scale(self.ground, (640,int(15*6.4)))
        self.silmukka()

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()

            if self.alkuvalikko:
                self.piirra_alkuvalikko()
                self.valitse()
            elif self.peli_paalla:
                self.lisaa_kolikko()
                self.lisaa_hirvio()
                self.pelaaja.update()
                self.kolikot.update()
                self.hirviot.update()
                if self.tormaa(self.kolikot):
                    self.pisteet += 1
                if self.tormaa(self.hirviot):
                    self.peli_paalla = False
                self.piirra_naytto()
            else:
                self.piirra_valikko()
                self.valitse()
            self.kello.tick(60)

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
    
    def lisaa_kolikko(self):
        if randint(1,100) < 3:
            self.kolikot.add(Kolikko(self.leveys, self.korkeus, 5))

    def lisaa_hirvio(self):
        if randint(1,1000) < 5:
            self.hirviot.add(Hirvio(self.leveys, self.korkeus, 5))

    def tormaa(self, group):
        if pygame.sprite.spritecollide(self.pelaaja.sprite, group, True, 
                pygame.sprite.collide_mask):
            return True
        else:
            return False

    def piirra_naytto(self):
        self.naytto.blit(self.sky, (0,0))
        self.naytto.blit(self.ground, (0,self.korkeus-self.ground.get_height()))
        self.pelaaja.draw(self.naytto)
        self.kolikot.draw(self.naytto)
        self.hirviot.draw(self.naytto)
        pisteet = self.pieni_fontti.render(f"Pisteet: {self.pisteet}", True, (0, 0, 240))
        self.naytto.blit(pisteet, (self.leveys - 180, 10))
        pygame.display.flip()

    def piirra_alkuvalikko(self):
        self.naytto.fill((0, 0, 0))
        otsikko = self.fontti.render("RahasadeV2", True, (255, 0, 180))
        kuvaus = "Kerää kolikkoja ja väistele hirviöitä."
        ohje = ["Komennot:","Liiku vasemmalle = vasen nuolinäppäin",
                "Liiku oikealle = oikea nuolinäppäin", "Hyppää = välilyönti"]
        self.naytto.blit(otsikko, ((self.leveys - otsikko.get_width())/2, 50))
        kuvausteksti = self.pieni_fontti.render(kuvaus, True, (255, 0, 180))
        self.naytto.blit(kuvausteksti, (100, 150))
        for i, rivi in enumerate(ohje):
            riviteksti = self.pieni_fontti.render(rivi, True, (255, 0, 180))
            self.naytto.blit(riviteksti, (100, 200+24*i))
        aloita = self.pieni_fontti.render("Aloita painamalla enter!", True, (255, 0, 180))
        self.naytto.blit(aloita, ((self.leveys - aloita.get_width())/2, 400))
        pygame.display.flip()
    
    def piirra_valikko(self):
        self.naytto.fill((0, 0, 0))
        pisteet = self.fontti.render(f"Pisteesi: {self.pisteet}", True, (255, 0, 180))
        uusi_peli = self.pieni_fontti.render("Aloita uusi peli painamalla enter!", True, (255, 0, 180))
        self.naytto.blit(pisteet, ((self.leveys - pisteet.get_width())/2, 100))
        self.naytto.blit(uusi_peli, ((self.leveys - uusi_peli.get_width())/2, 200))
        pygame.display.flip()

    def valitse(self):
        napit = pygame.key.get_pressed()
        if napit[pygame.K_RETURN]:
            self.peli_paalla = True
            self.alkuvalikko = False
            self.pisteet = 0
            self.kolikot.empty()
            self.hirviot.empty()
            self.pelaaja.empty()
            self.pelaaja.add(Pelaaja(self.leveys, self.korkeus))

if __name__ == "__main__":
    RahasadeV2()

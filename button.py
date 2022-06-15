
import pygame

# setez valorile pentru culorile pe care le folosesc
RED = (255, 0, 0)       #pentru a ilustra o piesa rege
CREAM = (248, 226, 177)     #piesa si patratel
BLACK = (0, 0, 0)       #piesa si patratel
WHITE = (255, 255, 255)      #pentru a ilustra user ului posibilele mutari     #pentru a putea distinge piesele negre pe patratele negre


class Button:
    def __init__(
            self,
            display=None,
            left=0,
            top=0,
            w=0,
            h=0,
            culoareFundal= CREAM,
            culoareFundalSel= RED,
            text="",
            font="arial",
            fontDimensiune=16,
            culoareText= BLACK,
            valoare="",
    ):
        self.display = display
        self.culoareFundal = culoareFundal
        self.culoareFundalSel = culoareFundalSel
        self.text = text
        self.font = font
        self.w = w
        self.h = h
        self.selectat = False
        self.fontDimensiune = fontDimensiune
        self.culoareText = culoareText
        fontObj = pygame.font.SysFont(self.font, self.fontDimensiune)
        self.textRandat = fontObj.render(self.text, True, self.culoareText)
        self.dreptunghi = pygame.Rect(left, top, w, h)
        self.dreptunghiText = self.textRandat.get_rect(center=self.dreptunghi.center)
        self.valoare = valoare

    def selecteaza(self, sel):
        self.selectat = sel
        self.deseneaza()

    def selecteazaDupacoord(self, coord):
        if self.dreptunghi.collidepoint(coord):
            self.selecteaza(True)
            return True
        return False

    def updateDreptunghi(self):
        self.dreptunghi.left = self.left
        self.dreptunghi.top = self.top
        self.dreptunghiText = self.textRandat.get_rect(center=self.dreptunghi.center)

    def deseneaza(self):
        culoareF = self.culoareFundalSel if self.selectat else self.culoareFundal
        pygame.draw.rect(self.display, culoareF, self.dreptunghi)
        self.display.blit(self.textRandat, self.dreptunghiText)

import main
import pygame
class Button:
    def __init__(
            self,
            display=None,
            left=0,
            top=0,
            w=0,
            h=0,
            culoareFundal=main.CREAM,
            culoareFundalSel=main.RED,
            text="",
            font="arial",
            fontDimensiune=16,
            culoareText= main.BLACK,
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
class Car:
    def __init__(self, marke, modell, ar):
        self.marke = marke
        self.modell = modell
        self.ar = ar
        self.igang = False

    def start(self):
        if not self.igang:
            self.igang = True
            print(f"{self.marke} {self.modell} startar.")
        else:
            print(f"{self.marke} {self.modell} är redan igång.")

    def stopp(self):
        if self.igang:
            self.igang = False
            print(f"{self.marke} {self.modell} stängs av.")
        else:
            print(f"{self.marke} {self.modell} är avstängd.")

    def visa_info(self):
        print(f"Bil: {self.ar} {self.marke} {self.modell}")
        if self.igang:
            print("Status: På")
        else:
            print("Status: Av")

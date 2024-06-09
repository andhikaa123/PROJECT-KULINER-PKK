class Motor:
    def _init_(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 5

    def keterangan(self):
        print(f"Motor baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer} kilometer")

motor_baru = Motor('ZX25R', 'Kawasaki', 2020)
motor_baru.keterangan()
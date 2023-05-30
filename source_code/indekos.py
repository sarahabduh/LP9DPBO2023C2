from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, daya_listrik):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.daya_listrik = daya_listrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_daya_listrik(self):
        return self.daya_listrik

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + self.nama_penghuni + "\nDaya Listrik : " + str(self.daya_listrik) + "VA\n"
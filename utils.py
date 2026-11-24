# utils.py - Fungsi aman, dipakai semua cabang biar tidak ngulang kode
def cek_bagi_nol(pembagi):
    """Return True kalau pembagi = 0, artinya tidak boleh dibagi."""
    return pembagi == 0

def format_angka(angka):
    """Format angka biar rapi, hilangkan .0 kalau bilangan bulat."""
    if angka == int(angka):
        return int(angka)
    return round(angka, 4)
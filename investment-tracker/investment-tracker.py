class Investment:
    def __init__(self, Inv_accname, Inv_num, Inv_val, Cur_val, Adm_char):
        self.accname = Inv_accname
        self.num = Inv_num
        self.val = Inv_val
        self.Cval = Cur_val
        self.Char = Adm_char
        self.prof = 0

    def calculate_profit(self):
        self.prof = (self.Cval - self.val) - self.Char


class HouseInvestment(Investment):
    def __init__(self, Inv_accname, Inv_num, Inv_val, Cur_val, Adm_char, Inv_dur):
        super().__init__(Inv_accname, Inv_num, Inv_val, Cur_val, Adm_char)
        self.Dur = Inv_dur

    def calculate_percent_profit(self):
        return (self.prof / self.val) * 100


House = HouseInvestment("Mide Reality Fund", "INV-001", 50000, 720000, 15000, 5)
House.calculate_profit()
percent_profit = House.calculate_percent_profit()

print(f"Account Name:        {House.accname}")
print(f"Investment Number:   {House.num}")
print(f"Initial Value:       ${House.val:,.2f}")
print(f"Investment Duration: {House.Dur} years")
print(f"Current Value:       ${House.Cval:,.2f}")
print(f"Profit:              ${House.prof:,.2f}")
print(f"Percentage Profit:   {percent_profit:.2f}%")

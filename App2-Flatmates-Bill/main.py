class Bill:
    """
    Object that contains details regarding Bill
    """

    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period

    
class Flatmate:
    """
    Object that contains details regarding flatmates
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        return (self.days_in_house / (self.days_in_house + flatmate2.days_in_house)) * bill.amount
        


class PdfReport:
    """
    Object that contains details regarding PDF Generated
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generatePdf(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(120, "March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))
# print(john.pays(bill=the_bill, flatmate2=marry) + marry.pays(bill=the_bill, flatmate2=john))
from fpdf import FPDF

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

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image icon
        pdf.image("App2-Flatmates-Bill/assets/house.png", w=30, h=30)
        

        # Title
        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        # Insert Period Label and Value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert Name and due amount of first FLatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert Name and due amount of second FLatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output('App2-Flatmates-Bill/assets/' + str(self.filename))

# App2-Flatmates-Bill/assets/bill.pdf

the_bill = Bill(120, "March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))
# print(john.pays(bill=the_bill, flatmate2=marry) + marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport("Report.pdf")
pdf_report.generatePdf(john, marry, the_bill)
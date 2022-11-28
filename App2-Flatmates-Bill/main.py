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

    def pays(self, bill):
        pass


class PdfReport:
    """
    Object that contains details regarding PDF Generated
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generatePdf(self, flatmate1, flatmate2, bill):
        pass
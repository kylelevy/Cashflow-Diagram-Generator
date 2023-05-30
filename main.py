import matplotlib.pyplot as plt

class CFDiagram():
    def __init__(self, cashflow):
        self.cashflow = cashflow

    def show(self):
        plt.title("Cash Flow Diagram")
        plt.ylabel("Cashflow in $")
        plt.xlabel("Time periods (n)")
        plt.stem(self.cashflow)
        for x,y in enumerate(self.cashflow):

            label = "${:.2f}".format(y)

            plt.annotate(label, 
                        (x,y), 
                        textcoords="offset points", 
                        xytext=(0,10), 
                        ha='center')
        plt.show()
        
if __name__ == '__main__':
    
    # Create cashflow as an array of cashflows for each period starting at n=0
    cashflow = [7600,200,200,200,200,-10000]

    # Creates an instance of a cashflow and displays it in a seperate window
    Q1 = CFDiagram(cashflow)
    Q1.show()
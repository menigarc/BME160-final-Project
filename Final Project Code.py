import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

'''plots a michaelis-Menten plot'''
def Michaelis_Menten(data):
    fig, ax1 = plt.subplots()
    #defining all lists of axis
    mentenx = []
    menteny1 = []
    menteny2 = []
    #iterating through the rows and getting the values in each column of that row
    for _, row in data.iterrows():
        mentenx.append(row.iloc[0])
        menteny1.append(row.iloc[1])
        menteny2.append(row.iloc[2])

    #plotting the graph and labeling it
    ax1.scatter(mentenx, menteny1, color = "blue", s =20, label = "CycA RbC WT" )
    ax1.scatter(mentenx, menteny2, color = "red", s =20, label = "CycA Rbc mutant")
    ax1.set_xlabel('FoxM1 (uM)')
    ax1.set_ylabel('Rate (micromolar/min')
    ax1.set_title('Michaelis-Menten Plot')
    ax1.legend()
    plt.show()

'''plots a lineweaver_burke plot using the same logic as the other graph'''
def LineWeaver_Burke(data):
    fig, ax2 = plt.subplots()
    weaverx = []
    weavery1 = []
    weavery2 = []
    for _, row in data.iterrows():
        weaverx.append(1/row.iloc[0])
        weavery1.append(1/row.iloc[1])
        weavery2.append(1/row.iloc[2])

    ax2.scatter(weaverx, weavery1, color="blue", s=20, label="CycA RbC WT")
    ax2.scatter(weaverx, weavery2, color="red", s=20, label="CycA Rbc mutant")
    ax2.set_xlabel('1/FoxM1 (uM)')
    ax2.set_ylabel('1/V0')
    ax2.set_title('LineWeaver-Burke Plot')
    ax2.legend()
    plt.show()

def main():
    #gets the exel file with the data you want to use
    file_path = "Input for Enzyme Kinematics Plotter.xlsx"
    data = pd.read_excel(file_path)
    print(data.head())
    #asks user which graph they want to plot and plots it
    menten = input("Do you want to plot a Michaelis Menten Plot? (y/n): ")
    if menten == "y":
        Michaelis_Menten(data)
    weaver = input("Do you want to plot a LineWeaver-Burke Plot? (y/n): ")
    if weaver == "y":
        LineWeaver_Burke(data)

if __name__ == "__main__":
    main()
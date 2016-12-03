# Sonosite PSU Fixture
from Tkinter import *
import ttk
root=Tk()

result_row = 10
high_volt_row = 40

RAILS = ['5P0_VA', '3P3_VA', '1P8_VA', '1P8_VD', '1P2_VD', '3P3_VD', '5P0_VD','12P0_VD',
            '12P0_VSHIF', '10P0_VSHIF','3P3_VSHIF', '5N0_VA','VTXP','VTXP_BIAS','VTXN','VTXN_BIAS']

#-------------------------------------------------------------
# secton for power enable and monitor to PSU
#-------------------------------------------------------------
w=Label(root, justify=RIGHT, padx=10,text="Vin").grid(row=1, column=0, sticky=E)
vin = Entry(root, width=10)
vin.grid(row=1, column=1, sticky=W)

psu_pwr =IntVar()
w=Checkbutton(root, variable=psu_pwr, text="PSU POWER").grid(row=1, column=2)
psu_pwr_sw =IntVar()
w=Checkbutton(root, variable=psu_pwr_sw, text="PSU POWER SW", state=DISABLED).grid(row=1, column=3)

w=Label(root, justify=RIGHT, padx=10,text="-----------").grid(row=2, column=0, sticky=E)

w=Label(root, justify=LEFT, text="Curr").grid(row=3,column=1)
w=Label(root, justify=LEFT, text="Power").grid(row=3,column=2)

w=Label(root, justify=RIGHT, padx=10,text="Digital").grid(row=4, column=0, sticky=E)
dig_curr = Entry(root, width=10)
dig_pwr = Entry(root, width=10)
dig_curr.grid(row=4, column=1, sticky=W)
dig_pwr.grid(row=4, column=2, sticky=W)

w=Label(root, justify=RIGHT, padx=10,text="Analog").grid(row=5, column=0, sticky=E)
ana_curr = Entry(root, width=10)
ana_pwr = Entry(root, width=10)
ana_curr.grid(row=5, column=1, sticky=W)
ana_pwr.grid(row=5, column=2, sticky=W)

#w=Label(root, justify=LEFT, padx=10,text="----------------").grid(row=4, column=0)
ttk.Separator(root,orient=HORIZONTAL).grid(row=6, columnspan=7,sticky="ew")

#-------------------------------------------------------------
# Section for Load Monitor and Control
#-------------------------------------------------------------
# Column 0: Labels
w=Label(root, justify=LEFT, padx=10,text="RAIL").grid(row=result_row, column=0)
count_row=0
for count_col in RAILS:
    Label(text=count_col, relief=RAISED, width=10).grid(row=result_row + 1 + count_row, column=0)
    count_row = count_row + 1

#Column 1: Voltage Measurement Results
w=Label(root, justify=LEFT, padx=10,text="Volt", width=10).grid(row=result_row, column=1)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+1, column=1)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+2, column=1)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+3, column=1)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+4, column=1)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+5, column=1)


#Column 2: Current Measurements
w=Label(root, justify=LEFT, padx=10,text="Curr").grid(row=result_row, column=2)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+1, column=2)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+2, column=2)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+3, column=2)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+4, column=2)
w=Label(root, justify=LEFT, padx=10,text="0.0", width=10, relief=RAISED).grid(row=result_row+5, column=2)


#Colum 3: Load A
w=Label(root, justify=CENTER, padx=10,text="LOAD_A").grid(row=result_row, column=3,columnspan=1)
load_a1 = IntVar()
load_a2 = IntVar()
w=Checkbutton(root, variable=load_a1).grid(row=result_row+1, column=3)
w=Checkbutton(root, variable=load_a2).grid(row=result_row+2, column=3)

#Column 4: Load B
w=Label(root, justify=LEFT, padx=10,text="LOAD_B").grid(row=result_row, column=4)
load_b1 = IntVar()
load_b2 = IntVar()
w=Checkbutton(root, variable=load_b1).grid(row=result_row+1, column=4)
w=Checkbutton(root, variable=load_b2).grid(row=result_row+2, column=4)




#Column 5: Manual button column a
w=Label(root, justify=LEFT, padx=10,text="MAN_A").grid(row=result_row, column=5)
man_a1 = IntVar()
man_a2 = IntVar()
#man_a1.set(1)
#man_a2.set(1)
w=Checkbutton(root, variable=man_a1, state=DISABLED).grid(row=result_row+1, column=5)
w=Checkbutton(root, variable=man_a2, state=DISABLED).grid(row=result_row+2, column=5)


# Manual button column b
w=Label(root, justify=LEFT, padx=10,text="MAN_B").grid(row=result_row, column=6)
man_b1 = IntVar()
man_b2 = IntVar()
w=Checkbutton(root, variable=man_b1, state=DISABLED, ).grid(row=result_row+1, column=6)
w=Checkbutton(root, variable=man_b2, state=DISABLED, ).grid(row=result_row+2, column=6)

#w=Label(root, justify=LEFT, padx=10,text="----------------").grid(row=4, column=0)
ttk.Separator(root,orient=HORIZONTAL).grid(row=result_row+18, columnspan=7,sticky="ew")


#-------------------------------------------------------------
# secton for High-Voltage Monitor and control
#-------------------------------------------------------------
w=Label(root, justify=RIGHT, padx=10,text="TXP Iset").grid(row=high_volt_row, column=0, sticky=E)
txp_iset = Entry(root, width=10)
txp_iset.grid(row=high_volt_row, column=1, sticky=W)
w=Label(root, justify=RIGHT, padx=10,text="TXP Imon").grid(row=high_volt_row, column=2, sticky=E)
txp_imon = Entry(root, width=10)
txp_imon.grid(row=high_volt_row, column=3, sticky=W)

w=Label(root, justify=RIGHT, padx=10,text="TXN Iset").grid(row=high_volt_row+1, column=0, sticky=E)
txp_iset = Entry(root, width=10)
txp_iset.grid(row=high_volt_row+1, column=1, sticky=W)
w=Label(root, justify=RIGHT, padx=10,text="TXN Imon").grid(row=high_volt_row+1, column=2, sticky=E)
txp_imon = Entry(root, width=10)
txp_imon.grid(row=high_volt_row+1, column=3, sticky=W)


# scan head disconnect section
sh_dsc0 = IntVar()
w=Checkbutton(root, variable=sh_dsc0, state=DISABLED, text="SH_DSC0").grid(row=high_volt_row+2, column=0)

sh_dsc_man0 = IntVar()
w=Checkbutton(root, variable=sh_dsc_man0, state=DISABLED, text="SH_MAN0").grid(row=high_volt_row+2, column=1)


sh_dsc1 = IntVar()
w=Checkbutton(root, variable=sh_dsc1, state=DISABLED, text="SH_DSC1").grid(row=high_volt_row+3, column=0)

sh_dsc_man1 = IntVar()
w=Checkbutton(root, variable=sh_dsc_man1, state=DISABLED, text="SH_MAN1").grid(row=high_volt_row+3, column=1)

# Alternate Bias Load
vtxp_bis_load= IntVar()
w=Checkbutton(root, variable=vtxp_bis_load, text="VTXP_Bias Load").grid(row=high_volt_row+4,
                                                                        column=0, columnspan=1)

vtxp_bis_load= IntVar()
w=Checkbutton(root, variable=vtxp_bis_load, text="VTX_Bias Load").grid(row=high_volt_row+4,
                                                                       column=2, columnspan=1)


mainloop()

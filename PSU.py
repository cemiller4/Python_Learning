# Sonosite PSU Fixture
from Tkinter import *
import ttk
root=Tk()
root.wm_title("Phoenix PSU Control")

misc_row=0
result_row = 10


RAILS = ['Vin', '5P0_VD','12P0_VD', '5P0_VA', '3P3_VA', '5N0_VA', 'TRIPLE', '1P8_VA',
         '1P8_VD', '1P2_VD', '3P3_VD', '3P3_VSHIF', '10P0_SW', '10P0_VSHIF',
         '12P0_VSHIF', 'VTXP', 'VTXN', 'BIAS', 'VTXP_BIAS', 'VTXN_BIAS']

# PCA Part Number Reading
w=Label(root, justify=RIGHT, padx=10,text="PCA P/N").grid(row=misc_row, column=1, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=misc_row,
            columnspan=2, column=2, sticky=W)

# Hardware ID Reading
w=Label(root, justify=LEFT, padx=10,text="HW ID").grid(row=misc_row+1, column=1, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=misc_row+1,
            columnspan=2, column=2, sticky=W)

# PCB Temperature
w=Label(root, justify=LEFT, padx=10,text="PCB Temp").grid(row=misc_row+2, column=1, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=misc_row+2,
            columnspan=2, column=2, sticky=W)

# Digital Readings
sh_dsc = IntVar()
w=Checkbutton(root, variable=sh_dsc, selectcolor="#FFF", text="PWR_BTNn").grid(row=misc_row,
                                        column=4, columnspan=2, sticky=W)
w=Checkbutton(root, variable=sh_dsc, selectcolor="#FFF", text="SH_DSC").grid(row=misc_row+1,
                                        column=4, columnspan=2, sticky=W)
w=Checkbutton(root, variable=sh_dsc, selectcolor="#FFF", text="HVT_GATE").grid(row=misc_row+2,
                                        column=4, columnspan=2, sticky=W)


# Digital Outputs
ps_ready = IntVar()
w=Checkbutton(root, variable=ps_ready, selectcolor="#FFF", text="PWR_BTN_DBn").grid(row=misc_row,
                                        column=6, columnspan=2, sticky=W)
w=Checkbutton(root, variable=ps_ready, selectcolor="#FFF", text="PS_READY").grid(row=misc_row+1,
                                        column=6, columnspan=2, sticky=W)


#-------------------------------------------------------------
# Section for Load Monitor and Control
#-------------------------------------------------------------
# Column 0: Labels
ttk.Separator(root,orient=HORIZONTAL).grid(row=result_row-1, columnspan=8,sticky="ew")
w=Label(root, justify=LEFT, text="#").grid(row=result_row, column=0)
w=Label(root, justify=LEFT, padx=10,text="RAIL").grid(row=result_row, column=1)
count_row=0
for count_col in RAILS:
    Label(text=count_row+1, width=3).grid(row=result_row + 1 + count_row, column=0)
    Label(text=count_col, width=10).grid(row=result_row + 1 + count_row, column=1)
    count_row = count_row + 1

#Colum 2: Enables
w=Label(root, justify=CENTER, padx=10,text="EN").grid(row=result_row, column=2)
load_a1 = IntVar()
load_a2 = IntVar()
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+1, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+2, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+3, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+4, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+5, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+6, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+7, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+8, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+9, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+10, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+11, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+12, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+13, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+14, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+15, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+16, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+17, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#FF0").grid(row=result_row+18, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+19, column=2)
w=Checkbutton(root, variable=load_a1, selectcolor="#DDD").grid(row=result_row+20, column=2)

#Column 3: Power Good
w=Label(root, justify=LEFT, padx=10,text="PG").grid(row=result_row, column=3)
load_b1 = IntVar()
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+1, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+2, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+3, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+4, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+5, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+6, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+7, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+8, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+9, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+10, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+11, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+12, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+13, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+14, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+15, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+16, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+17, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+18, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+19, column=3)
w=Checkbutton(root, variable=load_b1, selectcolor="#FFF").grid(row=result_row+20, column=3)

#Column 4: Sync Enable
w=Label(root, justify=LEFT, padx=10,text="SYNC").grid(row=result_row, column=4)
load_b1 = IntVar()
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+1, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+2, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+3, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+4, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+5, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+6, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+7, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+8, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+9, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+10, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+11, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+12, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+13, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+14, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+15, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+16, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+17, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#FF0").grid(row=result_row+18, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+19, column=4)
w=Checkbutton(root, variable=load_b1, selectcolor="#DDD").grid(row=result_row+20, column=4)

#Column 5: SYNC Frequency
w=Label(root, justify=RIGHT,text="FREQ").grid(row=result_row, column=5)
sync_freq1 = Entry(root, width=8, bg="#FF0")
sync_freq2 = Entry(root, width=8, bg="#FF0")
sync_freq3 = Entry(root, width=8, bg="#FF0")
sync_freq4 = Entry(root, width=8, bg="#FF0")
sync_freq5 = Entry(root, width=8, bg="#FF0")
sync_freq6 = Entry(root, width=8, bg="#FF0")
sync_freq7 = Entry(root, width=8, bg="#FF0")
sync_freq8 = Entry(root, width=8, bg="#FF0")
sync_freq9 = Entry(root, width=8, bg="#FF0")
sync_freq10 = Entry(root, width=8, bg="#FF0")
sync_freq11 = Entry(root, width=8, bg="#FF0")
sync_freq12 = Entry(root, width=8, bg="#FF0")
sync_freq13 = Entry(root, width=8, bg="#FF0")
sync_freq14 = Entry(root, width=8, bg="#FF0")
sync_freq15 = Entry(root, width=8, bg="#FF0")
sync_freq16 = Entry(root, width=8, bg="#FF0")
sync_freq17 = Entry(root, width=8, bg="#FF0")
sync_freq18 = Entry(root, width=8, bg="#FF0")
sync_freq19 = Entry(root, width=8, bg="#FF0")
sync_freq20 = Entry(root, width=8, bg="#FF0")
sync_freq21 = Entry(root, width=8, bg="#FF0")
sync_freq1.grid(row=result_row+1, column=5, sticky=W)
sync_freq2.grid(row=result_row+2, column=5, sticky=W)
sync_freq3.grid(row=result_row+3, column=5, sticky=W)
sync_freq4.grid(row=result_row+4, column=5, sticky=W)
sync_freq5.grid(row=result_row+5, column=5, sticky=W)
sync_freq6.grid(row=result_row+6, column=5, sticky=W)
sync_freq7.grid(row=result_row+7, column=5, sticky=W)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+8, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+9, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+10, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+11, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+12, column=5, sticky=E)
sync_freq15.grid(row=result_row+13, column=5, sticky=W)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+14, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+15, column=5, sticky=E)
sync_freq18.grid(row=result_row+16, column=5, sticky=W)
sync_freq19.grid(row=result_row+17, column=5, sticky=W)
sync_freq20.grid(row=result_row+18, column=5, sticky=W)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+19, column=5, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+20, column=5, sticky=E)

#Column 6: ADC Voltage Measurements
w=Label(root, justify=RIGHT,text="V_meas").grid(row=result_row, column=6)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+1, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+2, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+3, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+4, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+5, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+6, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+7, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+8, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+9, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+10, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+11, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+12, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+13, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+14, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+15, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+16, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+17, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+18, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+19, column=6, sticky=E)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+20, column=6, sticky=E)

#Column 7: ADC Current Measurements
w=Label(root, justify=RIGHT,text="I_meas").grid(row=result_row, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+1, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+2, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+3, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+4, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+5, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+6, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+7, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+8, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+9, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+10, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+11, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+12, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+13, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+14, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+15, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+16, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+17, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+18, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+19, column=7)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=result_row+20, column=7)



#-------------------------------------------------------------
# secton for High Voltage Control
#-------------------------------------------------------------
hv_row = 40

#w=Label(root, justify=LEFT, padx=10,text="----------------").grid(row=4, column=0)
ttk.Separator(root,orient=HORIZONTAL).grid(row=hv_row, columnspan=8,sticky="ew")

# TXP Control
w=Label(root, justify=LEFT, text="TXP State").grid(row=hv_row+1, column=0, columnspan=2)
w=Label(root, justify=LEFT, text="TXP Voltage").grid(row=hv_row+1, column=4, columnspan=2)
txp_state = IntVar()
txp_button = Radiobutton(root, text="OFF", variable=txp_state, value=0, selectcolor="#FF0")
txp_button.grid(row=hv_row+2, column=1, sticky=W)
txp_button = Radiobutton(root, text="ON", variable=txp_state, value=1, selectcolor="#FF0")
txp_button.grid(row=hv_row+3, column=1, sticky=W)
txp_button = Radiobutton(root, text="DISCHARGE", variable=txp_state, value=2, selectcolor="#FF0")
txp_button.grid(row=hv_row+4, column=1, sticky=W)

w = Scale(root, from_=0, to=80, orient=HORIZONTAL, tickinterval=10).grid(row=hv_row+2,column=2,
            columnspan=5, rowspan=3, sticky=EW)

# TXN Control
ttk.Separator(root,orient=HORIZONTAL).grid(row=hv_row+5, columnspan=8,sticky="ew")
w=Label(root, justify=LEFT, text="TXN State").grid(row=hv_row+6, column=0, columnspan=2)
w=Label(root, justify=LEFT, text="TXN Voltage").grid(row=hv_row+6, column=4, columnspan=2)
txn_state = IntVar()
txn_button = Radiobutton(root, text="OFF", variable=txn_state, value=0, selectcolor="#FF0")
txn_button.grid(row=hv_row+7, column=1, sticky=W)
txn_button = Radiobutton(root, text="ON", variable=txn_state, value=1, selectcolor="#FF0")
txn_button.grid(row=hv_row+8, column=1, sticky=W)
txn_button = Radiobutton(root, text="DISCHARGE", variable=txn_state, value=2, selectcolor="#FF0")
txn_button.grid(row=hv_row+9, column=1, sticky=W)

w = Scale(root, from_=0, to=80, orient=HORIZONTAL, tickinterval=10).grid(row=hv_row+7,column=2,
            columnspan=5, rowspan=3, sticky=EW)





#-------------------------------------------------------------
# secton for I/O communication with Power Path and Charger
#-------------------------------------------------------------
io_row = 60

ttk.Separator(root,orient=HORIZONTAL).grid(row=io_row-1, columnspan=8,sticky="ew")
# Power Path Column 1
w=Label(root, text="Power Path Ctrl").grid(row=io_row, column=1, columnspan=2, sticky=W)
pwr_path_en = IntVar()
w=Checkbutton(root, text="DISABLE", variable=pwr_path_en, selectcolor="#FF0").grid(row=io_row+1, column=1, sticky=W)
w=Checkbutton(root, text="SHUTDOWN", variable=pwr_path_en, selectcolor="#FF0").grid(row=io_row+2, column=1, sticky=W)

# Power Path Readings
w=Label(root, text="Power Path Mon").grid(row=io_row, column=3, columnspan=2, sticky=W)
pwr_path_en = IntVar()
w=Checkbutton(root, text="AC Power", variable=pwr_path_en, selectcolor="#FFF").grid(row=io_row+1,
                                                                    column=3, sticky=W, columnspan=2)
w=Checkbutton(root, text="Stand Battery", variable=pwr_path_en, selectcolor="#FFF").grid(row=io_row+2,
                                                    column=3, sticky=W, columnspan=2)
w=Checkbutton(root, text="System Battery", variable=pwr_path_en, selectcolor="#FFF").grid(row=io_row+3,
                                                    column=3, sticky=W, columnspan=2)

# Charger Control
w=Label(root, justify=LEFT, text="Charger Control").grid(row=io_row, column=6, columnspan=2, sticky=W)
charge_ctrl = IntVar()
charge_button = Radiobutton(root, text="DISABLE", variable=charge_ctrl, value=0, selectcolor="#FF0")
charge_button.grid(row=io_row+1, column=6, sticky=W)
charge_button = Radiobutton(root, text="STAND", variable=charge_ctrl, value=1, selectcolor="#FF0")
charge_button.grid(row=io_row+2, column=6, sticky=W)
charge_button = Radiobutton(root, text="SYSTEM", variable=charge_ctrl, value=2, selectcolor="#FF0")
charge_button.grid(row=io_row+3, column=6, sticky=W)

w=Label(root, justify=LEFT, text="Vmax").grid(row=io_row+4, column=7, sticky=W)
charge_volt = Entry(root, width=10, bg="#FF0")
charge_volt.grid(row=io_row+4, column=6, sticky=E)

w=Label(root, justify=LEFT, text="Imax").grid(row=io_row+5, column=7, sticky=W)
charge_curr = Entry(root, width=10, bg="#FF0")
charge_curr.grid(row=io_row+5, column=6, sticky=E)

#-------------------------------------------------------------
# Section for Battery Section
#-------------------------------------------------------------
# Column 0: Labels
w=Label(root, justify=LEFT, text="   ").grid(row=result_row, column=8)
w=Label(root, justify=LEFT, padx=10,text="BATTERY READINGS").grid(row=result_row, column=9, columnspan=3)

w=Label(text="PARAM", relief=RAISED, width=15).grid(row=result_row + 1, column=9)
w=Label(text="STAND", relief=RAISED, width=10).grid(row=result_row + 1, column=10)
w=Label(text="SYSTEM", relief=RAISED, width=10).grid(row=result_row + 1, column=11)

# Battery Serial Number
w=Label(text="S/N", width=15).grid(row=result_row + 2, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+2, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+2, column=11)


# Battery Voltage
w=Label(text="Voltage", width=15).grid(row=result_row + 3, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+3, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+3, column=11)

# Battery Current
w=Label(text="Current", width=15).grid(row=result_row + 4, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+4, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+4, column=11)

# Battery Temperature
w=Label(text="Temp", width=15).grid(row=result_row + 5, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+5, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+5, column=11)

# Battery Temperature
w=Label(text="Rem. Capacity", width=15).grid(row=result_row + 6, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+6, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+6, column=11)

# Battery Temperature
w=Label(text="Rem. Run Time", width=15).grid(row=result_row + 7, column=9)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+7, column=10)
w=Label(root, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=result_row+7, column=11)



mainloop()

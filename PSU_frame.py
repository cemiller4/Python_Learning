# Sonosite PSU Fixture
# Some documentation which may be needed to autogenerate buttons:  lambda i=i: self.open_this(i)
from Tkinter import *
import ttk
root=Tk()
root.wm_title("Phoenix PSU Control")



RAILS = ['Vin', '5P0_VD','12P0_VD', '5P0_VA', '3P3_VA', '5N0_VA', 'TRIPLE', '1P8_VA',
         '1P8_VD', '1P2_VD', '3P3_VD', '3P3_VSHIF', '10P0_SW', '10P0_VSHIF',
         '12P0_VSHIF', 'VTXP', 'VTXN', 'BIAS', 'VTXP_BIAS', 'VTXN_BIAS']

RAIL_LIST = (('Vin',        1, 0, 1, 1, 1, 0),
			 ('5P0_VD',     0, 1, 0, 1, 0, 0),
			 ('12P0_VD',    1, 1, 1, 1, 0, 0),
			 ('5P0_VA',     0, 1, 1, 1, 0, 0),
			 ('3P3_VA',     1, 1, 1, 1, 0, 0),
             ('5N0_VA',     1, 1, 1, 1, 0, 0),
             ('TRIPLE',     1, 1, 1, 1, 0, 0),
             ('1P8_VA',     1, 1, 1, 0, 0, 0),
             ('1P8_VD',     1, 1, 1, 0, 0, 0),
             ('1P2_VD',     1, 1, 0, 0, 0, 0),
             ('3P3_VD',     1, 1, 1, 0, 0, 0),
             ('3P3_VSHIF',  1, 1, 1, 0, 0, 0),
             ('10P0_SW',    1, 1, 1, 1, 0, 0),
             ('10P0_VSHIF', 1, 1, 1, 0, 0, 0),
             ('12P0_VSHIF', 1, 1, 1, 0, 0, 0),
             ('VTXP',       1, 1, 1, 1, 0, 0),
             ('VTXN',       1, 1, 1, 1, 0, 0),
             ('BIAS',       1, 1, 1, 1, 0, 0),
             ('VTXP_BIAS',  1, 0, 1, 0, 0, 0),
             ('VTXN_BIAS',  1, 0, 1, 0, 0, 0))

def enRail(index):
    print('EN ' + RAILS[index])
    var_obj = rail_val.get(index)
    print(var_obj.get())

def checkButtonOff(index):
    print('Turn off')

def pgRail(index):
    print('PG ' + RAILS[index])
    var_obj = pg_val.get(index)
    print(var_obj.get())

def pgButtonOff(index):
    print('Turn off')

def syncEnable(index):
    print('Sync ' + RAILS[index])
    var_obj = sync_en.get(index)
    print(var_obj.get())

def syncButtonOff(index):
    print('Turn off')


Frame_psu = Frame(root, bg="red")
Frame_rails = Frame(root, bg="blue")
Frame_hv = Frame(root, bg="green")
Frame_IO = Frame(root, bg="yellow")
Frame_bat = Frame(root, bg="purple")

Frame_psu.grid(row = 0, column = 0, sticky=W+E+N+S, columnspan=2)
Frame_rails.grid(row = 1, column = 0, sticky=W+E+N+S)
Frame_hv.grid(row = 2, column = 0, sticky=W+E+N+S)
Frame_IO.grid(row = 2, column = 1, sticky=W+E+N+S)
Frame_bat.grid(row = 1, column = 1, sticky=W+E+N+S)


# PCA Part Number Reading
w=Label(Frame_psu, justify=RIGHT, padx=10,text="PCA P/N").grid(row=0, column=1, sticky=E)
w=Label(Frame_psu, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=0,
            columnspan=2, column=2, sticky=W)

# Hardware ID Reading
w=Label(Frame_psu, justify=LEFT, padx=10,text="HW ID").grid(row=1, column=1, sticky=E)
w=Label(Frame_psu, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=1,
            columnspan=2, column=2, sticky=W)

# PCB Temperature
w=Label(Frame_psu, justify=LEFT, padx=10,text="PCB Temp").grid(row=2, column=1, sticky=E)
w=Label(Frame_psu, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=2,
            columnspan=2, column=2, sticky=W)

# Digital Readings
sh_dsc = IntVar()
w=Checkbutton(Frame_psu, variable=sh_dsc, selectcolor="#FFF", text="PWR_BTNn").grid(row=0,
                                        column=4, columnspan=2, sticky=W)
w=Checkbutton(Frame_psu, variable=sh_dsc, selectcolor="#FFF", text="SH_DSC").grid(row=1,
                                        column=4, columnspan=2, sticky=W)
w=Checkbutton(Frame_psu, variable=sh_dsc, selectcolor="#FFF", text="HVT_GATE").grid(row=2,
                                        column=4, columnspan=2, sticky=W)


# Digital Outputs
ps_ready = IntVar()
w=Checkbutton(Frame_psu, variable=ps_ready, selectcolor="#FFF", text="PWR_BTN_DBn").grid(row=0,
                                        column=6, columnspan=2, sticky=W)
w=Checkbutton(Frame_psu, variable=ps_ready, selectcolor="#FFF", text="PS_READY").grid(row=1,
                                        column=6, columnspan=2, sticky=W)


#-------------------------------------------------------------
# Section for Load Monitor and Control
#-------------------------------------------------------------
# Column 0: Labels
#ttk.Separator(root,orient=HORIZONTAL).grid(row=0-1, columnspan=8,sticky="ew")
w=Label(Frame_rails, justify=LEFT, text="#").grid(row=0, column=0)
w=Label(Frame_rails, justify=LEFT, padx=10,text="RAIL").grid(row=0, column=1)
count_row=0
#for count_col in RAILS:
#    Label(Frame_rails, text=count_row+1, width=3).grid(row=1 + count_row, column=0)
#    Label(Frame_rails, text=count_col, width=10).grid(row=1 + count_row, column=1)
#    count_row = count_row + 1

#ttp://stackoverflow.com/questions/24663661/tkinter-get-values-from-dynamic-checkboxes

#Colum 2: Enables
w=Label(Frame_rails, justify=CENTER, padx=10,text="EN").grid(row=0, column=2)

rail_val = dict()
pg_val = dict()
sync_en = dict()
for i in range(0, 20):
    # Column 0- Row Index
    Label(Frame_rails, text=count_row+1, width=3).grid(row=1 + count_row, column=0)

    #Column 1 - Rail names
    Label(Frame_rails, text=RAIL_LIST[i][0], width=10).grid(row=1 + count_row, column=1)

    #Column 2 - Enable signals
    rail_val[i] = IntVar()
    if RAIL_LIST[i][1] == 1:
        l = Checkbutton(Frame_rails, variable=rail_val[i], command=lambda i=i: enRail(i)).grid(row=i+1, column=2)
    else:
        l = Checkbutton(Frame_rails, variable=rail_val[i],
            selectcolor="#DDD", command=lambda i=i: checkButtonOff(i)).grid(row=i+1, column=2)

    # Generate Column 3 which are Power Good Checkbuttons
    pg_val[i] = IntVar()
    if RAIL_LIST[i][2] == 1:
        l = Checkbutton(Frame_rails, variable=pg_val[i], command=lambda i=i: pgRail(i)).grid(row=i+1, column=3)
    else:
        l = Checkbutton(Frame_rails, variable=pg_val[i],
            selectcolor="#DDD", command=lambda i=i: pgButtonOff(i)).grid(row=i+1, column=3)

    # Generate Column 4 which are Sync Enable Checkbuttons
    sync_en[i] = IntVar()
    if RAIL_LIST[i][3] == 1:
        l = Checkbutton(Frame_rails, variable=sync_en[i], command=lambda i=i: syncEnable(i)).grid(row=i+1, column=4)
    else:
        l = Checkbutton(Frame_rails, variable=sync_en[i],
            selectcolor="#DDD", command=lambda i=i: syncButtonOff(i)).grid(row=i+1, column=4)


    count_row = count_row + 1



#load_a1 = IntVar()
#load_a2 = IntVar()
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=enRail(0)).grid(row=1, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(1)).grid(row=2, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(2)).grid(row=3, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(3)).grid(row=4, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(4)).grid(row=5, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(5)).grid(row=6, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=lambda: enRail(6)).grid(row=7, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(7)).grid(row=8, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(8)).grid(row=9, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(9)).grid(row=10, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(10)).grid(row=11, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(11)).grid(row=12, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(12)).grid(row=13, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(13)).grid(row=14, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(14)).grid(row=15, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=lambda: enRail(15)).grid(row=16, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=lambda: enRail(16)).grid(row=17, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#FF0", command=lambda: enRail(17)).grid(row=18, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=lambda: enRail(18)).grid(row=19, column=2)
#w=Checkbutton(Frame_rails, variable=load_a1, selectcolor="#DDD", command=lambda: enRail(19)).grid(row=20, column=2)

#Column 3: Power Good
w=Label(Frame_rails, justify=LEFT, padx=10,text="PG").grid(row=0, column=3)
# load_b1 = IntVar()
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=1, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=2, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=3, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=4, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=5, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=6, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=7, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=8, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=9, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=10, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=11, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=12, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=13, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=14, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=15, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=16, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=17, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=18, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=19, column=3)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FFF").grid(row=20, column=3)

#Column 4: Sync Enable
w=Label(Frame_rails, justify=LEFT, padx=10,text="SYNC").grid(row=0, column=4)
# load_b1 = IntVar()
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=1, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=2, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=3, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=4, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=5, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=6, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=7, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=8, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=9, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=10, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=11, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=12, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=13, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=14, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=15, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=16, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=17, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#FF0").grid(row=18, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=19, column=4)
# w=Checkbutton(Frame_rails, variable=load_b1, selectcolor="#DDD").grid(row=20, column=4)

#Column 5: SYNC Frequency
w=Label(Frame_rails, justify=RIGHT,text="FREQ").grid(row=0, column=5)
sync_freq1 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq2 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq3 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq4 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq5 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq6 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq7 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq8 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq9 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq10 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq11 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq12 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq13 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq14 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq15 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq16 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq17 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq18 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq19 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq20 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq21 = Entry(Frame_rails, width=8, bg="#FF0")
sync_freq1.grid(row=1, column=5, sticky=W)
sync_freq2.grid(row=2, column=5, sticky=W)
sync_freq3.grid(row=3, column=5, sticky=W)
sync_freq4.grid(row=4, column=5, sticky=W)
sync_freq5.grid(row=5, column=5, sticky=W)
sync_freq6.grid(row=6, column=5, sticky=W)
sync_freq7.grid(row=7, column=5, sticky=W)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=8, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=9, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=10, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=11, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=12, column=5, sticky=E)
sync_freq15.grid(row=13, column=5, sticky=W)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=14, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=15, column=5, sticky=E)
sync_freq18.grid(row=16, column=5, sticky=W)
sync_freq19.grid(row=17, column=5, sticky=W)
sync_freq20.grid(row=18, column=5, sticky=W)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=19, column=5, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=20, column=5, sticky=E)

#Column 6: ADC Voltage Measurements
w=Label(Frame_rails, justify=RIGHT,text="V_meas").grid(row=0, column=6)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=1, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=2, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=3, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=4, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=5, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=6, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=7, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=8, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=9, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=10, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=11, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=12, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=13, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=14, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=15, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=16, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=17, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=18, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=19, column=6, sticky=E)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=20, column=6, sticky=E)

#Column 7: ADC Current Measurements
w=Label(Frame_rails, justify=RIGHT,text="I_meas").grid(row=0, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=1, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=2, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=3, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=4, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=5, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=6, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=7, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=8, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=9, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=10, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=11, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=12, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=13, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=14, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=15, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=16, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=17, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=18, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=19, column=7)
w=Label(Frame_rails, justify=RIGHT,width=8, relief=SUNKEN, bg="#DDD").grid(row=20, column=7)



#-------------------------------------------------------------
# secton for High Voltage Control
#-------------------------------------------------------------
#w=Label(root, justify=LEFT, padx=10,text="----------------").grid(row=4, column=0)
ttk.Separator(Frame_hv,orient=HORIZONTAL).grid(row=0, columnspan=8,sticky="ew")

# TXP Control
w=Label(Frame_hv, justify=LEFT, text="TXP State").grid(row=1, column=0, sticky=W)
txp_state = IntVar()
txp_button = Radiobutton(Frame_hv, text="OFF", variable=txp_state, value=0, selectcolor="#FF0")
txp_button.grid(row=2, column=0, sticky=W)
txp_button = Radiobutton(Frame_hv, text="ON", variable=txp_state, value=1, selectcolor="#FF0")
txp_button.grid(row=3, column=0, sticky=W)
txp_button = Radiobutton(Frame_hv, text="DISCHARGE", variable=txp_state, value=2, selectcolor="#FF0")
txp_button.grid(row=4, column=0, sticky=W)

w=Label(Frame_hv, justify=LEFT, text="TXP Voltage", width=10).grid(row=1, column=3, columnspan=2)
w = Scale(Frame_hv, from_=80, to=0, tickinterval=10, length=200).grid(row=2,column=3, rowspan=15, columnspan=2)

# TXN Control
ttk.Separator(Frame_hv,orient=HORIZONTAL).grid(row=5, columnspan=2,sticky="ew")
w=Label(Frame_hv, text="TXN State").grid(row=1, column=6, sticky=W)
w=Label(Frame_hv, justify=LEFT, text="TXN Voltage").grid(row=1, column=7, columnspan=2, sticky=W)
txn_state = IntVar()
txn_button = Radiobutton(Frame_hv, text="OFF", variable=txn_state, value=0, selectcolor="#FF0")
txn_button.grid(row=2, column=6, sticky=W)
txn_button = Radiobutton(Frame_hv, text="ON", variable=txn_state, value=1, selectcolor="#FF0")
txn_button.grid(row=3, column=6, sticky=W)
txn_button = Radiobutton(Frame_hv, text="DISCHARGE", variable=txn_state, value=2, selectcolor="#FF0")
txn_button.grid(row=4, column=6, sticky=W)

#w = Scale(Frame_hv, from_=0, to=80, orient=HORIZONTAL, tickinterval=10).grid(row=hv_row+7,column=2,
#            columnspan=5, rowspan=3, sticky=EW)
w = Scale(Frame_hv, from_=0, to=-80, tickinterval=10, length=200).grid(row=2,column=7, rowspan=12)





#-------------------------------------------------------------
# secton for I/O communication with Power Path and Charger
#-------------------------------------------------------------

#ttk.Separator(Frame_IO,orient=HORIZONTAL).grid(row=, columnspan=8,sticky="ew")
# Power Path Column 1
w=Label(Frame_IO, text="Power Path Ctrl").grid(row=0, column=0, columnspan=2, sticky=W)
pwr_path_en = IntVar()
w=Checkbutton(Frame_IO, text="DISABLE", variable=pwr_path_en, selectcolor="#FF0").grid(row=1, column=1, sticky=W)
w=Checkbutton(Frame_IO, text="SHUTDOWN", variable=pwr_path_en, selectcolor="#FF0").grid(row=2, column=1, sticky=W)

# Power Path Readings
w=Label(Frame_IO, text="Power Path Mon").grid(row=0, column=3, columnspan=2, sticky=W)
pwr_path_en = IntVar()
w=Checkbutton(Frame_IO, text="AC Power", variable=pwr_path_en, selectcolor="#FFF").grid(row=1,
                                                                    column=3, sticky=W, columnspan=2)
w=Checkbutton(Frame_IO, text="Stand Battery", variable=pwr_path_en, selectcolor="#FFF").grid(row=2,
                                                    column=3, sticky=W, columnspan=2)
w=Checkbutton(Frame_IO, text="System Battery", variable=pwr_path_en, selectcolor="#FFF").grid(row=3,
                                                    column=3, sticky=W, columnspan=2)

# Charger Control
w=Label(Frame_IO, justify=LEFT, text="Charger Control").grid(row=0, column=6, columnspan=2, sticky=W)
charge_ctrl = IntVar()
charge_button = Radiobutton(Frame_IO, text="DISABLE", variable=charge_ctrl, value=0, selectcolor="#FF0")
charge_button.grid(row=1, column=6, sticky=W)
charge_button = Radiobutton(Frame_IO, text="STAND", variable=charge_ctrl, value=1, selectcolor="#FF0")
charge_button.grid(row=2, column=6, sticky=W)
charge_button = Radiobutton(Frame_IO, text="SYSTEM", variable=charge_ctrl, value=2, selectcolor="#FF0")
charge_button.grid(row=3, column=6, sticky=W)

w=Label(Frame_IO, justify=LEFT, text="Vmax").grid(row=4, column=7, sticky=W)
charge_volt = Entry(Frame_IO, width=10, bg="#FF0")
charge_volt.grid(row=4, column=6, sticky=E)

w=Label(Frame_IO, justify=LEFT, text="Imax").grid(row=5, column=7, sticky=W)
charge_curr = Entry(Frame_IO, width=10, bg="#FF0")
charge_curr.grid(row=5, column=6, sticky=E)

#-------------------------------------------------------------
# Section for Battery Section
#-------------------------------------------------------------
# Column 0: Labels
w=Label(Frame_bat, justify=LEFT, text="   ").grid(row=0, column=8)
w=Label(Frame_bat, justify=LEFT, padx=10,text="BATTERY READINGS").grid(row=0, column=9, columnspan=3)

w=Label(Frame_bat, text="PARAM", relief=RAISED, width=15).grid(row=0 + 1, column=9)
w=Label(Frame_bat, text="STAND", relief=RAISED, width=10).grid(row=0 + 1, column=10)
w=Label(Frame_bat, text="SYSTEM", relief=RAISED, width=10).grid(row=0 + 1, column=11)

# Battery Serial Number
w=Label(Frame_bat, text="S/N", width=15).grid(row=0 + 2, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=2, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=2, column=11)


# Battery Voltage
w=Label(Frame_bat, text="Voltage", width=15).grid(row=0 + 3, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=3, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=3, column=11)

# Battery Current
w=Label(Frame_bat, text="Current", width=15).grid(row=0 + 4, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=4, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=4, column=11)

# Battery Temperature
w=Label(Frame_bat, text="Temp", width=15).grid(row=0 + 5, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=5, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=5, column=11)

# Battery Temperature
w=Label(Frame_bat, text="Rem. Capacity", width=15).grid(row=0 + 6, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=6, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=6, column=11)

# Battery Temperature
w=Label(Frame_bat, text="Rem. Run Time", width=15).grid(row=0 + 7, column=9)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=7, column=10)
w=Label(Frame_bat, justify=RIGHT,width=8, relief=SUNKEN, bg="#FFF").grid(row=7, column=11)



mainloop()

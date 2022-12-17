#My budget calculator for first semester (3 months) in Euro
#total income of 5000 per month for 3 months from part time job
total_income_amount = 5000*3
#monthly house rent expense of 300 for 3 months
exp1_houserent = 300*3 
#monthly electricity expense of 60 for 3 months
exp2_electricity = 60*3
#monthly oil expense of 200 for 3 months
exp3_oil = 200*3
#monthly broadband expense of 50 for 3 months
exp4_broadband = 50*3
#monthly mobile expense of 20 for 3 months
exp5_mobile = 20*3
#monthly cloths expense of 75 for 3 months
exp6_cloths = 75*3
#monthly food expense - 10 Euro per day for 3 months
exp7_food = 10*30*3
#Other expenses of 90 for 3 months
exp8_miscellaneous = 90*3
print (f"total income for 3 months is Euro {total_income_amount}")
print (f"total expenditure for 3 months is Euro {exp1_houserent+exp2_electricity+exp3_oil+exp4_broadband+exp5_mobile+exp6_cloths+exp7_food+exp8_miscellaneous}")
print (f"total available balance for 3 months is Euro {total_income_amount-(exp1_houserent+exp2_electricity+exp3_oil+exp4_broadband+exp5_mobile+exp6_cloths+exp7_food+exp8_miscellaneous)}")
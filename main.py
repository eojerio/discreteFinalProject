import pandas as pd

# dataframe
df= pd.read_excel('Test-Data-for-Discrete-Hoho.xlsx');

#printing table value
#print(df);

# school list
schools = ["Comembo ES (M)",
        "Nueva Ecija Girls' Home (P)",
        "Young Focus:Love2Learn (M)",
        "Bahay Tuluyan Laguna (P)",
        "Philippine Inst. for the Deaf PID (M)",
        "Project Pearl Bulacan (P)",
        "Mad Travel Subic (P)",
        "RED 2 (Renovate to Educate) (M)",
        "Hospicio de San Jose: Welfare Institution (M)",
        "SBP (M)",
        "Kids International (M)",
        "SPECS Tramo (M)",
        "Tarlac Farming Community (P)",
        "Papaya Academy HS students (M)",
        "Project Best at Buting ES (M)",
        "Baguio Bethesda School (P)",
        "Stepping Stones (M)",
        "GK Muntinlupa (M)",
        "Botolan Aeta Farming Community (P)",
        "Special Olympics w/ADB (M)",
        "CJ Learning Rizal (P)",
        "RED 1 (Renovate to Educate) (M)",
        "Banawe School and Rice Terraces (P)",
        "Papaya Academy ES Students (M)",
        "SPECS Pasay (M)",
        "Estancia Elementary School Panay (P)",
        "Stairway Foundation (P)",
        "Eco Stairway (P)",
        "rED Baguio (P)",
        "ICARE A.L.O.T (P)",
        "Bataan Sea Turtles (P)",
        "La Union (P)"]

## empty list
#gender_status
gender_status = []

#schools list
master_list = []

school_comemboES = []
school_nueva_ecija = []
school_young_focus = []
school_laguna = []
school_PID = []
school_bulacan = []
school_subic = []
school_red_2 = []
school_san_jose = []
school_SBP = []
school_kids_international = []
school_specs = []
school_tarlac = []
school_papaya_HS = []
school_buting = []
school_baguio = []
school_stepping_stones = []
school_muntinlupa = []
school_botolan = []
school_special_olympics = []
school_rizal = []
school_red_1 = []
school_banawe = []
school_papaya_ES = []
school_pasay = []
school_panay = []
school_stairway = []
school_eco_stairway = []
school_red_baguio = []
school_iCareAlot = []
school_bataaan = []
school_launion = []

# Appending to a singular list
master_list.append(school_comemboES)
master_list.append(school_nueva_ecija)
master_list.append(school_young_focus)
master_list.append(school_laguna)
master_list.append(school_PID)
master_list.append(school_bulacan)
master_list.append(school_subic)
master_list.append(school_red_2)
master_list.append(school_san_jose)
master_list.append(school_SBP)
master_list.append(school_kids_international)
master_list.append(school_specs)
master_list.append(school_tarlac)
master_list.append(school_papaya_HS)
master_list.append(school_buting)
master_list.append(school_baguio)
master_list.append(school_stepping_stones)
master_list.append(school_muntinlupa)
master_list.append(school_botolan)
master_list.append(school_special_olympics)
master_list.append(school_rizal)
master_list.append(school_red_1)
master_list.append(school_banawe)
master_list.append(school_papaya_ES)
master_list.append(school_pasay)
master_list.append(school_panay)
master_list.append(school_stairway)
master_list.append(school_eco_stairway)
master_list.append(school_red_baguio)
master_list.append(school_iCareAlot)
master_list.append(school_bataaan)
master_list.append(school_launion)


# resets index
df = df.reset_index()

#Iterate and save the P1 value as row to compare school
# for row in df['P1']:
#         # checks if match
#         if (row == schools[0]):
#                 if (df['Gender'].iloc[counter_school_1] == 'Male'):
#                         male_count += 1
#                 elif (df['Gender'].iloc[counter_school_1] == 'Female'):
#                         female_count += 1
#                 else:
#                         print("Invalid Gender")
#                 # gets the student number and stores it into school list
#                 school_comemboES.append(int(df['Student_Number'].iloc[counter_school_1]))
#         counter_school_1 += 1




#gender distribtuion list
male_count = 0
female_count = 0
counter_list = 0
counter_school = 0
#Iterate and save the P1 value as row to compare school
while(True):
        if(counter_list < 32):
                counter_school = 0
                for row in df['P1']:
                        if (row == schools[counter_list]):
                                # gets the student number and stores it into school list
                                master_list[counter_list].append(int(df['Student_Number'].iloc[counter_school]))
                        counter_school += 1
                counter_list += 1
        else:
                break



# print((df['Gender'] == 'Male').sum())
# print((df['Gender'] == 'Female').sum())
# df2 = df[['Student_Number']].copy()
# # print(df2)
# print("length is: " + str(len(df2.index)))

#For checking list print
# print(school_comemboES)

#Printing List
print()
print_counter = 0
for x in master_list:
        print(master_list[print_counter])
        print_counter+=1


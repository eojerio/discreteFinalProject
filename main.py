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
school_comemboES = []
school_iCareAlot = []

# resets index
df = df.reset_index()

#gender distribtuion list
male_count = 0
female_count = 0
counter_school_1 = 0
counter_school_2 = 0

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

#Iterate and save the P1 value as row to compare school
for row in df['P1']:
        if (row == schools[29]):
                if (df['Gender'].iloc[counter_school_2] == 'Male'):
                        male_count += 1
                elif (df['Gender'].iloc[counter_school_2] == 'Female'):
                        female_count += 1
                else:
                        print("Invalid Gender")
                # gets the student number and stores it into school list
                school_iCareAlot.append(int(df['Student_Number'].iloc[counter_school_2]))
        counter_school_2 += 1

print((df['Gender'] == 'Male').sum())
print((df['Gender'] == 'Female').sum())
df2 = df[['Student_Number']].copy()
# print(df2)
print("length is: " + str(len(df2.index)))

#For checking list print
# print(school_comemboES)
print(school_iCareAlot)


import pandas as pd

# dataframe
df= pd.read_excel('Test-Data-for-Discrete-Hoho.xlsx');

#printing table value
print(df);

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

# empty list
school_comemboES = []
school_iCareAlot = []

# resets index
df = df.reset_index()

# appending to empty list
for row in df['P1']:
    if(row == schools[0]):
        school_comemboES.append(row)

for row in df['P1']:
    if(row == schools[29]):
        school_iCareAlot.append(row)

print(school_comemboES)
print(school_iCareAlot)


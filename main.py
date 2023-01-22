import xml.etree.ElementTree as ET


#Ne cream o clasa in care retinem o serie de elemente specifice pt fiecare pilot
class Pilot:
    def __init__(self, name, team, season_wins, win_locations, season_DNF, DNF_locations):
        self.name = name
        self.team = team
        self.season_wins = season_wins
        self.win_locations = win_locations
        self.season_DNF = season_DNF
        self.DNF_locations = DNF_locations

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_season_wins(self):
        return self.season_wins

    def get_win_loc(self):
        return self.win_locations

    def get_season_DNF(self):
        return self.season_DNF

    def get_DNF_loc(self):
        return self.DNF_locations

    def set_name(self, new_name):
        self.name = new_name



#Incepem sa procesam XML-ul si sa retinem datele in liste ce urmeaza a fi procesate
tree = ET.parse('F1_knowledge_base.xml')  #cream un obiect de tipul ElementTree in care vom stoca datele din XML sub forma de arbore 
root = tree.getroot()  #aici dorim sa retinem radacina arborelui
print(root)  #ne va afisa denumirea etichetei si adresa  
            #de memorie unde este stocata

names = []
for pilot in tree.findall("./fapte/piloti_echipe/pilot_echipa/pilot"):
    names.append(pilot.text)  #lista in care memoram numele pilotilor

teams = []
for index in tree.findall("./fapte/piloti_echipe/pilot_echipa/echipa"):
    teams.append(index.text) #lista in care memoram numele echipelor

DNF_name_list = []
for index in tree.findall("./fapte/curse_neterminate/cursa_neterminata/pilot"):
    DNF_name_list.append(index.text) #lista in care memoram numele pilotilor care au dat DNF

DNF_loc_list = []
for index in tree.findall("./fapte/curse_neterminate/cursa_neterminata/cursa"):
    DNF_loc_list.append(index.text) #lista in care memoram numele tarilor in care au dat DNF fiecare pilot

wins_name_list = []
for index in tree.findall("./fapte/clasari_primu_loc/pilot_cursa/pilot"):
    wins_name_list.append(index.text)  #lista in care memoram numele pilotilor care au castigat

wins_loc_list = []
for index in tree.findall("./fapte/clasari_primu_loc/pilot_cursa/cursa"):
    wins_loc_list.append(index.text) #lista in care memoram numele tarilor in care a castigat fiecare pilot

pilot_dic = []  #o lista cu dictionare ce ne va ajuta sa aflam numarul de vitorii, locurile in care fiecare pilot a invins, numarul de DNF 
                #si locurile in care fiecare pilot a dat DNF
for index in names:    
    pilot_dic.append({'name':index, 'team': '', 'wins': 0, 'DNFs': 0,
                        'loc_DNF': [], 'loc_wins': []})  

for i in pilot_dic:
    index = 0
    for j in range(len(wins_name_list)):
        if(wins_name_list[j] == i['name']):
            i['wins'] += 1
            i['loc_wins'].append(wins_loc_list[j])
            index += 1

    index = 0
    for k in range(len(DNF_name_list)):
        if(DNF_name_list[k] == i['name']):
            i['DNFs'] += 1
            i['loc_DNF'].append(DNF_loc_list[k])
            index += 1

    index = 0
    for l in names:
        if(l == i['name']):
            i['team'] = teams[index]
        else:
            index += 1


list_of_pilots = [] #cream o lista cu obiecte de tipul clasei Pilot, definite de catre noi, in care retinem datele fiecarui pilot in parte si o transmitem catre GUI
index = 0
for i in pilot_dic:
    list_of_pilots.append(Pilot(i['name'], i['team'], i['wins'], i['loc_wins'],
                                i['DNFs'], i['loc_DNF']))

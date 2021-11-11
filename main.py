import random
import datetime
from codicefiscale import codicefiscale
import pandas as pd
from numpy.random import choice
import randomname
from faker import Faker

""" --- GLOBAL_VARIABLES, SET, FUNCTIONS  -start- ------------------------- """
global dfPeople
global dfPlaces

fake = Faker('it_IT')

DIM = 100  # dfPeople
DIM_places = 50  # dfPlaces

covid_start_date = datetime.datetime(2020, 2, 1, 00, 00)

setNames = ["Leonardo", "Francesco", "Lorenzo", "Alessandro", "Andrea", "Mattia", "Gabriele", "Tommaso", "Riccardo",
            "Edoardo", "Matteo", "Giuseppe", "Nicolo'", "Antonio", "Federico", "Diego", "Davide", "Giovanni", "Pietro",
            "Samuele", "Christian", "Filippo", "Marco", "Michele", "Luca", "Simone", "Giulio", "Elia", "Alessio",
            "Salvatore", "Gabriel", "Enea", "Emanuele", "Vincenzo", "Gioele", "Giacomo", "Manuel", "Jacopo", "Daniele",
            "Thomas", "Samuel", "Cristian", "Giorgio", "Luigi", "Daniel", "Domenico", "Liam", "Nathan", "Raffaele",

            "Sofia", "Aurora", "Giulia", "Ginevra", "Alice", "Emma", "Giorgia", "Beatrice", "Greta", "Vittoria", "Anna",
            "Martina", "Chiara", "Matilde", "Ludovica", "Nicole", "Sara", "Bianca", "Camilla", "Arianna", "Noemi",
            "Gaia", "Francesca", "Mia", "Alessia", "Rebecca", "Elena", "Adele", "Elisa", "Viola", "Marta", "Giada",
            "Isabel", "Gioia", "Maria", "Emily", "Cecilia", "Azzurra", "Carlotta", "Ambra", "Margherita", "Chloe",
            "Eleonora", "Asia", "Melissa", "Anita", "Miriam", "Benedetta", "Irene", "Rachele"]

setSurnames = ["Rossi", "Ferrari", "Russo", "Bianchi", "Romano", "Gallo", "Costa", "Fontana", "Conti", "Esposito",
               "Ricci", "Bruno", "De Luca", "Moretti", "Marino", "Greco", "Barbieri", "Lombardi", "Giordano", "Cassano",
               "Colombo", "Mancini", "Longo", "Leone", "Martinelli", "Marchetti", "Martini", "Galli", "Gatti",
               "Mariani", "Ferrara", "Santoro", "Marini", "Bianco", "Conte", "Serra", "Farina", "Gentile", "Caruso",
               "Morelli", "Ferri", "Testa", "Ferraro", "Pellegrini", "Grassi", "Rossetti", "D'Angelo", "Bernardi",
               "Mazza", "Rizzi"]

setCities = ["Agrigento", "Alessandria", "Ancona", "Aosta", "Arezzo", "Ascoli Piceno", "Asti", "Avellino", "Bari",
             "Barletta", "Andria", "Trani", "Belluno", "Benevento", "Bergamo", "Biella", "Bologna", "Bolzano",
             "Brescia", "Brindisi", "Cagliari", "Caltanissetta", "Campobasso", "Carbonia", "Iglesias", "Caserta",
             "Catania", "Catanzaro", "Chieti", "Como", "Cosenza", "Cremona", "Crotone", "Cuneo", "Enna", "Fermo",
             "Ferrara", "Firenze", "Foggia", "Forlì", "Cesena", "Frosinone", "Genova", "Gorizia", "Grosseto", "Imperia",
             "Isernia", "La Spezia", "L'Aquila", "Latina", "Lecce", "Lecco", "Livorno", "Lodi", "Lucca", "Macerata",
             "Mantova", "Massa", "Carrara", "Matera", "Messina", "Milano", "Modena", "Monza", "Napoli", "Novara",
             "Nuoro", "Olbia", "Oristano", "Padova", "Palermo", "Parma", "Pavia", "Perugia", "Pesaro", "Urbino",
             "Pescara", "Piacenza", "Pisa", "Pistoia", "Pordenone", "Potenza", "Prato", "Ragusa", "Ravenna",
             "Reggio di Calabria", "Reggio nell'Emilia", "Rieti", "Rimini", "Roma", "Rovigo", "Salerno", "Sassari",
             "Savona", "Siena", "Siracusa", "Sondrio", "Taranto", "Teramo", "Terni", "Torino", "Trapani",
             "Trento", "Treviso", "Trieste", "Udine", "Varese", "Venezia", "Cusio", "Vercelli", "Verona",
             "Vibo Valentia", "Vicenza", "Viterbo"]

setApps = ["Immuni", "Stopp Corona App", "Coronalert", "CovTracer-EN", "TousAntiCovid", "Corona-Warn-App"]

def random_birthdate():
    # Generate a random datetime between `start` and `end`
    start = datetime.datetime.strptime("01/01/1900", '%d/%m/%Y')
    end = datetime.datetime.strptime("01/01/2021", '%d/%m/%Y')
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def createPerson():
    sex = random.choice(['M', 'F'])
    name = random.choice(setNames[0:49]) if sex == 'M' else random.choice(setNames[50:99])
    surname = random.choice(setSurnames)
    birthDate = random_birthdate().strftime("%d/%m/%Y")
    birthPlace = random.choice(setCities)
    phoneNumber = f'34{random.randrange(0, 10 ** 8):08}'  # number with 10 digits, starting with 34........
    fiscalCode = codicefiscale.encode(surname=surname, name=name, sex=sex, birthdate=birthDate, birthplace=birthPlace)
    # to do: check if this _fiscalCode already exist
    isVaxed = random.choice(['Yes', 'No'])

    idFamily = f'{setSurnames.index(surname):04}'  # everyone with same surnname is in the same family
    idApp = f'{abs(hash(fiscalCode)):020}'
    # to do: check if this idApp already exist

    return [fiscalCode, name, surname, sex, birthDate, birthPlace, phoneNumber, isVaxed, idFamily, idApp]


"""
    una persona positiva deve avere un ultimo test recente? (al momento non è garantito)
    puo' aver incontrato persone anche se ha fatto un test ed è risultato positivo? (al momento è ammesso)
"""
def createNewTest():
    dateLastTest = ((covid_start_date + datetime.timedelta(days=random.randrange(730)) +
                     datetime.timedelta(minutes=random.randrange(1440))).strftime("%Y-%m-%dT%H:%M"))
    resultLastTest = random.choice(['Positive', 'Negative'])

    return [dateLastTest, resultLastTest]


"""
    - assumiamo che una persona possa essere stata infettata in un luogo casuale, e che non debba essere stato 
    registrato dall'app. 
    - potrebbe conoscersi solo la data dell'infezione, ma non il luogo
"""
def newInfection(personId):
    dateInfection = ""
    areaInfection = ""
    isInfected = dfPeople.at[personId, "resultLastTest"]
    if (isInfected == "Positive"):
        dateLastTest = datetime.datetime.strptime((dfPeople.at[personId, "dateLastTest"]), "%Y-%m-%dT%H:%M")
        dateInfection = (dateLastTest - datetime.timedelta(days=random.randrange(60)) -
                     datetime.timedelta(minutes=random.randrange(1440))).strftime("%Y-%m-%dT%H:%M")
        # does we know the place of the infection?
        areaKnown = choice([True, False], 1, p=[0.6, 0.4])
        if (areaKnown):
            areaInfection = random.randint(0, DIM_places-1)

    return [dateInfection, areaInfection]


def createAppConnection(personId):  # personId and contactId are persons
    numOfConnections = random.randint(0, 3)

    for i in range(numOfConnections):
        contactId = random.choice([x for x in range(DIM - 1) if x != personId])
        print(personId, contactId)
        newConnectionDate = ((covid_start_date + datetime.timedelta(days=random.randrange(730)) +
                            datetime.timedelta(minutes=random.randrange(1440))).strftime("%Y-%m-%dT%H:%M"))
        newAppName = random.choice(setApps)
        #update personId row
        isPersonIdEmpty = dfPeople.at[personId, "appContactId"]
        if isPersonIdEmpty == "":
            dfPeople.at[personId, "appContactId"] += str(contactId)
            dfPeople.at[personId, "appContactDate"] += newConnectionDate
            dfPeople.at[personId, "appName"] += newAppName
        if isPersonIdEmpty != "":
            dfPeople.at[personId, "appContactId"] += ':' + str(contactId)
            dfPeople.at[personId, "appContactDate"] += ';' + newConnectionDate
            dfPeople.at[personId, "appName"] += ';' + newAppName
        #update contactId row
        isContactIdEmpty = dfPeople.at[contactId, "appContactId"]
        if isContactIdEmpty == "":
            dfPeople.at[contactId, "appContactId"] += str(personId)
            dfPeople.at[contactId, "appContactDate"] += newConnectionDate
            dfPeople.at[contactId, "appName"] += newAppName
        if isContactIdEmpty != "":
            dfPeople.at[contactId, "appContactId"] += ":" + str(personId)
            dfPeople.at[contactId, "appContactDate"] += ";" + newConnectionDate
            dfPeople.at[contactId, "appName"] += ";" + newAppName


def createPlace():
    name = randomname.get_name(noun=("buildings", "houses"))
    type = name.partition('-')[2]

    address = fake.street_suffix() + ' ' + fake.street_name() + ', ' + fake.building_number()
    city = random.choice(setCities)

    return [name, type, address, city]


def createPlaceConnection():
    numOfConnections = random.randint(0, 3)
    connections = []
    connectionsStr = ""
    connectionDateStart = ""
    connectionDateEnd = ""
    for i in range(numOfConnections):
        personContactID = random.randint(0, DIM-1)
        while (personContactID in connections):
            personContactID = random.randint(0, DIM-1)

        connections.append(personContactID)

    dataReference = (covid_start_date + datetime.timedelta(days=random.randrange(730)) +
                     datetime.timedelta(minutes=random.randrange(1440)))

    """
        connectionsStr += str(personContactID) + ':'
        newConnectionDateStart = ((covid_start_date + datetime.timedelta(days=random.randrange(730)) +
                                   datetime.timedelta(minutes=random.randrange(1440))).strftime("%Y-%m-%dT%H:%M"))
        connectionDateStart += newConnectionDateStart + ';'
        connectionDateEnd += ((datetime.datetime.strptime(newConnectionDateStart, "%Y-%m-%dT%H:%M")) +
                              datetime.timedelta(minutes=random.randrange(1440))).strftime("%Y-%m-%dT%H:%M") + ';'
    connectionsStr = connectionsStr[:-1]
    connectionDateStart = connectionDateStart[:-1]
    connectionDateEnd = connectionDateEnd[:-1]
    """

    #return [connectionsStr, connectionDateStart, connectionDateEnd]
    return [connections, dataReference]

def addPlaceToPerson(placeID, personID, date):
    placeStr = dfPeople.at[personID, "placeContactId"]
    dateStart = (date + datetime.timedelta(minutes=random.randrange(30)))
    dateEnd = (dateStart + datetime.timedelta(minutes=random.randrange(180)))
    if (placeStr == ""):
        dfPeople.at[personID, "placeContactId"] += str(placeID)
        dfPeople.at[personID, "placeContactDateStart"] += dateStart.strftime("%Y-%m-%dT%H:%M")
        dfPeople.at[personID, "placeContactDateEnd"] += dateEnd.strftime("%Y-%m-%dT%H:%M")
    else:
        dfPeople.at[personID, "placeContactId"] += ":" + str(placeID)
        dfPeople.at[personID, "placeContactDateStart"] += ";" + dateStart.strftime("%Y-%m-%dT%H:%M")
        dfPeople.at[personID, "placeContactDateEnd"] += ";" + dateEnd.strftime("%Y-%m-%dT%H:%M")

""" --- GLOBAL_VARIABLES, SET, FUNCTIONS  -end- --------------------------- """


""" --- PROJECT -start- --------------------------------------------------- """

""" -1- CREATION OF DATA -start- ------------------------------------------ """

# creation of PEOPLE dataframe
dfPeople_columns = ['fiscalCode', 'name', 'surname', 'sex', 'birthDate', 'birthPlace', 'phoneNumber', 'isVaxed',
                    'idFamily', 'idApp']
dfPeople = pd.DataFrame(columns=dfPeople_columns)

# creation of people and add to dataframe
for i in range(DIM):
    person = createPerson()
    print(person)
    dfPerson = pd.DataFrame(data=[person], columns=dfPeople_columns)
    dfPeople = dfPeople.append(dfPerson, ignore_index=True)

# give a name to the default index
dfPeople.index.names = ['idPerson']

# add col dateLastTest, resultLastTest to dataframe
dfPeople = dfPeople.assign(dateLastTest='', resultLastTest='')
dfPeople_columns += ['dateLastTest', 'resultLastTest']  # just for consistency
for i in range(DIM):
    needNewTest = choice([True, False], 1, p=[0.7, 0.3])
    if (needNewTest):
        newTest = createNewTest()
        dfPeople.at[i, "dateLastTest"] = newTest[0]
        dfPeople.at[i, "resultLastTest"] = newTest[1]

# add col dateInfection, areaInfection to dataframe
dfPeople = dfPeople.assign(dateInfection='', areaInfection='')
dfPeople_columns += ['dateInfection', 'areaInfection']  # just for consistency
for i in range(DIM):
    infection = newInfection(i)
    dfPeople.at[i, "dateInfection"] = infection[0]
    dfPeople.at[i, "areaInfection"] = infection[1]

# add col familyMembers to dataframe -- for relationship FAMILY
dfPeople = dfPeople.assign(familyMembers='')
dfPeople_columns += ['familyMembers']  # just for consistency
for i in range(DIM):
    myId = dfPeople.at[i, "idFamily"]
    myFamilyMembers = ''
    for j in range(DIM):
        if dfPeople.at[j, "idFamily"] == myId:
            myFamilyMembers += str(j) + ':'
    myFamilyMembers = myFamilyMembers[:-1]
    dfPeople.at[i, "familyMembers"] = myFamilyMembers

# add col appContactId, appContactDate to dataframe -- for relationship APP
dfPeople = dfPeople.assign(appContactId='', appContactDate='', appName='')
dfPeople_columns += ['appContactId', 'appContactDate', 'appName']  # just for consistency
for i in range(DIM):
    createAppConnection(i)


# creation of PLACES dataframe
dfPlaces_columns = ['name', 'type', 'address', 'city']
dfPlaces = pd.DataFrame(columns=dfPlaces_columns)

# creation of Places and add to dataframe
for i in range(DIM_places):
    place = createPlace()
    print(place)
    dfPlace = pd.DataFrame(data=[place], columns=dfPlaces_columns)
    dfPlaces = dfPlaces.append(dfPlace, ignore_index=True)

# give a name to the default index
dfPlaces.index.names = ['idPlace']

# add col placeContactId, placeContactDateStart, placeContactDateEnd to dataframe -- for relationship PLACE
dfPeople = dfPeople.assign(placeContactId='', placeContactDateStart='', placeContactDateEnd='')
dfPeople_columns += ['placeContactId', 'placeContactDate', 'placeContactDateEnd']  # just for consistency
for i in range(DIM_places):
    [peopleConnections, dataPlace] = createPlaceConnection()
    print("placeID, people: ")
    print(i, peopleConnections)
    for j in range(len(peopleConnections)):
        addPlaceToPerson(i, peopleConnections[j], dataPlace)

    """
    dfPeople.at[i, "placeContactId"] = newConnections[0]
    dfPeople.at[i, "placeContactDateStart"] = newConnections[1]
    dfPeople.at[i, "placeContactDateEnd"] = newConnections[2]
    """

print("\n\n\n", dfPeople, "\n\n\n")
# write df into csv
dfPeople.to_csv("People.csv")

print("\n\n\n", dfPlaces, "\n\n\n")
# write df into csv
dfPlaces.to_csv("Places.csv")

""" -1- CREATION OF DATA -end- -------------------------------------------- """

""" -2- CREATION OF RELATIONSHIP -start- ---------------------------------- """

# DATAFRAME FAMILY RELATIONSHIP
dfRelationshipFamily_columns = ['id_from', 'id_to']
dfRelationshipFamily = pd.DataFrame(columns=dfRelationshipFamily_columns)

for i in range(DIM):
    id_from = i
    for j in range(len(dfPeople.at[i, 'familyMembers'].split(':'))):
        id_to = dfPeople.at[i, 'familyMembers'].split(':')[j]
        if int(id_from) != int(id_to):
            dfNewRelationship = pd.DataFrame(data=[[id_from, id_to]], columns=dfRelationshipFamily_columns)
            dfRelationshipFamily = dfRelationshipFamily.append(dfNewRelationship, ignore_index=True)

print("\n\n\n", "dfRelationshipFamily\n", dfRelationshipFamily)
# write df into csv
dfRelationshipFamily.to_csv("RelationshipFamily.csv")


# DATAFRAME APP RELATIONSHIP
dfRelationshipApp_columns = ['id_from', 'id_to', 'appContactDate', 'appName']
dfRelationshipApp = pd.DataFrame(columns=dfRelationshipFamily_columns)

for i in range(DIM):
    id_from = i
    for j in range(len(dfPeople.at[i, 'appContactId'].split(':'))):
        id_to = dfPeople.at[i, 'appContactId'].split(':')[j]
        date = dfPeople.at[i, 'appContactDate'].split(';')[j]
        appName = dfPeople.at[i, 'appName'].split(';')[j]
        if id_to != "":
            if int(id_from) != int(id_to):
                dfNewRelationship = pd.DataFrame(data=[[id_from, id_to, date, appName]], columns=dfRelationshipApp_columns)
                dfRelationshipApp = dfRelationshipApp.append(dfNewRelationship, ignore_index=True)

print("\n\n\n", "dfRelationshipApp\n", dfRelationshipApp)
# write df into csv
dfRelationshipApp.to_csv("RelationshipApp.csv")


# DATAFRAME PLACE RELATIONSHIP
dfRelationshipPlaces_columns = ['id_from', 'id_to', 'start', 'end']
dfRelationshipPlaces = pd.DataFrame(columns=dfRelationshipPlaces_columns)

for i in range(DIM):
    id_from = i
    for j in range(len(dfPeople.at[i, 'placeContactId'].split(':'))):
        id_to = dfPeople.at[i, 'placeContactId'].split(':')[j]
        start = dfPeople.at[i, 'placeContactDateStart'].split(';')[j]
        end = dfPeople.at[i, 'placeContactDateEnd'].split(';')[j]
        if id_to != "":
            if int(id_from) != int(id_to):
                dfNewRelationship = pd.DataFrame(data=[[id_from, id_to, start, end]], columns=dfRelationshipPlaces_columns)
                dfRelationshipPlaces = dfRelationshipPlaces.append(dfNewRelationship, ignore_index=True)

print("\n\n\n", "dfRelationshipPlaces\n", dfRelationshipPlaces)
# write df into csv
dfRelationshipPlaces.to_csv("RelationshipPlaces.csv")

""" -2- CREATION OF RELATIONSHIP -end- ------------------------------------ """

""" --- PROJECT -end- ----------------------------------------------------- """


""" 
- COMMANDS TO POPULATE THE DB :

    LOAD CSV WITH HEADERS FROM 'file:///People.csv' AS row
    WITH row WHERE row.idPerson IS NOT NULL
    CREATE (p: Person { idPerson: row.idPerson,
                        fiscalCode: row.fiscalCode, 
                        name: row.name,
                        surname: row.surname,
                        sex: row.sex,
                        birthDate: row.birthDate,
                        birthPlace: row.birthPlace,
                        phoneNumber: row.phoneNumber,
                        isVax: row.isVaxed,
                        dateLastTest: localdatetime(row.dateLastTest),
                        resultLastTest: row.resultLastTest,
                        dateInfection: localdatetime(row.dateInfection),
                        areaInfection: row.areaInfection});
                        
    LOAD CSV WITH HEADERS FROM 'file:///Places.csv' AS row
    WITH row WHERE row.idPlace IS NOT NULL
    CREATE (p: Place { idPlace: row.idPlace,
                        name: row.name,
                        type: row.type,
                        address: row.address,
                        city: row.city});
                        
    LOAD CSV WITH HEADERS FROM "file:///RelationshipFamily.csv" AS row
    MATCH (p1:Person {idPerson:row.id_from}), (p2:Person {idPerson:row.id_to})
    CREATE (p1)-[:isInTheFamily]->(p2);
    
    LOAD CSV WITH HEADERS FROM "file:///RelationshipApp.csv" AS row
    MATCH (p1:Person {idPerson:row.id_from}), (p2:Person {idPerson:row.id_to})
    CREATE (p1)-[:isInContact{appContactDate:localdatetime(row.appContactDate), appName:row.appName}]->(p2);
    
    LOAD CSV WITH HEADERS FROM "file:///RelationshipPlaces.csv" AS row
    MATCH (p:Person {idPerson:row.id_from}), (pl:Place {idPlace:row.id_to})
    CREATE (p)-[:visit{startTime:localdatetime(row.start), endTime:localdatetime(row.end)}]->(pl);


- COMMANDS TO CHECK THE RELATIONSHIPS

    MATCH (n:Person)-[r:isInContact]->(b:Person) RETURN r LIMIT 100
    
    MATCH (n:Person)-[r:isInContact]->(b:Person) RETURN n, b LIMIT 10
    
    MATCH (n:Person)-[r:visit]->(b:Place) RETURN r LIMIT 100
    
    MATCH (p:Person)--(pl:Place) RETURN p, pl LIMIT 25

- OTHERS

    MATCH (n) detach delete n

- QUERY VERIFICATE

    1- 
    MATCH (person:Person)-[:isInContact]->(app_contact:Person)
    WHERE person.idPerson = "5"
    RETURN app_contact, person
    
    2- 
    MATCH (person:Person)-[:isInTheFamily]->(family_contact:Person)
    WHERE person.idPerson = "6"
    RETURN family_contact
    
    3- run, but 0 results:
        MATCH (person:Person)-[a:visit]->(place:Place)<-[b:visit]-(place_contact:Person)
        WITH place_contact, CASE WHEN a.startTime >= b.startTime THEN a.startTime ELSE b.startTime END as max_start, CASE WHEN a.endTime <= b.endTime THEN a.endTime ELSE b.endTime END as min_end
        WHERE person.idPerson  = "5" AND max_start <= min_end AND localtime() + duration.inSeconds(max_start, min_end) >= localtime() + duration({minutes: 15})
        RETURN DISTINCT place_contact
    
    4- 2nd version, not running
        MATCH (person:Person)-[:isInTheFamily]->(family_contact:Person)
        WHERE person.idPerson = "5"
        RETURN family_contact
        UNION
        MATCH (person:Person)-[app:isInContact]->(app_contact:Person)
        WHERE app.appContactDate IS NULL OR localtime() + duration.inSeconds(appContactDate, localtime()) <= localtime() + duration({days:5})
        RETURN app_contact
        UNION
        MATCH (person:Person)-[a:visit]->(place:Place)<-[b:visit]-(place_contact:Person)
        WHERE localtime() + duration.inSeconds(a.startTime, localtime()) <= localtime() + duration({days: 5})
        WITH place_contact, CASE WHEN a.startTime >= b.startTime THEN a.startTime ELSE b.startTime END as max_start, CASE WHEN a.endTime <= b.endTime THEN a.endTime ELSE b.endTime END as min_end
        WHERE person.idPerson  = "5" AND max_start <= min_end AND localtime() + duration.inSeconds(max_start, min_end) >= localtime() + duration({minutes: 15})
        RETURN DISTINCT place_contact
    
    5- All sub queries in an UNION must have the same column names (line 5, column 1 (offset: 193))
        MATCH (person: Person)-[:isInTheFamily]->(family_person:Person) <-[:isInContact]-(family_contact: Person)
        WHERE person.idPerson= "5" AND person <>family_contact
        RETURN DISTINCT family_contact
        
        UNION
        
        MATCH (person: Person)-[:isInTheFamily]->(family_person:Person)-[a:visit]->(place: Place)<-[b:visit]-(family_place: Person)
        WITH family_place, CASE WHEN a.startTime >= b.startTime THEN a.startTime ELSE b.startTime END as max_start, CASE WHEN a.endTime <= b.endTime THEN a.endTime ELSE b.endTime END as min_end
        WHERE person.idPerson= "5" AND person <>family_place AND max_start <= min_end AND localtime() + duration.inSeconds(max_start, min_end) >= localtime() + duration({minutes: 15})
        RETURN DISTINCT family_place
        
        UNION
        
        MATCH (person:Person) -[:isInContact]->(app_contact:Person)<-[:IsInTheFamily]-(contact_family:Person)
        WHERE person.idPerson= "5" AND person <>contact_family
        RETURN DISTINCT contact_family
        
        UNION
        
        MATCH (person:Person) -[:isInContact]->(app_contact:Person)-[a:visit]->(place:Place)<-[b:visit]-(contact_place: Person)
        WITH contact_place, CASE WHEN a.startTime >= b.startTime THEN a.startTime ELSE b.startTime END as max_start, CASE WHEN a.endTime <= b.endTime THEN a.endTime ELSE b.endTime END as min_end
        WHERE person.idPerson= "5" AND person <>contact_place AND max_start <= min_end AND localtime() + duration.inSeconds(max_start, min_end) >= localtime() + duration({minutes: 15})
        RETURN DISTINCT contact_place
        
        UNION
        
        MATCH (person:Person)-[:isInContact*2]->(app_family_contact:Person)
        WHERE person.idPerson = "5"
        RETURN DISTINCT app_family_contact
        UNION
        MATCH (person:Person)-[a:visit]->(place:Place)<-[b:visit]-(place_contact:Person)<-[:isInTheFamily|:isInContact]-(second_contact:Person)
        WITH second_contact, CASE WHEN a.startTime >= b.startTime THEN a.startTime ELSE b.startTime END as max_start, CASE WHEN a.endTime <= b.endTime THEN a.endTime ELSE b.endTime END as min_end
        WHERE person.idPerson = "5" AND max_start <= min_end AND localtime() + duration.inSeconds(max_start, min_end) >= localtime() + duration({minutes: 15})
        RETURN DISTINCT second_contact;
    
    6 -
    MATCH (contact:Person)-[tracked:visit]->(place:Place)
    WHERE place.idPlace = "21" and tracked.startTime >= localdatetime("2021-01-09T00:09") and tracked.startTime <= localdatetime("2021-03-09T00:09")
    RETURN DISTINCT contact
    
    7 - run, but 0 results
    MATCH (place:Place)<-[v:visit]-(contact:Person)
    WHERE localtime() + duration.between(v.endTime, contact.dateLastTets) <= localtime() + duration({days: 7}) AND contact.resultLastTest = "Positive"
    WITH place, COUNT(contact) as contactCount
    WHERE contactCount >= 10
    RETURN place

    8 -
    MATCH (all:Person)
    WITH COUNT(*) as total
    MATCH (vax:Person)
    WHERE vax.isVax = "Yes"
    WITH total, COUNT(vax) as vaxCount
    MATCH (no_vax:Person)
    WHERE no_vax.isVax = "No"
    WITH total, vaxCount, COUNT(no_vax) as noVaxCount
    RETURN 100.0 * vaxCount / total, 100.0 * noVaxCount / total;
    
    8 - alternative formulation
    CALL{
       MATCH (all:Person)
       RETURN COUNT(*) as total
    }
    CALL{
       MATCH (vax:Person)
       WHERE vax.isVax = "Yes"
       RETURN COUNT(vax) as vaxCount
    }
    CALL{
       MATCH (no_vax:Person)
       WHERE no_vax.isVax = "No"
       RETURN COUNT(no_vax) as no_vaxCount
    }
    RETURN 100.0 * vaxCount / total, 100.0 * no_vaxCount / total;

    9 -
    MATCH (person:Person)
    WITH MAX(localtime() + duration.between(person.dateLastTest, person.dateInfection)) as longest_infection, person 
    RETURN longest_infection, person
    
    10 -
    MATCH (p:Person)-[con:isInContact]->()
    WHERE con.appName = "Immuni"
    RETURN DISTINCT p
    
    
    non vanno 4-5
    vanno, ma non ci sono esempi verificabili: 3-7
"""
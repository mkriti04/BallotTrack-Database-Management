import subprocess as sp
import pymysql
import pymysql.cursors

keys = ["TS#101","TS#102","TS#103"]

def insertVoter():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["voterID"] = input("Enter 8-character Voter ID:")
        name = input("Enter Name (FName LName):")
        name = name.split()
        voter_details["Fname"] = name[0]
        voter_details["Lname"] = name[1]
        voter_details["Phone"] = input("Enter 10 digit Mobile Number:")
        voter_details["email"] = input("Enter E-mail ID:")
        voter_details["dob"] = input("Enter D.O.B in (YYYY-MM-DD):")
        voter_details["Address_voter"]=input("Enter Address:")
        voter_details["Station_ID"]=input("Enter 4 digit station ID:")
        voter_details["eventID"] = input("Enter 12 digit Event-ID:")
        dob = voter_details["dob"]
        voterID = voter_details["voterID"]
        for key in voter_details:
            voter_details[key] = '"' + voter_details[key] + '"'
        query = 'INSERT INTO Voters(Voter_ID,Fname,Lname,Phone_Number,Email_ID,DOB,Address_voter,Station_ID,Event_ID) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (voter_details["voterID"],voter_details["Fname"],voter_details["Lname"],voter_details["Phone"],voter_details["email"],voter_details["dob"],voter_details["Address_voter"],voter_details["Station_ID"],voter_details["eventID"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    
    insertDemographicData(voterID,dob)
    return
def createEvent():
    try:
        event_details = {}
        print("Enter Event details:")
        event_details["elecID"] = input("Enter 12-character Event ID:")
        event_details["date"] = input("Enter date of event (YYYY-MM-DD):")
        event_details["type_event"]=input("Enter event type:")
        event_details["ElectionType"]=input("Enter Election type:")
        for key in event_details:
            event_details[key] = '"' + event_details[key] + '"'
        query = 'INSERT INTO Election_events Values (%s,%s,%s,%s)' % (event_details["elecID"],event_details["date"],event_details["type_event"],event_details["ElectionType"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Event Logged")
    except Exception as e:
        con.rollback()
        print("Failed to Log into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertStation():
    try:
        station_details = {}
        print("Enter Station details:")
        station_details["stationID"] = input("Enter 4-character Station ID:")
        station_details["Address_station"]=input("Enter Address:")
        station_details["Phone"] = input("Enter 10 digit Mobile Number:")
        station_details["email"] = input("Enter E-mail ID:")
        station_details["eventID"] = input("Enter 12 digit Event-ID:")
        for key in station_details:
            station_details[key] = '"' + station_details[key] + '"'
        query = 'INSERT INTO Polling_Stations Values (%s,%s,%s,%s,%s)' % (station_details["stationID"],station_details["Address_station"],station_details["Phone"],station_details["email"],station_details["eventID"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertParty():
    try:
        party_details = {}
        print("Enter Party details:")
        party_details["BallotID"] = input("Enter 4-character Ballot ID:")
        party_details["PartyName"]=input("Enter Party Name:")
        for key in party_details:
            party_details[key] = '"' + party_details[key] + '"'
        query = 'INSERT INTO List_of_parties Values (%s,%s)' % (party_details["BallotID"],party_details["PartyName"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertCandidate():
    try:
        candidate_details = {}
        print("Enter Candidate details:")
        candidate_details["canID"] = input("Enter 7-character Candidate ID:")
        name = input("Enter Name (FName LName):")
        name = name.split()
        candidate_details["Fname"] = name[0]
        candidate_details["Lname"] = name[1]
        candidate_details["Phone"] = input("Enter 10 digit Mobile Number:")
        candidate_details["email"] = input("Enter E-mail ID:")
        candidate_details["Party"] = input("Enter Party Affliation:")
        candidate_details["Candidate_exp"]=int(input("Input candidate expenditure:"))
        candidate_details["eventID"] = input("Enter 12 digit Event-ID:")
        for key in candidate_details:
            if type(candidate_details[key]) == str:
                candidate_details[key] = '"' + candidate_details[key] + '"'
        query = 'INSERT INTO Candidates Values (%s,%s,%s,%s,%s,%s,%d,%s)' % (candidate_details["canID"],candidate_details["Fname"],candidate_details["Lname"],candidate_details["Phone"],candidate_details["email"],candidate_details["Party"],candidate_details["Candidate_exp"],candidate_details["eventID"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertCampaignFinance():
    try:
        party_details = {}
        print("Enter Party details:")
        party_details["TransID"] = input("Enter 10-character Transaction ID:")
        party_details["amount"]=int(input("Enter Amount:"))
        party_details["CanID"]= input("Enter Candidate ID:")
        party_details["Date"]= input("Enter Date of Campaign:")
        for key in party_details:
            if type(party_details[key]) == str:
                party_details[key] = '"' + party_details[key] + '"'
        query = 'INSERT INTO Campaign_finance Values (%s,%d,%s,%s)' % (party_details["TransID"],party_details["amount"],party_details["canID"],party_details["Date"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return    
def insertOfficial():
    try:
        off_dets = {}
        print("Enter Election Official details:")
        off_dets["Official_ID"] = input("Enter 5-character Official ID:")
        name = input("Enter Name of Official (FName LName):")
        name = name.split()
        off_dets["Fname"] = name[0]
        off_dets["Lname"] = name[1]
        off_dets["Phone_number"] = input("Enter Phone Number of Officer:")
        off_dets["Email_ID"]=input("Enter E-mail ID of officer:")
        off_dets["Role_official"]=input("Enter Role of the officer:")
        off_dets["Event_ID"]=input("Enter 12-digit Event ID:")
        for key in off_dets:
            off_dets[key] = '"' + off_dets[key] + '"'
        query = 'INSERT INTO Election_Officials Values (%s,%s,%s,%s,%s,%s,%s)' % (off_dets["Official_ID"],off_dets["Fname"],off_dets["Lname"],off_dets["Phone_number"],off_dets["Email_ID"],off_dets["Role_official"],off_dets["Event_ID"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Official Logged")
    except Exception as e:
        con.rollback()
        print("Failed to Log into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertCandidateToList():
    try:
        candidate_list={}
        print("Enter candidate details") 
        candidate_list["Candidate_Name"]=input("Enter Candidate Name:")
        candidate_list["Ballot_ID"]=input("Enter Ballot ID:")
        for key in candidate_list:
                if type(candidate_list[key]) == str:
                    candidate_list[key] = '"' + candidate_list[key] + '"'
        query = 'INSERT INTO List_of_candidates Values (%s,%s)' % (candidate_list["Candidate_Name"],candidate_list["Ballot_ID"])

            # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertHistoricalElectionData():
    try:
        hist_dets = {}
        print("Enter historical details:")
        hist_dets["Event_ID"] = input("Enter 12-character Event ID:")
        hist_dets["Date_of_event"] = input("Enter Date of event:")
        hist_dets["Election_type"] = input("Enter Type of election:")
        hist_dets["Total_Votes"] = int(input("Enter Total votes in that event:"))
        name = input("Enter Name of Winner (FName LName):")
        name = name.split()
        hist_dets["Fname"] = name[0]
        hist_dets["Lname"] = name[1]
        hist_dets["Turnout_rate"] = int(input("Enter Turnout rate of this event:"))
        for key in hist_dets:
            if type(hist_dets[key]) == str:
                hist_dets[key] = '"' + hist_dets[key] + '"'
        query = 'INSERT INTO Historical_Data Values (%s,%s,%s,%d,%s,%s,%d)' % (hist_dets["Event_ID"],hist_dets["Date_of_event"],hist_dets["Election_type"],hist_dets["Total_Votes"],hist_dets["Fname"],hist_dets["Lname"],hist_dets["Turnout_rate"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertRecords():
    try:
        vote_dets = {}
        print("Enter Voter Records:")
        vote_dets["voter_ID"] = input("Enter 8-character Voter ID:")
        vote_dets["Status_of_vote"] = input("Enter Status of vote:")
        vote_dets["Voted_on"] = input("Enter Date of vote:")
        for key in vote_dets:
            if type(vote_dets[key]) == str:
                vote_dets[key] = '"' + vote_dets[key] + '"'
        query = 'INSERT INTO Vote_Status(Voter_ID,Status_of_vote,Voted_on) Values (%s,%s,%s)' % (vote_dets["voter_ID"],vote_dets["Status_of_vote"],vote_dets["Voted_on"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def insertDemographicData(voterID,dob):
    try:
        demo_details = {}
        print("Enter demographic details:")
        demo_details["voter_ID"] = voterID
        # print(int(dob[0:3]))
        age = 2023-int(dob[0:4])
        # print(dob)
        # print(age)
        demo_details["Age"] = age
        demo_details["Gender"] = input("Enter Gender:")
        demo_details["Ethnicity"] = input("Enter Ethnicity:")
        demo_details["Education_level"]=input("Enter Education Level:")
        demo_details["Income_level"]=input("Enter Level of Income:")
        for key in demo_details:
            if type(demo_details[key]) == str:
                demo_details[key] = '"' + demo_details[key] + '"'
        query = 'INSERT INTO Demographic_Information(Voter_ID,Age,Gender,Ethnicity,Education_level,Income_level) Values (%s,%d,%s,%s,%s,%s)' % (demo_details["voter_ID"],int(demo_details["Age"]),demo_details["Gender"],demo_details["Ethnicity"],demo_details["Education_level"],demo_details["Income_level"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

# delete

def deleteVoter():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["voterID"] = input("Enter 8-character Voter ID:")
        for key in voter_details:
            voter_details[key] = '"' + voter_details[key] + '"'
        query = 'DELETE FROM Voters WHERE Voter_ID=%s' % (voter_details["voterID"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def deleteEvent():
    try:
        event_details = {}
        print("Enter Event details:")
        event_details["elecID"] = input("Enter 12-character Event ID:")
        for key in event_details:
            event_details[key] = '"' + event_details[key] + '"'
        query = 'DELETE FROM Election_events WHERE Event_ID = %s' % (event_details["elecID"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Event Deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def deleteStation():
    try:
        station_details = {}
        print("Enter Station details:")
        station_details["stationID"] = input("Enter 4-character Station ID:")
        for key in station_details:
            station_details[key] = '"' + station_details[key] + '"'
        query = 'DELETE FROM Polling_Stations WHERE Station_ID = %s' % (station_details["stationID"])

        # print(query)
        cur.execute(query)
        con.commit()
        print("Polling Station Deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return
    
def deleteParty():
    try:
        party_details = {}
        print("Enter Party details:")
        party_details["BallotID"] = input("Enter 4-character Ballot ID:")
        party_details["PartyName"]=input("Enter Party Name:")
        for key in party_details:
            party_details[key] = '"' + party_details[key] + '"'
        query = 'DELETE FROM List_of_parties WHERE Ballot_ID = %s AND Party_Name = %s' % (party_details["BallotID"],party_details["PartyName"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def deleteCandidate():
    try:
        candidate_details = {}
        print("Enter Candidate details:")
        candidate_details["canID"] = input("Enter 7-character Candidate ID:")
        for key in candidate_details:
            if type(candidate_details[key]) == str:
                candidate_details[key] = '"' + candidate_details[key] + '"'
        query = 'DELETE FROM Candidates WHERE Candidate_ID = %s' % (candidate_details["canID"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Deleted From Database")
    except Exception as e:
        con.rollback()
        print("Failed to Delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def deleteOfficial():
    try:
        off_dets = {}
        print("Enter Election Official details:")
        off_dets["Official_ID"] = input("Enter 5-character Official ID:")
        for key in off_dets:
            off_dets[key] = '"' + off_dets[key] + '"'
        query = 'DELETE FROM Election_Officials WHERE Official_ID = %s' % (off_dets["Official_ID"])
 
        # print(query)
        cur.execute(query)
        con.commit()
        print("Official deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

# update

def updateVoter():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["voterID"] = input("Enter 8-character Voter ID:")
        name = input("Enter Name (FName LName):")
        if name != '':
            name = name.split()
            voter_details["Fname"] = name[0]
            voter_details["Lname"] = name[1]
        else:
            voter_details["Fname"] = ''
            voter_details["Lname"] = ''
        voter_details["Phone"] = input("Enter 10 digit Mobile Number:")
        voter_details["email"] = input("Enter E-mail ID:")
        voter_details["dob"] = input("Enter D.O.B in (YYYY-MM-DD):")
        voter_details["Address_voter"]=input("Enter Address:")
        voter_details["Station_ID"]=input("Enter 4 digit station ID:")
        voter_details["eventID"] = ''
        attr_list = ["Voter_ID","Fname","Lname","Phone_Number","Email_ID","DOB","Address_voter","Station_ID","Event_ID"]
        set_string = ''
        i = 0
        for key in voter_details:
            if voter_details[key] != '':
                if type(voter_details[key]) == str:
                    set_string += f'{attr_list[i]} = "{voter_details[key]}",'
                else:
                    set_string += f'{attr_list[i]} = {voter_details[key]}, '
            i += 1
        set_string = set_string[0:-1]
        # print(f'\n{set_string}\n')
        query = f'UPDATE Voters SET {set_string} WHERE Voter_ID = {voter_details["voterID"]}'
        # print(f'\n{query}\n')
        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateEvent():
    try:
        event_details = {}
        print("Enter Event details:")
        event_details["elecID"] = input("Enter 12-character Event ID:")
        event_details["date"] = input("Enter date of event (YYYY-MM-DD):")
        event_details["type_event"]=input("Enter event type:")
        event_details["ElectionType"]=input("Enter Election type:")
        attr_list = ["Event_ID","Date_of_event","Type_event","Election_Type"]
        set_string = ''
        i = 0
        for key in event_details:
            if event_details[key] != '':
                if type(event_details[key]) == str:
                    set_string += f'{attr_list[i]} = "{event_details[key]}",'
                else:
                    set_string += f'{attr_list[i]} = {event_details[key]}, '
            i += 1
        set_string = set_string[0:-1]
        # print(f'\n{set_string}\n')
        query = f'UPDATE Election_events SET {set_string} WHERE Event_ID = {event_details["elecID"]}'
        # print(f'\n{query}\n')
        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateStation():
    try:
        station_details = {}
        print("Enter Station details:")
        station_details["stationID"] = input("Enter 4-character Station ID:")
        station_details["Address_station"]=input("Enter Address:")
        station_details["Phone"] = input("Enter 10 digit Mobile Number:")
        station_details["email"] = input("Enter E-mail ID:")
        station_details["eventID"] = input("Enter 12 digit Event-ID:")
        attr_list = ["Station_ID","Address_station","Phone_Number","Email_ID","Event_ID"]
        set_string = ''
        i = 0
        for key in station_details:
            if station_details[key] != '':
                if type(station_details[key]) == str:
                    set_string += f'{attr_list[i]} = "{station_details[key]}",'
                else:
                    set_string += f'{attr_list[i]} = {station_details[key]}, '
            i += 1
        set_string = set_string[0:-1]
        # print(f'\n{set_string}\n')
        query = f'UPDATE Polling_Stations SET {set_string} WHERE Station_ID = {station_details["stationID"]}'
        # print(f'\n{query}\n')
        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateParty():
    try:
        Party_dets = {}
        print("Enter Party details:")
        Party_dets["Ballot_ID"] = input("Enter 4-character Ballot ID:")
        Party_dets["Party_Name"] = input("Enter Party Name:")
        attr_list = ["Ballot_ID","Party_Name"]
        set_string = ''
        i = 0
        for key in Party_dets:
            if Party_dets[key] != '':
                if type(Party_dets[key]) == str:
                    set_string += f'{attr_list[i]} = "{Party_dets[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {Party_dets[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE List_of_parties SET {set_string} WHERE Ballot_ID = {Party_dets["Ballot_ID"]}'

        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated the Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateCandidate():
    try:
        cand_dets = {}
        print("Enter Candidate details:")
        cand_dets["Candidate_ID"] = input("Enter 7-character Candidate ID:")
        name = input("Enter Name (FName LName):")
        if name != '':
            name = name.split()
            cand_dets["Fname"] = name[0]
            cand_dets["Lname"] = name[1]
        else:
            cand_dets["Fname"] = ''
            cand_dets["Lname"] = ''        
        cand_dets["Phone_Num"] = input("Enter Phone Number:")
        cand_dets["Email_id"] = input("Enter Email_id:")
        cand_dets["Party_Affiliation"]=input("Enter Education Level:")
        cand_dets["Candidate_exp"]=int(input("Enter expenditure of candidate:"))
        cand_dets["event_id"]=input("Enter 7-character Event ID:")
        attr_list = ["Candidate_ID","Fname","Lname","Phone_Num","Email_id","Party_Affiliation","Candidate_exp","event_id"]
        set_string = ''
        i = 0
        for key in cand_dets:
            if cand_dets[key] != '':
                if type(cand_dets[key]) == str:
                    set_string += f'{attr_list[i]} = "{cand_dets[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {cand_dets[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE Candidates SET {set_string} WHERE Candidate_ID = {cand_dets["Candidate_ID"]}'

        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated the Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateOfficial():
    try:
        off_dets = {}
        print("Enter Official details:")
        off_dets["Official_ID"] = input("Enter 5-character Officer ID:")
        name = input("Enter Name (FName LName):")
        if name != '':
            name = name.split()
            off_dets["Fname"] = name[0]
            off_dets["Lname"] = name[1]
        else:
            off_dets["Fname"] = ''
            off_dets["Lname"] = ''        
        off_dets["Phone_Num"] = input("Enter Phone Number:")
        off_dets["Email_id"] = input("Enter Email_id:")
        off_dets["Role_official"]=input("Enter Role of Officer:")
        off_dets["event_id"]=input("Enter 7-character Event ID:")
        attr_list = ["Official_ID","Fname","Lname","Phone_Num","Email_id","Role_official","event_id"]
        set_string = ''
        i = 0
        for key in off_dets:
            if off_dets[key] != '':
                if type(off_dets[key]) == str:
                    set_string += f'{attr_list[i]} = "{off_dets[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {off_dets[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE Election_Officials SET {set_string} WHERE Official_ID = {off_dets["Official_ID"]}'

        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated the Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return
def updateHistoricalElectionData():
    try:
        hist_dets = {}
        print("Enter historical details:")
        hist_dets["Event_ID"] = input("Enter 12-character Event ID:")
        hist_dets["Date_of_event"] = input("Enter Date of event:")
        hist_dets["Election_type"] = input("Enter Type of election:")
        hist_dets["Total_Votes"] = input("Enter Total votes in that event:")
        if hist_dets["Total_Votes"]:
            hist_dets["Total_Votes"] = int(hist_dets["Election_type"])
        name = input("Enter Name (FName LName):")
        if name != '':
            name = name.split()
            hist_dets["Fname"] = name[0]
            hist_dets["Lname"] = name[1]
        else:
            hist_dets["Fname"] = ''
            hist_dets["Lname"] = ''
        hist_dets["Turnout_rate"] = input("Enter Turnout rate of this event:")
        if hist_dets["Turnout_rate"]:
            hist_dets["Turnout_rate"] = int(hist_dets["Turnout_rate"])
        attr_list = ["Event_ID","Date_of_event","Election_type","Total_Votes","Fname","Lname","Turnout_rate"]
        set_string = ''
        i = 0
        for key in hist_dets:
            if hist_dets[key] != '':
                if type(hist_dets[key]) == str:
                    set_string += f'{attr_list[i]} = "{hist_dets[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {hist_dets[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE Historical_Data SET {set_string} WHERE Event_ID = {hist_dets["Event_ID"]}'

        print(query)
        cur.execute(query)
        con.commit()
        print("Updated Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return

def updateVoterstatus():
    try:
        vote_dets = {}
        print("Enter Voter Records:")
        vote_dets["voter_ID"] = input("Enter 8-character Voter ID:")
        vote_dets["Status_of_vote"] = input("Enter Status of vote:")
        vote_dets["Voted_on"] = input("Enter Date of vote:")
        attr_list = ["Voter_ID","Status_of_vote","Voted_on"]
        set_string = ''
        i = 0
        for key in vote_dets:
            if vote_dets[key] != '':
                if type(vote_dets[key]) == str:
                    set_string += f'{attr_list[i]} = "{vote_dets[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {vote_dets[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE Vote_Status SET {set_string} WHERE Voter_ID = {vote_dets["voter_ID"]}'

        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated the Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return

def updateDemographicData():
    try:
        demo_details = {}
        print("Enter demographic details:")
        demo_details["voter_ID"] = input("Enter 8-character Voter ID:")
        demo_details["Age"] = int(input("Enter Age( >=18):"))
        demo_details["Gender"] = input("Enter Gender:")
        demo_details["Ethnicity"] = input("Enter Ethnicity:")
        demo_details["Education_level"]=input("Enter Education Level:")
        demo_details["Income_level"]=input("Enter Level of Income:")
        attr_list = ["Voter_ID","Age","Gender","Ethnicity","Education_level","Income_level"]
        set_string = ''
        i = 0
        for key in demo_details:
            if demo_details[key] != '':
                if type(demo_details[key]) == str:
                    set_string += f'{attr_list[i]} = "{demo_details[key]}", '
                else:
                    set_string += f'{attr_list[i]} = {demo_details[key]},'
            i += 1
        set_string = set_string[0:-2]
        query = f'UPDATE Demographic_Information SET {set_string} WHERE Voter_ID = {demo_details["voter_ID"]}'

        # print(query)
        cur.execute(query)
        con.commit()
        print("Updated the Database")
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return

# Sort

def sortVoter():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["order"] = input("Enter the Order to sort:")
        if voter_details["order"].lower() == "ascending":
            voter_details["order"] = "ASC"
        elif voter_details["order"].lower() == "descending":
            voter_details["order"] = "DESC"
        query = 'SELECT * FROM Voters LEFT JOIN Demographic_Information On Voters.Voter_ID = Demographic_Information.Voter_ID ORDER BY Age %s' % (voter_details["order"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Sorted")
        rows = cur.fetchall()
        for row in rows:
                print(f"{row['Voter_ID']} {row['Fname']} {row['Lname']} {row['Age']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def sortVotersOnIncome():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["order"] = input("Enter the Order to sort:")
        if voter_details["order"].lower() == "ascending":
            voter_details["order"] = "ASC"
        elif voter_details["order"].lower() == "descending":
            voter_details["order"] = "DESC"
        query = 'SELECT * FROM Voters LEFT JOIN Demographic_Information On Voters.Voter_ID = Demographic_Information.Voter_ID ORDER BY Income_level %s' % (voter_details["order"])
        # print(query)
        cur.execute(query)
        con.commit()
        print("Sorted")
        rows = cur.fetchall()
        for row in rows:
                print(f"{row['Voter_ID']} {row['Fname']} {row['Lname']} {row['Income_level']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

#Projection
def voterContactInfo():
    try:
        query = 'SELECT * FROM Voters'
        # print(query)
        cur.execute(query)
        con.commit()
        print("Voter Contact Details:")
        rows = cur.fetchall()
        for row in rows:
                print(f"Name: {row['Fname']} {row['Lname']} Phone Number: {row['Phone_Number']} Email-Id: {row['Email_ID']} ")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
def candidatesInfo():
    try:
        query = 'SELECT * FROM Candidates'
        # print(query)
        cur.execute(query)
        con.commit()
        print("Candidate Details:")
        rows = cur.fetchall()
        for row in rows:
                print(f"Name: {row['Fname']} {row['Lname']} Party: {row['Party_Affiliation']} ")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
def voterPollingStations():
    try:
        query = 'SELECT * FROM Voters JOIN Polling_Stations ON Voters.Station_ID = Polling_Stations.Station_ID'
        # print(query)
        cur.execute(query)
        con.commit()
        print("Voter Polling Stations:")
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
                print(f"Name: {row['Fname']} {row['Lname']} Station Address: {row['Address_station']} {row['Station_ID']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
#search
def station_for_voter():
    vot_id=input("Enter required voter ID:")
    try:
        query = f'SELECT * FROM Voters JOIN Polling_Stations ON Voters.Station_ID = Polling_Stations.Station_ID WHERE Voters.Voter_ID={vot_id}'
        # print(query)
        cur.execute(query)
        con.commit()
        print("Voter Polling Stations:")
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
                print(f"Station Address: {row['Address_station']} {row['Station_ID']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
def voter_by_id():
    vot_id=input("Enter required voter ID:")
    try:
        query=f'SELECT * from Voters Where Voters.Voter_ID={vot_id}'
        cur.execute(query)
        con.commit()
        print("Voter Details")
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
                print(f"Name: {row['Fname']} {row['Lname']} Phone Number: {row['Phone_Number']} Email-Id: {row['Email_ID']} ")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
def candidate_by_party():
    party_name=input("Enter Party Name:")
    try:
        query=f'SELECT * from Candidates Where Candidates.Party_Affiliation LIKE "%{party_name}%"'
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
                print(f"Candidate Id: {row['Candidate_ID']},Name: {row['Fname']} {row['Lname']}, party:  {row['Party_Affiliation']}")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
def station_by_address():
    address=input("Enter address to search:")
    try:
        query=f'SELECT * from Polling_Stations Where Address_station LIKE "%{address}%"'
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
            print(f"Station Id: {row['Station_ID']},Phone Number:  {row['Phone_Number']},Email-ID: {row['Email_ID']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
# aggregate
def totalvoters():
    try:
        voter_details = {}
        print("Enter voter details:")
        voter_details["Event_ID"] = input("Enter the Event ID:")
        voter_details["Status_of_vote"] = "YES"
        voter_details["Status_of_vote"] = '"' + voter_details["Status_of_vote"] + '"'
        query = 'SELECT COUNT(*) AS Voters FROM Voters JOIN Vote_Status ON Voters.Voter_ID = Vote_Status.Voter_ID WHERE Event_ID = %s AND Vote_Status.Status_of_vote = %s GROUP BY Event_ID' % (voter_details["Event_ID"], voter_details["Status_of_vote"])
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
                print(f"Total voters participated: {row['Voters']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def avgfund():
    try:
        candidate_details = {}
        print("Enter voter details:")
        candidate_details["Candidate_ID"] = input("Enter the Candidate ID:")
        query = 'SELECT AVG(Amount) AS Avgfund FROM Campaign_finance WHERE Candidate_ID = %s GROUP BY Candidate_ID' % (candidate_details["Candidate_ID"])
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        for row in rows:
                print(f"Average fund: {row['Avgfund']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
#analysis
def get_age_range_from_user():
    try:
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        return min_age, max_age
    except ValueError:
        print("Please enter valid age values.")
        return None, None

def Get_PP_By_Age():
    age_range = get_age_range_from_user()
    if age_range[0] is not None and age_range[1] is not None:
        try:
            minAge = int(age_range[0])
            maxAge = int(age_range[1])
            # Define the SQL query to get the poll percentage based on age range
            query = "SELECT COUNT(V.Voter_ID) AS Total_Voters, SUM(CASE WHEN VS.Status_of_vote = 'Yes' THEN 1 ELSE 0 END) AS Voted_Yes FROM Voters V JOIN Demographic_Information D ON V.Voter_ID = D.Voter_ID JOIN Vote_Status VS ON V.Voter_ID = VS.Voter_ID WHERE D.Age >= %d AND D.Age <= %d" %(minAge,maxAge)
       

            # Execute the query with user-defined age range
            cur.execute(query)
            result = cur.fetchone()
            if result:
                total_voters = result["Total_Voters"]
                voted_yes = result["Voted_Yes"]
                if total_voters > 0:
                    poll_percentage = (voted_yes / total_voters) * 100
                    print(f"Poll percentage for age range {age_range[0]} to {age_range[1]}: {poll_percentage:.2f}%")
                    return
                else:
                    print("No voters in the specified age range.")
                    return
        except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to the database")
            tmp = input("Enter any key to CONTINUE>")

def get_gender_from_user():
    gender = input("Enter gender (Male/Female/Other): ")
    return gender

def Get_PP_By_Gender():
    gender = get_gender_from_user()
    if gender:
        try:
            

            # Define the SQL query to get the poll percentage based on gender
            query = """
                SELECT COUNT(V.Voter_ID) AS Total_Voters, SUM(CASE WHEN VS.Status_of_vote = 'Yes' THEN 1 ELSE 0 END) AS Voted_Yes FROM Voters V JOIN Demographic_Information D ON V.Voter_ID = D.Voter_ID JOIN Vote_Status VS ON V.Voter_ID = VS.Voter_ID WHERE D.Gender = '%s' """ % (gender)
            
            # Execute the query with user-defined gender
            cur.execute(query)
            
            result = cur.fetchone()

            if result:
                total_voters = result["Total_Voters"]
                voted_yes = result["Voted_Yes"]
                if total_voters > 0:
                    poll_percentage = (voted_yes / total_voters) * 100
                    print(f"Poll percentage for {gender} voters: {poll_percentage:.2f}%")
                    return
                else:
                    print(f"No {gender} voters found.")
                    return
        except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to the database")
            tmp = input("Enter any key to CONTINUE>")

def get_income_range_from_user():
    try:
        lower_bound = int(input("Enter lower income bound: "))
        upper_bound = int(input("Enter upper income bound: "))
        return lower_bound, upper_bound
    except ValueError:
        print("Please enter valid income values.")
        return None, None

def Get_PP_By_Income():
    income_range = get_income_range_from_user()
    if income_range[0] is not None and income_range[1] is not None:
        try:
            lb = int(income_range[0]) 
            ub = int(income_range[1])

            # Define the SQL query to get the poll percentage based on income range
            query = """
                SELECT COUNT(V.Voter_ID) AS Total_Voters, SUM(CASE WHEN VS.Status_of_vote = 'Yes' THEN 1 ELSE 0 END) AS Voted_Yes FROM Voters V JOIN Demographic_Information D ON V.Voter_ID = D.Voter_ID JOIN Vote_Status VS ON V.Voter_ID = VS.Voter_ID WHERE D.Income_level >= %d AND D.Income_level <= %d""" % (lb,ub)

            # Execute the query with user-defined income range
            cur.execute(query)
            result = cur.fetchone()

            if result:
                total_voters = result["Total_Voters"]
                voted_yes = result["Voted_Yes"]
                if total_voters > 0:
                    poll_percentage = (voted_yes / total_voters) * 100
                    print(f"Poll percentage for income range ${income_range[0]} to ${income_range[1]}: {poll_percentage:.2f}%")
                    return
                else:
                    print("No voters in the specified income range.")
                    return
        except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to the database")
            tmp = input("Enter any key to CONTINUE>")
def getReport():
    pass

def Insert():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1. Insert Voter")  
    print("2. Log Event") 
    print("3. Create New Station")  
    print("4. Log Party") 
    print("5. Log Candidate")  
    print("6. Insert Campaign Finance") 
    print("7. Insert Election Official")  
    print("8. Insert Historical Election Data") 
    print("9. Insert Records") 
    print("10. Insert Candidate into ballot") 
    print("11. Exit from Insert") 
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 11:
        pass
    elif(ch == 1):
        insertVoter()
    elif(ch == 2):
        createEvent()
    elif(ch == 3):
        insertStation()
    elif(ch == 4):
        insertParty()
    elif(ch == 5):
        insertCandidate()
    elif(ch == 6):
        insertCampaignFinance()
    elif(ch == 7):
        insertOfficial()
    elif(ch == 8):
        insertHistoricalElectionData()
    elif(ch == 9):
        insertRecords()
    elif(ch == 10):
        insertCandidateToList()
    else:
        print("Error: Invalid Option")
    # print("Function executed successfully")
def Delete():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1. Delete Voter")  
    print("2. Delete Event") 
    print("3. Delete Station")  
    print("4. Delete Party") 
    print("5. Delete Candidate")  
    print("6. Delete Election Official")
    print("7.Exit from Delete")    
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 7:
        pass
    elif(ch == 1):
        deleteVoter()
    elif(ch == 2):
        deleteEvent()
    elif(ch == 3):
        deleteStation()
    elif(ch == 4):
        deleteParty()
    elif(ch == 5):
        deleteCandidate()
    elif(ch == 6):
        deleteOfficial()
    else:
        print("Error: Invalid Option")

def Update():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1. Update Voter")  
    print("2. Update Event") 
    print("3. Update Station")  
    print("4. Update Party") 
    print("5. Update Candidate")  
    print("6. Update Election Official")  
    print("7. Update Historical Election Data") 
    print("8. Update Voter Status")  
    print("9. Update Demographic Data")
    print("10.Exit from Update")  
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 10:
        pass
    elif(ch == 1):
        updateVoter()
    elif(ch == 2):
        updateEvent()
    elif(ch == 3):
        updateStation()
    elif(ch == 4):
        updateParty()
    elif(ch == 5):
        pass
        updateCandidate()
    elif(ch == 6):
        pass
        updateOfficial()
    elif(ch == 7):
        updateHistoricalElectionData()
    elif(ch == 8):
        updateVoterstatus()
    elif(ch == 9):
        updateDemographicData()
    else:
        print("Error: Invalid Option")

def Sort():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1.Sort voters by Age")  
    print("2.Sort voters by Income")
    print("3.Exit from sort")  
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 3:
        pass
    elif(ch == 1):
        sortVoter()
    elif(ch == 2):
        sortVotersOnIncome()
    else:
        print("Error: Invalid Option")

def Aggregate():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1.Total voters participated in an event")  
    print("2.Average of campaign fund")
    print("3.Exit from aggregate")  
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 3:
        pass
    elif(ch == 1):
        totalvoters()
    elif(ch == 2):
        avgfund()
    else:
        print("Error: Invalid Option")
def Project():
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1.Voter Contact Details")  
    print("2.Candidates Information")
    print("3.Voter Polling Stations") 
    print("4.Exit from Project")  
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 4:
        pass
    elif(ch == 1):
        voterContactInfo()
    elif(ch == 2):
        candidatesInfo()
    elif(ch == 3):
        voterPollingStations()
    else:
        print("Error: Invalid Option")
def Search():
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1.Polling station assigned for a Voter")  
    print("2.Details of a Voter") 
    print("3.Candidate representing a Party") 
    print("4.Polling Station based on Address")
    print("5.Exit from Project")  
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 5:
        pass
    elif(ch == 1):
        station_for_voter()
        pass
    elif(ch == 2):
        voter_by_id()
        pass
    elif(ch == 3):
        candidate_by_party()
        pass
    elif(ch == 4):
        station_by_address()
        pass
    else:
        print("Error: Invalid Option")
def Get_Poll():
    """
    Function that maps helper functions to option entered
    """
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    tmp = sp.call('clear', shell=True)
    print("1. Based On Age")  
    print("2. Based On Gender") 
    print("3. Based On Income")  

    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    if ch == 4:
        pass
    elif(ch == 1):
        Get_PP_By_Age()
    elif(ch == 2):
        Get_PP_By_Gender()
    elif(ch == 3):
        Get_PP_By_Income()
    else:
        print("Error: Invalid Option")        

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    print("reached")
    if(ch == 1):
        Insert()
    elif(ch == 2):
        Delete()
    elif(ch == 3):
        Update()
    elif(ch == 4):
        Sort()
    elif(ch == 5):
        Get_Poll()
    elif(ch == 6):
        Aggregate()
    elif(ch == 7):
        Project()
    elif(ch == 8):
        Search()
    elif(ch == 10):
        getReport()
    else:
        print("Error: Invalid Option")
def AddKey():
    new_key = input("Enter key to add")
    your_key = input("Enter your key")
    if your_key in keys:
        keys.append(new_key)
    else:
        print("Invalid key!!!")
        print("Access Denied!!!")
def AdminAccess():

    print("Please enter your access key:")
    key = input()
    if key in keys:
        try:
            while True:
                tmp = sp.call('clear', shell=True)
                print("1. Insert") 
                print("2. Delete")   
                print("3. Update") 
                print("4. Sort") 
                print("5. Get Poll Percentage Based On Social Tendencies")
                print("6. Aggregate")  
                print("7. Project")
                print("8. Search")
                print("9.Add access key")
                print("10.Get Report")
                print("11. Exit")  
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 11:
                    return
                elif(ch == 9):
                    AddKey()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

        except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to the database")
            tmp = input("Enter any key to CONTINUE>")
    else:
        print("Invalid key!!!")
        print("Access Denied!!!")
        return

def UserAccess():
    try:
        while True:
            tmp = sp.call('clear', shell=True)
            print("4. Sort") 
            print("5. Get Poll Percentage Based On Social Tendencies")
            print("6. Aggregate")  
            print("7. Project")
            print("8. Search")
            print("10. Get Report")
            print("11. Exit")  
            ch = int(input("Enter choice> "))
            tmp = sp.call('clear', shell=True)
            if ch == 10:
                return
            else:
                dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to the database")
        tmp = input("Enter any key to CONTINUE>")

def accessGate():
        while True: 
            tmp = sp.call('clear', shell=True)
            print("Enter yor mode:")
            print("1.User")
            print("2.Administrator")
            print("3.Exit")
            ch = int(input("Enter choice> "))
            tmp = sp.call('clear', shell=True)
            if ch == 3:
                exit()
            elif(ch == 1):
                UserAccess()
            elif(ch == 2):
                AdminAccess()

while True:
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    pwd = input("Password: ")
    con = pymysql.connect(
        user=username,
        password=pwd,
        db='Election_Database',
        cursorclass=pymysql.cursors.DictCursor
    )        
    tmp = sp.call('clear', shell=True)

    if con.open:
        print("Connected")
    else:
        print("Failed to connect")

    tmp = input("Enter any key to CONTINUE>")
    with con.cursor() as cur:
        accessGate()
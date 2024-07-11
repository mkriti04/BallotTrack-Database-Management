CREATE DATABASE Election_Database;

USE Election_Database;

CREATE TABLE Election_events (
    Event_ID CHAR(12) PRIMARY KEY,
    Date_of_event DATE NOT NULL,
    Type_event VARCHAR(255) NOT NULL,
    Election_Type VARCHAR(255) NOT NULL
);

CREATE TABLE Polling_Stations (
    Station_ID CHAR(4) PRIMARY KEY,
    Address_station VARCHAR(255) NOT NULL,
    Phone_Number CHAR(10) NOT NULL,
    Email_ID VARCHAR(255),
    Event_ID CHAR(12) NOT NULL,
    Foreign KEY(Event_ID) REFERENCES Election_events(Event_ID)
     ON DELETE CASCADE 
);

CREATE TABLE Voters (
    Voter_ID CHAR(8),
    Fname VARCHAR(255) NOT NULL,
    Lname VARCHAR(255) NOT NULL,
    Phone_Number CHAR(10),
    Email_ID VARCHAR(255),
    DOB DATE NOT NULL, 
    Address_voter VARCHAR(255) NOT NULL,
    Station_ID CHAR(4),
    Event_ID CHAR(12),
    PRIMARY KEY(Voter_ID, Event_ID),
    FOREIGN KEY(Station_ID) REFERENCES Polling_Stations(Station_ID)  ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(Event_ID) REFERENCES Election_events(Event_ID) ON DELETE CASCADE 
);

CREATE TABLE Demographic_Information (
    Voter_ID CHAR(8) PRIMARY KEY,
    Age INT CHECK (Age >= 18),
    Gender VARCHAR(255),
    Ethnicity VARCHAR(255),
    Education_level VARCHAR(255),
    Income_level VARCHAR(255),
    FOREIGN KEY(Voter_ID) REFERENCES Voters(Voter_ID)  ON DELETE CASCADE 
);

CREATE TABLE Candidates (
    Candidate_ID CHAR(7) PRIMARY KEY,
    Fname VARCHAR(255) NOT NULL,
    Lname VARCHAR(255) NOT NULL,
    Phone_Number CHAR(10) NOT NULL,
    Email_ID VARCHAR(255),
    Party_Affiliation VARCHAR(255) NOT NULL,
    Candidate_exp INT NOT NULL,
    Event_ID CHAR(12) NOT NULL,
    FOREIGN KEY(Event_ID) REFERENCES Election_events(Event_ID)  ON DELETE CASCADE
);

CREATE TABLE Ballots (
    Ballot_ID CHAR(4) PRIMARY KEY,
    Election_event VARCHAR(255) NOT NULL,
    Station_ID CHAR(4) NOT NULL,
    FOREIGN KEY(Station_ID) REFERENCES Polling_Stations(Station_ID) ON DELETE CASCADE
);

CREATE TABLE List_of_candidates (
    Candidate_Name VARCHAR(255) PRIMARY KEY,
    Ballot_ID CHAR(4) NOT NULL,
    FOREIGN KEY(Ballot_ID) REFERENCES Ballots(Ballot_ID) ON DELETE CASCADE
);

CREATE TABLE List_of_parties (
    Ballot_ID CHAR(4),
    Party_Name VARCHAR(255),
    PRIMARY KEY(Ballot_ID, Party_Name),
    FOREIGN KEY(Ballot_ID) REFERENCES Ballots(Ballot_ID) ON DELETE CASCADE
);

CREATE TABLE Historical_Data (
    Event_ID CHAR(12) PRIMARY KEY,
    Date_of_event DATE NOT NULL,
    Election_type VARCHAR(255) NOT NULL,
    Total_Votes INT NOT NULL,
    Fname VARCHAR(255) NOT NULL,
    Lname VARCHAR(255) NOT NULL,
    Turnout_rate INT NOT NULL,
    FOREIGN KEY(Event_ID) REFERENCES Election_events(Event_ID) ON DELETE CASCADE
);

CREATE TABLE Vote_Status (
    Voter_ID CHAR(8) PRIMARY KEY,
    Status_of_vote VARCHAR(255) NOT NULL,
    Voted_on DATE NOT NULL,
    FOREIGN KEY(Voter_ID) REFERENCES Voters(Voter_ID) ON DELETE CASCADE
);

CREATE TABLE Election_Officials (
    Official_ID CHAR(5) PRIMARY KEY,
    Fname VARCHAR(255) NOT NULL,
    Lname VARCHAR(255)NOT NULL,
    Phone_number CHAR(10) NOT NULL,
    Email_ID VARCHAR(255),
    Role_official VARCHAR(255) NOT NULL,
    Event_ID CHAR(12) NOT NULL,
    Foreign KEY(Event_ID) REFERENCES Election_events(Event_ID) ON DELETE CASCADE
);

CREATE TABLE Event_station (
    Station_ID CHAR(4),
    Event_ID CHAR(12),
    PRIMARY KEY(Station_ID, Event_ID),
    FOREIGN KEY(Event_ID) REFERENCES Election_Officials(Event_ID) ON DELETE CASCADE,
    FOREIGN KEY(Station_ID) REFERENCES Polling_Stations(Station_ID) ON DELETE CASCADE
);

CREATE TABLE Campaign_finance (
    Transaction_ID CHAR(10) PRIMARY KEY,
    Amount INT,
    Candidate_ID CHAR(7) NOT NULL,
    Date_campaign DATE NOT NULL,
    FOREIGN KEY(Candidate_ID) REFERENCES Candidates(Candidate_ID) ON DELETE CASCADE
);

INSERT INTO Election_events
Values (202311300129,'2023-11-30',"Assembly","General");

INSERT INTO Election_events
Values (201905150021,'2019-05-15',"Parliment","General");

INSERT INTO Election_events
Values (202211031129,'2022-11-03',"Assembly","By Election");

INSERT INTO Election_events
Values (198001060013,'1980-01-06',"Parliment","General");

INSERT INTO Election_events
Values (201708231028,'2017-08-23',"Assembly","By Election");




INSERT INTO Polling_Stations
Values (1107,"15-8-1000/2/1/G,Khammam North,Telangana",6916969571,"dps.mamta@tselc.in",202311300129);

INSERT INTO Polling_Stations
Values (1104,"10-2-2/4,Samatha Nagar,Ongole East,Telangana",8013066985,"vb.mayuri@tselc.in",202311300129);

INSERT INTO Polling_Stations
Values (1098,"1-9-322P/4,VNR Nagar,Secunderabad South,Telangana",7369586969,"spyka.sec@tselc.in",202311300129);

INSERT INTO Polling_Stations
Values (1102,"5-502-1361/21/1,Pulivendhula,Kadapa West,Telangana",9169136901,"rps.hyd.@tselc.in",202311300129);

INSERT INTO Polling_Stations
Values (1196,"143-143-420/404/301,Erragutta Centre,Telangana",7702733269,"rit.gutta@tselc.in",202311300129);


INSERT INTO Voters
Values (29110011,"Yashwanth","Duggi",7989099505,"yashwanth.duggi@tsvoter.in",'1992-12-12',"15-8-1003/2/1/G,Khammam North,Telangana",1107,202311300129);

INSERT INTO Voters
Values (29110019,"Krishna","Koushik",8156365369,"krishna.koushik@tsvoter.in",'2004-09-09',"1-9-320P/4,VNR Nagar,Secunderabad South,Telangana",1098,202311300129);

INSERT INTO Voters
Values (29110039,"Sudha","Kunapareddy",7989036498,"sudha.k@tsvoter.in",'1976-05-03',"1-9-312P/4,VNR Nagar,Secunderabad South,Telangana",1098,202311300129);

INSERT INTO Voters
Values (29112343,"Vamseedhar","Vanarasi",8169369369,"vamseedhar.vanarasi@tsvoter.in",'1988-01-24',"143-143-410/404/301,Erragutta Centre,Telangana",1196,202311300129);

INSERT INTO Voters
Values (29112369,"Karthika","Chaganti",8365369369,"karthika.ch@tsvoter.in",'1949-05-11',"1949-143-410/404/301,Erragutta Centre,Telangana",1196,202311300129);

INSERT INTO Demographic_Information
Values (29112343,35,"Male","Parsi","Post Graduate","436000");

INSERT INTO Demographic_Information
Values (29112369,74,"Female","Jain","SSC",NULL);

INSERT INTO Demographic_Information
Values (29110039,47,"Female","Hindu","Graduate","125000");

INSERT INTO Demographic_Information
Values (29110011,30,"Male","Hindu","PHD","2100000");

INSERT INTO Demographic_Information
Values (29110019,19,"Male","Muslim","Graduate","4400000");

INSERT INTO Candidates
Values (1252323,"Vivek","Kavuri",7980099505,"kavuri.hryday@tscd.in","BJP",143690,202311300129);

INSERT INTO Candidates
Values (1252324,"Kriti","Madumadukala",8196365369,"kriti.m@tscd.in","BRS",35600,202311300129);

INSERT INTO Candidates
Values (1252327,"Jahnavi","Venkamsetty",7989666498,"jahnavi.vv@tscd.in","Janasena",90000,202311300129);

INSERT INTO Candidates
Values (1252325,"Chandana","Yalamanchili",8169367369,"chandana.y@tsvoter.in","TDP",132867,202311300129);

INSERT INTO Candidates
Values (1252328,"Sohan","Mupparapu",8363369369,"karthik.ch@tsvoter.in","YSRCP",696969,202311300129);

INSERT INTO Ballots
Values (1231,"TS Assembly Election 2023",1098);

INSERT INTO Ballots
Values (1234,"TS Assembly Election 2023",1107);

INSERT INTO Ballots
Values (1252,"TS Assembly Election 2023",1107);

INSERT INTO Ballots
Values (1421,"TS Assembly Election 2023",1196);

INSERT INTO Ballots
Values (1221,"TS Assembly Election 2023",1196);


INSERT INTO List_of_candidates
Values ("Kriti Madumadukala",1231);

INSERT INTO List_of_candidates
Values ("Jahnavi Venkamsetty",1252);

INSERT INTO List_of_candidates
Values ("Vivek Kavuri",1231);

INSERT INTO List_of_candidates
Values ("Chandana Yalamanchili",1234);

INSERT INTO List_of_candidates
Values ("Sohan Mupparapau",1234);

INSERT INTO List_of_parties
Values (1231,'BRS');

INSERT INTO List_of_parties
Values (1234,'BRS');

INSERT INTO List_of_parties
Values (1252,'BJP');

INSERT INTO List_of_parties
Values (1252,'TDP');

INSERT INTO List_of_parties
Values (1252,'BRS');

INSERT INTO Historical_Data
Values (202311300129,'2023-11-30',"General",150,"Vivek","Kavuri",44);

INSERT INTO Historical_Data
Values (201905150021,'2019-05-15',"General",5,"Vivek","Kavuri",78);

INSERT INTO Historical_Data
Values (202211031129,'2022-11-03',"By Election",100,"Kriti","Madumadukala",75);

INSERT INTO Historical_Data
Values (198001060013,'1980-01-06',"General",65,"Vivek","Kavuri",77);

INSERT INTO Historical_Data
Values (201708231028,'2017-08-23',"By Election",80,"Kriti","Madumadukala",78);

INSERT INTO Vote_Status
Values ("29110011","YES",'2023-11-30');

INSERT INTO Vote_Status
Values ("29110019","NO",'2023-11-30');

INSERT INTO Vote_Status
Values ("29110039","NO",'2023-11-30');

INSERT INTO Vote_Status
Values ("29112343","YES",'2023-11-30');

INSERT INTO Vote_Status
Values ("29112369","YES",'2023-11-30');


INSERT INTO Election_Officials
Values (23231,"Praneeth","Bommana",6344345394,"praneeth.b@tsec.in","executive",202311300129);

INSERT INTO Election_Officials
Values (23232,"Mitra","Somayaji",9344545342,"mitra.somayaji@tsec.in","supervisor",202311300129);

INSERT INTO Election_Officials
Values (23233,"Nijesh","Raghava",8919211702,"nijesh.r@tsec.in","polling officer",202311300129);

INSERT INTO Election_Officials
Values (23234,"Deekshitha","Sagiraju",9473145648,"deekshitha.sagiraju@tsec.in","preceding officer",202311300129);

INSERT INTO Election_Officials
Values (23235,"Vysistya","Karanam",7349345344,"vysh.karanam@tsec.in","sub-executive",202311300129);

INSERT INTO Event_station
Values (1107,202311300129);

INSERT INTO Event_station
Values (1104,202311300129);

INSERT INTO Event_station
Values (1098,202311300129);

INSERT INTO Event_station
Values (1102,202311300129);

INSERT INTO Event_station
Values (1196,202311300129);

INSERT INTO Campaign_finance
Values (3771772772,14369,1252323,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772773,35600,1252323,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772774,90000,1252327,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772775,132867,1252325,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772776,696969,1252328,'2023-01-31');
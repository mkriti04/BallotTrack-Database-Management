INSERT INTO Election_events
Values (202311300129,2023-11-30,"Assembly","General");

INSERT INTO Election_events
Values (201905150021,2019-05-15,"Parliment","General");

INSERT INTO Election_events
Values (202211031129,2022-11-03,"Assembly","By Election");

INSERT INTO Election_events
Values (198001060013,1980-01-06,"Parliment","General");

INSERT INTO Election_events
Values (201708231028,2017-08-23,"Assembly","By Election");



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
Values (29110011,"Yashwanth","Duggi",7989099505,"yashwanth.duggi@tsvoter.in",'2004-12-12',"15-8-1003/2/1/G,Khammam North,Telangana",1107,202311300129);

INSERT INTO Voters
Values (29110019,"Krishna","Koushik",8156365369,"krishna.koushik@tsvoter.in",'2004-09-09',"1-9-320P/4,VNR Nagar,Secunderabad South,Telangana",1098,202311300129);

INSERT INTO Voters
Values (29110039,"Sudhan","Kunapareddy",7989036498,"sudhan.k@tsvoter.in",'2004-05-03',"1-9-312P/4,VNR Nagar,Secunderabad South,Telangana",1098,202311300129);

INSERT INTO Voters
Values (29112343,"Vamseedhar","Vanarasi",8169369369,"vamseedhar.vanarasi@tsvoter.in",'2004-01-24',"143-143-410/404/301,Erragutta Centre,Telangana",1196,202311300129);

INSERT INTO Voters
Values (29112369,"Karthikeya","Chaganti",8365369369,"karthik.ch@tsvoter.in",'2004-05-11',"123-143-410/404/301,Erragutta Centre,Telangana",1196,202311300129);



INSERT INTO Demographic_Information
Values (29112343,NULL,"Male","Parsi","SSC","No Income");

INSERT INTO Demographic_Information
Values (29112369,NULL,"Male","Jain","SSC","No Income");

INSERT INTO Demographic_Information
Values (29110039,NULL,"Male","Hindu","Intermediate","No Income");

INSERT INTO Demographic_Information
Values (29110011,NULL,"Male","Hindu","Intermediate","No Income");

INSERT INTO Demographic_Information
Values (29110019,NULL,"Male","Muslim","Pre-Primary","No Income");




INSERT INTO Candidates
Values (1252323,"Vivek","Kavuri",7980099505,"kavuri.hryday@tscd.in","BJP",14369,202311300129);

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
Values (1231,BRS);

INSERT INTO List_of_parties
Values (1234,BRS);

INSERT INTO List_of_parties
Values (1252,BJP);

INSERT INTO List_of_parties
Values (1252,TDP);

INSERT INTO List_of_parties
Values (1252,BRS);



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
VAlues (1107,202311300129);

INSERT INTO Event_station
VAlues (1104,202311300129);

INSERT INTO Event_station
VAlues (1098,202311300129);

INSERT INTO Event_station
VAlues (1102,202311300129);

INSERT INTO Event_station
VAlues (1196,202311300129);


INSERT INTO Campaign_finance
Values (3771772773,14369,1252323,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772774,35600,1252324,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772775,90000,1252327,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772776,132867,1252325,'2023-01-31');

INSERT INTO Campaign_finance
Values (3771772777,696969,1252328,'2023-01-31');
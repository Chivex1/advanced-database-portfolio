Advanced Database Systems 



<!-- Start of picture text -->
© M P H<br><!-- End of picture text -->

Review of Traditional Relational Databases and 

###### Advanced Concepts 

|PartA|02|
|---|---|
|111<br>IntroductiontoDatabaseSystemDesign|02|
|11.2 StagesOfDatabase Design|11|
|11.3Types ofdatabase systems|15|
|11.4Database Systemsand Database ManagementSystem|30|
|11.5Components ofDatabaseSystem|32|
|11.6 Characteristics of aGood Database|33|
|11.7 Normalisation|33|
|11.8 LimitationsOfTraditional DatabaseManagementSystem|35|
|Summary|38|
|Conclusion|39|
|Distributed DatabaseSystem||
|PartA|42|
|211 Background OfDistributed DatabaseSystem|42|
|21.2 Distributed Database SystemArchitecture|43|
|21.3 Peer-Peer, Client-ServerAnd Federated DatabaseArchitectures|46|
|21.4 DataFragmentation, ReplicationAndConsistencyModels|49|
|Part B|51|
|2.2.1 CAPTheorem, DBASEvsACID Models|51|
|2.2.2Trade-offs in Distributed SystemswithCAPCAPtheorem, BASE<br>and ACID models|53|
|Summary|57|
|Conclusion|58|



Summary Conclusion 

Advanced Database Systems 



<!-- Start of picture text -->
© M P H<br><!-- End of picture text -->

|Big DataAndCloud DatabaseSystems||
|---|---|
|PartA|61|
|3.111 Big Data|61|
|3.1.2 Cloud DatabaseSystems|72|
|3.1.3 UseCasesofCloud Database Systems|80|
|PartB|82|
|3.21 Introduction toDataWarehouse|82|
|3.2.2 IntroductiontoDatabaseSecurity|84|
|Summary|91|
|Conclusion|92|
|QueryOptimisation inDatabase||
|PartA|95|
|411 introduction toqueries|95|
|41.2 IntroductiontoQueryOptimisation|98|
|41.3QueryExecution Plansand Cost Estimation|103|
|PartB|112|
|4.21 IntroductionTo FileOrganisation InDatabase|112|
|Summary|118|
|Conclusion|119|



ii 

Advanced Database Systems 



<!-- Start of picture text -->
© M P H<br><!-- End of picture text -->

###### Emerging Trends in Database Systems 

|PartA<br>5.1.1 Overview of Database Evolution|122<br>122|
|---|---|
|511.2Al-Powered Databases (Autonomous DB, Oracle Al DB)|122|
|5.1.3 Blockchain and Distributed Databases|124|
|5.1.4Edge Databases|125|
|5.1.5 Serverless Databases|127|
|PartB|129|
|5.2.1 Graph Databasesand KnowledgeGraphs|129|
|Summary|136|
|Conclusion|136|
|Introduction toData Securityand Data Privacy||
|PartA|139|
|6.11 Introduction toData Privacy|139|
|PartB|143|
|6.2.1 AdvancedQuantitativeTechniques|143|
|6.2.2ChallengesofEnsuring Data Privacy|144|
|6.2.3 Best PracticesforImplementing Data Privacy|145|
|Summary|147|
|Conclusion<br>References|147<br>148|



iii 

STUDY SESSION ONE 

##### Review of Traditional Relational Databases and Advanced Concepts 

###### Review of Traditional Relational Databases andAdvanced Concepts 

###### Ss) M I T 



<!-- Start of picture text -->
| NT1X@) D)UCT I(@)|<br>yy :<br>Cat 4 ,<br>\ © =|<br>= } Gor<br>Sy\ wil 2 |<br>= NS . Y ge &<br>- gE “ . :<br><P rt eit = = A. y<br>— f 4p > D><br><!-- End of picture text -->

Database design is the process of designing a database for a given application. Designing a databaseisjust like designing every other thing, such as buildings, cars, road networks, etc. Care mustmistakes. be taken Database to plan properly design follows to avoid some costly specific approaches and steps. Prior to database design, it is good to understand some basic concepts and ed GEES oe CEUESEESS HENeA) or unknowingly, either in manual or automated form. When designing a database, it is good to knew, uea Why. such 2 Gatahese Ss reaulred, as this will help to guide in designing a useful database for the organisation. It is also important to look at the database environment when designing a database. A database environment consists of the hardware and operating system platform on which the database resides. It also includes a means through which the user can access the database, such as a network. The database environment can help determine what type of database model should be used and how the database will be implemented and managed. 

Ainformation database oris an data organised usually storedcollection electronicallyof structuredina computer system. A database is usually controlled by a Database Management System (DBMS). 

Database Management Software (DBMS) is a complex Software that constructs, expands and maintains the database. Examples: On PCs, Microsoft Access is a popular example of a single or small-group-user DBMS. Microsoft's SQL Server is 

an example of a DBMS that serves database requests from multiple (client) users. Other popular DBMSs are IBM's DB2, Oracle Corporation's Oracle, and Sybase Corporation's Sybase. Learning Outcomes When you have studied this session, you 11 Define Database should be able to: 1.2 State the different between Database and Database Management System (DBMS) 

1.3 Explain components of database 

1.4 State types of Database 

1.5 State the characteristics ofagood aatepecel 

- 1.6 Discuss stages of database design 

1.7 Explain the normalisation in databases. 1.8 Discuss limitations of traditional DBMS 1.9 Describe types of advanced databases. 

1.10 Explain the concept of NoSQL and NewSQL Databases. 

. . NIBIEGWSSiehicisincay peste ese GEIERESED, 

112 Compare NoSQL and NewSQL databases. 

###### Part A BASICS OF RELATIONAL DY WNBAS E 

###### 1.1.1 Introduction to Database System Design 

Database system design is a fundamental aspect of information technology that involves structuring data in a way that facilitates efficient storage, retrieval, and management. In today’s digital age, organisations rely heavily on well-designed 

‘© Copyright 2025 MIVA Open University All Rights Reserved 

22 

###### Review ofTraditional Relational Databases and Advanced Concepts 

###### G M I a 

databases to manage vast amounts of information. From e-commerce platforms and banking systems to healthcare applications and social media networks, database design is the backbone that ensures data integrity, security, and accessibility. The way the data is stored in the database determines based on multiplehow easycriteria.it is toData search should for informationalso be easy to add to the database, modify, and remove. 

A legacy database is simply an existing5 ft database of an organisationé that has been around for several years which is no longer up to date with the current technology. - design a newWhen database, a companythe existing has determineddatabase tois referred to as the legacy database. 

Examples of databases with which we are all familiar include 

Good decisions require good information derived from raw facts. 

systems,i thus,pas, understandingMnSerstang ng fileMesystesystem characteristics is important in learning about astaaLaDase SYSTEM.e 

Data are raw facts. A data item is a piece of raw entityY which has no meaning9 untilr it is associated with aA phenomenon. Example: 3, is. a data item with no significance.. It becomes meaningful- when we say that “there are 3 lectures in a week’ A data item can also be numeric or alphabetic.: To give meaning, data items are usuallyS collected into records. A record is made up of fields each of which holds a data item pertaining to a given phenomenon or entity. 



<!-- Start of picture text -->
a tert FS<br>i<br>een<br>H eas 7:<br>eT : ae<br>3 : : H<br>seme : iy<br><!-- End of picture text -->

###### Example: 

Sample database table 

|Ada|19|F|
|---|---|---|
|Adamu|22|M|
|Olu|20|M|



###### Personal address books 

Each row above is a record; a collection of records with the same characteristics is called a file. Examples: a file of student record, a file of medical records etc. 

###### Telephone books 

Adatabase is a collection of files of data 

Card catalogs at libraries 

|Onlinebookstores<br>:<br>Personal financesoftware|
|---|



pertaining to a given activity of an 

organisation. Or it can be defined as a collection of stored operational data of an organisation or enterprise. The 

operationalorganisation_ data dependsis the for data.its on primary which. an functions. 

Road maps 

Data is managed most efficiently when stored ina The database concept e developedp as a database. Databases evolved from computer file7 computerisedas a result of threerecord basic keeping needs: system has emerged 

© Copyright 2025 MIVA OpenUniversityAllRights Reserved 

3 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

A systemTo provide rapid access to all data in the 

03 | Updating data in the database 

B To provide simple and expressive user interface 

04 Deleting data from the database 

Cc To provide flexibility in the sharing of data between users concurrently. 

A database must provide a means of: 

INSEDI SNSAeERNE EESEES 

02 | Sorat data from the database easy 

Information is the result of processing raw data to reveal meaningful knowledge. Information requires context to reveal meaning. Raw data must be formatted for storage, processing, and presentation. Data are the foundation of information, which is the bedrock of knowledge. Data is the building blocks of information; information is produced by processing data. It is the process of revealing the meaning in a data set. Accurate, relevant, timely information is the key to good decision making. Good decision making is the key to organisational survival. 

Asample of the employee database table is shown below 

###### Employee Table 

|7369|SMITH|CLERK|7902|17-DEC-80|800|
|---|---|---|---|---|---|
|7499|ALLEN|SALESMAN|7698|20-FEB-81|1600|
|7521|WARD|SALESMAN|7698|22-FEB-81|1250|
|7566|JONES|MANAGER|7839|02-APR-81|2975|
|7654|BLAKE|MANAGER|7839|Q1-MAY-81|2850|



###### 1.1.1.1 Components of a database system 

Database system is simply a computerised record keeping system. It has four basic components: 



<!-- Start of picture text -->
rm brs<br>Hardware Software Users Data<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AlRights Reserved 

4 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

1 

###### HARDWARE 

The hardware consists of secondary storage on which the database physically resides together with the associated I/O devices( disk drives), device controllers, |/O channels and so forth. 

The hardware consists of the secondary storage devices such as magnetic disks (hard disk, zip disk, floppy disks), optical disks (CD-ROM), magnetic tapes etc. on which data is stored together with the Input/Output devices (mouse, keyboard, printers), processors, main memory etc. which are used for storing and retrieving the data in a fast and efficient manner. Since database can range from those of a single user with a desktop computer to those on mainframe computers with thousand of users, therefore proper care should be taken for choosing appropriate hardware devices for a required database. 

###### 2 SOFTWARE 

Mainly the DBMS between the physical database and the users. All request from users for access to the database are handled by the DBMS. Thus, the DBMS shields the database users from hardware level details. Database Management Software (DBMS) is a complex Software that constructs, expands and maintains the database. Examples: On PCs, Microsoft Access is a popular example of a single or small-group user DBMS. Microsoft's SQL Server is an example of a DBMS that serves database requests from multiple (client) users. Other popular DBMSs are IBM's DB2, Oracle Corporation's Oracle, and Sybase Corporation's Sybase. 

###### 3 USERS 

Users are those persons who need the information from the database to carry out their primary business responsibilities i.e. Personnel, Staff, Clerical, Managers, Executives etc. Depending on the job and requirements the users are provided access to the database totally or partially. 

We have three categories of users: 

- + Database Administrators (DBA) 

- + Database Designers/Programmers 

+ End Users 

Database Administrator (DBA) is that person in an organisation that has the central responsibility for the operational data. The job of the DBA requires high degree of technical expertise and understanding of the organisational structure and operations. The position of the DBA in an organisation is very important one, he is to ensure the security of the data in database by protecting it from malicious access and accidental loss of data. This is to ensure data integrity (Correctness of data) that is to ensure data is correct and up to date. 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

5 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

Database Designer/Programmers makes use of DBMS and programming languages to create database. 

End Users makes use of query language or menu driven interface. 

Responsibilities of the DBA 

;-—® Deciding the information content of the database 

2 © Deciding the storage structure and access strategy Leasing with users ; } . < © Defining strategy for back up and recovery ‘ Defining security and integrity checks 

——® Monitoring performance and responding to changing requirements 

###### 4 DATA 

It is a very important component of the database system. Most of the organisations generate, store and process large amount of data. The data acts as a bridge between the machine parts i.e. hardware and software and the users which directly access it or access it through some 

application programs. Data may be of different types. 

D> User Data - It consists ofa table(s) of data called Relation(s) where Column(s) are called fields of attributes and rows are called Records for tables. A Relation must be structured properly. 

D Metadata - A description of the structure of the database is known as Metadata. It basically means “data about data" System Tables store the Metadata which includes: 

+ Number of Tables and Table Names 

+ Number of fields and field Names 

- + Primary Key Fields 

Application Metadata - It stores the structure and format of Queries, reports and other applications components. 

© Copyright 2025 MIVA Open University All Rights Reserved 

6 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->



<!-- Start of picture text -->
aeae saat<br>q\ ee =><br>= A LZ/hM\= —=_- =<br>SSS<br>= > im<br>>, r<br><!-- End of picture text -->

###### 11.1.2 Functions of the DBMS 

Data definition: The DBMS provides functions to define the structure of the data. These functions include defining and modifying the record structure, the data type of fields, and the various constraints to be satisfied by the data in each field. It is the responsibility of the database administrator to define the database and make changes to its definition (if required) using the DDLand other privileged commands. 

Concurrency and data recovery: The DBMS also contains some functions that deal with the concurrent access of records by multiple users and the recovery of data after a system failure. 



<!-- Start of picture text -->
Maintains the data in the<br>database<br>~ ‘ Provide an interface<br>Allocates<br>( ) ¥ between the user and<br>storage to data \\ } Vea ‘817 the database<br><!-- End of picture text -->

Provides security for the data in the database: The DBMS contains functions, which handle the security and integrity of data stored in the database. Since these functions can be easily invoked by the application, the application programmer need not code these functions in the programs. 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

Performance optimisation: The DBMS hasa set of functions that optimise the performance of the queries by evaluating the different execution plans of a query and choosing the best among them. 

Itaccess the data dictionary It keeps statistics of the use for necessary information made of the data in the database nip» v v v It transforms data as it moves from level to level 

###### 11.1.3 Advantages of aDBMS 

Using a DBMS to manage data has many advantages: 

representationData Independence: and storage, Application The DBMS programs provides shouldnot an abstractbeexposed view of theto details data thatof data hides such details. 

@ 

Efficient Data Access: A DBMS utilises a variety of sophisticated techniques to store and a data efficiently. This feature is especially important if the data is stored on external storage devices. 

> integrityData Integri cons **t** raiya **n** ts.d Security:For example,Ifdatabefore is always inserting acce **s** alarysed through informa **t** ionhe DBMS,for an employee,theDBMS thecan DBMS"| can check that the department budget is not exceeded. Also, it can enforce access controls that govern what data is visible to different classes of users. Datacan offerAdministration: significant improvements.When several usersshareExperiencedtheprofessionals,data, centralising who understand the the administration nature of ofAQ the data being managed, and how different groups of users use it, can be responsible for organising the data representation to minimise redundancy and for fine-tuning the storage of the data to make retrieval efficient. 

© Copyright 2025 MIVA Open University AlRights Reserved 

8 

###### Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

Concurrent Access and Crash Recovery: A DBMS schedules concurrent accesses to the data in such a manner that users can think of the data as being accessed by only one user at a time. In addition, the DBMS protects users from the effects of system failures. 

Reduced Application Development Time: The DBMS supports important functions that are common to many applications accessing data in the DBMS. This, in conjunction with the high-level interfaceto the data, facilitates quick application development. DBMS applications are also likely to be more robust than similar stand-alone applications because many important tasks are handled by the DBMS (and do not have to be debugged and tested in the application). 

###### 1.1.1.4 

###### Components of DBMS 



<!-- Start of picture text -->
Creating and changing Data<br>the logical structure of aoe D<br>adatabase Definition<br>B<br>M =_.<br>Querying and making Data ~<br>changes to the baat Ss<br>information Manipulation 5<br>re<br>lenus, data entry ees RE 5<br>screens, reports, and Application n =<br>application software Generation g r<br>i<br>Who can use and see n<br>what information;<br>methods for backup and .<br>recovery Data<br>Administration<br>Queries to see the<br>effect of structural<br>changes<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AllRights Reserved 

9 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

###### —— 

j Database Engine: | The Database Engine is the core service for storing, processing, and securing data. The ' Database Engine provides controlled access and rapid transaction processing to meet the 1 therequirements Database of Enginethe mostdemanding to create relational data databases consuming for applications within online transaction processing your enterprise. or online Use analytical processing data. This includes creating tables for storing data, anddatabase objects such as indexes, views, and stored procedures for viewing, managing, and securing data. You can use SQL Server Management Studio to manage the database objects, and SQLServer Profiler for capturing server events. 

## a 

# iData dictionary: 

i Adata dictionary is a reserved space within a database which is used to store information | about the database itself. A data dictionary is a set of table and views which can only be read ' and never altered. Most data dictionaries contain different information about the data used in i the enterprise. In terms of the database representation of the data, the data table defines all | schema objects including views, tables, clusters, indexes, sequences, synonyms, procedures, q packages, functions, triggers and many more. This will ensure that all these things follow one ! standard defined in the dictionary. The data dictionary also defines how much space has been 1 allocated for and / or currently in used by all the schema objects. A data dictionary is used when | finding information about users, objects, schema and storage structures. Every time a data ' definition language (DDL) statement is issued, the data dictionary becomes modified. 2 Adata dictionary may contain information such as: Database performance @ Ls! a Database design etntictice & <Y information BoeleS grewh i B efs5 YY] {sa] StoredSQL procedures statistics bY ‘2 Database process ga, j_\ 2 a : : is] ¢ User permissions information fs User statistics 

© Copyright 2025 MIVA Open University AlRights Reserved 

10 

###### Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

————— \ Query Processor: i Arelational database database consists of many parts, : storage engine and engine and and the query processor. The storage engine writes data to and reads data 

Arelational database database consists of many parts, but at its heart are two major components: the storage engine and engine and and the query processor. The storage engine writes data to and reads data from the disk. It manages records, controls concurrency, and maintains log files. The query processor accepts SQL syntax, selects a plan for executing the syntax, and then executes the chosen plan. The user or program interacts with the query processor, and the query processor in turn interacts with the storage engine. The query processor isolates the user from the this result is obtained. 3 details of execution: The user specifies the result, and the query processor determines how 

The query processor components include pep, DDLinterpreter (G) © DML compiler (oy) Query evaluation engine 

### ee 

| Report writer: 

Also called a report generator, a program, usually part of a database management system, that extracts information from one or more files and present the information in a specified format. 4 Most report writers allow you toselect records that meet certain conditions and to display selected fields in rows and columns. You can also format data into pie charts, bar charts, and other diagrams. Once you have created a format for a report, you can save the format specifications in a file and continue reusing it for new data. 

###### 1.1.2 Stages of Database Design 

Database design is a structured process that involves several stages to ensure data is efficiently stored, accessed, and managed. 

© Copyright 2025 MIVA Open University AlRights Reserved 

11 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
)<br>6 MMIVA OPEN UNIVERSITYI a<br><!-- End of picture text -->

The following are the key stages in database design: 

###### 1. Requirements Analysis 

This is the initial stage where the database designers gather and analyse the needs of users and business processes. It involves: 

= 

pall 

- + Identifying the purpose of the database 

- + Understanding user requirements and data needs 

- + Defining key entities, attributes, and relationships 

- + Gathering functional and non-functional requirements 

###### 2. Conceptual Design 

Conceptual data model describes the information used by an organisation in a way that is independent of any implementation-level issues and details. The main advantage of a conceptual data model is that it is independent of implementation details and hence can be understood even by the end users having a non-technical background. The most popular conceptual data model is the Entity-Relationship (E-R) model. 

In this stage, a high-level design of the database is created using Entity-Relationship itoR (ER) models or UMLdiagrams. It includes: 

- + Identifying entities and their attributes 

- + Establishing relationships among entities 

- + Creating an Entity-Relationship Diagram (ERD) 

- + Defining constraints such as primary keys and cardinalities 

Simply stated, the ER model is a conceptual data model that views the real world as 

entities and relationships. The basic component of the model is the Entity- Relationship diagram which is used to visually represents data objects 

###### Asample E-R model diagram 



<!-- Start of picture text -->
—_—— Proj_Name<br>Cee] He<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University All Rights Reserved 

12 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### Notations for Entity Relationship Diagrams 

- + Entity - Rectangle 

- + Attribute - Ellipse connected to Rectangle 

- + Multi-valued attribute - Double Ellipse 

- + Composite attribute - Ellipse connected to Ellipse 

- Derived Attribute- Dashed Ellipse 

- + Relationship - Diamond Box 



<!-- Start of picture text -->
[|<br>><br>< ><br><>)<br>i 2<br>ae<br><!-- End of picture text -->

###### 3. Logical Design 

The conceptual model is transformed into a logical model that follows a specific database management system (DBMS), such as relational, NoSQL, or hierarchical. a 0 i This+ Converting stage includes: ERD into relational schema (tables, columns, relationships) 

- + Defining primary keys, foreign keys, and constraints 

- + Normalizing the database to remove redundancy and anomalies 

- + Ensuring data integrity and consistency 

###### 4. Physical Design 

The logical model is translated into a physical structure suited for performance and storage optimisation. This stage involves: 

- + Selecting the DBMS and defining storage structures (indexes, partitions, views) 

   - + Defining access paths for optimised query performance 

wae 

- + Configuring security policies and backup mechanisms 

- + Establishing indexing strategies for efficient data retrieval 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

13 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### 6. Testing and Evaluation 

The database is tested to ensure it meets the requirements and performs efficiently. Testing includes: 

— 90 + Data validation and integrity checks eX) + Performance testing (query optimisation and response times) 

- + Security testing to prevent unauthorised access 

- + Functional testing to ensure correct data retrieval and updates 

###### 7. Deployment and Maintenance 

Once tested, the database is deployed for use. Ongoing maintenance is required to ensure efficiency, security, and adaptability. This stage includes: 

- ato + Monitoring performance and optimising queries 

- a + Applying updates, patches, and security enhancements 

   - + Handling backups and disaster recovery 

   - + Modifying the database as business needs evolve 

The database design process is iterative and requires careful planning to ensure efficiency, scalability, and security. Following these structured stages helps in developing a robust and well-optimised database system that aligns with business objectives. 



<!-- Start of picture text -->
ah<br>.\ a<br>.<br>is a<br>= a =<br>4<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University All Rights Reserved 

14 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
LU<br>6 M IVA OPEN UNIVERSITYI a<br><!-- End of picture text -->

###### 1.1.3 Types of database systems 

A database system is a structured collection of data that enables efficient storage, retrieval, and management of information. There are several types of database systems, each designed to meet specific needs. The main types include: 

###### 11.3.1 Hierarchical Database 

Ahierarchical database is one of the earliest models used to store and manage data, and it remains significant in certain industries and legacy systems. As its name suggests, this database type structures data in a tree-like hierarchy where each piece of data (child) is connected to a higher-level element (parent). This model emphasises the one-to-many relationship — each parent node can have multiple child nodes, but each child has only one parent. This rigid structure makes the hierarchical model efficient for applications with well-defined relationships and fixed schema. 

Despite being considered an older model, the hierarchical database is still valuable in specific domains such as file systems and older banking applications. Understanding its architecture, critical components, advantages, and limitations is important for professionals working with or migrating legacy systems. 

The hierarchical database model mirrors the structure of a tree. The top node is called the root, and all other nodes branch out from it. These branches represent parent-child relationships, where: 

Achild node has only one parent, A parent node can have < ensuring a strict tree hierarchy multiple child nodes. > without cycles or shared children. 

Each node in this tree contains a record, and each record contains fields or data attributes. The hierarchy allows for quick traversal, particularly in applications where the data naturally forms a nested relationship. For example, in a university's course registration system, a university (root) may have multiple faculties (children), and each faculty can have several departments (sub-children), and departments can contain various courses. 

The diagram in Figure 1.4 shows the hierarchical model of Online Book database. It consists of three record types, namely, PUBLISHER, BOOK, and REVIEW. For simplicity, only few fields of each record type are shown. One complete record of each record type represents a node. 

© Copyright 2025 MIVA Open University AllRights Reserved 

15 

###### Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

###### Hierarchical Data Model for Online Book Database 



<!-- Start of picture text -->
PUBLISHER (P_ID, Pname, Phone)<br>POO1 | HillsPublications | 7134019<br>CaP EES) REVIEW (R_ID, Rating)<br>REVIEW (R_ID, Rating) ‘A006<br>Link to AUTHOR<br>record type<br><!-- End of picture text -->

###### Use Cases of Hierarchical Databases 

Despite their rigidity, hierarchical databases are suitable for domains where the data inherently follows a tree structure and needs predictable, high-speed access. 

Content Management Systems: 

Legacy Systems: 

- + Many older systems in banking, airline reservation, insurance, and telecommunications telecommunications still run on hierarchical databases. 



<!-- Start of picture text -->
+ Some CMS platforms use reservation, insurance, and telecommunications telecommunications<br>hierarchical models to still run on hierarchical databases.<br>slr ne ae a + These systems were originally built using models<br>Ra BE Nace like IBM's IMS (Information Management System),<br>4 which pioneered this approach.<br>Geographical Applications: GS, Directory Services:<br><!-- End of picture text -->

- + Forrepresenting country > state > city > district data. 

   - + Hierarchical structures are ideal for file systems, where files and directories follow a tree-based path 

- + The hierarchy mirrors the geographical containment relationships perfectly. 

- + Anexample is the Windows Registry, where keys and values are organised hierarchically. 

© Copyright 2025 MIVA Open University AlRights Reserved 

16 

Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
J<br>6 MMIVA OPEN IUNIVERSITY a<br><!-- End of picture text -->

###### 1.1.3.2 Network Database 

The network database model is a significant advancement in the evolution of database systems, emerging as an improvement over the rigid hierarchical model. Where hierarchical databases enforce a strict parentchild relationship, network databases offer greater flexibility by allowing each record (or node) to have multiple parent and child relationships, effectively modelling many-to-many associations. This is made possible by using a graph-like structure where data records are connected via set relationships. 

Initially popularised by the Conference on Data Systems Languages (CODASYL), the network model addresses limitations in hierarchical databases, especially in systems where data entities interact in complex, non-linear ways. Although largely replaced by relational and NoSQL databases in modern applications, network databases still serve critical roles in performance-sensitive domains like engineering and telecommunications. 

Anetwork database organises data using a graph structure that allows any record to be linked to any other record. This model introduces the concept of “sets” — collections of one owner record and multiple member records — to define relationships. 

Each record (data entity) is stored as a node, and relationships are represented by pointers connecting these nodes. These relationships are predefined, allowing direct and rapid traversal of the database structure. The network model allows a record to participate in multiple sets, effectively supporting many-tomany relationships, which are not feasible in the hierarchical model without redundancy. 

Network Data Base Model 

Parent Parent Child_Level_1 Child_Level_1 Child_Level_2 =i Sa = Child_Level_2 

Child_Level_2 

© Copyright 2025 MIVA Open University AllRights Reserved 



<!-- Start of picture text -->
7<br><!-- End of picture text -->

Review of Traditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
ay<br>G M I T<br><!-- End of picture text -->

For example, in a supply chain database, a single component might be part of several assemblies, and each assembly might also use multiple components. Modeling such relationships is cumbersome in hierarchical databases but straightforward in network databases. 

The main advantage of network data model is that a parent node can have many child nodes, and a child can also have many parent nodes. Thus, the network model permits the modeling of many-to-many relationships in data. The main limitation of the network data model is that it can be quite complicated to maintain all the links, and a single broken link can lead to problems in the database. In addition, since there are no restrictions on the number of relationships, the database design can become complex. The diagram below shows the network model of Online Book database. 

###### Network Data Model 



<!-- Start of picture text -->
PUBLISHER (P_ID, Pname, Phone)<br>Poo1 Hills Publications | 7134019<br>BOOK (ISBN, Book_title, Price)<br>ce 0or- 987-7608<br>/\ REVIEW (R_ID, Rating) fo.<br>Y<br>Se RI al tes \ hors<br>See ce? 20 oa<br>: DNA LT See<br>™ .<br>a e<br>SSS _<br>= ss-<br><!-- End of picture text -->

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### Use Cases of Network Databases 

Network databases have historically been adopted in areas requiring high performance and the ability to model complex interdependencies among data entities. Below are some domains where they have proven particularly useful: 

###### Manufacturing and Engineering 

###### Systems 

- + Inproduct design and assembly, components are often reused in multiple products. 

###### Telecommunications 

   - + Telecom systems involve various 

   - interrelated components: users, devices, switches, call records, billing records, and service plans. 

- + Forinstance, ina car manufacturing database, a single engine type might be used across multiple car models. 

- Conversely,v a model might9 use civcee: oa “ ifferent variantsSl of POcomponents. 

- + Modeling such many-to-many relationships efficiently is a core 

   - + Each component interacts with multiple others, necessitating a highly interconnected data model. 

   - ee ; 

   - + Networkaccess anddatabases update capabilities helpmaintainea in such rapid 

   - multi-relational environments. 

- strength of the network model. 

#### Real-Time Systems 3) Government and Defense Systems 2 

- + Systems that require fast and predictable data access benefit from the pointer-based navigation of 

- network models. 

   - + Some older military and government systems still rely on network databases for data that is structured 

   - but highly interconnected and 

- + Examples include inventory. . mission-critical. 

- management, airline scheduling, and 

- logistics networks, where 

performance is critical. 

###### 11.3.3 Relational Database (RDBMS) 

The Relational Database Management System (RDBMS) is the most widely used type of database model in the world. Introduced in the 1970s by Dr. E. F. Codd, the relational model revolutionised data management by using mathematical set theory and relational algebra to store and manage data in a logical, structured way. In an RDBMS, data is organised into tables (also called relations), each consisting of rows and columns. These tables can be linked using keys that define relationships between different datasets. The structure promotes data integrity, consistency, and normalization, making it ideal for applications requiring complex queries and precise data control. 

© Copyright 2025 MIVA Open University All Rights Reserved 

19 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

At its core, a relational database is made up of one or more tables that represent entities (such as customers, orders, or products). Each table is composed of: 

- + Rows (records): Represent individual entries in the table. 

- + Columns (fields): Represent attributes of the entity. 

Tables are related through primary keys (a unique identifier in a table) and foreign keys (a reference toa primary key in another table). These relationships allow users to<sup>join tables and construct complex queries</sup> using Structured Query Language (SQL), the standard language for RDBMS operations. 

Relational databases are ideal for structured data where relationships between different data elements can be clearly defined and enforced through constraints. They follow the ACID principles—Atomicity, Consistency, Isolation, Durability—which ensure reliable transactions and strong data consistency even in the event of system failures. The diagram below shows the relational model of Online Book database. 

###### Relational Model for Online Book Database 

BOOK 

||PUBLISHER<br><br>|||
|---|---|---|---|
|||||
|<br>Hills<br>Publication|<br><br>12,ParkStreet, |Georgia<br>|Atalanta|<br>|7134019||H_pub@hills.com|



|fe|REVIEW<br> <sup>[eran</sup>|
|---|---|
|<br>A006|<br>001-354-921-1|
|A008|001-987-760-9|



© Copyright 2025 MIVA Open University All Rights Reserved 

20 

LU 6 MMIVA OPEN UNIVERSITYI a 

###### Review ofTraditional Relational Databases and Advanced Concepts 

###### ielIteeiitens 

- + RDBMSs are commonly used in Customer Relationship Management (CRM) systems, Enterprise Resource Planning (ERP) platforms, and financial applications. 

- + These applications benefit from the transactional integrity and relationship 

- management that relational databases offer. 

###### Applications 

- + Many web-based platforms use RDBMSs like MySQL or PostgreSQLfor backend data storage. 

- + RDBMSs provide reliable user data management, session handling, and 

- transaction support in e-commerce, social 

media, and online services. 

###### 3 Enterprise Data Warehousing 

- . RDBMSs can ee used for data warehousing, where large amounts of structured historical data are stored for business intelligence and reporting purposes. 

- Tools like Microsoft SQL Server, Oracle Database, and IBM DB2 are common in enterprise data environments. 

- Government and 5 Educational Healthcare Systems Institutions and 7 7 Ri rch 

- Systems requiring stringent requiring stringent stringent seer’ 

- 7 7 Ri rch 

- + Systems requiring stringent requiring stringent stringent seer’ data integrity and auditability + RDBMSs are used to —such as tax systems, manage academic records, patient records, and legal research data, and archives—rely on the administrative workflows. robustness of relational databases. 

Choosing RDBMS should be based on a comprehensive understanding of the data structure, performance needs, and operational context. With a sound design and the right tooling, relational databases provide a reliable and efficient platform for managing data in almost any domain. 

###### 11.3.4 Object-Oriented Database (OODBMS) 

An Object-Oriented Database Management System (OODBMS) combines the capabilities of a database system with the principles of object-oriented programming (OOP). Unlike traditional relational databases that store data in tables made up of rows and columns, an OODBMS stores data in the form of objects, as used in object-oriented languages like Java, C++, and Python. This allows for<sup>tighterintegrationbetween</sup> databases and the application code, enabling more natural and efficient data modeling in complex environments. 

In OODBMS, data entities are treated as objects. These objects not only store data but also include methods (functions) that operate on the data, which is a key concept of object-oriented design. Each object is an instance of a class, and classes can inherit attributes and behaviours from other classes— facilitating reuse and abstraction. 

© Copyright 2025 MIVA Open University AllRights Reserved 

21 

###### Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
J<br>6 MMIVA OPEN IUNIVERSITY, a<br><!-- End of picture text -->

###### The system supports essential object-oriented features such as: 

a ' (2) ic) al* faye Q Encapsulation: Inheritance: Polymorphism: Combines data Allows new Enables different and behaviour object classes to objects to into a single be defined based respond to the unit (the on existing same method call object). classes. in different ways. 

An Object Identifier (OID) is assigned to each object to uniquely identify it, regardless of changes to its attribute values. These identifiers simplify the referencing and linking of objects in a database. 

OODBMSs support complex data types, such as nested objects, lists, and arrays, which are cumbersome to represent in traditional relational models. This capability makes them especially suitable for domains that handle intricate and interconnected data structures. 

###### Use Cases 

OODBMS is particularly effective in domains that require representation and storage of complex and multimedia data, such as: 

Multimedia Systems: Audio, video, and image data can be stored as objects with metadata and methods. 

Scientific and Research Applications: Data with deeply nested structures and unique processing requirements. 

CAD/CAM Applications: Engineering designs consist of intricate components with detailed relationships. 

Real-Time Systems: Such as telecom billing systems, which need rapid and reliable handling of complex transactions. 

© Copyright 2025 MIVA Open University AllRights Reserved 

22 

Review ofTraditional Relational Databases and Advanced Concepts 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### 1.1.3.5 NoSQL Database 

NoSQL databases represent a broad class of database management systems that diverge from the traditional relational model. Unlike relational databases (RDBMS) that use structured schemas and SQL for querying, NoSQL databases are designed to handle large volumes of unstructured, semi-structured, or rapidly evolving data formats. They provide flexibility, scalability, and high performance, making them ideal for modern applications involving real-time processing, big data, and cloud-native environments. 

NoSQL stands for “Not Only SQL,” emphasising that these databases do not strictly adhere to the relational model but can still support simple SQL-like querying. Instead of relying on rigid table structures and predefined schemas, NoSQL databases use a variety of data models to store and manage data efficiently. 

NoSQL databases often sacrifice strict ACID (Atomicity, Consistency, Isolation, Durability) compliance in favour of eventual consistency to improve scalability and performance. This trade-off enables horizontal scaling across distributed systems, allowing them to handle millions of operations per second. 

There are four primary types of NoSQL databases: 

1. Document Store: 2. Key-Value Store: Stores data as Stores data as 

JSON-like simple key-value documents. Each pairs, offering document is selfextremely fast describing, making it lookup times. highly flexible. Example: Redis, Example: MongoDB, DynamoDB 

CouchDB 

3. Column-Family Store: Stores data in columns rather than rows, which is useful for analytics and handling large datasets. 

Example: Apache 

4. Graph Database: Uses nodes and 

edges to represent and query relationships. Example: Neo4j, 

Amazon Neptune 

Cassandra, HBase 

Use Cases 

NoSQL databases excel in scenarios where traditional RDBMSs face limitations, such as: 

+ Big Data Applications: Where data is generated at high velocity and volume. 

+ Real-Time Analytics: For processing streaming data from web services, sensors, or loT devices. 

* Content Management Systems: Due to schema flexibility and quick access. 

+ Mobile and Web Applications: Require fast response times and high user concurrency. 

+ Recommendation and Personalisation Engines: Especially using graph or document stores. 

© Copyright 2025 MIVA Open University AlRights Reserved 

23 

###### Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
6 M I “Is<br><!-- End of picture text -->



<!-- Start of picture text -->
ali<br>:<br>;<br>central NoSQL database<br><!-- End of picture text -->



<!-- Start of picture text -->
social media<br><!-- End of picture text -->



<!-- Start of picture text -->
e-commerce<br><!-- End of picture text -->



<!-- Start of picture text -->
loT<br>finance<br><!-- End of picture text -->



<!-- Start of picture text -->
gaming<br><!-- End of picture text -->

###### 1.1.3.6 NewSQL Database 

NewSQL databases represent an emerging class of modern relational database systems that blend the best features of traditional Relational Database Management Systems (RDBMS) and NoSQL technologies. Designed to overcome the scalability limitations of conventional RDBMS while maintaining ACID (Atomicity, Consistency, Isolation, Durability) guarantees, NewSQL systems deliver both high performance and strong transactional consistency. They are particularly useful in scenarios demanding real-time data processing at web scale. 

Traditional RDBMSs, such as MySQL or PostgreSQL, provide strong consistency and structured querying through SQL but often struggle with horizontal scalability, especially in distributed cloud environments. NoSQL systems address the scalability and flexibility challenge but often sacrifice consistency and ACID compliance. 

NewSQL offers a middle ground by preserving SQL-based interfaces and relational models while adopting distributed architectures that can scale horizontally like NoSQL systems. These databases leverage modern computing capabilities—such as in-memory processing, multi-version concurrency control (MVCC), and distributed execution engines—to provide scalable, fault-tolerant, and high-performance transaction management. 

###### Use Cases 

NewSQL databases are particularly suited for mission-critical applications where both consistency and high performance are crucial. Common use cases include: 

© Copyright 2025 MIVA Open University AllRights Reserved 

24 

) 6 MMIVA OPEN UNIVERSITYI a 

###### Review ofTraditional Relational Databases and Advanced Concepts 

###### SaaS Applications: 

Multi-tenant platforms needing flexible scaling and reliable transactional support. Li = Operational Analytics: Gr, 

Applications that require both fast transactional updates and near-real-time analytical queries on fresh data. 

###### E-Commerce Platforms: 

High-volume transactional systems that require rapid response times and absolute data accuracy (e.g., shopping carts, payment processing). 

###### Real-Time Financial Systems: 

Trading platforms, fraud detection systems, and digital wallets that demand immediate transaction confirmation and fault tolerance. 

Popular examples of NewSQL databases include Google Spanner, CockroachDB, VoltDB, and MemSQL (SingleStore). 

###### 1.1.3.7 Cloud Database 

A cloud database is a type of database that is built, deployed, and accessed through a cloud computing platform. It provides organisations with the flexibility to manage their data without the need to maintain physical infrastructure. Cloud databases are delivered as Database-as-aService (DBaaS) or as self-managed databases hosted on cloud infrastructure. Their main appeal lies in scalability, global accessibility, high availability, and reduced administrative overhead 

Unlike traditional on-premises databases, cloud databases operate on virtualised infrastructure provided by cloud service providers such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), and others. These databases can scale resources dynamically based on demand, reducing the need for manual intervention. Cloud providers often offer fully managed services that handle database provisioning, patching, backup, recovery, and monitoring. 

Cloud databases can support both relational (e.g., MySQL, PostgreSQL, Microsoft SQL Server) and non-relational models (e.g., MongoDB, DynamoDB). The pay-as-you-go model ensures cost efficiency, especially for businesses with fluctuating workloads. 

###### Use Cases 

Cloud databases are widely adopted across industries due to their flexibility and cost-efficiency. Typical use cases include: 

© Copyright 2025 MIVA Open University All Rights Reserved 

25 

LU 6 **M** IVA OPEN UNIVERSITYI a 

Review ofTraditional Relational Databases and Advanced Concepts 

###### SaaS Platforms: 

Cloud-native applications use cloud databases to provide scalable, multi-tenant solutions for millions of users. 

EX | Global Enterprise Applications: aaa en f ‘ eee 2.) dataApplications synchronisatio requiri **n** gacr gl **o** balss accessibilityregions benefitand from real-time cloud databases distributed architecture. ((¢ cloudHybridinfrastructureand Multi-Cloudor useStrategies: multiple cloud providers a) Organisations that combine on-premise systems with redundancy. ij Dl **e** verage cloudvOps and CI/CD databases Environmen for da **t** s:aconsistency and 

@ Developers benefit from the rapid provisioning of databases for testing, deployment, and agile development workflows. 

###### 1.1.3.8 Distributed Database 

A Distributed Database is a type of database system where the data is stored across multiple physical locations or computing nodes. These nodes may be located within the same data centre or spread across geographically distant sites. Despite the physical separation, a distributed database functions as a unified system to the user, providing seamless data access and management. 

Distributed databases are designed to offer scalability, fault tolerance, and availability, making them ideal for modern applications that require continuous uptime and responsiveness across multiple regions. 

In a distributed database system, data can be replicated or partitioned across different nodes. Replication involves storing copies of the same data on multiple nodes to enhance reliability and speed, while partitioning divides the database into segments that are stored on different nodes, optimising performance and storage efficiency. 

Each node in the system may run the same or different Database Management Systems (DBMS). This gives rise to two categories: 

- + Homogeneous Systems: All nodes use the same DBMS and data model. 

- + Heterogeneous Systems: Nodes may use different DBMSs, data models, or schemas. 

Distributed databases must implement synchronisation mechanisms to maintain consistency between nodes. They often rely on distributed transaction protocols, time-stamping, and consensus algorithms to manage data integrity. 

© Copyright 2025 MIVA Open University AllRights Reserved 

26 

6, M | T ay 

###### Review of Traditional Relational Databases and Advanced Concepts 

Akey theoretical principle in distributed databases is the CAP Theorem, which states that a distributed system can only provide two of the following three guarantees at any given time: 



<!-- Start of picture text -->
Availability (every request<br>gets a response)<br>Consistency (all nodes — 8 Partition tolerance<br>see the same data) f CY Y @ (system functions<br>ees Ve = S?J despite network splits)<br>yay \ aN<br><!-- End of picture text -->

###### Use Cases 

Distributed databases are used in scenarios that demand high availability, global scalability, and rapid responsiveness. Key use cases include 

1. GlobalE-commerce § 2. Content Delivery Platforms: Serving Networks (CDNs): users across Storing and continents with delivering media or localised content application data and low latency. from the closest edge server. 

3. Edge Computing 4. Real-Time Applications: Analytics: Supporting local Analysing processing of data streaming data at the edge of the from various network, especially sources in different in loT environments. locations. 

###### 1.1.3.9 Graph Database 

AGraph Database is a type of database designed to represent and query data in terms of nodes (entities) and edges (relationships). Unlike relational databases that rely on tables and joins, graph databases directly model relationships, making them ideal for applications with complex and dynamic interconnections among data points. 



<!-- Start of picture text -->
2xiv<br>go<br>5<br>neai Peoy, Posted<br>Posted<br>%oy Posted<br>os oo Wey<br>Fy Cn oste<br>& %bigy r<br>E TeNdship with<br>@ %% &<br>J$<br><!-- End of picture text -->

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### Review ofTraditional Relational Databases and Advanced Concepts 

Graph databases allow for more intuitive and efficient data traversal, especially when analysing networks, relationships, or hierarchies. They offer a schema-fiexible design, making them suitable for rapidly evolving datasets 

Ina graph database, data is organised as a graph structure: 

- + Nodes represent entities such as people, products, or locations. 

   - ge raud Detection: IG Outying SUSPiouS patterns through relationship anomalies 

   - in financial transactions 

   - + Knowledge Graphs: Representing structured information for semantic 

   - Search and Al applications: 

   - + Network Management: Visualising and managing complex IT infrastructures and 

   - dependencies. 

- + Edges represent relationships between nodes, like “FRIENDS_WITH,” “BOUGHT,” or “LOCATED_IN.” 

- + Properties are key-value pairs attached to both nodes and edges, providing more context. 

A defining feature is index-free adjacency, meaning each node directly pointstoitsrelatednodes. This makes traversing relationships highly" efficientsa. and avclds the e¥pensivé join operations typically seen intelational HiGUElS: 

Graph databases also support graph algorithms, such as: 

- + Shortest path: Finding the minimal distance between two nodes. 

- + PageRank: Measuring the influence of nodes (used by search engines). 

- + Community detection: Identifying clusters of interconnected nodes. 

###### 11.310 Time-Series Database 

ATime-Series Database (TSDB) is a specialised Hype of Gatabase designed for storing; PIOCeSSing: 2"4analysing time-stamped or time-indexed data. Unlike3 18 general-purpose: databases, TSDBs" are optimised for high ingestion rates, efficient data compression. and fast querying of large volumes of chronological data. This makes them ideal for applications where data points are continuously collected and must be analysed over time to identify trends, patterns, or anomalies. 



<!-- Start of picture text -->
a —<br>« S<br># ® = —_—<br>ey<br>TSDB ee<br>Ee<br><!-- End of picture text -->

###### Use Cases 

Graph databases are widely used in 

scenarios that involve relationship-intensive queries 

- Social Networke!odeingendenalysing user connections, mutual friends, groups, endactuitics: 

- Recommendation Engines: Suggesting products, content, or connections based on user behaviour and shared interests. 

Time-series data typically consists of sequences of values ordered bya such as cpu Usage Per second; sensor readings every millisecond, or stock prices per tick. A TSDB is structured to index data by time, enabling rapid reads and writes of sequential entries. It supports: 

- + Efficient ingestion of millions of data points per 

- second. 

‘© Copyright 2025 MIVA Open UniversityAll<sup>Rights Reserved</sup> 

28 

###### Review ofTraditional Relational Databases and Advanced Concepts 

###### 6 M I a 

- + Compression algorithms that reduce storage needs for large volumes of similar or continuous values. 

- + Downsampling, rollups, and aggregation, which help manage long-term storage by summarising historical data at lower resolutions. 

+ Retention policies that automatically delete older or less relevant data after a specified time. detection tools, continuous queries, and Additionally, many TSDBs include anomaly integration with visualisation platforms like eiatane 

###### Use Cases 

Time-series databases are used across various industries where time-stamped Sates creel 

- + loT Platforms: For collecting and analysing sensor readings from devices in smart homes, factories, or cities. 

###### 1.1.3.11 Choosing the Right Database 

Choosing the right database system is a foundational decision in any software architecture. It influences not only data storage but also performance, scalability, consistency, maintenance, and long-term viability. As applications grow more complex and varied, selecting the appropriate database requires balancing multiple technical, operational, and business considerations. 

###### (fi) Data Model 

The data model is perhaps the most critical factor. It determines how data is organised, stored, and queried. 

   - + Relational Databases (RDBMS) use structured schemas with tables, making 

   - them suitable for structured data and transactional systems. 

   - + NoSQL Databases offer flexible schemas and are ideal for handling unstructured or semi-structured data at scale. This category includes: 

      - + Document stores (e.g., MongoDB) 

- + Application and Infrastructure Monitoring: Collecting logs, CPU usage, memory, or network stats for DevOps or system administrators. 

- + Financial Services: Recording and analysing stock tick data, trades, or transaction history. 

- + Utilities and Energy: Monitoring consumption patterns, load forecasting, and smart meter data. 

- + Healthcare: Storing time-stamped vitals and patient monitoring system outputs. 

Popular TSDBs include InfluxDB, TimescaleDB, Prometheus, and OpenTSDB. 

   - + Key-value stores (e.g., Redis) 

   - + Column-family stores (e.g., Cassandra) 

   - + Graph databases (e.g., Neo4j) 

- + Object-Oriented Databases (OODBMS) tightly integrate with object-oriented programming models. 

- + Time-Series Databases specialise in timestamped data for real-time analysis. 

- + NewSQL Databases combine the structure of RDBMS with the scalability of NoSQL. 

Choosing the right model depends on the nature of your data and how you intend to interact with it. 

© Copyright 2025 MIVA Open University All Rights Reserved 

29 

) 6 MMIVA OPEN UNIVERSITYI a 

###### Review ofTraditional Relational Databases and Advanced Concepts 

###### Scalability 

###### Performance Requirements 

Scalability determines how well the database grows with your data and user load. 

Performance metrics such as latency, throughput, and fault tolerance matter significantly: 

- + Vertical scaling (scale-up) involves 

- upgrading server hardware and is typical of + Latency: How quickly queries quickly queries queries are answered. answered. traditionalelles) RDBMS.= ‘ + Throughput: How many operations per 

- Horizontal scaling scaling (scale-out) distributes second the system can handle. ogin EEStaNoSQLacrossin EEStaNoSQLacross EEStaNoSQLacrosstaNoSQLacrossNoSQLacrossacross andmultiple NewSQLS INE systems.servmultiple NewSQLS INE systems.serv NewSQLS INE systems.servS INE systems.serv INE systems.serv systems.servserv SCIndAEIndAEAE isOEEcommonMIE.OEEcommonMIE.commonMIE.MIE. + Fault Tolerance:2 : Ability27 F to remain4 operational during failures. 

- your. de. de de applicationeSiseSisis ex,peedpeedd too handleao handlea handleaa Applicationsan requiring- real-timeF data 

- massive growth, growth, especially in user or user or or ees Z ‘ : Z processing, like financial trading or loT, need 

- transaction volume, volume, a horizontally scalable horizontally scalable scalable . system is: is:: often preferable. preferable. tolerantlow-latency, systems. high-throughput, and fault- 

   - + Latency: How quickly queries quickly queries queries are answered. answered. 

+ Horizontal scaling scaling (scale-out) distributes ogin EEStaNoSQLacrossin EEStaNoSQLacross EEStaNoSQLacrosstaNoSQLacrossNoSQLacrossacross andmultiple NewSQLS INE systems.servmultiple NewSQLS INE systems.serv NewSQLS INE systems.servS INE systems.serv INE systems.serv systems.servserv SCIndAEIndAEAE isOEEcommonMIE.OEEcommonMIE.commonMIE.MIE. If ytyour. de. de de applicationeSiseSisis ex,peedpeedd too handleao handlea handleaa massive growth, growth, especially in user or user or or : Z transaction volume, volume, a horizontally scalable horizontally scalable scalable system is: is:: often preferable. preferable. 

###### Consistency and Availability: CAP Theorem 

The CAP theorem states that a distributed system can only guarantee two of the following three: Consistency, Availability, and Partition 

###### WELSH 

- + Relational databases often favour consistency and partition tolerance. 

- + NoSQL systems (like Cassandra or DynamoDB) may trade consistency for availability, offering eventual consistency. 

Understanding your application's tolerance for inconsistency or downtime is key to making this decision. 

###### MeIntebao cape VepcOuECoS etait Consider the operational complexity and ecosystem support: 

- + Managed cloud services (like Amazon RDS or Google BigQuery) reduce maintenance but may involve vendor lock-in. 

- + Open-source databases provide flexibility but may require more in-house expertise. 

- Evaluate community support, tooling, documentation, and integration with your existing tech stack. 

###### Workload Type: OLTP vs. OLAP 

- + OLTP (Online Transaction Processing) systems are optimised for a high volume of short, transactional operations—suitable for banking, e-commerce, or inventory systems. 

- + OLAP (Online Analytical Processing) systems handle complex queries on large datasets, ideal for business intelligence, data mining,Ing and reporting.porane 

- Your workload determines whether transactional IRtearKyarty Granalvtical . 

- performance takes priority. Y 

No single database fits all scenarios. The right choice depends on your data characteristics, workload, scalability needs, consistency requirements, and operational capabilities. A deliberate evaluation of these factors ensures a robust, scalable, and future-proof data infrastructure. 

###### 1.1.4 Database Systems and Database Management System 

‘ The difference between a database system anda database management system (DBMS) lies in their scope and functionality: 

© Copyright 2025 MIVA Open University All Rights Reserved 

30 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->



<!-- Start of picture text -->
Dateiat a eebase areSystem Database(DBMS)  Management System<br>Acomplete databaseP  cohsystemale ), I ACIUaIeIrefersjudi 9 to2  the ADBMSusers interactA  is. the software withA  the database. that helpsIt<br>+ The database itself (which stores provides tools for:<br>data).) .<br>+ Data storage and retrieval (e.g.,<br>+ The database management system SQL queries).<br>the( DBMS) database).Meaien(software that manages9 + Data(access security control,: and backups). integrity‘ P<br>+ The hardware, software, and users :<br>. ‘ &<br>interacting with the system. + Concurrency5  control (handling<br>multiple users accessing the<br>In short, a database system is the database).<br>entire ecosystem that supports data<br>storage, retrieval, and management<br><!-- End of picture text -->

###### Table 1.1: Key Difference between Database Systems and Database Management System 

|Aspect|DatabaseSystem|DatabaseManagementSystem<br>(DBMS)|
|---|---|---|
|Definition|Acompletesystem includingthe<br>database, DBMS, hardware,<br>software, and users.|Asoftwaresystemthatmanagesand<br>interactswith the database.|
|Scope|Broaderconcept, including<br>everything needed tostoreand<br>managedata.|Focusedonlyonmanagingand<br>controllingaccesstothedatabase.|
|Aspect|DatabaseSystem|DatabaseManagementSystem<br>(DBMS)|
|Components|Includesthedatabase, DBMS,<br>hardware, OS, network, and users.|Onlyincludessoftwareusedto<br>interactwith thedatabase.|
|Examples|Abank’sentiredatabase<br>infrastructure.|MySQL, PostgreSQL, OracleDB,<br>MicrosoftSQLServer.|



© Copyright 2025 MIVA OpenUniversityAllRights Reserved 

31 

Review of Traditional Relational Databases and Advanced Concepts 

6, M | T ay 

###### 1.1.6 Characteristics of a Good Database 

Classical motivation theories, such as Self-Determination Theory (SDT) and job design principles, can be enriched by incorporating POB insights. For A good database should have the following characteristics: 

Datalintedtity EOS SS eas Data Security - Protects data from accuracy, consistency, and F@ By unauthorised access and breaches reliability of data. Scalability - Can handle Performance - Provides fast query increasing amounts of data and | XY execution and transaction users efficiently. processing. RedUndancyMebSceeuslesuenemel Management: es|iff Ga Data Consistencyuniformity across the - Maintains database ensures efficient storage. Backup andRecovery__ al Concurrency Control - Allows Supports data recovery in case a la multiple users to access data of failures without conflicts. Flexibility - Adapts to Normalization - Organises data changing business needs and oy ay efficiently to reduce redundancy and requirements. improve relationships between tables. 

###### 1.1.7 Normalisation 

Normalisation in database design is a systematic approach to organising data in a relational database to minimise redundancy and improve data integrity. It involves decomposing large tables into smaller, related tables and defining relationships among them to eliminate anomalies and ensure data consistency. 

###### 11.7.1 Objectives of Normalisation 

Eliminate Redundancy: Enhance Query Performance: Reduces duplicate data to save Organises data to optimise storage space and maintain yi retrieval and update consistency. yy f operations. Avoid Anomalies: Prevents insertion, | 4 Ensure Data Integrity: Maintains update, and deletion anomalies that accuracy and consistency in the arise due to poorly designed tables. database. 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
LU<br>6 M IVA OPEN UNIVERSITYI a<br><!-- End of picture text -->

###### 1.1.7.2 Normalisation Process 

Normalisation follows a series of stages called Normal Forms (NFs). Each normal form builds upon the previous one to enhance database structure 

First Normal Form (1NF): Ensures atomicity by eliminating duplicate columns. 

Second Normal Form (2NF): Ensures that all non-key attributes are fully dependent on the primary key. 



<!-- Start of picture text -->
“~M> Third Normal Form (3NF): Eliminates transitive dependencies.<br>oe~> Boyce-Codd Normal Form (BCNF): A stricter version of 3NF that<br>resolves remaining anomalies.<br><!-- End of picture text -->

Normalisation is crucial in relational database design to enhance efficiency and maintain consistency. While it minimises redundancy, excessive normalization can increase query complexity. Thus, striking a balance between normalization and performance is essential for an optimised database design. 

Apply normalization to the given unnormalised table. 

###### Given Table: 

|StudentID|StudentName|Course|Instructor|InstructorPhone|
|---|---|---|---|---|
|101|JohnDoe|Math|Dr. Smith|123-456-7890|
|102|JaneRoe|Math|Dr.Smith|123-456-7890|
|103|SamJoe|Physics|Dr.Brown|987-654-3210|
|104|AliceRay|Math|Dr.Smith|123-456-7890|



© Copyright 2025 MIVA Open University AlRights Reserved 

34 

Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
@ M I “Is<br><!-- End of picture text -->

###### Normalisation Steps: 

First Normal Form (1NF): Ensure atomicity by creating separate tables for students and instructors. 

|101|JohnDoe|Math|
|---|---|---|
|102|JaneRoe|Math|
|103|SamJoe|Physics|
|104|AliceRay|Math|



Second Normal Form (2NF): Remove partial dependencies by creating a separate table for courses. 

|1<br>Dr. Smith|123-456-7890|
|---|---|
|2<br>Dr.Brown|987-654-3210|



Third Normal Form (3NF): Remove transitive dependencies. 

|q|Math|1|
|---|---|---|
|2|Physics|2|



The tables are now fully normalised, reducing redundancy and improving efficiency. 

###### 11.8 Limitations of Traditional Database Management System 

Traditional Database Management Systems (DBMS) have long been the backbone of data storage and retrieval in various applications. However, as data needs have evolved, these systems face several limitations that impact their efficiency, scalability, and adaptability. Below are some of the key limitations of traditional DBMS: 

© Copyright 2025 MIVA Open University All Rights Reserved 

35 

MIVA OPEN UNIVERSITY 

###### Review of Traditional Relational Databases and Advanced Concepts 

###### 8, M I T L 

SCALABILITY ISSUES: Traditional DBMS, particularly relational databases, struggle with handling large volumes of data and concurrent transactions. Vertical scaling (adding more power to a single machine) is often costly and has limits, while horizontal scaling (distributing data across multiple servers) is challenging due to rigid schema structures. 

RIGID SCHEMA DESIGN: Traditional DBMS require predefined schema, meaning that any change in data structure necessitates significant modifications. This rigidity makes it difficult to handle dynamic and unstructured data efficiently. 

LIMITED PERFORMANCE WITH BIG DATA: The structured approachof traditional databases makes them inefficient for handling massive datasets, especially unstructured or semi-structured data like social media posts, sensor data, and multimedia files. Query performance can degrade significantly as the data grows. COMPLEXITY IN HANDLING DISTRIBUTED DATA: Traditional DBMS were designed for centralised data storage. As modern applications demand global accessibility and distributed data storage, traditional databases struggle with maintaining consistency, replication, and synchronisation across multiple locations. 

HIGH MAINTENANCE COSTS: Managing a traditional DBMS requires significant resources, including database administrators (DBAs) for optimisation, security, and regular maintenance. This increases the overall operational costs, especially for large enterprises. 

CONCURRENCY AND LOCKING ISSUES: Handling concurrent transactions can lead to locking and deadlocks, affecting performance and user experience. As multiple users access and modify data, contention for resources may slow down transaction processing. 

LIMITED SUPPORT FOR REAL-TIME ANALYTICS: Traditional databases are optimised for Online Transaction Processing (OLTP) but struggle with Online Analytical Processing (OLAP). This limitation makes them unsuitable for real-time analytics and business intelligence applications that require fast query execution on massive datasets. 

SECURITY AND COMPLIANCE CHALLENGES: While traditional DBMS provide security mechanisms like access control and encryption, they often lack robust support for modern security needs such as advanced encryption techniques, zero-trust architectures, and compliance with evolving regulations like GDPR and CCPA 

Review ofTraditional Relational Databases and Advanced Concepts 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

INABILITY TO HANDLE NOSQL REQUIREMENTS: Many modernapplicationsrequire NoSQL capabilities to manage unstructured or semi-structured data. Traditional relational databases are not designed to accommodate such data models, making them unsuitable for applications like loT, social media, and big data analytics. 

LIMITED SUPPORT FOR CLOUD INTEGRATION: While cloud computing has become essential for modern businesses, traditional DBMS are often not optimised for cloud-native environments. Migrating legacy databases to the cloud can be complex, requiring extensive modifications and reconfiguration. 

Although traditional DBMS have been reliable for structured data management, their limitations have led to the rise of NoSQL, NewSQL, and other modern database technologies. Organisations now seek more flexible, scalable, and performance-driven solutions to meet the demands of big data, real-time analytics, and distributed computing. 



<!-- Start of picture text -->
A SS<br>ay” Sa<br><!-- End of picture text -->

Review of Traditional Relational Databases andAdvanced Concepts 



<!-- Start of picture text -->
“<br>Ss) MIVAMOPEN IUNIVERSITY T<br><!-- End of picture text -->

J) 

###### SUMMARY 

This study session examined the foundations of traditional relational databases and their progression into advanced database concepts. It began by reviewing the relational model, which structures data into tables governed by keys, relationships, and constraints. The discussion also covered the essential components of a relational database system, such as tables, records, attributes, and schemas, and highlighted the processes involved in designing databases, including entity-relationship modelling and schema development. An important part of the design process is normalisation, which eliminates redundancy, improves consistency, and ensures that data is stored efficiently. These principles form the basis for maintaining data integrity, enabling reliable querying, and sustaining performance in relational systems. 

The session also acknowledged the limitations of traditional relational databases. While they are highly effective in managing structured data and transactional operations, they struggle with the scale, diversity, and velocity of modern data. The rise of big data, unstructured information, and the need for distributed systems has revealed the shortcomings of purely relational approaches. To respond to these challenges, new categories of databases have emerged. Students were introduced to advanced technologies such as NoSQL and NewSQL systems, which provide scalability and flexibility, as well as distributed and cloud-based databases, which enhance availability and resilience. Specialised databases such as graph and time-series systems were also discussed as solutions designed for complex, domain-specific applications. Together, these developments demonstrate how modern databases extend and complement the relational model, ensuring relevance in both traditional and contemporary applications. 

© Copyright 2025 MIVA Open University AllRights Reserved 

38 

Review of Traditional Relational Databases andAdvanced Concepts 

> “ Ss) MIVAMOPEN IUNIVERSITY T 

Traditional Database Management Systems (DBMS) have been fundamental in structuring, storing, and managing data efficiently across various industries. They provide structured data storage, integrity, security, and standardised query capabilities, making them essential for applications such as banking, e- commerce, and enterprise resource planning. 

However, despite their strengths, traditional DBMS face several limitations, including scalability issues, rigid schema structures, and inefficiencies in handling large-scale or unstructured data. Their centralised approach poses challenges for distributed data management, while high maintenance costs and concurrency control issues hinder performance in modern applications. Additionally, their limited adaptability to real-time analytics, cloud integration, and NoSQL requirements make them less suitable for dynamic and evolving business needs. 

As technology advances, organisations are increasingly turning to NoSQL, NewSQL, and cloud-based databases to overcome the constraints of traditional DBMS. These modern solutions offer greater flexibility, scalability, and performance optimisation for big data, real-time processing, and globally distributed applications. While traditional DBMS remain valuable for structured data management, adapting to emerging database technologies is crucial for meeting the demands of today’s data-driven world. 

In conclusion, a well-informed database selection should consider the specific needs of an application, balancing the reliability of traditional DBMS with the flexibility and performance benefits of modern database solutions. 

© Copyright 2025 MIVA Open University AllRights Reserved 

39 

STUDY SESSION TWO 

Distributed Database System 

###### Distributed Database System 



<!-- Start of picture text -->
P<br>“<br>Ss) MIVAMOPEN IUNIVERSITY T<br><!-- End of picture text -->

A Distributed Database System (DDBS) is a collection of multiple, logically interrelated databases distributed over a computer network. Unlike centralised databases where all data is stored and managed ona single server, a distributed database system allows data to be stored across different locations, often on different machines, and accessed as if it were a single unified database. This architecture is designed to improve performance, availability, and reliability, especially for organisations with global operations or systems that require high scalability. 

To the user, a distributed database system should appear as a single database. This is achieved through a key property called transparency, which encompasses several forms: location transparency (users don't need to know where data is stored), replication transparency (users are unaware of the replication details), fragmentation transparency (users don’t need to know how data is divided), and transaction transparency (ensuring that operations meet the ACID properties—Atomicity, Consistency, lsolation, Durability—even across distributed components). 

~~ — The architecture of a DDBS can be homogeneous or 4 heterogeneous. In homogeneous systems, all ———< ¥ dng hia nodes use the same database management 7 = \ P| nf) system (DBMS) software, simplifying integration y NY / “ “< _ and communication. In contrast, heterogeneous Pip. ’ . <e systems use different DBMSs, which introduces —_—= > =>Zé =SS | butcomplexityut allowsall greater ingreater dataflexibility exchangeflexibility inandintegratingtegrating query processinglegacylegac J i - systems or specialised databases. The evolutionofdistributed database systems volumesstems from of thete9 anesgrowing needaactoss to manageelvast Distributed database systems offer several database systems offer several offer several several . geographical locations. As organisationsne expanded benefits,;; including improved improved reliability,:: as the failurei the failurei failureii and interneti technologiesi matured, centralised: of one site does not. one site does not. site does not. does not. not.. necessarilyosos render the entire the entire entire =tems began facing limitations interms of system unusable; unusable; scalability, as more nodes can be more nodes can be can be be a added to handle handle increasing data loads; and faster scalability, fault tolerance, and latency. In response, . ‘ distributed databaseaystemeu enieried asa data access, as queries can be directed to the site access, as queries can be directed to the site as queries can be directed to the site queries can be directed to the site can be directed to the site be directed to the site directed to the site to the site the site site é powerful alternative, leveraging the advantages3 of closest to the user. However, they: the user. However, they: user. However, they: However, they: they:: also introduce introduce decentralised control and parallel processin Challenges suchas Cate Consistency, suchas Cate Consistency, Cate Consistency, Consistency, U P 9: synchronisation, concurrency control, and security concurrency control, and security control, and security and security security 

Distributed database systems offer several database systems offer several offer several several benefits,;; including improved improved reliability,:: as the failurei the failurei failureii of one site does not. one site does not. site does not. does not. not.. necessarilyosos render the entire the entire entire system unusable; unusable; scalability, as more nodes can be more nodes can be can be be added to handle handle increasing data loads; and faster . ‘ data access, as queries can be directed to the site access, as queries can be directed to the site as queries can be directed to the site queries can be directed to the site can be directed to the site be directed to the site directed to the site to the site the site site closest to the user. However, they: the user. However, they: user. However, they: However, they: they:: also introduce introduce Challenges suchas Cate Consistency, suchas Cate Consistency, Cate Consistency, Consistency, synchronisation, concurrency control, and security concurrency control, and security control, and security and security security management across multiple sites. 

One of the defining characteristics of a DDBS is data distribution, which can be classified into two . . an main strategies: fragmentation and replication. Fragmentation involves£ dividinga a database intoA smaller pieces (fragments) that are stored at different sites.i These fragments can be horizontal (rows-based), vertical. (columns-based), or a hybridof both. Replication, on the other hand, involves rig nae eee copying and storing the same data at multiple sites to increase: data availabilityrn and enhance fault tolerance. Many systems use a combination of both to balance performance and reliability. 

- ‘ In conclusion, distributed database systems play a a A critical role in modern data management,: [PETE Ineoelem sMslegp layers en globally distributed applications.‘ As dataey continues to grow in scaleE and complexity,fi the principles and cae eS Ue P ESAs Secale increasingly essential for building resilient, high6 performance information systems. 

© Copyright 2025 MIVA Open University AllRights Reserved 

41 

Gce M ceeI T 

###### Distributed Database System 

###### Key components of distributed database architecture include: 

Data Fragmentation:The database is divided into smallerq smallerq 

The database database is divided into smallerq smallerq parts called fragments. These can be: 

- + Horizontal fragments: subsets of rows. 

- + Vertical fragments: subsets of CSE 

- + Mixed fragments: a combination of both. Fragmentation improves performance by allowing queries to access only the relevant portion of data. 

DataCopies—_”of the same DataDetermines—_ where data may be stored at each fragment or multiple sites to replica should be increase reliability stored. Allocation and data availability. strategies are Replication ensures designed to hateveniione site alias fails, data can still be communication accessed from costs and optimise another. query performance. 

Transparency: One of the main architectural goals is to provide different types of transparency: 

q i goals Network: 

Arobust and efficient network is crucial for data sharing and synchronisation among sites. It supports query routing, transaction coordination, and system monitoring. 

- + Location transparency: Users do not need to know the physical location of data. 

- + Replication transparency; Usels are unaware of how many copies 

- Of data exist. 

- + Fragmentation transparency: Users do not need to know how data is divided. 

###### Distributedxy (DDBMS): 

This software layer manages the entire distributed system. It handles query processing, transaction management, 

concurrency control, and recovery across multiple nodes. 

- + Transaction transparency: Transactions are processed as if the data were centralised, maintaining consistency and integrity. 

Distributed Database System 

###### 6 M I a 



<!-- Start of picture text -->
_ “Ss Database<br>tae ” Architecture<br>H<br>ts 5<br>7 mr:<br>|«iti4<br>[<br>7<br>if if t —<br>. C i ae PM —_-<br><!-- End of picture text -->

In conclusion, the architecture of a distributed database system plays a critical role in ensuring data is managed effectively across geographically or logically separated sites. A well-designed architecture provides users with seamless access, ensures data consistency, and supports scalability, fault tolerance, and high availability. The architecture of a distributed database is as shown in Figure 3.1. 



<!-- Start of picture text -->
Distributed Database System<br>Architecture<br>Communication<br>Network<br>Site 1 Site 2 Site 3<br>Distributed Distributed Distributed<br>DBMS DBMS DBMS<br>Communication<br>Network<br>Communication<br>Network<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AllRights Reserved 

45 

Distributed Database System 

8, M I T ay 

###### 2.1.3 Peer-Peer, Client-Server and Federated Database Architectures 

Organisational structure is not just a theoretical concept; it has profound practical implications for how leaders make decisions, implement strategies, and guide their organisations to success. 

1. Client-Server Architecture Definition: 

In aClient-Server Database Architecture, the database resides on a central server, and client machines send requests to the server to access and manipulate data. 

###### Structure: 

Characteristics: Advantages: Disadvantages: + Centralised data * Centralised * Single point of control. management and failure. * Clients’ interact* Backup: + Performance through a DBMS API or + Controlled access bottleneck at the query language (e.g.. and security. server under high sal). load. + Good for medium- 

* Client: Requests data or services é (e.g.,Sepuser Baront-enaications, **e** nd interfaces). 

+ Good for mediumto-large scale licati applications. 

+ Server: Hosts the 5 Ga seSccins| + Easierconsistency to maintain and DBMS, prprocesses 5 enforce security RUSHES manage policies. . data storage. 

Use Cases: Banking 9 systems,Sy ° ERP systems, corporate intranets. 



<!-- Start of picture text -->
Client /<br><!-- End of picture text -->

Distributed Database System 



<!-- Start of picture text -->
£5,<br>G M I a<br><!-- End of picture text -->

2. Peer-to-Peer (P2P) Architecture Definition: 

In a Peer-to-Peer Database Architecture, each node (peer) acts as both a client and a server. All peers share data and workload equally, without a central coordinator. 



<!-- Start of picture text -->
Structure: Characteristics: Advantages: Disadvantages:<br>+ Nocentral server. + Decentralised + High fault + Complex<br>+ Eachnode stores control. welEMne consistencySyncnron aneand<br>part of the + Dynamic and + Scalable and if Ii<br>database and can scalable network. distributed mechanisms.<br>querylery otherrppeers. + Nodes can join.  or workload. + Securityurity andru trust<br>leave without + Resilient tonode issues among<br>disrupting the failures. aeson<br>system.<br><!-- End of picture text -->

Use Cases: File sharing systems (e.g., BitTorrent), blockchain, and some NoSQL systems. 



<!-- Start of picture text -->
Peer<br>EL}.<br>ee oe PS<br>ote : ne<br>[ sercceeccencecenccnncetennetarccenccencceeocneeceeees [<br>mS. F er es<br>Peer co H or Peer<br>ae i ao<br>=<br>Peer<br>rea =| =<br><!-- End of picture text -->

Distributed Database System 



<!-- Start of picture text -->
LU<br>6 MMIVA OPEN UNIVERSITYI a<br><!-- End of picture text -->

3. Federated Database Architecture Definition: 

A Federated Database System (FDBS) integrates multiple autonomous databases into a single federated system, allowing them to cooperate while retaining their independence. 



<!-- Start of picture text -->
Structure: Characteristics: Advantages: Disadvantages:<br>+ Local DBs: + Nocentral control + Preserves local + Complex query<br>Autonomous over local databases. autonomy. processing and<br>databasesindependent!Pe  managed 9¥ +useEachlocal different DB DBMSsmay + Allowsheterogeneousintegration of data+ Inconsistentintegration.9<br>+ Federated Engine: A and data models. systems. policies and data<br>middleware or global P models may cause<br>schemams  that enables” + acrossUsers can databases query + Idealwithfor independent.  organisations conflicts.<br>unified querying and a<br>data - . using a global departments or<br>integration. schema. partners.<br>Use Cases: Federated DBMS<br>Merged ee nn on<br>academic research jcobpreations. Vi Ricans: | :GeppEeat ons |<br>networks, multi- i i a /<br>collaborations. : a i | —<br>| DB1 ii DB2 le | DBn | Global DB<br>» (eg.aRDB) | | Lfeg-anoops)} = |_(e.g-an ADB) J<br>_ epes1 CDBS2. ss CBSn<br><!-- End of picture text -->

Feature Client-Server Peer-to-Peer Federated Control Centralised Decentralised Distributed/ Autonomous Scalability Moderate High Moderate to High Fault Tolerance Low (server failure) High Medium Complexity Low to Moderate High High Use Case Example Banking system Blockchain, P2P Research data sharing collaboration 

© Copyright 2025 MIVA Open University AllRights Reserved 

48 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Distributed Database System 

###### 2.1.4 Data Fragmentation, Replication and Consistency Models 

In distributed database systems, data is stored across multiple sites to improve performance, scalability, and availability. To manage this distribution effectively, key strategies such as data fragmentation, replication, and consistency models are employed. These strategies work together to balance data access speed, fault tolerance, and system integrity. 

###### 2.1.4.1 Data Fragmentation 

Data fragmentation is the process of dividing a database into smaller, manageable pieces Callcg fragments, which are stored at different locations in a distributed system. The goal is to improve performance by storing. data closer to where it—is needed, reduce access latency, and optimisea resource usage. 

###### Replication can be classified into: 

- + Full Replication: Every site stores a copy of the rte Cstebese: 

- + Partial Replication: Only selected fragments are replicated at specific sites. 

There are also two main approaches to data Toolleation: P » | 

- + Synchronous Replication: Updates are propagated to all replicas immediately, ensuring strong consistency but increasing overhead and latency. 

- + Asynchronous Replication: Updates are propagated after some delay, reducing overhead but risking temporary inconsistency. 

7 he f While; replication improves system robustness, it also increases complexity,; particularly in managing updates; and ensuring consistency across all replicas. 

There are three main types of fragmentation: 

- + Horizontal Fragmentation: Divides a table into subsets of rows. For example, customer records can be split by geographic region. 

- F . ae % 

- + Vertical Fragmentation: Divides a table into subsets of columns. This: can be useful when . oe . 

- different applications need access to different attributes of aracord 

- rvanant zi c Ryo (Mixed) ppt unser g comneton a 

- both horizontal and vertical fragmentation. 

Fragmentationsubset3 of data! .isensures accessedss thatduringonly. y thea query,relevantwhich. reduces data transfer and improves performance. However, it. requires2 careful design to maintain‘ coiipletanees|P (po datas losbvand (i . reconstructability (original data can be reassembled). 

###### — 2.1.4.2 Data Replication 

Data replication involves maintaining multiple copies of data at different locations. The main objectives of replication are to enhance availability, improve fault tolerance, and increase access speed by allowing: users to access a nearby replica.7 

###### 2.1.4.3 Consistency Models 

Consistency models define how updates to replicated data are visible across the distributed : ; ‘ system.a The choice of model impacts the. system's reliability, performance, and user experience. 

Key consistency models include: 

- + Strong Consistency: Ensures all users see the same data at all times. Updates are immediately Phe . ‘ 

- visible system-wide. It provides correctness but can slow performance. 

- + Eventual Consistency: Guarantees that,E .in the absence of new updates, all replicas will ‘ eventually converge to the same state. It's commonly used in large-scale systems (e.g., NoSQLé databases) where availability is prioritised. 

- + Causal Consistency: Maintains the order of related operations. If one update logically follows another, all users see them in the same order. 

- . . f 

- . eet hes Ensures thata poe! or thesresuleel teroWn Upsates immediately. 

© Copyright 2025 MIVA Open University AlRights Reserved 

49 

Distributed Database System 

LU 6 **M** IVA OPEN UNIVERSITYI a 

Consistency models must balance the CAP theorem trade-offs—Consistency, Availability, and Partition tolerance—depending on the system's goals. 

ITQ 21: 

Explain how data fragmentation, replication, and consistency models work together in distributed databases. 

ITA 2.1: 

Data fragmentation splits databases into smaller parts to improve performance, while replication creates data copies across sites to enhance availability and fault tolerance. Consistency models ensure how updates are reflected across replicas, balancing performance with reliability. Together, these strategies optimise data access, system integrity, and fault tolerance in distributed databases. 

In Conclusion, Data fragmentation and replication are foundational concepts in the design of efficient and reliable distributed databases. When applied effectively, they enhance performance, ensure availability, and maintain data integrity, enabling robust and scalable data-driven systems. 

© Copyright 2025 MIVA Open University AllRights Reserved 

50 

###### Distributed Database System 



<!-- Start of picture text -->
><br>Ss) M I T<br><!-- End of picture text -->

###### Part B 

CAP TH EORE h ( BAS E A N D IX@ | D MO1D)9 E LS ’ 

- CA (Consistency<sup>+Availability): Only possible</sup> if there are no network partitions—which is unrealistic in distributed environments. 

###### 2.2.1 CAP Theorem, DBASE vs ACID Models , 

Distributed databases must balance consistency, availability, and reliability while handling data across multiple locations. To guide the design of such systems, key concepts like the CAP Theorem, DBASE model," and ACID properties play a critical‘ role. 

###### 2.2.1.1 CAP Theorem 

The CAP Theorem, proposed by Eric Brewer, states that in any distributed data system, it is impossible to simultaneouslyIh guarantee all thithree ofif theth following: 



<!-- Start of picture text -->
j :<br>{Consistency<br>CA CP<br>Sey oe<br>- a Partition<br>Availability Tolerance /<br>AP<br>=<br><!-- End of picture text -->

###### | CAP Theory Diagram 

The CAP theorem helps database designers make trade-offs based on system requirements and failure scenarios 

eee | —=Qe 1. Atomicity: 

- Qe 1. Atomicity: Each<sup>transactionisall-</sup> v or-nothing—either it is fully completed or not executed at all. 

- = 2. Consistency: Transactions bring 

- Cy,© j, the database from one valid state wee to another, preserving data integrity. 

According to the theorem, a distributed system can only provide two out of the three guarantees at the same time. For; example: a 

   3. Isolation: Concurrent transactions 

   Ww are executed as if they were j sequential, preventing data anomalies 

- CP (Consistency + Partition Tolerance): Systems like traditional SQL databases prioritise consistency over availability. 

   4. Durability:Once a transaction is POinited treme coterenin the event of a system failure, as eRovmbalov 

- + AP {availabilityrena + Partitiona Tolerance): Systems like Amazon's Dynamo or Cassandra allow data to be eventually consistent for high availability. 

© Copyright 2025 MIVA Open University AllRights Reserved 

51 

###### Distributed Database System 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->



<!-- Start of picture text -->
a<br>_ Atomicityy aoe » Consistency-<br>i All or nothing ; : Preserving database invariants '<br>i es | [ conetatont state |<br>'H __ commit all __ Transactions<br>: watels) or nothing *SsDB ! - i -<br>il Teaneaction consistent state B<br>isolated from each other<br>:<br>r sss transaction<br>' = ' 1.commit '<br>1 Transactionre  A baa: SS > ve 2. i} ‘DB;-_ H|<br>isolated yv i ak<br>H SeayMites)b i an DB ji'H 2.replicated@ 2 2.replicatedne S i<br>Transaction B ‘ ' '<br>H ' replicaa replicab |<br><!-- End of picture text -->

ACID is essential in environments where data integrity and reliability are critical—such as banking, finance, and enterprise resource planning (ERP) systems. However, strict adherence to ACID can reduce performance and scalability in distributed systems, prompting the need for more flexible models. 

###### 2.2.1.3 DBASE Model 

The DBASE model, proposed for modern distributed and NoSQL databases, offers a relaxed approach compared to ACID to support scalability and high availability: 

© Copyright 2025 MIVA Open UniversityAllRights Reserved 

52 

6 Miva OPEN IUNIVERSITY a 

###### Distributed Database System 

Durability: Basically Available: Soft state: Eventual Similar to ACID, it The system The system state consistency: ensures that guarantees may change over The system will committed data availability, though time, even become consistent survives system responses may not withoutinput, over time, assuming failures. always be the most due to eventual no new updates. up-to-date. consistency. 

DBASE aligns closely with AP systems in the CAP model, favouring scalability and fault tolerance over immediate consistency. It is commonly used in NoSQL databases like Cassandra, Couchbase, and DynamoDB. 

In Conclusion, the CAP Theorem, ACID, and DBASE models represent different philosophies in distributed database design. While ACID focuses on data integrity and reliability, DBASE supports scalability and availability in large, distributed environments. The CAP theorem frames the unavoidable trade-offs among consistency, availability, and partition tolerance, guiding the choice of database models based on specific application needs. 

###### 2.2.2 Trade-offs in Distributed Systems with CAP CAP theorem, BASE and ACID models 

###### 2.2.2.1 Definition 

The CAP Theorem states that a distributed database cannot simultaneously guarantee Consistency, Availability, and Partition Tolerance. 

|Guarantee|Description|
|---|---|
|Consistency (C)|Allnodesseethesamedataatthesametime|
|Availability (A)|Everyrequestgetsaresponse (success/failure), even ifnotthelatest|
|PartitionTolerance(P)|Systemcontinuesoperatingdespitenetworkfailures|



© Copyright 2025 MIVA Open University AllRights Reserved 

53 

Distributed Database System 

###### G M I a 

###### CAP Trade-off Examples 

|Model|Guarantees|Examples|Notes|
|---|---|---|---|
|cP|Consistency +|HBase,MongoDB (with|Sacrifices availabilityduring|
||PartitionTolerance|strong consistencymodes)|partitions|
|AP|Availability+ Partition|Cassandra, Amazon|Allows stale reads; eventual|
||Tolerance|DynamoDB|consistency|
|CA|Consistency + Availability|TraditionalRDBMS (only in|Notfeasible indistributed|
|||non-partitionedsystems)|systemswithfailures|



###### 2.2.2.2 ACID Properties (Ideal for RDBMS) 

|Property|Description|Application<br>Examples|
|---|---|---|
|Atomicity|Transactionsareall-or-nothing|Banking systems|
|Consistency|Maintainsvaliddatabasestatebeforeandafter<br>transactions|Financial<br>databases|
|Isolation|Prevents interference betweenconcurrenttransactions|Airline booking<br>systems|
|Durability|Committeddata remainsintactdespitefailures|ERP,healthcare<br>systems|



Best For: Systems needing strict integrity - SQL databases (PostgreSQL, Oracle) 

###### 2.2.2.3 DBASE Model (Ideal for NoSQL/Distributed Systems) 

|Property|Description|Examples<br>(NoSQL)|
|---|---|---|
|Durability|SimilartoACID—datasurvivessystemcrashes|DynamoDB,<br>Couchbase|
|Basically Available|High availability even ifnot fullyconsistent|Cassandra, Riak|
|Soft State|Systemstatecanchangeovertimeevenwithout input<br>(dueto replication)|CouchDB|
|Eventual|Datawillbecomeconsistenteventuallyifnonewwrites|AmazonS3,|
|Consistency|<br>occur|<br>DynamoDB|



Best For: High-scale, fault-tolerant systems with relaxed consistency 

© Copyright 2025 MIVA Open University All Rights Reserved 

54 

Distributed Database System 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

###### 2.2.2.4 ACID vs. DBASE Comparison Table 

|Feature|ACID (RDBMS)|DBASE(NoSQL)|
|---|---|---|
|Focus|Integrity, Reliability|Scalability, Availability|
|ConsistencyLevel|Strong|Eventual|
|Availability|Canbecompromised innetworksplits|High|
|Performance inScale|Lower|Higher|
|Best For|Finance, ERP, Healthcare|Social media, loT, E-<br>commerce|



- + CAP Theorem highlights unavoidable trade-offs in distributed databases. 

- + ACID ensures strong guarantees for critical applications. 

- + DBASE offers flexibility for modern, distributed, high-availability systems. 

- + Design choice depends on application needs: integrity (ACID) vs scalability and fault-tolerance (DBASE). 

© Copyright 2025 MIVA Open University AlRights Reserved 

55 

Distributed Database System 



<!-- Start of picture text -->
“<br>Ss) MIVAMOPEN IUNIVERSITY T<br><!-- End of picture text -->

J) 

###### SUMMARY 

A Distributed Database System (DDBS) is a robust architecture designed to store and process data across multiple physical locations, offering users a unified, seamless experience despite the distribution of data. The two primary types of DDBS are Homogeneous and Heterogeneous. Homogeneous systems utilise the same Database Management System (DBMS) and Operating System (OS) across all sites, making them easier to manage and maintain with consistency. In contrast, Heterogeneous systems integrate different platforms and DBMSs, requiring middleware for seamless data management, making them suitable for complex, multi-faceted organisations. 

Key concepts in DDBS architecture include fragmentation, replication, and data allocation. Fragmentation involves splitting data to improve efficiency, replication ensures data availability and fault tolerance, and data allocation strategically places data across locations for optimal performance. Transparency—in terms of location, replication, and transaction handling—ensures users are unaware of the system's underlying complexities, providing an easy-to-use interface. 

DDBS can be structured in various architectural models, including Client-Server, Peer-to-Peer (P2P), and Federated Systems. Client-Server models centralise control, simplifying management but introducing risks such as single points of failure. P2P systems are decentralised, offering scalability and fault tolerance but challenging consistency and security. Federated systems allow independent databases to work together under a global schema, making them ideal for cross-departmental or cross-institutional collaborations. 

Data warehouses serve as central repositories for historical data, playing a critical role in data consolidation and analytics. Unlike federated databases, which provide real-time access without central storage, data warehouses integrate and structure data for in-depth business intelligence and decision-making. The CAP Theorem formalises the trade-offs inherent in distributed systems, stating that a system can only guarantee two out of three properties: Consistency, Availability, and Partition Tolerance. Traditional relational databases typically favour consistency, while systems like NoSQL prioritise availability and partition tolerance. 

In terms of transaction management, distributed systems rely on two primary models: ACID and DBASE. ACID (Atomicity, Consistency, Isolation, Durability) ensures strict data integrity, making it suitable for critical applications, while the DBASE model (Durability, Basically Available, Soft state, Eventual consistency) offers flexibility, supporting high-availability systems such as modern cloud applications and web services. 

© Copyright 2025 MIVA Open University AllRights Reserved 

56 

Distributed Database System 

“ Ss) MIVAMOPEN IUNIVERSITY T 

J) 

###### CONCLUSION 

Distributed database systems have become indispensable in modern data management, offering scalability, fault tolerance, and enhanced performance by distributing data across multiple physical locations. Their architecture ensures users can access and manipulate data seamlessly, without needing to understand the underlying distribution. These systems are primarily built using either homogeneous or heterogeneous architectures—homogeneous systems use a uniform DBMS across sites, promoting easier maintenance and consistency, while heterogeneous systems integrate diverse databases and technologies, offering flexibility in complex enterprise environments. 

A well-structured distributed database architecture comprises key components like data fragmentation, replication, allocation, and transparency. Fragmentation enhances performance by breaking databases into logical pieces (horizontal, vertical, or hybrid), while replication ensures availability and fault tolerance by creating redundant copies across sites. Allocation optimises storage location to reduce communication costs. Transparency—whether in location, replication, or fragmentation—hides system complexity from users, ensuring ease of use. 

Three major architectural paradigms help implement distributed systems based on organisational needs: Client-Server, Peer-to-Peer (P2P), and Federated architectures. The Client-Server model centralises control and simplifies management but risks single points of failure. P2P systems are fully decentralised, enabling robust scalability and fault tolerance, though they introduce challenges in consistency and security. Federated databases allow autonomous systems to cooperate without relinquishing control, making them suitable for cross-institutional or departmental collaborations. 

As organisations seek to consolidate and analyse vast data from disparate sources, data warehousing plays a pivotal role. Unlike federated databases that provide real-time access without central storage, data warehouses integrate and clean data into a centralised, historical repository optimised for business intelligence and analytical queries. Warehouses are subject-oriented, time-variant, and non-volatile, supporting long-term insights and decision-making. 

Data fragmentation and replication are central strategies in distributed database design. Fragmentation improves localised access and reduces latency, while replication enhances system reliability and access speed. However, replication introduces the challenge of maintaining consistency, which is governed by different models such as strong consistency, eventual consistency, causal consistency, and read-yourwrites consistency. Each model involves trade-offs between performance, availability, and integrity. 

These trade-offs are formalised in the CAP Theorem, which states that a distributed system can only simultaneously satisfy two out of three: Consistency, Availability, and Partition Tolerance. This principle guides the design of systems like traditional SQL databases (which prioritise consistency) and NoSQL systems like Cassandra (which favour availability and partition tolerance). 

© Copyright 2025 MIVA Open University AllRights Reserved 

57 

Distributed Database System 

> “ Ss) MIVAMOPEN IUNIVERSITY T 

To manage transactions in distributed settings, two philosophical models are adopted: ACID and DBASE. The ACID model (Atomicity, Consistency, Isolation, Durability) ensures strict data integrity and is wellsuited for mission-critical systems. In contrast, the DBASE model (Durability, Basically Available, Soft state, Eventual consistency) supports flexibility and scalability in high-availability environments, such as modern web and cloud applications. 

In essence, distributed database systems blend architectural ingenuity with strategic trade-offs to support varied business needs—from transactional accuracy to analytical depth. Understanding their structures, models, and operational paradigms enables organisations to build resilient, high-performing, and scalable data infrastructures for the data-driven era. 

© Copyright 2025 MIVA Open University AllRights Reserved 

58 

STUDY SESSION THREE 

Big Data and Cloud Database Systems 

“ Ss) MIVAMOPEN IUNIVERSITY T 

###### Big Data and Cloud Database Systems 

###### INTRODUCTION 

In the digital era, data is being generated at an Cloud platforms such as Amazon Web Services such as Amazon Web Services as Amazon Web Services Amazon Web Services Web Services Services unprecedented pace from a multitude of sources, (AWS), Microsoft Azure, Azure, and Google Cloud Platform Google Cloud Platform Cloud Platform Platform such as social media platforms, sensors, mobile (GCP) offer managed managed Big Data services that services that that devices, enterprise applications, and the Internet integrate storage, storage, processing, analytics, and of Things (loT). This explosion in data volume, machine learning, making it easier easier for businesses businesses to velocity, and variety has given rise tothe conceptof —— derive insights without managing without managing managing infrastructure Big Data, which refers to datasets that are so large complexities. or complex that traditional data processing tools ue InesleebeNe WolRe mal ouRSEIEIBEAE 5 Cloud databases can be classified into two main databases can be classified into two main can be classified into two main classified into two main two main main ERE EEIENE | Bfare Oe Ns ME SSE types: relational and non-relational. Relational and non-relational. Relational non-relational. Relational NET) NTE TEIN jena TES VEEHIES . cloud databases, such as Amazon RDS and Google databases, such as Amazon RDS and Google such as Amazon RDS and Google as Amazon RDS and Google Amazon RDS and Google and Google Google byanligie ic eWelleng[eS istoung) Processing: Cloud SQL, support structured data and use SQL, support structured data and use support structured data and use structured data and use data and use and use CREWE) and extracting meaningful insights from traditional SQL for querying. SQL for querying. for querying. querying. Non-relational or ESE VES elG PREMISE CEES: NoSQL cloud databases like DynamoDB or Cosmos cloud databases like DynamoDB or Cosmos databases like DynamoDB or Cosmos like DynamoDB or Cosmos DynamoDB or Cosmos or Cosmos Cosmos 

Cloud platforms such as Amazon Web Services such as Amazon Web Services as Amazon Web Services Amazon Web Services Web Services Services (AWS), Microsoft Azure, Azure, and Google Cloud Platform Google Cloud Platform Cloud Platform Platform (GCP) offer managed managed Big Data services that services that that integrate storage, storage, processing, analytics, and machine learning, making it easier easier for businesses businesses to derive insights without managing without managing managing infrastructure complexities. 

Cloud databases can be classified into two main databases can be classified into two main can be classified into two main classified into two main two main main types: relational and non-relational. Relational and non-relational. Relational non-relational. Relational cloud databases, such as Amazon RDS and Google databases, such as Amazon RDS and Google such as Amazon RDS and Google as Amazon RDS and Google Amazon RDS and Google and Google Google Cloud SQL, support structured data and use SQL, support structured data and use support structured data and use structured data and use data and use and use traditional SQL for querying. SQL for querying. for querying. querying. Non-relational or NoSQL cloud databases like DynamoDB or Cosmos cloud databases like DynamoDB or Cosmos databases like DynamoDB or Cosmos like DynamoDB or Cosmos DynamoDB or Cosmos or Cosmos Cosmos DB are optimised for scalability and handle various data formats including JSON, XML, and graphs. The choice between them depends on the nature of the data, application requirements, and performance needs. 

To manage and analyse Big Data efficiently, organisations have increasingly turned to cloud computing—a model that provides on-demand access to shared computing resources over the internet. Cloud database systems are databases that run on cloud ILLES SE offering scalable, Wewlevchshesscicaioce Mie AE SHEE? aWelinetieg erate Ualteotse slice ae (SERIES databases, cloud GEV SESS benefit from the elastic nature of the cloud, allowing users to scale resources up or down based on demand. 

One of the major benefits of using cloud databases in Big Data environments is high availability and disaster recovery. Data replication across multiple geographic regions ensures continuity and resilience. Moreover, pay-as-you-go pricing models F , ee in cloud services allow organisations to manage costs effectively, paying only for the resources they consume. 

Big Data technologies such as Hadoop, Spark, and NoSQL databases (e.g., MongoDB, Cassandra, base) Deve Seoue ESTASev Wats testicle CEH UEE GEV) NES systems are geagued po distoure data Across indlidfe OTe eIESs Grelelias palele ee ems. ET EST EREIME SS 5G ETT UTES ES CHEST SIME ESSE, 

These advanced concepts are needed to manage data efficiently. To keep this data out of reach for bad actors, we need robust data security. Data security refers to the processes and technologies used to protect data from unauthorised access, corruption, or theft. It involves the implementation of physical, administrative, and technical Sacer vee as encryption, firewalls, access controls, intrusion detection systems, and regular security audits. The goal of data security is to ensure confidentiality, integrity, and availability— often summarised as the CIA triad. Confidentiality ensures that data is only accessible to authorised users; integrity guarantees that data is accurate and unaltered; and availability ensures that information is accessible when needed. 



<!-- Start of picture text -->
: ™. j<br>atl y ‘ , = % P|<br>>ak aSI> a I ‘y<br>ofl heey Gero! tis<br>eel at Ese aaey rial<br>_——— oy a ae ih<br>2Syl ee uF<br>: E ‘ |<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AllRights Reserved 

60 

###### Big Data and Cloud DatabaseSystems 

In summary, the convergence of Big Data and cloud database systems represents a powerful shift in how data is stored, processed, and analysed. By leveraging the scalability of cloud computing and the power of distributed data processing, businesses and researchers can gain faster and **d** riveneeper decisions insights, drivmor **e** innovation,efficiently than and makeever before. data- 

Learning Outcomes When you have studied this session, you should be able to 3.1 Define Big Data. 

> PRACT MIDEee Sorensen 

3.33.4 DiscussDescribe differentPlatforms typesfor Big of CloudData Databases 

3.5 Explain Big Data Technologieslike Hadoop and Spark 

## PartA CBIGLO DATAU D DATA ANDBAS E 

3-11 Big3 Deka Big Data refers to Data refers to refers to to extremely large datasets that 

Big Data refers to Data refers to refers to to extremely large datasets that cannot be efficientlya stored, processed, or analysed using traditionali data processing tools. It involves complex data coming from diverse sources in various5 formats, and 4it requiresé specialised1 A technologies for effective handling. 



<!-- Start of picture text -->
ol Zea :<br>Lf. BIG<br>“e° SDATA<br><!-- End of picture text -->

### G M I a 

###### 3.1.1.1 Characteristics of Big Data (The 5 V's): 

1. Volume - Refers to the massive amount of data generated daily devices,from sourcesen **s** ors, like socialtransactions, media, loT etc. 



<!-- Start of picture text -->
ia<br><!-- End of picture text -->

2. Velocity - The speed at which new 

oN Geta depetated and processed: For example, real-time data from 

x y, . . 

be c financial markets or social media Sueanis! 

3. Variety - Data comes in different 

68 databases), semi-structuredformats: structured (e.g., relational(e.g., XML, JSON), and unstructured (e.g., videos, images, text). ‘ a 

   4. VeracityThe reliability or trustworthinessinvolves dealing with of data. This inconsistencies, incompleteness, and uncertainty in data. 

   5. Value - The potential of data to createbusiness meaningful value through insights analysis.and 

@)ZN 

< 

sik, ral 

3.1.1.2 Sources of Big Data: Big data refers to extremely | id lex dat ipea retcelsrs =ex1 reme yaalgIr penelal Com peavetax sets that traditional data processing tools cannot efficiently4 manage or analyse. It is characterised by the five V's: Volume, Velocity,. Variety,‘ Veracity, and Value. The sources of big data are diverse and span multiple domains. Understanding these sources is essential to effectively collect, process, and extract insights from big data. Below are the primary sources ofbig data: 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

61 

wavs 6 Mont univensiryI a 

###### Big Data and Cloud DatabaseSystems 

###### Transactional Data 

###### Social. Media. Platforms 

One of the most significantoo sources of big, data today is: social media.' Platforms like Facebook, Twitter, Instagram, TikTok, and ace ‘ ale Linkedin generate vast volumes of useroe eralited content in the form of text, images.9 videos, likes, shares, and comments. These platforms continuously produce real-time data that can be used for sentiment: analysis,; consumer behaviour prediction, and targeted advertising. 



<!-- Start of picture text -->
me) 2 ~<br>)6... 0,9<br><_ f a<br>*<br>*? o@<br>t<br>TheMachineInternetand ofSensor DataThingsInternetand ofSensor DataThings ofSensor DataThingsThings (loT) (oT) connects physical‘@] connects physical‘@] physical‘@]<br><!-- End of picture text -->

TheMachineInternetand ofSensor DataThingsInternetand ofSensor DataThings ofSensor DataThingsThings (loT) (oT) connects physical‘@] connects physical‘@] physical‘@] devices to the internet, enabling them to collect and exchange data. Sensors 

embedded in vehicles, smart homes, industrial machines, agricultural equipment, and wearable devices continuously produce data on temperature, speed, motion, pressure, and more. This machine-generated data is a major contributor to big data, particularly in industries like manufacturing, healthcare, and smart cities. 



<!-- Start of picture text -->
CU)»<br>INTERNET OF THINGS<br>* Xo)<br>>(L$ao= =<br>emo *<br>aa ——<br><!-- End of picture text -->

Business transactions from e-commerce ‘ : 7 platforms, financial services, and retail systems generate large amounts of structured data. This includes sales records, ie Heeinteractions. Transactional datatel is vital for : % a business‘ intelligence, fraud detection,: and improving customer service. 



<!-- Start of picture text -->
=<br><!-- End of picture text -->

WebEveryand actionClickstream users take Data on a 



<!-- Start of picture text -->
‘@]<br><!-- End of picture text -->

Everyand actionClickstream users take Data on a actionClickstream users take Data on a users take Data on a on a a website or application—clicks, scrolls, searches, and purchases—is recorded as clickstream data. Web servers log millions of user activities daily, creating an extensive digital trail. This data is used for website optimisation, user experience analysis, and personalised marketing. 



<!-- Start of picture text -->
Ke €<br>\ 7 = Le<br>f<br>i<br>eB<br>\ —<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University All Rights Reserved 

62 

###### Big Data and Cloud DatabaseSystems 

###### Multimedia Data 

Images, audio, and video4 files from; surveillance like YouTube,cameras,online meetings, video-sh **a** ring platformsnd ; broadcasting services generate9 vast data sets. Multimedia- data ‘is complex to analyse due to its unstructured nature but provides valuable insights in fields such as security, entertainment, and medical imaging. 

###### Mobile Devices 

Smartphones and tablets collect and transmit large volumes of data through apps, GPS services, messages, and calls. Mobile data includes location information, browsing history, app usage, and user preferences. Telecommunication companies and app developers use this data to enhance service delivery and customer experience. 



<!-- Start of picture text -->
~~<br>ot ay<br>S ~<a” =<br>aa<br>a<br><!-- End of picture text -->

To 07 

Scientific Research andPublicData 07 Scientific experiments in fields like genomics, astronomy, and climate science generate enormous data sets. Public data from government agencies,: health institutions,— and : " ; educational organisations also contribute significantly to big data. These datasets support innovation, public policy, and academic research. 

### G M I a 



<!-- Start of picture text -->
=.<br>‘ \ N<br>a]<br>a,\ iNi,er<br>PLey _<br>> : Sq a<br><!-- End of picture text -->

Big data originates from a wide range of sources across digital platforms, physical devices, human interactions, and scientific studies. Its continuous growth presents both opportunities and challenges for organisations. Effective big data management requires advanced tools and technologies for data storage, processing, and analysis to convert raw data into actionable insights. 

###### 311.3 Importance of Big Data 

Big data refers to massive volumes of data that are generated from various sources at high speed and in awide variety of formats. It is often 

characterised by the 5Vs: Volume, Velocity, Variety, Veracity, and Value. As digital 

technologies become more embedded in everyday life, the importance of big data continues to grow across all sectors. It has become a critical asset for organisations, governments, and individuals. 

hn TT \ Informed Decision-Making i One of the most significant benefits of big data is its ability to support data-driven decision-making. By analysing large 1 datasets, businesses and organisations SENGEMA RSME ces Sane that wereey hidden. Thisstrategic decisions,; helps| leadersea make reducePe informed risks,A and improve operational efficiency. 

© Copyright 2025 MIVA OpenUniversityAllRights Reserved 

63 

) 6 MMIVA OPEN UNIVERSITYI a 

###### Big Data and Cloud DatabaseSystems 

————————— i Enhanced Customer Experience i 2 Big data allows companies to understand customer preferences, behaviours, and feedback in j real-time. This enables personalised services, targeted marketing, and improved customer ‘ engagement. For instance, e-commerce platforms use big data to recommend products based f onuser behaviour, increasing customer satisfaction and sales. 

_ 

i Innovation and Product Development i 3 By analysing customer needsand market trends, big data provides insights that can lead to j innovative products and services. It helps in identifying gaps in the market and designing t solutions that are more aligned with user expectations. Companies like Netflix and Amazon use | big data to develop content and services that caterto specific audiences. 

_ 

i Operational Efficiency i 4 Big data analytics can optimise business processes by identifying inefficiencies and areas for | improvement. For example, in supply chain management, real-time data from logistics and { inventory systems can help companies reduce delays, cut costs, and manage resources more | effectively. 

amma i Fraud Detection and Risk Management i 5 Financial institutions and insurance companies use big data to detect fraudulent activities by j analysing unusual transaction patterns or inconsistencies. Risk management also becomes ' more robust with predictive analytics, helping organisations foresee potential issues and take : preventive measures. 

# a 

iHealthcare Advancements i 6 In healthcare, big data is transforming patient care and medical research. Electronic health ] records, wearable devices, and genomic data are being used to improve diagnosis, monitor { patient health, and personalise treatment plans. Big data also supports the early detection of | disease outbreaks and medical trends. 

###### Smart Cities and Governance 

7 Governments use big data to improve public services, urban planning, and disaster response. Traffic patterns, energy usage, and pollution levels can be monitored to create smarter, more sustainable cities. Additionally, data analytics enhance transparency and decision-making in \ governance. 

© Copyright 2025 MIVA Open University All Rights Reserved 

64 

LU 6 **M** IVA OPEN UNIVERSITYI a 

Big Data and Cloud DatabaseSystems 

——————— Scientific and Academic Research ' 8 Big data is crucial in research fields such as climate science, physics, and biology. It allows i researchers to analyse massive datasets from experiments and simulations, accelerating i discoveries and innovations. 

Big data is not just about the volume of data but the value that can be extracted from it. Its importance lies in its ability to provide insights, drive innovation, improve services, and solve complex problems across multiple industries. As technology evolves, the role of big data will become even more central to progress and development. 

###### 3.1.1.4 Technologies of Big Data 

Big data technologies are tools, frameworks, and platforms used to store, process, analyse, and visualise large and complex datasets that traditional systems cannot handle efficiently. These technologies are essential for extracting meaningful insights and making informed decisions in various industries. Big data technologies can be broadly categorised into data storage, data processing, data analysis, and data visualisation tools. 

###### 1. Data Storage Technologies 

One of the core challenges of big data is storing large volumes of structured, semi-structured, and unstructured data. Technologies used include: 

Hadoop Distributed File System (HDFS): A fundamental part of the Apache Hadoop framework, HDFS allows the storage of huge amounts of 1 data across multiple machines. It is fault-tolerant and scalable. NoSQL Databases: Unlike traditional relational databases, NOSQL Technologies databases such as MongoDB, Cassandra, and Couchbase are used 2 designed to handle unstructured and semi-structured data. They are highly scalable and provide fast data access. % Cloud Storage Services: Platforms like Amazon S3, Google Cloud Storage, and Microsoft Azure offer scalable, flexible, and cost-effective solutions for storing big data. 

© Copyright 2025 MIVA Open University AllRights Reserved 

65 

###### Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### 2. Data Processing Technologies 



<!-- Start of picture text -->
=», _So —y——<br>!<br>a=<br>ee, A<br>_ za<br><!-- End of picture text -->

- Processing big data efficiently and in real-time is crucial for timely insights. Key technologies include: 

- + Apache Hadoop: A popular open-source framework for distributed data processing. It uses the MapReduce programming model to process large datasets in parallel across clusters of computers. 

- + Apache Spark: A powerful and fast in-memory data processing engine. Spark is more efficient than Hadoop for many tasks and supports batch and real-time data processing. 

- + Apache Flink and Storm: These frameworks are designed for real-time stream processing, allowing organisations to analyse data as it is generated. 

###### 3. Data Analysis and Machine Learning 

To extract insights from big data, advanced analytics and machine learning tools are used: 

TensorFlow and Apache Mahout and PyTorch: Rand Python: MLlib (Spark): Popular open-source Programming Libraries that provide frameworks for deep languages widely machine learning learning and Al used for statistical algorithms for applications, often used analysis, data mining, clustering, inbig deta projects for and machine learning classification, and complex analysis. inbig data recommendation. 02 environments. 

© Copyright 2025 MIVA Open University AllRights Reserved 

66 

Big Data and Cloud DatabaseSystems 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### 4. Data Visualisation Technologies 



<!-- Start of picture text -->
ace DATA —F<br>oe ‘ '<br>— = = :<br>1Qa<br><!-- End of picture text -->

- Visualisation tools help present data insights in an understandable format. Key tools include: 

- + Tableau and Power BI: User-friendly platforms for creating dashboards, reports, and interactive visualisations. 

- + Apache Superset and Grafana: Open-source visualisation tools that integrate well with big data platforms and databases. 

###### 5. Data Integration and Management 

Combining data from different sources and managing its quality and flow is vital: 

Apache NiFi and Talend: Tools for automating data movement, transformation, and integration. 

Data Lakes: Storage systems like AWS Lake Formation and Azure Data Lake are used to centralise and manage vast datasets from multiple sources. 

Big data technologies form the foundation of modern data-driven decision-making. From storage to realtime analytics and visualisation, these tools enable organisations to handle the complexity and scale of big data effectively. As data continues to grow, these technologies will evolve to meet new challenges and opportunities. 

###### 3.1.1.5 Big Data Architecture 

Big data architecture is the structural design that enables the collection, storage, processing, and analysis of massive volumes of data from various sources. As organisations increasingly rely on data for decisionmaking, having a well-structured big data architecture is essential to efficiently handle the complexity, scale, and speed of big data. 

Big data architecture typically consists of several key layers or components, each responsible for a specific function in the data lifecycle: 

© Copyright 2025 MIVA Open University AlRights Reserved 

67 

Big Data and Cloud Database Systems 

#### @MITM 

###### 1. Data Sources Layer 

This is the entry point where data is generated and collected. Big data comes from various sources such as: 

###### 2 

NoSQL Databases: MongobDB, Cassandra, and HBase are used for semi-structured and unstructured data. 

+ Social media platforms 

- + lol devices and sensors 

- + Enterprise applications 

- + Web logs and clickstreams 

###### 3 

Data Lakes: Centralised repositories like AWS Lake Formation or Azure Data Lake can store all types of data in raw form 

- + Mobile apps 

+ Public and scientific data sources 

‘Thetdata'collected can be structured. semi: structured, or unstructured, and it may arrive in real-time or batches. 

###### 2. Data Ingestion Layer 

The ingestion layer transfers data from multiple sourcesui i into the big i data system. . **I** tt supportsupports both batch and real-time9 data ingestion¥ PP 

1. Batch 2. Real-Time Ingestion: Ingestion: Tools Tools like like Apache Kafka, Apache Sqoop Apache Flume, and Talend are and Amazon lsacion soca importing Kinesis support large volumes streaming and of data at low-latency intervals. transfers. 

###### 3. Data Storage Layer 

Once ingested, data is stored in scalable and distributed storage systems. This layer must accommodate high volume and varied data types: 

###### 4. Data Processing Layer 

This layer transforms raw data into usable insights. t includes both batch and real-time processing rameworns 

1. Batch 

2. Stream 

- Processing: 

   - Processing: Apache Storm, Apache Fine and Spark Streaming handle real-time data analytics. 

- Apache Hadoop MapRedtce)) Apache Spark, and Hive. are used to process large data sets over time. 

###### 5. Data Analysis Layer 

Hi q i learning,and business intelligence operations take his is where advanced = «leo machine place. Data scientists and analysts use tools like 

. Apache Mahout, Spark MLIib (for machine learning) 

* Python, R (for statistical analysis) Jupyter Notebooks and SQL-based * querying tools 

1 

Hadoop Distributed File System (HDFS): For storing large-scale data in distributed clusters 

###### Big Data and Cloud DatabaseSystems 

### 6 M I a 

###### 6. Data Visualisation Layer 

To help users understand complex data, visualisation tools present processed data in graphs, dashboards, and reports: 

+ Tableau, Power BI, Grafana, and Apache Superset are commonly used to create interactive visualisations for decision-makers. 

Big data architecture is a critical framework that supports the entire journey of big data from source to insight. It ensures that large and diverse datasets can be handled efficiently, enabling organisations to gain timely, meaningful insights and maintain data integrity. A well-designed architecture is essential for the successful implementation of big data projects. 

###### 3.1.1.6 Challenges of Big Data 

###### 7. Data Management and Governance Layer 

This layer ensures data quality, security, privacy, and compliance. It includes: 

GX] vetacats management ; lo GES coiloiog 

cess control and encryption fos<sup>Galineage and audittrails</sup> 

Datasets used for Big Data are characterised by their high volume, variety, and velocity, making them difficult to manage using traditional data processing tools. Despite its potential for driving innovcritic l **a** tion challenges. and insights, The most Big Data presents prominent among several thesedatasets, include ensuring storing data and managi quality a **n** dg con ist ncy, ma **s** siv **e** handling privacy and security concerns, performing resource allocation. real-time analytics, and managing cost and 

###### Storing and Managing Massive Datasets 

One of the foremost challenges in Big Data is storing and managing the enormous volumes of data generated every second. Traditional storage systems often fall short when dealing with petabytes or even exabytes of data. Organisations must adopt distributed storage solutions like Hadoop Distributed File System (HDFS) or cloud-based platforms to store data efficiently. However, implementing these systems requires advanced infrastructure and technical expertise. Additionally, organising, indexing, and retrieving data in such vast environments can become increasingly complex over time. 

###### Ensuring Data Quality and Consistency 

Big Data often originates from diverse sources, leading to variations in format, accuracy, and completeness. Data may include duplicate entries, missing values, or inconsistent formats, which can affect the accuracy of analytics and decision-making. Ensuring data quality and consistency is critical but challenging, especially when dealing with real-time and unstructured data. Data cleansing, validation, and standardisation processes must be applied regularly to maintain reliability and trustworthiness across datasets. 

© Copyright 2025 MIVA Open University AllRights Reserved 

69 

Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### Handling Data Privacy and Security 

Big Data systems handle large volumes of sensitive information, including personal, financial, and behavioural data. This makes them attractive targets for cyberattacks and unauthorised access. Protecting data throughout its lifecycle—from collection and storage to analysis—is essential. Organisations must implement robust security measures such as encryption, access control, and auditing. Additionally, complying with data protection laws and regulations, such as the General Data Protection Regulation (GDPR) or Nigeria Data Protection Regulation (NDPR), is crucial to avoid legal and reputational risks. 



<!-- Start of picture text -->
aT " 4<br>———<br>a! <<br><!-- End of picture text -->

###### Performing Real-Time Analytics 

Many applications, such as fraud detection, online recommendations, and traffic monitoring, require real-time or near real-time analytics. Traditional batch processing systems are not designed to handle this requirement. Real-time processing frameworks like Apache Kafka, Spark Streaming, and Flink enable fast data analysis, but their deployment and maintenance are complex. Ensuring low latency while processing high-speed data streams remains a significant technical challenge. 

###### Managing Cost and Resource Allocation 

Big Data projects often require significant investment in hardware, software, skilled personnel, and infrastructure. Cloud services offer scalable solutions, but they can become costly over time if not managed properly. Efficiently allocating resources such as storage, computing power, and bandwidth while controlling operational costs is a critical challenge. Organisations must strike a balance between performance and affordability to sustain their Big Data initiatives. 

© Copyright 2025 MIVA Open University All Rights Reserved 

70 

###### Big Data and Cloud DatabaseSystems 

While Big Data offers transformative potential, it also brings considerable challenges. Addressing issues related to storage, quality, privacy, real-time analytics, and cost is essential for organisations to effectively harness the power of Big Data and make informed decisions. 

###### 3.1.1.7 Application of Big Data 

With the right tools and technologies, Big Data can be analysed to uncover patterns, trends, and insights that help improve decision-making and innovation. Today, Big Data is applied across a wide range of industries and domains. Below aresomeof the key applications of Big Data: 

###### 1. Healthcare 

In healthcare, Big Data is used to improve patient care, optimise operations, and support medical research. Hospitals and clinics use data from electronic health records (EHRs), wearable devices, and diagnostic tools to monitor patients in realtime, predict disease outbreaks, and personalise treatment plans. Predictive analytics helps identify high-risk patients and prevent hospital readmissions. Additionally, Big Data supports drug discovery by analysing vast datasets from clinical trials and genomic research. 



<!-- Start of picture text -->
. <S<br>g é g<br>i<br>" =<br>K Fo} i & =<br>ae, a e =<br>= ¢ =<br>¥ ln) 2}\<br><!-- End of picture text -->

### 6 M I a 

banking services and targeted marketing. 

###### 5: Retalland E-commerce 

; , Inthe:retall industry, Big Data helps businesses understand customer preferences, shopping patterns, and market trends. Retailers use this information to optimise inventory, improve customer experience, and personalise marketing campaigns. E-commerce platforms analyse user behaviour to recommend products, set dynamic pricing, and enhance supply chain management. Companies like Amazon and Walmart rely heavily on Big Data to stay competitive and improve operational efficiency. 



<!-- Start of picture text -->
A<br>.<br>. 0° ey<br>\ — 5<br>— =<br>: é<br><!-- End of picture text -->

###### 4. Transportation and Logistics 

Big Data is transforming the transportation and logistics industry through route optimisation, realtime tracking, and predictive maintenance. Logistics companies analyse traffic data, weather conditions, and delivery schedules to minimise delays and reduce fuel costs. Public transportation fleets, and provide real-time updates to systems use Big Data to improve services, manage passengers. In aviation and railways, predictive analytics helps in maintaining equipment and preventing accidents. 

###### 5. Education 

###### 2. Finance and Banking 

Financial institutions use Big Data for fraud detection, risk management, customer analytics, and algorithmic trading. By analysing transaction patterns and customer behaviour in real-time, banks can detect and prevent fraudulent activities. Credit scoring models are enhanced with data from various sources to make more accurate lending decisions. Big Data also supports personalised 

Educational institutions use Big Data to enhance learning experiences and improve administrative processes. Learning analytics track student performance, engagement, and behaviour to identify struggling students and personalise learning materials. Universities use data to evaluate teaching effectiveness, allocate resources efficiently, and develop data-driven strategies for student success. 

© Copyright 2025 MIVA Open University All Rights Reserved 

71 

###### Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
Zin gs : -i= om: :<br>7 | uw we!<br>M 1 ont 9 y . F.<br>|<br>“ an "5 bh (3<br>-<br>A iIE<br>\ ~ ;<br>——— oe<br><!-- End of picture text -->

###### 6. Government and Public Services 

safety.Governmentsservices,Data from improve use sensors, policy-making,Big Data tosocial enhance andmedia, ensurepublicand public surveillance systems are used in smart city projects for traffic management, crime prevention, and energy optimisation. Big Data also helps in disaster response, resouree’ allocation, and monitoring economic indicators. 

###### 7. Media and Entertainment 

Streaming platforms like Netflix and Spotify use Big Data to understand viewer preferences, recommend content, and plan new productions. Social media companies analyse user interactions to improve engagement, tailor content, and target advertising. Big Data also plays a role in sentiment analysis, content performance measurement, and audience segmentation. 



<!-- Start of picture text -->
~<br>SxSs ann. ™<br>= Seat ~A<br>- < i<br><!-- End of picture text -->

Big Data has become a powerful tool across multiple sectors, enabling smarter decisions, improved services, and greater efficiency. As technology continues to evolve, the applications of Big Data are expected to expand further, reshaping industries and everyday life. 

### 6 M I a 

###### 3.1.2 Cloud Database Systems 

Acloud database system is a database that runs on acloud computing platform rather than on local physical servers. It provides flexible, scalable, and managed database services over the internet, enabling users to access and manage data from anywhere, anytime. 

###### 3.1.2.1 Why use Cloud Databases? 



<!-- Start of picture text -->
db4 ;<br>tnceecences bo Teewee eens<br>: | — :<br>e<br>L —_<br><!-- End of picture text -->

Cloud databases are a modern approach to storing, managing, and accessing data over the internet using cloud computing platforms. Unlike traditional on-premises databases, which require physical infrastructure and manual upkeep, cloud databases. are hosted by cloud service providers and offer a range of advantages in terms of cost, scalability, maintenance, and accessibility. Organisations are increasingly turning to cloud databases to address the limitations of traditional systems. Here’s why cloud databases are becoming essential: 

Traditional on-premises databases require significant initial investment in hardware, including servers, storage systems, and networking equipment. Organisations must also invest in backup solutions, cooling systems, and secure data centres. These costs can be especially burdensome for small and medium-sized businesses. Cloud databases eliminate the need for such upfront capital expenditure. Instead, users pay ona subscription or pay-as-you-go basis, significantly reducing financial barriers. This shift from capital expenditure (CapEx) to operational expenditure (OpEx) enables more flexible budgeting and resource planning. 

© Copyright 2025 MIVA Open University AlRights Reserved 

72 

Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### 02 Limited Scalability 

One of the biggest drawbacks of traditional databases is their limited scalability. As data grows, organisations often need to purchase and configure additional hardware, which can be timeconsuming and costly. Scaling up can also lead to disruptions and downtime. Cloud databases offer on-demand scalability, allowing organisations to quickly adjust storage and computing resources as needed. Whether scaling up during peak usage or scaling down during off-peak periods, cloud databases offer the flexibility to grow with business needs without major infrastructure changes. 

###### 03 Complex Maintenance and Upgrades 

Maintaining and upgrading on-premises databases requires specialised IT staff to handle software patches, performance tuning, backup management, and system monitoring. These tasks can be complex and error-prone, leading to downtime or data loss if not handled properly. Cloud databases reduce this burden by automating most of the maintenance tasks. Cloud providers manage updates, patches, backups, and monitoring, ensuring that the system remains secure and up-todate. This allows internal IT teams to focus on more strategic tasks rather than routine maintenance. 

###### 04 Limited Accessibility and Availability 

Traditional databases are typically hosted within a company’s local network, making remote access difficult or limited. This becomes a challenge for businesses with remote teams, global operations, or the need for real-time collaboration. Cloud databases are accessible over the internet from anywhere in the world, provided there is a secure connection. This improves collaboration, supports remote work, and enables real-time data access for decision-making. Moreover, leading cloud providers offer high availability through redundant systems and data centres across regions, minimising the risk of downtime. 

Cloud databases offer a powerful alternative to traditional on-premises systems by addressing key limitations related to cost, scalability, maintenance, and accessibility. By leveraging cloud-based solutions, organisations can reduce infrastructure expenses, scale easily with demand, simplify operations, and enable better access to data. As businesses increasingly prioritise flexibility, speed, and innovation, cloud databases are playing a central role in modern data management strategies. 

###### 3.1.2.2 Key Features of Cloud Databases 

Cloud databases have become an essential part of modern IT infrastructure, offering flexibility, efficiency, and cost-effectiveness. Unlike traditional on-premises databases, cloud databases are hosted on cloud platforms and provide a wide range of features that address the growing demands of data management. Below are the key features that make cloud databases highly attractive for organisations of all sizes: 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

73 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Big Data and Cloud DatabaseSystems 

###### Scalability 

One of the most important features of cloud databases is their ability to scale seamlessly. They support both vertical scaling (increasing the resources of a single server, such as CPU, memory, or storage) and horizontal scaling (adding more servers ? (1) or nodes to handle increased load). This ensures that organisations can handle growing amounts of data and user requests without experiencing performance bottlenecks. Scalability in cloud databases is typically automatic or easily configurable, enabling businesses to adapt quickly to changing demands without downtime or manual reconfiguration. 

###### High Availability 

Cloud databases are designed for high availability, ensuring that data and applications remain accessible at all times. This is achieved through built-in redundancy and ® (2) automatic failover mechanisms across multiple data centres and geographic regions. In case of hardware failure or system outages, the database automatically switches toa backup instance without interrupting services. This minimises downtime and ensures continuous business operations, making cloud databases reliable even in critical and real-time applications. 

###### Managed Services 

One of the standout advantages of cloud databases is that they are often provided as fully managed services. This means the cloud service provider takes care of routine ° (3) administrativeperformance monitoring, tasks such and as software system optimisation. updates, security As a result,patching, internalautomated IT teamsbackups, are freed from time-consuming maintenance work and can focus on strategic projects. Managed services also reduce the risk of human error, improve security, and enhance overall system performance. 

###### Elasticity 

Cloud databases offer a high degree of elasticity, allowing organisations to dynamically allocate resources based on real-time workload demands. During peak usage periods, @ (4) additional resources can be provisioned automatically, and during off-peak times, those resources can be scaled back to save costs. This pay-as-you-go model ensures that organisations only pay for what they actually use, making cloud databases a costeffective solution, especially for businesses with fluctuating workloads. 

###### Global Access 

With cloud databases, users can access data from any location with an internet connection. This global accessibility supports remote work, global teams, mobile @ (5) applications, and real-time data sharing. It also enables collaboration across regions and time zones without the need for complex networking setups. Most cloud platforms also offer tools for secure access control, ensuring that data remains protected while being easily reachable. 

© Copyright 2025 MIVA Open University AlRights Reserved 

14 

Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
6 M I a<br><!-- End of picture text -->

+ Amazon RDS (Relational Database Service) 

Cloud databases are revolutionising the way organisations manage and utilise data by offering key features such as scalability, high availability, managed services, elasticity, and global access. These capabilities not only enhance operational efficiency but also provide the flexibility needed to thrive in today’s fast-paced digital landscape. As data continues to grow, the features of cloud databases will remain critical for modern, data-driven enterprises. 

###### 3.1.2.3 Types of Cloud Databases 

Cloud databases come in various forms to meet different data management and processing needs. The type of cloud database chosen depends on the nature of the data, the use case, and the performance requirements of the organisation. Generally, cloud databases can be categorised into relational (SQL), non-relational (NoSQL), data warehouses, and distributed databases. Each type has distinct features and is suited for specific applications. 

+ Google Cloud SQL 

These platforms support popular relational database engines like MySQL, PostgreSQL, SQL Server, and Oracle. 

###### 2. Non-relational (NoSQL) Databases 

NoSQL databases are designed to handle unstructured or semi-structured data, making them more flexible than traditional SQL databases. They do not rely ona fixed schema and can efficiently manage large volumes of diverse data types, such as documents, key-value pairs, graphs, or wide-column stores. This makes NoSQL databases ideal for modern web and mobile applications, real-time analytics, and big data workloads. 

NoSQL databases excel in horizontal scalability and are preferred in situations where data structure may evolve over time. Examples of cloudbased NoSQL databases include: 

+ MongoDB Atlas (document-based) 

###### 1. Relational (SQL) Databases 

Relational databases are the most traditional and widely used type of database. They store structured data in rows and columns using tables thatcan be'telanadito one'anotheraThese databases follow the ACID properties (Atomicity, Consistency, Isolation, Durability), ensuring strong transactional integrity and reliability. 

Cloud-based relational. databases are ideal. _ . . for applications that require consistency and structured data organisation,alae such as enterprise resource planning (ERP), customer relationship management (CRM), and financial systems. 

Relational databases use Structured Query Language (SQL) to manage and query data. Popular cloud-based examples include: © Copyright 2025 MIVA Open University AllRights Reserved 

+ Amazon DynamoDB (key-value store) 

###### 3: Data Warehouses 

Data warehouses are specialised cloud databases designed for analytics and reporting. They are optimised to perform complex queries on large datasets and are commonly used in business intelligence (Bl) systems. Unlike operational databases that handle real-time transactions, data warehouses: storeS historical dataF and support OLAP (Online Analytical Processing). 

These databases enable organisations to generate reports, dashboards, and data visualisations that help in strategic decision-making. They often integrate with various data sources and support massive parallel processing, as shown in Figure 3.1 Notable cloud-based data warehouses include: - Amazon Redshift and Snowflake. 

75 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Big Data and Cloud DatabaseSystems 



<!-- Start of picture text -->
9<br>a on Ga<br>Boia<br>fe | En a wis<br>— a, a ‘gg<br>a)i va aa388\Data Warehouse [=<br>Ee) ats<br>Lene aneeeaen Fe<br><!-- End of picture text -->

###### |<sup>|</sup> 

###### 4. Distributed Databases 

Distributed databases spread data across multiple cloud nodes or locations, providing high availability, fault tolerance, and improved performance. These databases are particularly useful for applications that need to scale globally and maintain consistent data across regions. 

T7031: Explain the advantages of using cloud databasesovertraditional on-premises systems. 

ITA3.: 

Cloud databasesITA3.: eliminatehigh upfront hardware costs, offer on-demand scalability, and reduce the complexity of maintenanceaccessibility by and enabling upgrades. globalThey access improve and support high availability with redundant systems. These databases provide flexibility, cost-efficiency, and easier resource management compared to traditional systems, making them ideal for businesses with fluctuating workloads and remote teams. 

###### 3.1.2.4 Cloud Deployment Models 

To truly understand why companies behave the way they do, we need to look beyond their internal workings. Institutional and Neo-institutional theory tells us that external forces play a huge role in shaping organisational culture. 

Distributed databases often combine the benefits of SQLand NoSQL systems and use consensus protocols to maintain data integrity across nodes. Popular cloud-based distributed databases include: Google Spanner and CockroachDB. 

Understanding the different types of cloud Cotebeses cee solution forNeIps their org dat **a** nisationsneeds. Whether chodse theit’s Dest structured data in SQL, flexible data in NoSQL, large-scale analytics in data warehouses, or global availability with distributed databases, cloud databases offer scalable and powerful solutions for the modern digital era. 

Cloud computing offers flexible, scalable, and costeffective solutions for managing IT infrastructure and data. One of the most important aspects of cloud computing is the deployment model, which determines how the cloud services are delivered, managed, and accessed. The choice of deployment model depends on an organisation's requirements for control security, cost, and performance. (he four main cloud deployment models are Public Cloud, : Private Cloud, ‘ Hybrid Cloud, : and Multi-cloud. : 

© Copyright 2025 MIVA Open University AllRights Reserved 

76 

Big Data and Cloud DatabaseSystems 

) 6 MMIVA OPEN UNIVERSITYI a 

###### 1. Public Cloud 

The public cloud is a deployment model where cloud services are offered to the general public by third-party providers over the internet. Examples of public cloud providers include Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). In this model, the infrastructure —such as servers, storage, and networking—is owned and managed by the cloud provider and is shared among multiple tenants or customers. 

Public clouds offer several advantages, including lower costs, high scalability, and ease of access. Since there is no need for organisations to invest in or manage physical infrastructure, the public cloud is especially attractive to small and medium-sized businesses. However, concerns about data security and regulatory compliance may limit its use in sensitive industries. 

###### 2. Private Cloud 

Aprivate cloud provides cloud infrastructure that is exclusively used by a single organisation. It may be hosted on the company's own premises or by a third-party service provider. Private clouds offer greater control over data, security, and compliance, making them suitable for organisations with strict regulatory or governance requirements, such as banks, government agencies, and healthcare institutions. 

While private clouds offer higher security and customisation, they typically require more investment in infrastructure and skilled personnel to manage and maintain the system. Despite the higher costs, private clouds are preferred for mission-critical applications that demand high levels of security and performance. 

###### 3. Hybrid Cloud 

The hybrid cloud is a deployment model that combines both public and private cloud environments, allowing data and applications to be shared between them. This model offers the flexibility to run sensitive or critical workloads in the private cloud while leveraging the scalability and costeffectiveness of the public cloud for less sensitive operations. 

Hybrid clouds are ideal for businesses that want to balance security with efficiency. For example, an organisation might store customer data in a private cloud for compliance reasons but use the public cloud for running analytics or handling peak demand. Effective integration and management of hybrid environments require advanced tools and strategies. 

© Copyright 2025 MIVA Open University All Rights Reserved 

77 

###### Big Data And Cloud Database Systems 

### G M I a 

###### 4. Multi-cloud 

Amulti-cloud approach involves using cloud services from multiple providers, such as AWS, Azure, and GCP either for redundancy or to avoid vendor lock-in. Organisations adopt multi-cloud strategies to take advantage of the unique features, pricing, or geographic presence of different vendors. 

Multi-cloud provides greater flexibility, risk mitigation, and improved performance, but it also adds complexity in terms of management, integration, and security. Proper planning and governance are essential for successful multi-cloud operations. 

Each cloud deployment model offers distinct advantages depending on business goals, compliance needs, and IT strategy. Understanding the differences between public, private, hybrid, and multi-cloud models helps organisations choose the best approach for scalability, cost-efficiency, and control in their cloud journey. 

###### . 1.2.5 =iCloudDatabaseiErovidersCl D. Provider: 



<!-- Start of picture text -->
GOOGLE aws<br>CLOUD PLATFORM<br>ORACLE Microsote<br>CLOUD Azure<br><!-- End of picture text -->

Cloud database providers offer a wide range of services to help organisations manage their data more efficiently in the cloud. These services support different data models, scalability options, and workloads—from transactional systems to big data analytics. Below are some of the major cloud providers and the key database services they offer: 

Amazon RDS (Relational Database Service): A fully managed service that supports several database engines like MySQL, PostgreSQL, Oracle, and SQL Server. It is ideal for traditional transactional applications. 

Amazon DynamoDB:A fast and flexible NoSQL database service that provides keyvalue and document-based storage. It is serverless, automatically scalable, and designed for low-latency access. 

Amazon Aurora: A high-performance, fully IieAe skewer database that is compatible with MySQL and PostgreSQL. Aurora offers greater speed and availability than traditional databases. 

###### 1. Amazon Web Services (AWS) 

Amazon Web Services (AWS) is one of the largest and most widely used cloud platforms in the world. It offers several robust and scalable database services tailored for various use cases. 

Amazon Redshift: A powerful cloud data warehouse designed for big data analytics and reporting. It Curses fast eSINin of Alig SEER Integrates easily with business intelligence tools. 

© Copyright 2025 MIVA Open University AllRights Reserved 

78 

###### Big Data and Cloud DatabaseSystems 

###### 2. Google Cloud Platform (GCP) 

Google Cloud Platform provides a set of innovative and efficient cloud database solutions, known for speed, scalability, and advanced analytics capabilities. 

Cloud SQL: A fully managed relational database service for MySQL, PostgreSQL, and SQL Server. It offers automatic replication, backups, and scaling. 

Cloud Firestore: ANoSQL document database that supports real-time data syncing. Itis particularly suited for mobile, web, and loT applications. 

BigQuery: A highly scalable and serverless data warehouse that enables fast SQL queries using Google's powerful processing infrastructure. It is ideal for big data analytics and machine learning integration. 

###### 3. Microsoft Azure 

Microsoft Azure offers a comprehensive portfolio of database services, especially strong in enterprise and hybrid cloud environments. 

pauls Sor ate ase: 2 ely megeded ria opel database that supports SL Server in the cloud. Itoffers high availability, scalability, and intelligent performance tuning. 

Azure Cosmos DB: A globally distributed NoSQL database designed for scalability and lowlatency access. It supports multiple data models, including document, key-value, column-family, and graph databases. 

### 6 M I a 

###### 4. Oracle Cloud 

Oracle Cloud focuses heavily on enterprisegrade database services with high automation and intelligence. 

Oracle Autonomous Database: A selfmanaging, self-patching, and self-securing database service. It offers high performance for both OLTP (Online Transaction Processing) and OLAP (Online Analytical Processing) workloads. The database automatically tunes itself for CANE [PSHM RISENY 

Each of these cloud providers—AWS, GCP Azure, and Oracle Cloud—offers a variety of database services to meet the diverse needs of modern businesses. Depending on the requirements for scalability, performance, cost, CMEC AES hspoh Ce ANSule Ie:NER ESS: the most suitable provider or even adopt<sup>a</sup> multi-cloud approach. Cloud databases continue to evolve, offering greater flexibility and functionality to support innovation in data Wee aU 

###### 3.1.2.6 Benefits of Cloud Database Systems 

Cloud database systems have become an integral part of modern data management strategies due to their flexibility, cost-efficiency, and ease of use. Unlike traditional on-premises databases, cloud databases are hosted on cloud platforms and offer a wide range of benefits for organisations of all sizes and industries. Below are some of the key advantages of using cloud database systems: 

###### 1. Reduced Cost 

z . One of the most attractive benefits of cloud databases is the significant cost savings they offer. Organisations no longer need to invest in expensive physical infrastructure, such as servers, storage devices, or networking equipment. There is also no need for large data centres or IT teams to manage hardware. Withapay-as-yourgo: 79 

© Copyright 2025 MIVA Open UniversityAll Rights Reserved 

Big Data and Cloud DatabaseSystems 

### 6 M I a 

pricing model, businesses only pay for the resources they actually use, helping them manage budgets more effectively. This makes cloud databases particularly beneficial for startups and small to medium-sized enterprises. 

###### 2. Faster Deployment 

Cloud database systems enable instant provisioning of databases. Traditional database setups often require days or weeks for hardware procurement, installation, and configuration. In contrast, cloud databases can be deployed within minutes through web interfaces or APIs. This rapid deployment accelerates development cycles, allowing teams to launch applications and services faster and respond to market demands more quickly. 

###### 3. Automatic Backups and Updates 

Cloud databases are typically provided as managed services, meaning the cloud provider takes care of routine maintenance tasks such as backups, software updates, and security patches. This reduces the burden on IT teams and minimises the risk of human error. Automated backups ensure that data is regularly saved and can be quickly restored in case of accidental loss or system failure. Automatic updates also ensure that databases always run the latest features and security ennancements. 

###### 4. Security and Compliance 

Security is a top priority for cloud database providers. These platforms offer built-in security features such as data encryption at rest and in transit, role-based access control, firewalls, and identity management. Additionally, many cloud providers are certified to meet international compliance standards like GDPR, HIPAA, and ISO, which is especially important for organisations in regulated industries such as healthcare, finance, and government. Centralised monitoring and auditing tools also enhance visibility into database activity and help maintain data integrity. 

###### 5. Integration with Advanced Services 

Cloud database systems are designed to seamlessly integrate with a wide range of other cloud services, including data analytics, artificial intelligence (Al), and machine learning (ML) platforms. This enables organisations to perform powerful analyses, develop predictive models, and make data-driven decisions without needing to move data across different environments. These integrations streamline workflows and support innovation by making advanced technologies more accessible. 

Cloud database systems offer a host of benefits, from reduced costs and faster deployment to enhanced security and seamless integration with advanced services. By adopting cloud-based databases, organisations can improve operational efficiency, reduce manual workload, and gain the agility needed to succeed in today's fast-paced digital landscape. As technology continues to evolve, cloud databases will remain a cornerstone of scalable and intelligent data management. 

###### 3.1.3 Use Cases of Cloud Database Systems 

Cloud databases have become essential in powering modern digital applications and services due to their flexibility, scalability, and ease of use. They support a wide range of use cases across industries and technological environments. From real-time analytics to managing data from Internet of Things (loT) devices, cloud databases provide the infrastructure and tools needed to manage large and dynamic datasets efficiently. Below are some of the most common and impactful use cases of cloud databases: 

© Copyright 2025 MIVA Open University AllRights Reserved 

80 

Big Data and Cloud DatabaseSystems 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### 1. Web and Mobile Application Backends 

Cloud databases are widely used as the backend storage systems for web and mobile applications. They provide developers with managed and scalable infrastructure to store user data, content, preferences, and application settings. Whether it’s user authentication, real-time messaging, or storing multimedia content, cloud databases like Firebase (for mobile apps), Amazon DynamoDB, and MongoDB Atlas support fast development and global access. Features like real-time syncing, auto-scaling, and serverless computing make them ideal for dynamic and high-traffic applications. 

###### 2. E-commerce Platforms 

E-commerce businesses rely heavily on cloud databases to manage product inventories, customer information, transactions, and recommendation engines. With high traffic fluctuations during sales or peak seasons, cloud databases provide the scalability and availability needed to ensure smooth operation. Services like Amazon Aurora and Azure SQL Database support secure transactions and integrate easily with payment systems and logistics platforms. Additionally, NOSQL databases help manage unstructured data such as customer reviews and browsing history. 

###### 3. Real-Time Analytics and Dashboards 

Organisations use cloud databases to power real-time analytics and dashboards that provide instant insights into customer behaviour, system performance, and sales trends. Tools like Amazon Redshift, Google BigQuery, and Azure Synapse Analytics allow businesses to process and visualise data from multiple sources within seconds. These use cases are common in digital marketing, finance, and operations, where decisions need to be made based on current data. Real-time processing helps in detecting anomalies, personalising user experiences, and monitoring KPIs. 

###### 4, Data Warehousing and Business Intelligence 

Cloud-based data warehouses serve as centralised repositories for structured and semi-structured data used in business intelligence (BI). Enterprises use them to consolidate information from various sources— like CRM, ERP, and third-party platforms—to run complex queries and generate reports. Services like Snowflake, Amazon Redshift, and Google BigQuery are designed to handle large-scale analytical workloads efficiently. They enable organisations to make informed strategic decisions, forecast trends, and evaluate performance. 

###### 5. loT Data Management 

The rise of the Internet of Things (loT) has generated massive volumes of data from devices like sensors, wearables, and smart appliances. Cloud databases are ideal for managing this data, which is often timeseries in nature and needs to be processed in real-time. Solutions like AWS loT Core, Azure Cosmos DB, and Google Cloud IoT provide the infrastructure to ingest, process, and store loT data. These systems support real-time monitoring, predictive maintenance, and automated responses in industrial, healthcare, and smart city applications. 

Cloud databases are versatile and powerful tools that support a wide array of modern use cases. From supporting mobile apps and e-commerce platforms to enabling data-driven decision-making and loT innovations, cloud databases are critical for organisations aiming to scale quickly, remain agile, and drive digital transformation. 

© Copyright 2025 MIVA Open University AllRights Reserved 

81 

###### Big Data and Cloud Database Systems 

## Ss) M | T 

PartB Another key characteristic of a data warehouse is its subject-orientation. Unlike transactional DATA iN K ES databases that store data for day-to-day WA R E H O U S ESont 8 ’ A N 1D) operationsinventory), (likea data processing warehouse orders organises data or updating DATA BA S E around key business subjects such as customers, S E C URI TY sales,and decisior pr **o** n-makersducts. This to makes query dat it e **a** sierbased for on analysts PRACTICES business needs. 

###### 3.2.1 Introduction to Data Warehouse 

AData Warehouse is a centralised repository that stores integrated data from multiple, often heterogeneous sources, specifically structured for querying, reporting, and data analysis. Unlike operational databases that are optimised for transactional processing, data warehouses are designed for analytical processing (OLAP), enabling organisations to derive insights and support decision-making processes. 

The concept of data warehousing emerged as businesses recognised the need to analyse historical data accumulated over time, rather than just processing day-to-day transactions. As data volumes grew and sources became more varied— ranging from customer relationship systems to necessary to consolidate this information ina financial. and supply chain databases—it became unified,<sup>consistentformat.</sup> 

Data warehouses are also time-variant. They store historical data over long periods, allowing organisations to perform trend analysis, forecasting, and performance tracking. Each record typically includes a timestamp or time-related dimension, enabling users to track changes and developments over time. 

Additionally, data warehouses are non-volatile, meaning once data is loaded into the warehouse, it is rarely changed or deleted. This provides a stable and consistent environment for users to perform repeatable analyses and compare results over time. 

There are several common architectures for implementing a data warehouse: 

Bacioarchitecturetinvolvcsa centre steal - | data warehouse fed by multiple & | source systems via ETL tools. 

One of the core principles of a data warehouse is datasystemsand transformedintegration. (ETL: Extract,Datainto Transform,ais common extractedformat, Load), from sourceand cleanedloaded into the warehouse. This process ensures that data is consistent, reliable, and ready for analysis, regardless of its original source The ETLProcess 



<!-- Start of picture text -->
= FO}<br>= > > =<br>Extract Transform Load<br><!-- End of picture text -->

Data Mart Architecture: A data mart isasmaller, focused version of a data ial< e warehouse,specific department typically created(e.g., marketing fora or finance). It can be independent or GLIRTSER CTENSSEI NEICMENES 

**—** — || AthatEnterprise large-scale, serves the Data integrated entire Warehouse organisation warehouse(EDW): Cloud Data Warehousing: Modern solutions such as Snowflake, Google fi BigQuery, and Amazon Redshift offer scalable, cloud-based data warehousing with lower infrastructure costs and easier maintenance. 



<!-- Start of picture text -->
82<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University All Rights Reserved 

Big Data and Cloud DatabaseSystems 

UL 6 **M** IVA OPEN UNIVERSITYI a 

Some key benefits of data warehousing include: 

Improved decision-making Historical analysis for forecasting through timely and and long-term planning. accurate data. Faster query performance compared Consolidated data from multiple to operational databases. sources in one place. 

In conclusion, a data warehouse serves as a powerful foundation for business intelligence (BI) and data analytics. It enables organisations to transform raw data into actionable insights, improve strategic planning, and gain a competitive edge in an increasingly data-driven world. 

3.2.1.1 Comparing Data Warehouse and Federated Database 

Data Warehouse vs. Federated Database System 

|Feature /Aspect|DataWarehouse|Federated DatabaseSystem|
|---|---|---|
|Definition|Acentralised repositoryfor<br>integrated, historical dataused for<br>analysis and reporting.|Asystemthatallowsmultiple<br>autonomousandheterogeneous<br>databasestoworktogetheras<br>one.|
|DataStorage|Storesdata physically ina central<br>location.|Dataremainsstored atthe<br>original, independentdatabases.|
|DataIntegration|UsesETL (Extract,Transform, Load)<br>processesto integrateand<br>standardisedata.|Providesvirtual integration; data<br>isaccessed in realtimewithout<br>physical consolidation.|
|Autonomyof<br>Sources|Sourcesystemsareseparatebut<br>losecontroloverdataonce it’s<br>loaded intothewarehouse.|Eachsourcedatabasemaintains<br>full controlandautonomy.|
|DataLatency|Data isnot real-time; it's refreshed<br>at intervals (batchupdates).|Provides real-timeaccessto live<br>data fromthesourcesystems.|
|Performance|Optimisedforfastquery<br>performanceandanalytical<br>processing.|Mayfaceperformanceissuesdue<br>to livequerying of distributed<br>sources.|
|Data Consistency|Highconsistency, asdata iscleaned<br>andstandardisedduringETL.|Mayvary; relieson localdatabase<br>schemasandformats.|



© Copyright 2025 MIVA Open University AllRights Reserved 

83 

Big Data and Cloud DatabaseSystems 

avs 6 Moven univensiryI a 

|UseCase|Best forhistorical data analysis,<br>trend forecasting, and Bl reporting.|Usefulwhen integratingdata from<br>diverse systemswithout<br>centralising it.|
|---|---|---|
|SystemComplexity|High initial setupforETL and storage<br>but simpler long-term analysis.|Complex duetoheterogeneous<br>DBMSs, schemas, and real-time<br>querying.|
|Examples|AmazonRedshift,Snowflake,Google<br>BigQuery,OracleDataWarehouse.|IBMInfoSphereFederationServer,<br>ApacheDrill.|



###### Summary 

- + AData Warehouse is ideal for consolidated, historical data analysis where performance and consistency are priorities. It’s widely used in business intelligence and strategic decision-making. 

- + AFederated Database System is suitable when you need real-time access to diverse, independent databases without copying or centralising the data. It works well in collaborative environments where data ownership and autonomy are important. 

###### 3.2.2 Introduction to Database Security 

In today's data-driven world, databases serve as the core storage systems for vast amounts of critical and sensitive information, including financial records, personal details, corporate secrets, and healthcare data. As the reliance on databases increase, ensuring their security has become a fundamental aspect of any information system. Database security refers to the range of processes, controls, tools, and technologies that are put in place to protect databases from threats such as unauthorised access, data breaches, misuse, and corruption. 

This section introduces the concept of database security and discusses its objectives, key components, common threats, and best practices for protecting databases in modern computing environments. 

Database security is the set of mechanisms that protect the database from unintended activities that could compromise the confidentiality, integrity, or availability of data. These mechanisms are implemented at different levels of the system, including the database management system (DBMS), operating system, and network infrastructure. 

###### 3.2.2.1 Objectives of Database Security 

Database security is a critical aspect of modern information systems, ensuring that organisational data remains protected against a wide range of threats. The three main objectives of database security align closely with the well-established CIA triad: Confidentiality, Integrity, and Availability. Together, these principles form the foundation for designing and maintaining secure database systems. 

Confidentiality is the first and perhaps the most emphasised objective of database security. It refers to the protection of sensitive information from unauthorised access or disclosure. Only authorised users or systems should have the ability to access or manipulate data based on their assigned roles and permissions. 

© Copyright 2025 MIVA Open University AllRights Reserved 

84 

Big Data and Cloud DatabaseSystems 

UL 6 **M** IVA OPEN UNIVERSITYI a 

Techniques such as access control mechanisms, authentication protocols, encryption, and role-based access management are commonly used to maintain confidentiality. For example, in a hospital database, only doctors and authorised staff should have access to patients’ medical records, while unauthorised individuals must be completely restricted. Breaches in confidentiality can lead to serious consequences, including identity theft, financial loss, or legal penalties. 

Integrity is the second key objective, focusing on maintaining the accuracy, consistency, and reliability of data throughout its lifecycle. Data must remain correct and unaltered, except through authorised transactions. Unauthorised modifications—whether accidental or malicious—must be detected and prevented. Integrity is preserved through techniques such as input validation, database constraints, transaction management, checksums, and audit trails. For instance, in a banking system, the balance ina customer's account must accurately reflect all deposits and withdrawals. If data integrity is compromised, it can lead to misinformation, flawed decision-making, and loss of trust in the system. 

Availability completes the triad, emphasising that data must be readily accessible to authorised users whenever needed. Ensuring high availability means protecting the database from threats like hardware failures, cyber-attacks (e.g., denial-of-service attacks), or natural disasters that could disrupt access. Techniques to support availability include database replication, backup and recovery solutions, faulttolerant architectures, and disaster recovery plans. For example, in e-commerce platforms, downtime of the database could mean significant financial losses and damage to customer trust. Therefore, maintaining continuous database service is crucial. 

In summary, confidentiality, integrity, and availability work together to create a secure database environment. Confidentiality ensures that sensitive data remains private, integrity ensures that data remains trustworthy, and availability ensures that users can rely on access when they need it. A weakness in any one of these areas can compromise the security of the entire system. Therefore, organisations must implement comprehensive security strategies that address all three objectives to protect their data assets effectively in today’s increasingly complex digital landscape. 

###### 3.2.2.2 Common Threat to Database Security 

Databases serve as the backbone of modern organisations, storing critical information such as financial records, personal data, and proprietary business information. Because of their immense value, databases are attractive targets for both internal and external threats. Protecting these vital assets requires an understanding of the many types of risks they face. Some of the most common threats to database security include unauthorised access, SQL injection attacks, malware and viruses, privilege abuse, backup data theft, and denial-of-service (DoS) attacks. 

###### Unauthorised Access 

Unauthorised access remains one of the most widespread and dangerous threats to database systems. Attackers often exploit weak authentication methods, poor password management, or misconfigured security settings to gain entry into a database. Once inside, they may steal, alter, or destroy sensitive information. In many cases, the initial breach occurs because of simple errors such as using default passwords or failing to enforce strong authentication protocols like multi-factor authentication (MFA). Unauthorised access can lead to severe consequences, including data breaches, regulatory penalties, financial losses, and damage to an organisation's reputation. Preventing such attacks requires stringent access controls, regular security audits, and continuous monitoring of database activities. 

‘© Copyright 2025 MIVA Open UniversityAll Rights Reserved 

85 

Big Data and Cloud DatabaseSystems 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### SQL<sup>InjectionAttacks</sup> 

SQL<sup>injectionisa well-knowntechnique whereattackersinsert maliciousSQL statementsinto a database</sup> query via input fields, such as login forms or search boxes. If the application interacting with the database fails to properly validate user input, an attacker can manipulate the database, retrieve unauthorised information, modify data, or even delete entire tables. SQL injection attacks are particularly dangerous because they can be executed remotely and often require minimal technical expertise. To mitigate this threat, developers must use parameterised queries, input validation, and web application firewalls that specifically detect and block SQL injection attempts. 

###### Malware and Viruses 

Malicious software poses another serious threat to database servers. Malware, viruses, ransomware, and spyware can infect database systems through insecure networks, phishing attacks, compromised software updates, or malicious insiders. Once a database server is infected, attackers can exfiltrate sensitive data, encrypt databases for ransom, or use the compromised system to launch further attacks within the network. Some malware is designed specifically to target databases, making traditional antivirus solutions insufficient on their own. Comprehensive cybersecurity strategies—including network segmentation, endpoint protection, regular patching, and user awareness training—are essential to defending databases against malware threats. 

###### Privilege Abuse 

Not all threats come from outsiders; internal actors, such as employees, contractors, or partners, can also pose significant risks. Privilege abuse occurs when authorised users misuse their access rights to perform unauthorised activities, such as stealing confidential information, altering data for personal gain, or sabotaging systems. Sometimes, users are given excessive privileges beyond what is necessary for their job functions, creating additional vulnerabilities. Managing this threat requires a principle known as “least privilege’, where users are granted only the access needed to perform their roles. Regular review of user permissions, activity monitoring, and behavioural analytics can help detect and prevent privilege abuse. 

###### Backup Data Theft 

While primary databases are often well-protected, backup copies may not receive the same level of security attention. Attackers who cannot breach the main database might target backups, which can be stored offsite, in the cloud, or on external drives. If these backups are unencrypted, improperly secured, or accessible without strong authentication, they become an easy target. Backup data theft can result in the same level of harm as a direct database breach. To defend against this threat, organisations must encrypt backup files, enforce strict access controls, and ensure that backup storage systems are subject to the same (or even stricter) security measures as production systems. 

###### Denial-of-Service (DoS) Attacks 

Denial-of-service attacks aim to make a database or application unavailable to legitimate users by overwhelming it with excessive requests, exploiting software vulnerabilities, or crashing the underlying infrastructure. In the case of databases, DoS attacks can cause serious disruptions to business operations, leading to lost revenue, customer dissatisfaction, and potential reputational damage. Databases that are part of critical services, such as banking or healthcare, are especially vulnerable. Protection against DoS attacks involves implementing robust network defences, such as firewalls and intrusion prevention systems; scaling resources to absorb traffic spikes; and using specialised anti-DoS technologies to detect and mitigate attacks early. 

‘© Copyright 2025 MIVA Open UniversityAll Rights Reserved 

86 

###### Big Data and Cloud DatabaseSystems 

### 6 M I a 

In today's digital environment, databases face a wide array of security threats that can arise from both external attackers and internal users. Unauthorised access, SQL injection, malware, privilege abuse, backup data theft, and DoS attacks represent some of the most common and dangerous challenges. To ensure the protection of critical data assets, organisations must adopt a comprehensive security strategy that includes technical defences, access controls, regular monitoring, employee training, and incident response planning. Only by recognising and proactively addressing these threats can organisations maintain the confidentiality, integrity, and availability of their valuable database systems. 

###### 3.2.2.3 Security Mechanisms for Effective Database Protection 

Databases store valuable and sensitive information, making them prime targets for attackers. Protecting databases requires a combination of security mechanisms that work together to defend against a wide range of threats. A robust database security strategy integrates authentication, authorisation, access control, encryption, auditing and monitoring, and backup and recovery processes, as well as specialised tools like database firewalls and intrusion detection systems (IDS). Each of these mechanisms plays a vital role in maintaining the confidentiality, integrity, and availability of data. 

###### Authentication and Authorisation 

Authentication and authorisation form the first layer of defence in securing a database. 

Authentication is the process of verifying the identity of users attempting to access the system. It ensures that only legitimate users are granted access. Authentication methods include passwords, smart cards, biometric verification a (such as fingerprint or facial recognition), and multi-factor authentication (MFA), (=) which combines two or more verification methods. Strong authentication reduces the risk of unauthorised access significantly. user is allowed to perform. Users are given specific roles and permissions that CS) Authorisation takes place after authentication and determines what actions a define whether they can view, edit, delete, or administer database contents. By implementing strict authorisation policies, organisations can limit the potential damage even if an account is compromised. 

###### Access Control 

Access control mechanisms enforce rules about who can access what information and under what circumstances. A widely adopted model is Role-Based Access Control (RBAC), where permissions are not assigned to individuals directly but to roles, and users are assigned to those roles. For instance, a “customer support" role may have permission to view customer records but not to delete them. RBAC simplifies management and minimises human errors. Effective access control ensures that users interact only with the data necessary for their duties, adhering to the principle of least privilege. 

###### Encryption 

Encryption is a critical technology for protecting database contents both at rest and in transit. 

© Copyright 2025 MIVA Open University AlRights Reserved 

87 

LU 6 MMIVA OPEN UNIVERSITYI a 

###### Big Data and Cloud Database Systems 

Data-at-rest encryption safeguards stored data, ensuring that even if the storage media is stolen, the data remains unreadable without the decryption key. 

Data-in-transit encryption protects data as it travels across networks, preventing interception by attackers using techniques such as man-inthe-middle attacks. 

Using strong encryption standards (like AES-256 for storage and TLS for communication) ensures that sensitive data remains confidential even if a security breach occurs. 

###### Auditing and Monitoring 

Regular auditing and monitoring activities are essential for detecting and responding to suspicious behaviour. 

Audit logs record detailed information about who accessed the database, what actions were performed, and when these actions occurred. These logs are invaluable for forensic investigations after a security incident and are often required for regulatory compliance. 

€ Monitoring tools continuously observe database activities and can trigger alerts * when unusual or unauthorised activities are detected. Proactive monitoring allows organisations to respond swiftly to potential threats before they escalate into serious breaches. 

###### Backup and Recovery 

Despite strong preventative measures, incidents such as ransomware attacks, hardware failures, or accidental data deletions can still occur. Therefore, a solid backup and recovery plan is vital. 

Regular backups ensure that an up-to-date copy of the database is available and can be restored in case of a disaster. 

- Backups must be stored securely, using the same encryption and access controls as the primary database, to prevent attackers from stealing or tampering with backup data. 

Recovery plans should be regularly tested to ensure that databases can be restored quickly “——e and accurately, minimising downtime and data loss. 

© Copyright 2025 MIVA Open University AllRights Reserved 

88 

Big Data and Cloud DatabaseSystems 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Database Firewalls and Intrusion Detection Systems (IDS) 

Specialised tools like database firewalls and IDS provide additional layers of protection. 

Database firewalls= act as gatekeepers, Z ee A E inspecting incoming SQL traffic for he : malicious patterns or unauthorised < pee queries. They can block SQLinjection attacks and other types of unauthorised database access attempts. 

- Intrusion Detection Systems (IDS) monitor network. traffic and database_ activities; for signs of abnormal or suspicious behaviour. ¢ 

- An IDS can detect brute force login 7 . 

- attempts, privilege escalation attacks, or Foes Rey 

- - data exfiltrationci activities. Wnen an intrusion is detected,i the system can generate alerts or trigger automated responses to contain the threat. 

Effective database security is not achieved through a single solution but through a layered approach that integrates multiple protective measures. Authentication and authorisation ensure that only the right users have access; access control limits what each user can do; encryption protects the data itself; auditing and monitoring help detect suspicious activities; backup and recovery ensure resilience in the face of failures or attacks; and firewalls and IDS add an extra line of defence against sophisticated threats. By implementing these security mechanisms cohesively, organisations can significantly ennance the security posture of their databases and safeguard their most critical digital assets. 

###### 3.2.2.4 Challenges in Database Security 

While a wide range of advanced tools and techniques are available to secure databases, protecting them effectively remains a complex and ongoing challenge. Various factors contribute to the difficulty, including the increasing complexity of IT environments, the need to balance performance with protection, the risk of insider threats, and the pressures of regulatory compliance. 

###### Managing Security Across Heterogeneous Environments 

One of the major challenges is managing security across diverse and heterogeneous environments. Organisations today often operate a mix of on-premises databases, cloud-based systems, and hybrid architectures. Each environment has different security models, risks, and management requirements. For example, a database stored in a public cloud must be secured differently than one hosted ona private server. Managing access controls, encryption, monitoring, and backup policies consistently across these varied platforms can be extremely difficult. It requires specialised skills, careful planning, and often complex integration of multiple security tools. 

###### Balancing Security and Performance 

Another significant challenge is finding the right balance between strong security measures and maintaining acceptable system performance. Many security practices—such as encryption, multi-factor authentication, detailed auditing, and traffic inspection—introduce additional computational overhead or latency. For high-transaction databases, especially those supporting real-time applications, even minor delays can impact user experience and business operations. Therefore, database administrators must carefully design security solutions that protect data without severely affecting the performance or responsiveness of the system. 

© Copyright 2025 MIVA Open University AlRights Reserved 

89 

Big Data and Cloud DatabaseSystems 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### Dealing with Insider Threats 

Insider threats are particularly difficult to detect and manage. Unlike external attackers, insiders often already have authorised access to the database. They might misuse their privileges for personal gain to sabotage the organisation, or accidentally expose sensitive information through careless behaviour. Traditional security defences like firewalls and antivirus software are often ineffective against insider threats. Detecting insider misuse requires advanced monitoring techniques, user behaviour analytics, strict access controls, and continuous auditing. Building a culture of security awareness among employees also plays a critical role in mitigating this risk. 

###### Ensuring Compliance with Multiple Overlapping Regulations: 

Organisations that store and process data must comply with a variety of data protection laws and regulations, often with overlapping or conflicting requirements. Examples include the General Data Protection Regulation (GDPR) in Europe, the Health Insurance Portability and Accountability Act (HIPAA) in the United States, and various industry-specific standards like PCI-DSS for payment data. Maintaining compliance across all applicable regulations can be daunting. It requires not only implementing the correct technical controls but also maintaining extensive documentation, conducting regular audits, and keeping up with changing legal requirements. Non-compliance can lead to significant financial penalties, legal consequences, and reputational damage. 

Despite the availability of sophisticated security tools, real-world database protection faces several complex challenges. Managing security across diverse platforms, balancing protection and performance, addressing insider threats, and ensuring regulatory compliance all demand careful strategy, ongoing vigilance, and significant resources. Organisations must recognise these challenges and adopt a proactive, layered approach to database security to safeguard their critical data assets effectively. 

© Copyright 2025 MIVA Open University AllRights Reserved 

90 

Big Data and Cloud Database Systems 

Ss) MIVAMOPEN IUNIVERSITY T 

1) 

##### SUMMARY 

In today's digital world, vast amounts of data are generated daily from a wide array of sources such as social media, loT devices, enterprise applications, and mobile platforms. This phenomenon has led to the emergence of Big Data, which refers to datasets that are too large or complex to be handled by traditional data processing systems. Big Data is defined by the 5 V's—Volume (large amounts of data), Velocity (rapid data generation and processing), Variety (different formats and sources), Veracity (data accuracy and reliability), and Value (usefulness of data for insights and decision-making). 

To manage and analyse Big Data effectively, organisations are increasingly adopting cloud computing. Cloud database systems offer scalable, flexible, and cost-efficient data management by running databases on cloud infrastructure. Unlike on-premises solutions, cloud databases allow users to scale resources as needed, making them suitable for handling dynamic and large-scale data environments. 

Big Data technologies such as Hadoop, Spark, and NoSQL databases (e.g., MongoDB, Cassandra) are essential for storing and processing unstructured and semi-structured data. These tools support distributed computing and parallel processing, enabling organisations to handle large datasets efficiently. Cloud service providers like Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP) offer integrated Big Data services that include storage, processing, analytics, and machine learning capabilities. 

Cloud databases are broadly categorised into relational (SQL) and non-relational (NoSQL) types. Relational cloud databases such as Amazon RDS and Google Cloud SQL use structured data and support SQL-based queries, while NoSQL databases like DynamoDB and Cosmos DB offer more flexibility and scalability for handling various data formats such as JSON and XML. 

The benefits of using cloud databases in Big Data contexts include high availability, disaster recovery, and cost efficiency. Cloud platforms replicate data across multiple regions to ensure continuity, and their payas-you-go models help organisations control IT spending effectively. 

Big Data has a wide range of applications, including healthcare (e.g., predictive analytics), finance (e.g... fraud detection), retail (e.g., personalised recommendations), smart cities (e.g., traffic optimisation), and marketing (e.g., sentiment analysis). It supports data-driven decision-making, operational efficiency, and innovation. 

However, several challenges come with Big Data, such as storing massive datasets, ensuring data quality, maintaining privacy and security, managing real-time analytics, and optimising resource use. A typical Big Data architecture includes data sources, ingestion tools (e.g., Kafka), distributed storage (e.g., HDFS), processing engines (e.g., Spark), and analytics tools (e.g., Power Bl). 

In conclusion, Big Data and cloud database systems together represent a transformative approach to managing and extracting value from data. The integration of distributed processing technologies with scalable cloud infrastructure empowers businesses to gain actionable insights, drive innovation, and remain competitive in a data-driven economy. Understanding these systems is essential for navigating the complexities of the modern data landscape. 

© Copyright 2025 MIVA Open UniversityAllRights Reserved 

91 

Big Data and Cloud Database Systems 

e Ss) MIVAMOPEN IUNIVERSITY T 

J) 

#### CONCLUSION 

In conclusion, Big Data and cloud database systems have become fundamental pillars in today's datadriven world. As organisations grapple with the increasing volume, velocity, and variety of data, cloudbased solutions provide the necessary scalability, flexibility, and cost-effectiveness to store, manage, and analyse information efficiently. Technologies such as Hadoop, Spark, and NoSQL databases enable realtime and distributed processing, while cloud platforms like AWS, Azure, and GCP offer integrated services that eliminate infrastructure complexities. By combining the strengths of Big Data and cloud computing, businesses can unlock valuable insights, drive innovation, and gain a competitive edge in an increasingly digital landscape. 

© Copyright 2025 MIVA Open University AllRights Reserved 

92 


STUDY SESSION FOUR Query Optimisation in Database 

###### Query Optimisation in Database 



<!-- Start of picture text -->
><br>Ss) M I T<br><!-- End of picture text -->

###### INTRODUCTION 

In modern database systems, the efficiency and On the other hand, hand, file organisation refers to how performance of data retrieval and manipulation are records are stored stored on disk. The physical layout of crucial. Two fundamental concepts that significantly | datahas a datahas a a direct impact on query impact on query on query query performance, as impact these aspects are query optimisation and file it determines determines how quickly data can be accessed accessed organisation. Both play an essential role in ensuring File organisation schemes can be broadly that databases operate effectively, especially when categorised into heap (unordered), sequential dealing with large volumes of data and complex (ordered), and hashed file structures queries. 

On the other hand, hand, file organisation refers to how records are stored stored on disk. The physical layout of | datahas a datahas a a direct impact on query impact on query on query query performance, as it determines determines how quickly data can be accessed accessed File organisation schemes can be broadly categorised into heap (unordered), sequential (ordered), and hashed file structures 

In aheap file organisation, records are placed wherever there is space, without any particular order. This method is simple and efficient for insertheavy workloads but can lead to poor performance in search and update operations. Sequential file organisation arranges records based on a particular attribute's order, facilitating faster range queries and ordered scans but making inserts and deletes more complex. Hashed file organisation uses a hash function to determine the location of a record, offering fast access for equality searches but being inefficient for range queries. 



<!-- Start of picture text -->
Database<br><!-- End of picture text -->

Query optimisation refers to the process of selecting the most efficient means of executing a database query. When a user submits a query to the database, there may be multiple ways to retrieve the requested HEE NSA SIN UNE EWN sequences of operations such as joins, selections and projections. The query optimiser, a component of the database management system (DBMS), evaluates these possible query execution plans and chooses the one that minimises the cost, which Bde Ne eles TMCS AONE gh tel. Ste) SiG NEMO SOnSUITIDEO!) The optimisation process can be divided into two LEURule-basedeH SSee Seto hens Geksi AeESe aledlanEsaisedn heuristics tooptimisation applies determine the execution predefinedstrategy, while cost-based optimisation uses statistical information about the data, such as table size, index availability, and data distribution, to estimate the cost of each possible plan. The optimiser selects the plan with the lowest estimated cost. Techniques such as query rewriting, predicate pushdown, join order optimisation, and index selection are commonly used to enhance performance. 

To complement file organisation, databases often use indexing techniques that allow quick access to rows ina table without scanning the entire file. Indexes can be built on one or more columns and are essential for efficient query execution, particularly when dealing with large datasets. Together, query optimisation and file organisation fomnithe backacne orericlentverabase performance. While query optimisation ensures that queries are executed using the best possible strategies, file organisation determines the physical structure that supports those strategies. A well-designed database system leverages both elements to provide fast, reliable, and scalable data management. —_j. gata volumes continue to grow and applications become more complex, the importance of advanced query optimisation and intelligent file organisation strategies becomes increasingly critical in database system design and implementation. 

© Copyright 2025 MIVA Open University AllRights Reserved 

94 

###### Query Optimisation in Database 

Example: SELECT name 

FROM Employees WHERE department = 'Sales'; This query retrieves the names of employees who work in the ‘Sales’ department. Conditions in the WHERE clause can use Son pecan operators (=, <>, <>, <=, >=), Kets) Geeuel (AND, OR, Nor). and PECAN REE, I, SERIES ue ie CaOURI By iend belek eves ihe GROUP. By GEES is eo wun performing aggregation in a query. It groups lows ee Wet dselmevallceilneeceiles Soluluinss nie Sel,ne commen ee gPERES Tunctions Used With) GROUP) BY ENCE CEM) EEO); ENTEO}o EEETOn ENEILEEKO), 

Eone SELECT department, COUNT(*) AS AECL STONER CES LEDS eee A Onepis utyee cod(Ossiee Hambeyasich ol enpcyee= 2 each department. 

The HAVING Clause is used to filter groups after the GROUP BY operation. It works like the WAN SiS HEWES IEE Se {ICBM Cees EISHTUS: 

Pane SELECT department, COUNT(*) AS pene oy eee BEL!GROUETCoeOe EENBETSUS quetyPx(E2UAC9) retires onlydepartment those GepatunedcsNoe CHES MATOS ASESS 

5. ORDER BY Clause 

IWEGSGER EMIEEMSI SSIS WENcE MUSSL EE en.o0e or Heine@olthuTaiss S\iSestclhe 7 sortsin ascending order (asc), but descending order (DESC) canalso be Speaintesh 

### 6 M I a 

###### Example: 

SELECT name, salary FROM Employees ORDER BY salary DESC; This query retrieves employee names and salaries and sorts the list from highest to lowest salary. 

Internal Representation of Queries Although SQL syntax is designed to be humanreadable and easy to write, database systems do not execute SQL directly. Internally, a SQL query is translated into a different form called a query representation or query tree that can be efficiently executed by the database engine. 

This representation captures the logical steps required to process the query. It forms the basis for query optimisation, where the system rearranges or transforms the query plan to reduce computation time and improve performance. ForSELECT example,es a SQL emquery: FROM Employees WHERE department = 'Sales'; may be internally represented as: + Step 1: Scan Employees table * Step 2: Apply selection predicate department 

- = ‘Sales’ 

+ Step 3: Project the name attribute 

By separating the logical query components from the physical execution, the DBMS can choose the most efficient way to execute the query, such as using indexes, join algorithms, or parallel processing. 

Atypical SQL query is built from components that specify what data is needed, from where it is drawn, under what conditions, and how it should be grouped WHERE,or sorted. GROUP These BY, components HAVING, and include ORDER SELECT, BY clauses FROM, Understanding how each part functions allows users to write more precise and efficient queries. 

transformedFurthermore, int kn **o** wingoptimised that queri repr **es** entations are internally by the DBMS helps in appreciating how databases manage performance and scalability. As data continues to grow in volume and complexity, mastery of query 

© Copyright 2025 MIVA Open University All Rights Reserved 

96 

###### Query Optimisation in Database 

components and their role in the query lifecycle remains essential in data-driven environments. 

###### 4.1.1.2 Forms of Query Representation 

To optimise query execution, the DBMS converts high-level queries into internal representations that are more suitable for analysis and execution planning. 

There are several forms of query representation used in database systems, including: 

1. Relational Algebra 

2. Relational Calculus 3.4. QueryQuery Trees Graphs 

###### 1, Relational Algebra 

Relational algebra is a procedural query language that uses a set of operations to manipulate relations (tables). It provides a foundation for expressing queries in a formal and mathematical manner. Operations in relational algebra include: 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### 2. Relational Calculus 

Relational calculus is a non-procedural query language, which means it focuses on what to retrieve rather than how to retrieve it. 

It is based on predicate logic and exists in two forms: 

- + Tuple Relational Calculus (TRC): Uses tuple variables to specify the desired result. 

- + Domain Relational Calculus (DRC): Uses domain variables that range over individual CIE EEE: 

> E{tnamemiesle tetiTapleayEmployeesRelations‘elational A t.departmentCalculus:Calculus? =- 'Sales'} 

This means: Retrieve the ‘name’ of all tuples 't’ from the Employees relation where the department is ‘Sales’. 

Relational calculus is primarily of theoretical interest and is used to express queries declaratively in formal database theory. 

Operations in relational algebra include: 

- Selection (0): Filters rows based ona condition. 

- Projection (1): Selects specific columns froma table. 

- « Union (U): Combines tuples from two relations. 

- Set Difference (-): Returns tuples present in one relation but not the other. 

- Cartesian Product (x): Combines each row of one relation with every row of another. 

- + Join (xj): Combines related tuples from two relations based on a common attribute. 

Example: The relational algebra equivalent of the earlier SQL query would be: 

T1_name (o_department='Sales’ 

(Employees)) 

This expression first selects all tuples where the department is ‘Sales’, and then projects only the ‘name’ attribute from the result. 



<!-- Start of picture text -->
5 ee<br>Le ve<br>, ~ A<br>fF. = |<br>Xo aa P<br>ays 4 2 =<br>a ee NX = a<br>~~. a — é<br>- ae | v ee<br>oo. a } —_ a3<br>a —— F ><br>a ~ ak i F * 2<br>we e *<br>“= a, lan, :<br>= —_<br>=<br>TT, —_—<br><!-- End of picture text -->

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

97 

Query Optimisation in Database 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### 3. Query Trees 

A query tree is a tree-structured representation ofa query. It is a graphical depiction of relationalalgebra expressions that illustrates the sequence of operations to be performed. Each node in the tree represents an operation such as selection, Projection, or join, and the leaves represent base tables. 

###### Example Query Tree: 



<!-- Start of picture text -->
Tp<br>|<br>C<) R.P=S.P<br><!-- End of picture text -->

Thame | 

###### o_department='Sales’ | Employees 

In this tree: + The leaf node is the base relation of Employees. 

- + The middle node is a selection operation that filters records by department. 

- + The root node is a projection that retrieves only the name attribute. 

Query trees are useful for visualising the execution of a query and are often used by query optimisers to evaluate different execution strategies. 

###### 4. Query Graphs 

Query graphs are another graphical representation used to describe joins and relationships among multiple tables. In a query graph: 

+ Nodes represent relations. 

+ Edges represent join conditions. 

This representation is especially useful for complex ae A aoe . queries involving multiple joins, as it allows the optimiser to determine efficient join orders and 

methods. Query graphs play a vital role in join order Ptimisation, which is crucial for performance when querying large datasets. 

Understanding the different forms of query representation is essential for comprehending how databases process and optimise queries. While end users interact with databases through high-level languages like SQL, the DBMS internally translates these queries into more formal and efficient representations, such as relational algebra expressions, calculusstructures like query trees formulas, and graphs. and graphical 

These representations allow the database system to evaluate multiple execution plans, select the most efficient one, and ultimately ensure fast and reliable data retrieval. For students and practitioners of database systems, mastering these foundational concepts is crucial for both theoretical understanding and practical performance tuning. 

###### 4.1.2 Introduction to Query Optimisation 

Query optimisation is a key component of database management systems (DBMS); it focuses on improving the efficiency of query processing. When users submit a query, especially in SQL, there are often multiple ways the database can execute that query. The DBMS must determine the best, most cost-effective way to perform the operation. This process is known as query optimisation 

Query optimisation is the process of selecting the most efficient way to execute a given database query. It ensures that the database system delivers results quickly and with minimal resource usage. 

The main goal of query optimisation is to minimise the resources used during query execution, such as CPU time, memory, and disk I/O, and to provide faster response times to users. It is especially important in lange"scele systemsiwhele poorly opumised queries can significantly degrade performance. 

© Copyright 2025 MIVA Open University AllRights Reserved 

98 

###### Query Optimisation in Database 

4.1.2.1 Query Optimisation Process Query optimisation is a critical component of database management systems (DBMS) that aims to improve the performance and efficiency of query execution. When a user submits a SQL query, the database system undergoes several internal steps before returning the desired results. These steps ensure that the query is valid, logically sound, and executed in the most resource-efficient manner. The key stages involved in the query optimisation process are parsing, translation, optimisation, and execution: 

###### Parsing 

The first step in the query optimisation process is parsing. Here, the DBMS checks the submitted query for correct syntax based on SQL grammar rules. If the query contains errors (such as misspelt keywords or invalid structure), an error message is returned to the user. 

If the syntax is valid, the query is converted into an internal data structure, usually a Parse tree or abstract syntax tree (AST). This structure captures the logical meaning of<sup>the query andis usedfor further</sup> processing. 

###### Translation 

02 

After parsing, the query is translated into: a relational algebra expression or logical query plan. Relational algebra is a formal language used to represent database queries in terms of mathematical operations like selection, projection, join, union, and difference. 

This logical plan is independent of the physical implementation and serves as a blueprint of what the query wants to achieve. It defines what data needs to be retrieved, but not how to retrieve it. This abstraction allows the system to explore different strategies for executing the query. 

### 6 M I a 

03 Optimisation ine: post crucial stage’ Is query! optimisation: DUIIOg this pbasenthie DEMS generates muttiple physical query plans, so representing a different way to execlite the logical query: These plans mayivary in iheintise.of indexes, Honinethods eg. nested-loop jain, hash join, merge join), eccoss pathisyand cLdchoropelauorss 

sl ‘The.query optimizer evaluates these plans based ona cost model, estimating how much time or resources each plan would consume. The cost model considers factors such as: 

- + Database statistics (e.g., table sizes, data distribution) 

- « Index availability 

###### » WO costs and CPU usage 

- + Memory usage 

- Parallelism and available system resources 

The optimiser then chooses the plan with the lowest estimated cost, assuming it will deliver the best performance. 

- There are two main types of optimisation: + Rule-based optimisation: Uses predefined rules to choose plans. 

- Cost-based optimisation: Uses estimated costs to evaluate and select 

the best plan. 

Execution Once the optimal planis selected, it is passed to the query execution engine. This component carries out the operations specified in the plan, retrieves the data from the underlying storage, applies filters and joins, and finally returns the results to the user. 

###### 04 



<!-- Start of picture text -->
99<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AllRights Reserved 

###### Query Optimisation in Database 

### G M I a 

Thefundamental query optimisation to the efficientprocess functioningis of Convert Cartesian_ prooucts inte joins rs 7 ‘ Cartesian products are expensive operations relational databases. By transforming a highlevel SQL query ‘into an optimised‘ execution and should only be used when necessary. The Planeane DBMS SSOSepnimalresouresimal optimiserproducts with attemptsselection to combineconditions Cartesianto form usage and faster response times. The query efficient join operations optimiser, using database statistics and cost estimates, plays a central role in identifying the best way to processa query. Use indexes w here available: If an index exists writeUnderstandingi queriesi that are this process both correct helps developers and “Prefersrefer:eeto USeae Iti to speedentersup datapaulretriev.retrieval performance-friendly. . Rule-based optimisation is simple and fast, making Their conflict is not just about the specific it usefulseful f for smala **l** l **er** databasesda SESOFor SY!system s: wherewhe it Butal Bar heir incl CEL query patterns are predictable. However, it lacks the osiiohy Dub also abou euisir ndlvigve flexibility to adapt to changing data distributions or career aspirations, their sense of self-worth, _ sctem states. Since it does not consider the actual and their belief in their own abilities. Similarly, data characteristics, the execution plan chosen may a team divided over the direction of aproject —_not always be the most efficient. may be grappling with different visions for the company's future, different philosophical 2. Cost-Based Optimisation (CBO) approaches to problem-solving, or different Cost-Based Optimisation is a more advanced and advanced and and perceptions of what constitutes success. accurate technique. technique. Instead of relying relying solely on on 

Cost-Based Optimisation is a more advanced and advanced and and accurate technique. technique. Instead of relying relying solely on on rules, the optimiser evaluates all possible execution plans and estimates the cost associated with each. The plan with the lowest estimated cost is selected for execution. 

###### 4.1.2.2 Types of Query Optimisation 

There are two primary types of query optimisation: Rule-Based Optimisation (RBO) and Cost-Based eae . Optimisation (CBO). Both aim to improve performance but differ in approach, complexity, and pocurecy, 

The cost is calculated based ona variety of factors, imeiuennes o 

Number of tuples (rows) in each relation: Larger tables typically result in higher processing costs. 

###### 1. Rule-Based Optimisation (RBO) 

Rule-Based Optimisation uses a predefined set of rules or heuristics to transform queries into more efficient forms. These rules are based on common database practices and logical assumptions that generally lead to better performance. 

Availability and type of indexes: Indexes can drastically reduce the number of rows accessed, reducing I/O and processing time. 

- Selectivity of conditions: This refers to how many; rows matchAn a condition. A condition; with high selectivity returns fewer rows, which is generally more efficient. 

Some common heuristics7 used in rule-based aan — optimisation include’ 

Perform selection operations early: By i filtering rows as early as possible, the size of 5 intermediate and processingresults time. is reduced, saving memory 

. . . . Join algorithms and order: Differentne join methods (e.g., nested-loop, hash join, merge join)ey Rehave citeentdifferent costseandependingdi on ea the size of input tables. 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

100 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Query Optimisation in Database 

SystemMemory, CPU, statisticsdisk and I/O rates, resource and availability:parallelism also influence plan selection. 

Cost-based optimisation requires accurate and upto-date statistics. If the data distribution has changed and statistics are outdated, the optimiser may choose a suboptimal plan. Despite being more complex and time-consuming, CBO usually provides better performance in large and dynamic databases. 

Both rule-based and cost-based optimisationae have their roles in query processing. Rule-based optimisation is fast and straightforward but lacks precision. Cost-based optimisation, although computationally more intensive, typically results in more efficient query execution. Modern database systems often favour cost-based optimisation for its adaptability and effectiveness in real-world scenarios. 

4.1.2.3 Methods and Techniques of Query Optimisation Several techniques. are used by optimisers to; transform queries and select efficient execution strategies. Below are some of the most commonly used query optimisation methods: 

ee SELECTION AND PROJECTION PUSHDOWN 

One of the most basic optimisation techniques involves applying selection and panes . projection operations as early as possible in the execution5 plan. ThisA reduces the sizeé of intermediate results and speeds up the ; query, 

Example: Instead of retrieving all records from a table and then applying a filter, the selection should be applied first to reduce the number of records retrieved. 

###### @ 

JOIN ORDER OPTIMISATION 

Whena query involves multiple joins, the order in which the joins are executed can greatly impact performance. The optimiser evaluatesdifferent join orders and chooses the one with the lowest estimated cost. 

Example: Joining smaller tables first or tables with selective conditions can significantly reduce the size of intermediate results. 

###### @ 

###### USE OF INDEXES 

Indexes greatly speed up access to specific rows in a table. The optimiser checks if a suitable index is available and uses it instead of performing a full table scan. 

Example: A WHERE clause ona column witha B-tree index allows the optimiser to quickly locate matching rows without scanning the entiratable: 

MATERIALISED =e VIEWS AND CACHING uy Seton sat sao ionic WEES an ° no chahg= ofen.miey canoe materialised (stored as actual tables) to . . . avoid recalculating them each time. . . Example: Pre-computing and storing the result ofacomplex Jjoin or aggregationggreg for reporilig purposes: 

© Copyright 2025 MIVA Open University AllRights Reserved 

101 

###### Query Optimisation in Database 

###### QUERY REWRITING 

The optimiser can rewrite queries into more efficient but semantically equivalent forms. 

Example: A nested query can often be rewritten as a join, which may be more efficient to execute. 

### 6 M I a 

###### USE OF PARALLELISM 

Modern database systems use parallel processing to divide the query into multiple parts and execute them simultaneously on multiple processors or cores. This is particularly useful for large-scale queries on big data. 

- Original 

SELECT name FROM Employees WHERE dept_idWHERE locationIN (SELECT = 'NY'); id FROM Departments 

- Rewritten SELECT e.name FROM Employees e JOIN Departmentsd ON e.dept_id = d.id WHERE d.location = ‘NY’: 

###### QUERY REWRITING 

The optimisera can rewrite. queries into more efficient but semantically equivalent forms. 

Example: Anested query can often be rewritten as a join, which may be more efficient to execute. 

- Original SELECT name FROM Employees WHERE dept_id IN (SELECT id FROM Departments WHERE location; = 'NY'); 

###### ~- Rewritten 

SELECT e.name FROM Employees e JOIN Departments d ON e.dept_id = d.id 

###### rs ) 

COST ESTIMATION AND STATISTICS 

The optimisera relles- on statisticsa such as the number of rows, distinct values, and data distribution to estimate the cost of different operations. Keeping database statistics up to date is crucial for effective optimisation. 

##### © 

SUBQUERYFLATTENING 

Nested subqueries can be transformed (flattened) into joins or set operations to allow more efficient execution. 

###### 10) 

PREDICATE MERGING AND SIMPLIFICATION 

The optimiser simplifies complex boolean conditions in the WHERE clause to reduce unnecessary computations. 

Example: WHERE (A = 5 AND A = 5)can be simplified toWHERE A = 5. 

WHERE d.location = 'NY'; 

© Copyright 2025 MIVA Open University AllRights Reserved 

102 

8, M I T ay 

###### Query Optimisation in Database 

a gd MEMORY USAGE Memory is used to store intermediate results IFLRsorting,RGIShashing,FECor joiningTO EHlarge ESAS tables may consume a lot of memory. If the memory is insufficient, the system may need to use temporary disk storage (external memory), increasing the I/O cost. 

> FactorsAmet creeid er - The optimiser checksee how much data can be processed in memory before spilling to disk. 

e J pplin \ rithm:i =e Some joins, like hash joins, are more memoryintensive than nested loop joins. 

@ QUERY EXECUTION PLAN éaa (QEP) STRUCTURE anestueture ontne cen execution panes that is, the order and method of operations — playsa direct role in determining cost 

- » Join order: Different join orders can produce widely varying intermediate resultsizes and Costs 

- Access methods: Choosing between full table scans, index scans, or index-only lance reerecost 

- P : 

- Operator implementations: Using efficient algorithms (e.g., merge join vs 

- pesredicoacninctcescost Pe . 

+ Sorting and aggregation 

Operations that require holding data in memory for ordering or grouping affect memory cost 

> Oe STATISTICS AND DATA 2 DISTRIBUTION 

Accurate statistical information is crucial for cost estimation 

These include 

$_Y SIZE OF INTERMEDIATE |=]S| RESULTS 

The size of intermediate results generated during query execution significantly impacts both memory and processing time. Larger intermediate results require more resources for storage, computation, and further processing 

- + Number of tuples in each relation 

- + Number of distinct values for attributes (cardinality) 

- + Selectivity of predicates (i.e., the fraction of rows that satisfy a condition) 

- + Histograms or frequency distributions of values 

Optimisers aim to: 

- + Minimise the size of intermediate tables by pushing down selections and projections. 

With this information, the optimiser estimates how many rows will be processed and how large the intermediate results will be, which is essential for cost estimation 

- + Choose join orders that produce smaller intermediate results first. 

Query Optimisation in Database 

8, M I T ay 

~ AVAILABILITY AND TYPE FER OF INDEXES 

Indexes significantly reduce the cost of data 

Minimising data movement across the network is a major consideration in GiEualsHSele MEIN esas 

access 

* Single-column vs. multi-column indexes: Multi-column indexes may offer more efficient retrieval for queries with compound conditions. 

- + Clustered vs. non-clustered indexes: Clustered indexes keep the data physically ordered, which is more efficient for range queries. 

- Covering indexes: When all required columns are included in the index, the DBMS can avoid accessing the base table, reducing cost. 

The presence or absence of indexes determines whether the optimiser can use index scans instead of full table scans. 

NETWORK COST (IN ef8 8 DISTRIBUTED DATABASES) 

In distributed database systems, data may be located across different nodes or data centres. When queries involve data from multiple sites, network communication cost becomes a critical factor. 

This includes + Data transfer time: Time to send data across the network. 

- + Latency: Delay in establishing and maintaining connections. 

+ Bandwidth constraints: Limitations on how much data can be transferred per unit time. 

CONCURRENCY AND WORKLOAD 

The current system workload and number of concurrent queries affect performance. Even if a query has a low estimated cost, it might perform poorly under high concurrency. 

- The optimiser may take into account: + Locking and blocking behaviour 

* Contention for I/O or memory 

+ Query prioritisation and resource limits 

Modern systems may use adaptive optimisation to adjust plans dynamically 

based on system load 

###### QUERY my COMPLEXITY 

Complex queries with multiple nested subqueries, joins, and aggregations require more sophisticated optimisation and evaluation strategies. 

More complex queries often involve + Higher CPU and memory usage 

- + More intermediate results 

- Greater potential for suboptimal join order or method selection 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Query Optimisation in Database 

Query evaluation cost is a multi-dimensional concept that depends on several interrelated factors, including disk I/O, CPU usage, memory availability, data distribution, indexing, and the structure of the execution plan. Understanding these factors helps database designers, developers, and administrators write more efficient queries and design better dsiabases. 

Methods of Evaluating Query Optimisation Several methods are used to analyse and evaluate how effective the optimisation process is. These methods aim to compare execution plans, identify inefficiencies, and determine whether a better plan could have been selected. 

###### 1. Execution Plan Analysis 

By considering these aspects, the query optimiser can generate cost-effective plans that deliver fast and efficient results — which is essential for maintaining performance in both transactional and analytical database systems. 

ITO 41: Wnatractors snotld necnacidersd when : ans . evaluating the cost of queries in relational database systems? 

ITA 4A: 

. The cost of query evaluation depends on factors A eat such as disk I/O, CPU usage, memory availability, the size: of intermediate. " results, query EXEdistribution, CTUONAen DANSthe availabilityTUCTULS SHAUSete of indexes,ECS210)andnetwork datsCa) costs in distributed systems, concurrency, and query complexity. Efficient query optimisation involves balancing these elements to ensure fast and resource-efficient query execution. 

###### 4.1.3.22 Methods and Metrics. off Evaluating1 z Query Optimisation 

Given that a query can often be executed in many different ways, the optimiser chooses the best execution plan based on various cost estimates. However, after an execution plan is selected and implemented, it becomes important to evaluate the effectiveness of the query optimisation process. Evaluating query optimisation helps database administrators and system developers understand performance characteristics, detect bottlenecks, and make informed decisions about indexing, schema design, and tuning strategies. 

One of the most direct methods for evaluating query optimisation is analysing the query execution plan generated by the DBMS. Most modern database systems provide tools to display and interpret these plans. 

- « EXPLAIN / EXPLAIN PLAN: These SQL commands show the step-by-step execution strategy for a given query, including join types, access methods, and estimated row counts. 

- Execution Plan Comparison: Comparing multiple alternative plans can help determine wha **e** ther the optimiser chose theF most efficient path. 

- F 

- + Visual Tools: GUI-based database tools (e.g., Oracle: SQL Developer,i PostgreSQL pgAdmin) present execution plans graphically, making them easier to analyse. 

Use case: If a query performs poorly, reviewing the plan may reveal that a full table scan was chosen when an index scan would have been better. 

2. Benchmarking and Testing with Query Workloads Benchmarking involves executing a set of queries (a workload) under controlled conditions to assess performance. 

- Synthetic workloads: Created to 

- simulate expected user queries. 

- +* Real-world workloads: Collected from actual system logs. 

These workloads are executed with different optimisation strategies, and performance is compared across eae are time, Resource deager end pap erection: 

© Copyright 2025 MIVA Open University AllRights Reserved 

106 

Query Optimisation in Database 

GNi MGiecicean Univeasit?I T 

3. Profiling and Monitoring Tools 

Database profiling tools allow the capture of runtime statistics and resource usage. These tools include: * Query profilers: show how much ume:was spent in each stage of execution (e.g., MySQL’s SHOW PROFILE). 

- + Performance monitors: Track CPU, memory, disk I/O, and query throughput over time. 

- * Dynamic tracing tools: Some databases provide tools to track query lifecycle in real time. 

This method is essential for understanding the actual behaviour of optimised queries in production environments. 

4. Experimental Query Tuning In experimental tuning, different versions of a query (or different database configurations) are tested to observe their impact on performance. 

###### This includes: 

+ Manually changing join orders 

- + Using or avoiding certain indexes + Rewriting queries using alternative logic (e.g., subqueries vs. joins) 

Performance results are compared to see how each change affects execution cost. 

5. Simulation and Modeling This method involves building mathematical or simulation models to predict query performance under different conditions. Though more theoretical, it helps researchers and designers understand how the optimiser’s cost models align with actual performance. 

###### Metrics for Evaluating Query Optimisation 

Once the methods are applied, various metrics are used to evaluate the performance and efficiency of query execution plans. These metrics help determine whether the optimiser's choices are effective. 

01. Execution Time 

02. Number of Disk I/O Operations 

03. CPU Usage 

Execution time (also called response time) is the total time taken from query submission to result retrieval. It is one of the most direct and important performance metrics 

- + Lower execution time implies better optimisation. 

- + Consistent execution time under similar workloads indicates stable optimisation. 

This metric is easy to measure 

using system logs or profiling tools. 

Disk access is often the most expensive operation in query execution. Measuring + Logical I/O: Pages read from the buffer cache. 

- + Physical I/O: Pages read from the disk directly. 

The fewer the I/O operations, the more efficientthe query plan. Optimisers aim to reduce disk I/O through indexes, projections, and join reordering. 

The percentage of CPU cycles used by the query process can indicate whether optimisation effectively minimises computation. High CPU usage might suggest inefficient Operations like excessive sorting or joining large datasets. 

GNi MGiecicean Univeasit?I T 

###### Query Optimisation in Database 

###### 04. 

Memory Consumption 

05. Throughput 

06. 

Plan Stability 

Queries that use complex joins, sorting, or hashbased operations consume memory. If memory consumption exceeds available RAM, performance can degrade due to disk swapping. Optimised queries minimise memory use without sacrificing correctness. 

Throughput is the number of queries executed per unit of<sup>time,</sup> especially important in multi-user or batch-processing environments. + High throughput indicates that the DBMS is handling more queries efficiently. 

- + This metric is especially useful for evaluating optimisation strategies in OLTP (Online Transaction Processing) systems. 

An important qualitative metric is plan stability, which refers to how consistently the optimiser selects the same or similar execution plans over time, especially under changing data distributions. 

Unstable plans can lead to unpredictable performance. Stable optimisers produce consistent results across similar queries 

Cost Estimates vs. Actual Costs 

Modern optimisers estimate query costs during plan generation Comparing these estimated costs with the actual observed costs helps evaluatethe accuracyofthe optimiser. 

- + Large discrepancies may indicate outdated statistics or poor cost models. 

- + Improving statistics can help the optimiser make better decisions. 

Evaluating query optimisation is essential for ensuring that queries run efficiently, especially in large-scale database environments. Methods like execution plan analysis, profiling, benchmarking, and experimental tuning allow administrators and developers to assess optimisation quality. 



<!-- Start of picture text -->
’ | \ | A ] 4<br>’ \ t Al<br>> ail \ a Al) .<br>a: 3 ly | fl} . &§<br>j ‘ : 4<br>> }<br>- ¢<br>- 7 f :<br>‘oo i om<br>“” -— ' %<br>4 '<br>bof<br><!-- End of picture text -->

Metrics such as execution time, disk I/O, CPU usage, memory consumption, and throughput offer measurable indicators of performance. By applying these methods and metrics, database professionals can continuously monitor, tune, and improve the effectiveness of query optimisation strategies, ultimately enhancing the performance, reliability, and scalability of the entire database system. 

###### 4.1.3.3 Optimisation Cost in Centralised and Distributed Database System 

Query optimisation is a vital process in any database system that aims to determine the most efficient way to execute a given query. The goal is to minimise the total cost of processing a query while ensuring accurate and timely results. The concept of optimisation cost refers to the estimation and evaluation of resources—such as CPU, memory, disk I/O, and network bandwidth—required to execute a query. 

The optimisation cost differs significantly between centralised and distributed database systems due to architectural variations, data location, and system complexity. This lecture explores the key factors affecting optimisation cost in both centralised and distributed environments. 

###### Query Optimisation in Database 

Optimisation Cost in Centralised Database Systems Acentralised database system stores all data ata single location, typically accessed througha local area network (LAN) or directly from a server. The oc . ach eee “and simplerto anage due fo a single point of access. 

### 6 M I a 



<!-- Start of picture text -->
QUERY PLAN COMPLEXITY<br>BEE<br><!-- End of picture text -->

The optimiser evaluates different query EuGRUILET IMENSINTETE GT SRI SATS table sizes and data distribution. Choosing a poor plan increases overall execution cost. 

Key Components of Optimisation Cost in Centralised Systems 

LACK OF NETWORK COST 

Disk 1/O Cost 

Disk Input/Output operations are typically the most expensive component in centralised systems. 

The number of disk block accesses required to retrieve and process data significantly affects the cost. 

- + Full table scans and index scans vary in cost depending on data volume and index availability. 

- + Efficient indexing and clustering reduce I/O costs 

- . 

- ER=@ CPU Cost CPU cost involves, the processing timePe needed for operations like: . Lunasee, nenenimenilafenory, buFFerS . ging ry purer 

- : . - Efficient algorithms like hash joins or merge yolns Delp miniinise Cou usage: 

w MEMORY USAGE 

intermedlete results from joins o ficient li fotos he etnies Be anejata vito disk,enincreasing_ I/O10 cost.Vs Wel 

One advantage of centralised systems is the absence of inter-site communication, making them less complex in terms of cost estimation. All components reside in a single system, and network latency is negligible. 

Optimisation Cost in Distributed Systems In in distributeddistributed databasedatabase systsystems, dada **t** a ia i **s** sprespre **a** d across multiple sites connected via a network. These systems introduce additional complexity due to data distribution, site autonomy, and network dependency. 

Key Components of Optimisation Cost in Distributed Systems 

Thea, Data most Communication critical and expensiveCost component in distributed optimisation is network communication . 

Queriesincur: that access datafrom multiple sites 

- + Data transfer time: Time taken to move data between nodes. 

- - Networkmaintaininglatency:peleaDelays in initiating9 and + Bandwidth limitations: Affect the speed of data transmission. 

Minimising data movement is a top priority in distributed query optimisation. 

b. Disk I/O and Local Processing Each participating site still performs local query processing, similarto a centralised system. 

© Copyright 2025 MIVA Open University AllRights Reserved 

109 

###### Query Optimisation in Database 

### G M I a 

Local disk I/O and CPU cost are calculated at each node based on: + Local data access 

- + Intermediate result generation 

Repartition Join: Reorganises data so that matching tuples are at the same site. 

The choice of strategy impacts CPU, memory, and communication costs. 

- + Local filtering and projection 

c. Site. Selection; and Fragmentation, AWATONGSS: 

- Data fragmentation (horizontal, or vertical); affects optimisation cost: 

- + The optimiser must locate relevant fragments and decide which site(s) to 

- OCCESS: 

- + Fragment replication may offer multiple access paths; choosing the closest or leastbusy replica reduces cost. 

d. Join Processing Across Sites Distributed joins are cost-intensive due to the need to move and combine data from multiple jacations 

Various strategies include: 

- Semi-join: Reduces the size of data transferred. 

- Distributed Hash Join: Distributes data based on hash values and joins locally. 

e. Query Decomposition and Localisation A global query must be decomposed into subqueries that execute at individual sites. The query localisation process maps global references to local schemas and determines execution plans for each subquery. 

Optimisation cost depends on: 

- + Number of subqueries 

- + Their interdependencies 

; . 

- + Volume of intermediate results exchanged 

- an — 

- f. Synchronisation'and Coordination Distributed systems need synchronisation for consistent data access and correct query results. Coordination adds overhead in the form a ; 

- + Locking across sites 

- + Two-phase commit protocols for WEWEE SACI 

- + Failure recovery mechanisms 

These components increase the total cost of optimisation and execution. 

###### Comparative Summary 

|Factor|Centralised System|Distributed System|
|---|---|---|
|DiskI/OCost|Localandmanageable|Local per site, but accumulatesglobally|
|CPU andMemoryCost|Centralised, easytoestimate|Distributed andvariable per site|
|NetworkCost|Negligible|Significant; affectsoverallperformance|
|JoinProcessing|Local, withvariousalgorithms|May requiredatashippingandcoordination|
|QueryPlanningComplexity|Relativelylow|Highduetofragmentation and replication|
|TransactionCoordination|Simple|Complexwith2PCandconsistency issues|
|OptimisationStrategy|Focuson!/OandCPU|Focus oncommunication andsiteselection|



© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

110 

Query Optimisation in Database 

LU 6 MMIVA OPEN UNIVERSITYI a 

The cost of query optimisation varies widely between centralised and distributed database systems. While centralised systems mainly focus on minimising disk /O and CPU usage, distributed systems must also consider network communication, data localisation, and site coordination. Understanding these differences is critical for database administrators and system architects when designing cost-effective and scalable database systems. 

By carefully analysing optimisation costs and leveraging appropriate algorithms, indexing strategies, and query rewriting techniques, both centralised and distributed systems can achieve efficient query processing and improved performance. 

© Copyright 2025 MIVA Open University AllRights Reserved 

111 

###### Query Optimisation in Database 



<!-- Start of picture text -->
><br>Ss) M I T<br><!-- End of picture text -->

###### Part B F ILE (@) RGANISATION, _ supportsefficient access, minimises resource usage. | N 1D)EX | N G ’ A N D » — andensuresBelow are the data key reliability. objectives explained in detail: 

> 4.2.1 Introductioni To FileA OrganisationCre In Database 

File organisation refers to the method by which data is arranged and stored in files on 

secondary storage devices such as hard disks. It plays a crucial role in the overall performance of adatabase system, particularly in ensuring efficient data retrieval, minimal storage wastage, and optimal input/output (I/O) Operations. The way records are organised affects the speed at which data can be searched, inserted, updated, or deleted 

cdeerdenEnable Efficient Access to Data (Seq(Sequential 

One of the main goals of file organisation is to support both sequential and random access to data. Sequential access refers to reading 

records in a specific order, which is ideal for operations like report generation or range queries. Random access, on the other hand, allows quick retrieval of individual records without scanning the entire file. The organisation of data must be tailored to the expected access patterns to ensure high performance. 

There are various file organisation techniques, each suited to different types of access patterns and use cases. Common methods include heap (unordered), sequential (ordered), hashed, and clustered file organisation. The choice of method SEE SMESCIN ESIC NE SUAS ERT LGN access, update operations, and the nature of queries: 

Efficient fle ordanication ea foundational fe ie 5 a = a i sae Hi is Lie eral a lnalae eae indexing and query optimisation to reduce query execution time and system load. Poor file . ; organisation can lead to increased access times, excessive disk I/O, and inefficient use of storage resources. Therefore, understanding and selecting the appropriate file organisation method is essential for database administrators and system designers aiming to build high-performance and scalable database systems 

4.211. Objectives of File Organisation File organisationP in database systems is; a fundamental concept that directly iimpacts the performance and efficiency; of data storage and retrieval. The primary objectives of file organisation revolve around structuring data in a way that 

###### 8)2 : Support Fast Insertion, Deletion, and Update Operations 

Aneffective file organisation scheme should ey : = deletionallow for rapid insertionof existing ones, of andnew smooth records,updates efficient to data. These operations should not degrade performance over time. Techniques such as indexing, hashing, or use of overflow areas can Pra - f be used to maintaingon performance while handling dynamic data modifications. 

a)z . Support Fast Insertion, Deletion, and Update Operations : ; : Disk|/O operations are typically the slowest part of data access due to physical limmations of storage hardware. A well-organised file structure minimises the number ofdisk reads and writes required to execute a query or perform updates. By grouping( Tresrelated records close together‘ and using efficientaT indexing strategies,a the system can: significantly‘x reduce the time spent accessing the disk. 

© Copyright 2025 MIVA Open University AllRights Reserved 

12 

###### Query Optimisation in Database 

###### 8, M I T L MIVA OPEN UNIVERSITY 

Ensure Data Integrity and Minimal 

###### Redundancy 

File organisation should support the maintenance of data integrity—ensuring that the data is accurate, consistent, and reliable. Additionally, it should help minimise redundancy, which occurs when the same data is unnecessarily stored in multiple places. Reducing redundancy not only saves storage space but also simplifies update operations and reduces the risk of data anomalies. 

###### Optimise Query Performance 

Ultimately, the goal of any file organisation method is to enhance query performance. This includes reducing response time for read and write operations and ensuring that the system can handle a large number of transactions efficiently. By organising data according to frequently used query patterns, the database system can retrieve results faster and improve the user experience. 

4.2.1.2 Types of File Organisation in Database Systems File organisation in database systems determines how records are stored, accessed, and managed on secondary storage devices such as hard disks. Choosing an appropriate file organisation method is critical for optimising data retrieval performance, minimising disk I/O operations, and ensuring system scalability and responsiveness. There are several types of file organisation techniques, each with specific structures, advantages, disadvantages, and use cases. This section discusses five major types: heap (unordered), sequential (ordered), hashing, clustered, and indexed file organisation. 

###### Heap (Unordered) File Organisation 

Heap file organisation, also known as unordered file organisation, is the simplest and most straightforward method of storing records. In this approach, records are stored in the order in which 



<!-- Start of picture text -->
mi 789<br>BS 192<br>RE av, a<br>R4 ON,<br>R5 zz<br>: 5<br>144<br>R2<br>152<br><!-- End of picture text -->

Figure 41: Heap file Organisation 

###### eharactaristice: 

- + There is no particular order to the data. 

- + Newrecords are simply appended totheendof the file or placed in the first available free 

###### eke 

- + Retrieval involves scanning the entire file sequentially to find a matching record. 

###### Advantages: 

- + Simplicity: Easy to implement and manage. 

- + Fast Insertions: Insertion of new records is very quick since there is no need to maintain any order. 

- + Low Overhead: No overhead from indexing or sorting mechanisms. 

- Disadvantages: + Slow Searches: Retrieving a specific record can be time-consuming as it may require scanning the entire file. 

- + Inefficiency for Range Queries: Since records are not ordered, range-based searches are inefficient. 

- + Not Suitable for Frequent Retrieval: pe otal ceaieces Moen eet large BLASELS WIR TTeuenL Ted Operanons: 

- se case: + Suitable for small tables, temporary data, or logging systems where insertions are more frequent than retrievals and the data lifecycle is short. 

###### Query Optimisation in Database 

###### Sequential (Ordered) File Organisation 

In sequential file organisation, records are stored in a sorted order based ona specific key field (e.g.. customer ID, product code). This ordering enables efficient retrieval, especially for operations involving range queries or sorted data access. The diagram is as represented in Figure 6.2 where records were entered sequentially or serially based on the chosen key field 

RI | R3 | seeeeeeeeeeeees | R5 | RG StartingSSEof aEnd of Figure 4.2: Sequential file organisation 

Characteristics: 

- + Allrecords are arranged in ascending or descending order of a chosen key. 

- + Searching can be done using binary search due to the ordering. - . . . 

- + Newrecord insertion or deletion requires maintaining the order. 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### Advantages: 

* vantages: 

- + Efficient for Range Queries: Queries that involve scanning records within a range of keys are executed efficiently. 

- + Better for Batch Processing: Sorted data is optimal for batch operations like report generation or summarisation. 

- + Supports Binary Search: Faster than linear search when finding specific entries. 

- Disadvantages: 

- Disadvantages: ; + High Maintenance for Updates: Inserting or deleting records may require reorganising the file or shifting records. : 

- + Performance Bottlenecks: Rewriting entire: blocksnenenel for simple updates is resource- 

- + Less Flexible: Not ideal for environments where data is constantly changing. 

- Use Case: Case: 

- Use Case: Case: . . + Best for static or archival data, where data is rarely updated but often queried in sorted order, such as historical records or financial archives. 

###### OS. 

Sequential (Ordered) File Organisation 

In sequential file organisation, records are stored in a sorted order based ona specific key field (e.g., customer ID, product code). This ordering enables efficient retrieval, especially for operations involving range queries or sorted data access. The diagram is as represented in Figure 6.2 where records were entered sequentially or serially based on the chosen key field 



<!-- Start of picture text -->
Data | Data02 Buckets<br>ase<br>ie (ies) 105 a<br>oe<br>New Yi<br>Record,<br><!-- End of picture text -->

Characteristics: + Designed for fast access to records using exact-match queries. 

- + Records are not ordered but grouped by hash buckets. 

- + Collisions (when two records hash to the same bucket) are handled using techniques like chaining or open addressing. 

Advantages: 

- + recordExtremely based on Fast Lookup:a specific Ideal for key (e.g., retrieving WHERE a ID 

   - = 101) 

- + Constant-Time Access: Under ideal 

- conditions, hash lookups can occur in O(1) time 

- + Efficient Insertions: Quickly determines the location to insert a new record. 

Figure 6.3: Hash File Organisation 

© Copyright 2025 MIVA OpenUniversityAllRights Reserved 

14 

###### Query Optimisation in Database 

### G M I a 

###### Disadvantages: 

- + Poor for Range Queries: Since data is not sorted, range queries require scanning all buckets. 

- + Collision Handling Required: Hash collisions can lead to 

- increased complexity and slower access. 

+ Rehashing Needed: When the hash table becomes too full, rehashing (reorganising the hash function and data) is necessary, which is time-consuming. 

###### Use Case: 

- + Ideal for exact-match search systems, such as user 

- authentication systems, caching systems, and indexing engines. 

Clustered file organisation groups records based on the similarity of values in a particular clustering field. In this method, records with related values are physicallycs stored together to improve query performance, especially for range and grouping operations. 

Let us understand the concept better with this illustration given a database for an online store with two tables: “Customers” and "Orders". 

###### Customer table: 

|:|||
|---|---|---|
|1<br>|<br>|RameshSharma|Delhi|
|2<br>||Priya Patel|Lucknow|
|3<br>||SanjayGupta|Patna|
|(QUSESIEEAIS|||



|mer_id|mer_name<br>||_id|date||
|---|---|---|---|---|---|
|1 ||namesh<br> §Rarmma<br>||Delhi<br>||101 ||2024-05-01<br>| Rs.|1500|
|1|hanan<br>Sharma<br>||Delhi<br>||103 ||2024-05-04<br>| Rs.|2500|
|2 ||PVe —<br>||Lucknow<br>||102 ||2024-05-05<br>|Rs.|10000|
|3|Enel<br>||Patna<br>||104||2024-05-06<br>|Rs|.500|



Because of this organisation, the database may quickly retrieve any relevant information in a single, contiguous block of storage when a query is made for Ramesh Sharma's order history, eliminating the need for numerous I/O operations. 

- Characteristics: + Often implemented: using clustered indexes, where the physical order of rows matches the index order. 

- + Optimised for operations that access records with the same clustering field value. 

|101<br>‘|<br>|<br>2024-05-01<br>||Rs.1500|
|---|---|
|102<br>2<br>|<br>2024-05-03<br>| <br><br><br><br><br>|Rs.10000<br>|
|103<br>1<br>|<br>2024-05-04<br>||Rs.2500|
|104<br>3.<br>|<br>2024-05-06<br>|<br><br>|Rs.500<br>|
|4<br>Thesystemmustquicklycombinethes<br>|e<br>|
|<br>databases inordertoobtainthenecess<br>f<br>4<br>when<br>aconsumerrequestsinformation <br>theirpurchasinghistory.Clusteredfile<br>|<br>arydata<br>about<br>|
|<br>organisationcangreatlyimprovethisp|ocedure.|



   - Cledted pelt abie: 

- Advantages: . Improved Query Performance: 7 Queriesieath t at filter or group by the clustering field (e.g., customer ID, department) perform significantly faster. Efficient fOr Bel 

- p Gulclecc UG, Related records ate. stored together, reducing disk read operations during ENA Bett @ He Pert Meeiat ’ 

- O eareaelccarear ale Woragumente Oamenceeyae are stored closely, fewer cache misses occur. 

By clustering the tables on the 

“customer_id" (cluster key), the records would be grouped as follows: 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

115 

###### Query Optimisation in Database 

### 6 M I a 

Disadvantages: 

- + High Maintenance Cost: Inserting or updating records can be expensive due to the need to preserve the clustering order. 

- + Limited Flexibility: If the data access pattern changes, the clustering strategy may no longer be effective. 

- * Single Clustering Field: Only one field can be used for clustering, limiting optimisation opportunities for other queries. 

###### Use Case: 

- + Useful in transaction systems, data warehousing, and analytical applications where data is often retrieved based on a particular category or iliellip) SUNS MEETSSTE mS oo Orsaies bes " 

###### 05. Indexed File Organisation 

Indexed file organisation uses an index structure to provide fast access to records in a file. The index acts like a table of contents, pointing to the physical location of data blocks or records. 



<!-- Start of picture text -->
{ Index File‘ ]<br>a Eee<br>| Key —+ addr |<br>101 —> 0001<br>| 103 —+ 0002 |<br>| 106 —+ 0003 |<br>110 —» 0004<br><!-- End of picture text -->

Types of Indexes: Indexes improve data retrieval speed in databases, ang they come in two main types: dense and sparse. A dense index includes an index entry for every record in the data file, providing fast and direct access but requiring more storage space. In contrast, a sparse index contains an index entry for each block or group of records, not for every individual record. While it uses less storage, it may require additional searching within a block to find the exact record. The choice between dense and sparse indexing depends on the trade-off between access speed and storage efficiency. 



<!-- Start of picture text -->
oo<br><!-- End of picture text -->

###### Common Indexing Structures: 

[ Data File ] Database systems use specialised indexing p—-————————— ———————., structures to improve data retrieval performance. | Key Record: ID=101, Name | Twowidely used structures are B+ Trees and Bitmap 101 -—+Record: ID=101, Name Indexes. 

|||Key|Record:|<br>ID=101,|<br>Name<br>||
|---|---|---|---|---|
|Address|101|-—+Record:|ID=101,|Name|
|||103|-—+Record:|ID=101,|Name<br>||
||106|—»Record:|ID=101,|Name|
|||110-|—»Record:|ID=101,|Name<br>||



B+ Trees are balanced tree structures ideal for | dynamic data operations. They maintain sorted data and allow fast search, allow fast search, fast search, search, insertion, and deletion. deletion. All actual data records are stored at the leaf nodes, and internal nodes store only keys for navigation. This structure ensures consistent performance and structure ensures consistent performance and ensures consistent performance and consistent performance and performance and and is commonly used commonly used used in transactional databases. transactional databases. databases. 

"————————————————"_ and allow fast search, allow fast search, fast search, search, insertion, and deletion. deletion. All 

Figure 6.4 Indexed file Organisation 

Indexed file organisation uses an index file to This structure ensures consistent performance and structure ensures consistent performance and ensures consistent performance and consistent performance and performance and and speed up data access. The index file stores key is commonly used commonly used used in transactional databases. transactional databases. databases. values along with their corresponding addresses or pointers to the actual data in the data file, Bitmap Indexes are highly efficient for low- Indexes are highly efficient for low- are highly efficient for low- highly efficient for low- efficient for low- for low- lowwhich contains the full records. Accessing a cardinality attributes—fields attributes—fields with a small number of a small number of small number of number of of record involves two steps: first, the system distinct values values (e.g., gender or status). Each distinct status). Each distinct Each distinct distinct searches the index using a key (e.g., 106) tofind value is represented represented by a bitmap a bitmap bitmap (bit array) array) the address; second, it retrieves the record from _ indicating the presence or absence of that value in indicating the presence or absence of that value in the presence or absence of that value in or absence of that value in absence of that value in of that value in in the data file using that address. This method each record. These These indexes are especially effective are especially effective especially effective effective improves search efficiency, especially in large in analytical analytical and data warehouse queries, where set data warehouse queries, where set warehouse queries, where set queries, where set where set set databases, by minimising the need for operations (AND, OR, NOT) on bitmaps can quickly bitmaps can quickly can quickly quickly sequential access to every record. filter large datasets. large datasets. datasets. 

Bitmap Indexes are highly efficient for low- Indexes are highly efficient for low- are highly efficient for low- highly efficient for low- efficient for low- for low- lowcardinality attributes—fields attributes—fields with a small number of a small number of small number of number of of distinct values values (e.g., gender or status). Each distinct status). Each distinct Each distinct distinct value is represented represented by a bitmap a bitmap bitmap (bit array) array) _ indicating the presence or absence of that value in indicating the presence or absence of that value in the presence or absence of that value in or absence of that value in absence of that value in of that value in in each record. These These indexes are especially effective are especially effective especially effective effective in analytical analytical and data warehouse queries, where set data warehouse queries, where set warehouse queries, where set queries, where set where set set operations (AND, OR, NOT) on bitmaps can quickly bitmaps can quickly can quickly quickly filter large datasets. large datasets. datasets. 

© Copyngnt zuzo Miva Upen University AlKignts Keservea 

116 

Query Optimisation in Database 

### 6 M I a 

###### Characteristics: 

- + Index files are kept separate from data files but synchronised for consistency. 

- + Multiple indexes can be created on different fields to support various query types. 

###### Advantages: 

- + Fast Search: Quickly locate records using indexed fields, especially when dealing with large datasets. 

- + Supports Multiple Access Paths: 

- Indexes can be used to optimise different types of queries. 

- + Efficient Range Queries: Especially with 

- tree-based indexes like B+ trees. 

###### Disadvantages: 

- + Additional Storage Cost: Indexes consume extra disk space. 

- + Maintenance Overhead: Inserts, deletes, or updates to records require updating the corresponding index entries. 

- + canComplexity:introduce Moreimplementation sophisticated index structurescomplexity. 

Use Case: 

- + Best suited for Online Analytical Processing (OLAP) systems, business intelligence 

- applications, or any system where frequent querying of large datasets occurs. Indexing is 

- especially effective when users need to filter and sort data on multiple fields. 

© Copyright 2025 MIVA Open University AllRights Reserved 

117 

Query Optimisation in Database 

Ss) MIVAMOPEN IUNIVERSITY T 

1) 

###### SUMMARY 

Efficient query processing is a cornerstone of modern database systems, particularly as data volumes and complexity continue to grow. Two critical components that contribute to this efficiency are query optimisation and file organisation. These elements work together to reduce resource consumption, improve response time, and ensure scalable performance. 

Query optimisation is the process of choosing the most efficient execution plan for a database query. Whena user submits a query, the database management system (DBMS) evaluates various possible plans involving operations like joins, selections, and projections. The goal is to find the plan that minimises cost, defined in terms of CPU usage, memory, and disk I/O. Query optimisation can be divided into two types: Rule-Based Optimisation (RBO) and Cost-Based Optimisation (CBO). RBO usesa set of fixed heuristics such as pushing selections early, using indexes, and replacing Cartesian products with joins. It is simple and fast but may not yield the best plan for all situations. CBO, on the other hand, estimates the cost of multiple query plans using statistical information like table size, index availability, and data distribution. It selects the plan with the lowest estimated cost and is more accurate but computationally intensive. 

Common query optimisation techniques include selection and projection pushdown, which reduces intermediate result sizes early; join order optimisation, which finds the most efficient sequence for joining tables; index utilisation, which speeds up access to rows using indexes; query rewriting, which transforms queries into more efficient forms; materialised views and caching, which store frequently used results; parallelism, which executes query parts simultaneously on multiple processors; and subquery flattening and predicate simplification, which converts nested queries and optimises Boolean expressions. These methods ensure that database systems handle large and complex queries efficiently. 

File organisation refers to how records are physically stored on disk, and the structure used impacts the speed of data access and overall system performance. Common file organisation methods include heap (unordered), where records are stored wherever space is available, making it simple and suitable for insertheavy operations but inefficient for search and update; sequential (ordered), where records are stored based on an attribute's order, enabling fast range queries but slower inserts and deletes; and hashed, which uses a hash function to determine record location, making it efficient for equality searches but not for range queries. To enhance file organisation, indexing is used. Indexes allow the DBMS to quickly locate records without scanning entire tables and are especially vital for queries with conditions in the WHERE clause or JOINs. 

Internally, SQL queries are transformed into forms that facilitate optimisation, including Relational Algebra, which is procedural and uses operators like 6, TI, }<]; Relational Calculus, which is non-procedural and based on logic; Query Trees, which are hierarchical representations of operations; and Query Graphs, which are used for visualising joins between relations. These forms help the optimiser analyse and choose efficient plans. 

Query optimisation and file organisation are fundamental to the performance of database systems. While optimisation ensures smart execution strategies, file organisation provides the physical structure to support them. Together, they enable fast, efficient, and scalable data access in both traditional and modern data environments. 

© Copyright 2025 MIVA Open University AllRights Reserved 

118 

Query Optimisation in Database 

e Ss) MIVAMOPEN IUNIVERSITY T 

J) 

#### CONCLUSION 

Query optimisation and file organisation are foundational pillars for achieving efficient performance in modern database systems. Query optimisation ensures that data retrieval is executed using the most costeffective strategy by leveraging techniques such as join ordering, index usage, query rewriting, and parallel processing. Complementing this, file organisation determines how data is physically stored, directly impacting access speed and efficiency. Additionally, understanding various query representation forms— such as relational algebra, query trees, and graphs—enables deeper insights into how queries are processed internally. Together, these concepts equip database professionals with the tools to design and manage systems that are scalable, responsive, and optimised for complex data operations in an increasingly data-driven world. 

© Copyright 2025 MIVA Open University AllRights Reserved 

119 

STUDY SESSION FIVE Emerging Trends in Database Systems 

###### Emerging Trends in Database Systems 

# Ss) M I T 

###### INTRODUCTION 

As we navigate an increasingly data-driven world, the evolution of database systems has become essential to organisational success across industries. This session focuses on Al-Powered Databases—such as Autonomous DB and Oracle Al DB—alongside Blockchain Databases and Distributed Ledgers and Graph Databases, discussing their applications with a particular emphasis on tools like Neo4j and Amazon Neptune. Together, these topics show the dynamic shifts towards scalability, security, and intelligent data handling that define modern database technologies. 

| Amazon Neptune provide robust platforms for managing interconnected data, supporting realtime analytics and semantic understanding. This part of the session will explore how these technologies empower organisations to derive deeper insights from relational data, particularly in domains requiring intricate network analysis. 

This study session aims to equip you with the knowledge to evaluate and implement these emerging trends effectively. By the end, you will appreciate how Al, blockchain, and graph-based approaches are not merely enhancements but transformative forces in database systems. 



<!-- Start of picture text -->
> Te approaches are not merely enhancements but<br>wo “aay transformative forces in database systems.<br>6= , \i——8= .fJ 5.1LearningIdentify:Identify: the Outcomes significance significance of emerging  the Outcomes significance significance of emerging<br><!-- End of picture text -->

5.1LearningIdentify:Identify: the Outcomes significance significance of emerging trends in database systems, focusing on scalability, flexibility, and security in a datadriven world. 

Traditional database systems, once confined to structured data storage and retrieval, are now adapting to hendlevast, diverse datasetswith unprecedented efficiency. The integration of Artificial Intelligence (Al) into database management,machine learning where to optimise autonomousperformance, systems leverageenhance security, and reduce human intervention. Platforms like Oracle Autonomous Database exemplify this trend, automating tasks such as indexing and anomaly detection. 

5 Assess the teaturesor al rowered i 7 Seesos 2nd el Use erect ne learning for administration and opinion 

5.3 Analyse the principles and applications of Blockchain Databases and Distributed Ledgers, including their decentralised and immutable nature. 

5.4 Compare distributed database platforms with blockchain systems for high availability and fault tolerance. 

Concurrently, Blockchain Databases and Distributed Ledgers offer decentralised, transparent solutions, Teyolutlonisingchain managementsectors with suchas immutable finance data andrecords. Supply These innovations address critical needs for trust and data ;integrity: in an era of heightened regulatory scrutiny. 

5.5 Evaluatethe structure; and- applications of rer Databases i modelling comes relationships and real-time analytics. 

5.6 Explore the role of Knowledge Graphs in enhancing Al-driven analytics and propose strategies for overcoming challenges in their adoption. 

In modern robust systems, Graph Databases stands out as they excel at modelling complex relationships through nodes and edges, making them ideal for applications like fraud detection and 

recommendation systems. Tools such as Neo4j and 

‘© Copyright 2025 MIVA Open University All Rights Reserved 

121 

###### Emerging Trends in Database Systems 

###### PartA Al =.POWE RE D AN D B LOC KC HAI N DATABASES 

5.1.1 Overview of Database Evolution Database systems are foundational to modern computing, enabling the storage, retrieval, and technology continuesmanagement of data acrosstoevolve industries. rapidly, new As trends are reshaping how databases are designed, deployed, and utilised. These emerging trends address the growing demands for scalability, flexibility, speed, and security in a data-driven 

world. 



<!-- Start of picture text -->
el "J 4<br>\<br>—_ . ae— $ ~_Ey<br>Vp Zz) = Ss «><br>aa ———<br>:<br>< ye :<br>™~ NS<br><!-- End of picture text -->

One of the most significant trends is the rise of cloud-native databases. Traditional on-premises databases are increasingly being replaced or supplemented by databases hosted in the cloud, such as Amazon Aurora, Google Cloud Spanner, and Microsoft Azure SQL. Cloud-native databases offer elasticity, high availability, and cost-efficiency, allowing organisations to scale resources up or down based on demand. Serverless databases, in particular, eliminate the need for manual infrastructure management, allowing developers to focus on application logic rather than provisioning and maintenance: 

NoSQL databases have also gained momentum, particularly for handling semi-structured and unstructured data. Unlike traditional relational databases, NoSQL systems—such as MongoDB (document-based), Cassandra (column-based) 

## 6 M I a 

and Redis (key-value store) are designed for high performance,data modelling. horizontal These systemsscalability, are and essential flexible for applications involving large volumes of real-time anddata,recommendation such as social media engines. platforms, loT devices, 



<!-- Start of picture text -->
rl<br>—— ee<br>= 22> =<br>ry)os 4 NoSQL | )<br>—_ = p_p<br>= zg =<br>itl<br>=<br><!-- End of picture text -->

Multi-model databases represent another key trend. These systems support multiple data models database(e.g., relational, engine. document,Examples graph) include withi Ara **n** agoDB single and OrientDB. By integrating various data madels; multimodel databases provide greater flexibility for complex applications, reducing the need for multiple database solutions and simplifying data integration. 

###### 5.1.2 Al-Powered Databases (Autonomous DB, Oracle Al DB) 

The integration of Artificial Intelligence (Al) and Machine Learning (ML) with database systems has opened a lot of possibilities in the management of data. 

Al-powered databases can automate routine administrative tasks such as indexing, query optimisation, anomaly detection, and workload forecasting. For instance, Oracle Autonomous Database uses machine learning to manage updates, optimise performance, and enhance Sees ARE MEAS In 

‘© Copyright 2025 MIVA Open University All Rights Reserved 

122 

Emerging Trends in Database Systems 



<!-- Start of picture text -->
G M I a<br><!-- End of picture text -->

###### 5.1.2 1 Features and Benefits 

###### 51.2.2 Tools and Platforms 

###### AUTOMATION 

One of the primary features is automation, where machine learning algorithms handle routine administrative tasks traditionally performed by database administrators. For instance, tasks such as indexing, query optimisation, and patching are executed autonomously, reducing human effort and the potential for errors. This automation is particularly evident in systems like the Oracle Autonomous Database, which leverages Al to adapt to workload changes in real time. 

###### PERFORMANCE OPTIMISATION 

Anotnen crue feature js performance optimisation. Al-Powered Databases employ predictive analytics to forecast workload demands, dynamically allocating resources to ensure optimal query execution and system efficiency. This capability allows organisations to maintain high performance even during peak usage, enhancing user experience and operational throughput. The Oracle Autonomous Database, for example, uses machine learning to adjust resource allocation and optimise SQL queries, resulting in faster data retrieval and processing. 

###### SECURITY 

Security is a further benefit, with Al-driven systems offering advanced protection against threats. These databases detect anomalies, such as unauthorised access or data breaches, using pattern recognition and behavioural analysis. . mie’oracle SUESROMIONS Database integrates security features |ike automaticencryption and access contol ensuring com plience wit regulations such as GDPR and NDPR while safeguarding sensitive data. Collectively, these features reduce operational overhead, improve efficiency, and strengthen data integrity, making AlPowered Databases indispensable in modern enterprises. 

Oracle Autonomous Database 

Aprominent example is the Oracle Autonomous Database, a cloud-native solution that fully automates database management. It supports both transactional (OLTP) and analytical (OLAP) workloads, scaling seamlessly based on demand 

The platform employs machine learning to perform self-tuning, self-patching, and selfsecuring functions, allowing developers to focus on application development rather than infrastructure maintenance. Its implementation is particularly effective in large-scale enterprises requiring high availability and robust security. 

###### 02) Oracle Al DB 

Another notable tool is the Oracle Al DB, an extension of Oracle's Al capabilities integrated into its database ecosystem. This platform enhances data processing with Aldriven insights, such as predictive analytics and anomaly detection, directly within the database layer. 

tis designed to support real-time decisionnielelnghycaletslel Nel mein alee Stans) models into SQL queries, making it suitable for applications in finance and healthcare whereImplementation rapid datainvo ana **l** vesysis leve is c **r** iticalaging Oracle Cloud Infrastructure, ensuring scalability and integration with existing enterprise systems. 

© Copyright 2025 MIVA OpenUniversityAll Rights Reserved 

123 

###### Emerging Trends in Database Systems 

### 6 M I a 

Additional platforms, such as Google Cloud's Alenhanced databases and Microsoft Azure's Al tools, also contribute to this landscape, offering similar automation and optimisation features. These tools aretypically deployed via cloud services, enabling organisations to adopt Pay-asyourgo model and scale’resources dynamically. The practical implementation of these platforms requires an understanding of cloud architecture and Al integration, equipping learners with skills to deploy and manage such systems effectively in diverse organisational contexts. 

It improves data availability, fault tolerance, and performance by distributing the workload. 

###### 1. Tools and Platforms 

- Blockchain Platforms 

- + Ethereum: A decentralised platform that supports smart contracts and decentralised applications (dApps). 

- a <i 

- . Byperleddel Fabric: A permissioned . blockchain framework ideal for enterprise 

- use cases with access control. 

* Corda: Focused on business use cases, particularly in the financial sector. 

5.1.3 Blockchain and Distributed Databases In addition to these, there are newBlockchain and distributed databases are and distributed databases are distributed databases are databases are are generation blockchains optimised for transforming the way information the way information way information information is stored, stored, shared, scalability and performance, like Polygon, and secured. These technologies offer secured. These technologies offer These technologies offer technologies offer offer Solana, and Avalanche. 

Blockchain and distributed databases are and distributed databases are distributed databases are databases are are transforming the way information the way information way information information is stored, stored, shared, and secured. These technologies offer secured. These technologies offer These technologies offer technologies offer offer decentralised, transparent, and fault-tolerant alternatives to traditional centralised database systems. As emerging trends, they are increasingly being adopted across industries such as finance, healthcare, supply chain, and digital identity management. 

###### Distributed Database Platforms 

- + Apache Cassandra: A highly scalable distributed NoSQL database suitable for real-time big data workloads. 

- + Amazon DynamoDB: A managed NoSQL database service known for its lowlatency and high availability. 



<!-- Start of picture text -->
Q / = (ey) ®_——© ’<br>@) ~_@)<br>@ Cee (Hl) By<br>> fi ©) @)-®<br>\7* BLOCK CHAIN ~~ D)_@<br>WG (6) =<br> @ @ ©<br>@ (co) 5)<br>© @) @)<br><!-- End of picture text -->

- CockroachDB: A<sup>distributedSQL</sup> database designed for global availability and strong consistency. 

- Google Spanner: A globally distributed relational database offering horizontal scaling and ACID compliance. 

###### ateohnidues aud lechnolodies 

###### 5.1.3.1 Understanding Blockchain and Distributed Databases 

Distributed Databases Consensus Algorithms are core to . . 7 blockchain, ensuring all participants agree on Blockchain is a specific type of distributed the state of the data. Common algorithms database that organises data in immutable blocks indueta, linked chronologically using cryptographic hashes. + Proof of Work (PoW): Used in Bitcoin; It operates on a peer-to-peer (P2P) network and ; ‘ uses consensus mechanisms (e.g., Proof of Work, energy-intensive but secure. Proof of Stake) to validate and agree on data + Proofof Stake (PoS) aMore cherays entries without a central authority. efficient, used In Ethereum 2.0. 

- + Byzantine Fault Tolerance (BFT): ee coue eve aed iu Pieeotce of malicious nodes (used in Hyperledger Fabric). 

A distributed database is a database in which data is stored across multiple physical locations, often across different servers or data centres. 

© Copyright 2025 MIVA Open University All Rights Reserved 

124 

###### Emerging Trends in Database Systems 

### 6 M I a 

Smart with termscontracts directly(self-executing contracts) written in code are a significant feature of blockchain, enabling automated transactions and business logic execution. 

Privacy-aware and compliant databases are gaining importance as regulations like GDPR, CCPA, and Nigeria's NDPR mandate stronger data governance. Emerging database systems are incorporating builtin support for data anonymisation, encryption, access control, and compliance tracking to protect user privacy and meet legal obligations. 

Sharding, replication, and partitioning are key techniques used in distributed databases to ensure scalability and fault tolerance. They scalability and fault tolerance. They and fault tolerance. They fault tolerance. They tolerance. They They allow data to be split or copied across nodes data to be split or copied across nodes to be split or copied across nodes be split or copied across nodes split or copied across nodes or copied across nodes copied across nodes across nodes nodes to improve access speed and reduce single improve access speed and reduce single access speed and reduce single speed and reduce single reduce single single points of failure. 



<!-- Start of picture text -->
ensure scalability and fault tolerance. They scalability and fault tolerance. They and fault tolerance. They fault tolerance. They tolerance. They They ii mag eri—ae—_ ae<br>allow data to be split or copied across nodes data to be split or copied across nodes to be split or copied across nodes be split or copied across nodes split or copied across nodes or copied across nodes copied across nodes across nodes nodes si ms rig bee “st ay sy 1% oe ‘ ‘<br>to improve access speed and reduce single improve access speed and reduce single access speed and reduce single speed and reduce single reduce single single nl re ALS Ke atl<br>points of failure. — “es od ii<br><.<br>3. Use Cases 5 at & ae<br>Blockchain ys —— .<br><!-- End of picture text -->

- + Finance and Banking: Secure, transparent transactions (eg., cryptocurrencies, cross-border 

Blockchain and distributed databases represent a shift toward decentralised, scalable, and secure data management. With growing concerns over ea ated Semcon. oie ced oo ae. ; gles are shaping the next generation o| resilient, intelligent, and interconnected systems. As tools and platforms evolve, their adoption will continue to expand across sectors demanding transparency, efficiency, and reliability. 

- payments). 

- + SupplyChain Management: Tracking product origins and movement with origins and movement with and movement with movement with with 

- product origins and movement with origins and movement with and movement with movement with with (aera 

- + Healthcare: Secure patient record sharing and drug traceability. 

- + Digital Identity: Self-sovereign identity systems with verifiable credentials. 

###### 5.1.4 Edge Databases 

###### Distributed Databases 

As digital applications move toward real-time responsiveness, the need for faster data processing closer to the source has led to the rise of edge databases. Edge databases represent a significant shift in database architecture, focusing on storing and processing data at the network edge closer to users, devices, or sensors rather than relying. solely on centralised cloud or data centre infrastructures. 

- + E-commerce: Handling millions of concurrent users and transactions globally. 

- Telecommunications: Real-time user data management and billing systems. 

- eachfrom systems.millions Vene0of connected: 10 disaidevices.F vate sate 

- Social Media Platforms: Supporting high availability and scalability of user content. 



<!-- Start of picture text -->
rai) 7<br>Ae<br>esas/ L \ eee<br>ie 2S<br>: Tr : said \<br>><br>=a) - Y = y<br>: G29 5779are 8 8 748ae8<br><!-- End of picture text -->

In terms of data integrity and transparency, blockchain-based databases are emerging. These systems store data in decentralised, immutable require auditability, such as supply chain tracking, digitalledgers,identity, making andthem financial ideal for transactions.applications that 

© Copyright 2025 MIVA Open University AllRights Reserved 

125 

Emerging Trends in Database Systems 

### G M I a 

Global Distribution: Support for multi-region data replication, enhancing fault tolerance and access speed 

Usage-based Billing: Charges are based on requests and compute usage, reducing costs for sporadic workloads. 

These features enable developers to build scalable, responsive applications with minimal operational overhead. 

###### 5.1.5.3. Use Cases 

Serverless databases are well-suited for a wide range of modern applications: 

(5 ay 

Web and Mobile Event-Driven PPE: (pda TEAC Inetelle , Reece nets ein hinreiaanit dieea<sup>itean</sup> efficiently without functions, enabling pre-provisioning real-time processing resources pipelines. 

BeA ayra Startups and MVPs E-commerce and Ideal for quick Marketing deployment and Platforms low-cost Scale easily during experimentation peak demand (e.g. without long-term holiday sales) and infrastructure contract afterward, commitments. ensuring cost efficiency. BR ate 

Serverless databases represent a paradigm shift in how data js Stored and managed In the cloud. BY eliminating server management, offering elastic scaling, and enabling cost-effective operations, they empower developers tobuild agile, scalable applications. As cloud adoption and microservices architecture continue to grow, serverless databases will become increasingly central to the _ future of data infrastructure. 

###### ITO52: 

Describe the key benefits and use cases of edge databases and serverless databases. 

ITA 5.1: 

Edge databases offer benefits such as processing byreduced latency storing and real-time and processing data data closer to the source, making them ideal for applications like loT devices, autonomous vehicles, and retail systems. They support offline functionality and synchronise data when connectivity is restored. Serverless databases, on the other hand, automatically scale based on demand, reducing the need for manual provisioning and offering cost efficiency by charging based on actual usage. 

loT and Edge Applications Combine with serverless functions to process and store data efficiently from distributed sources 

###### Emerging Trends in Database Systems 

# Ss) M | T 

###### Part B 

detection, recommendation systems, knowledge graphs, and network analysis. and network analysis. network analysis. analysis. 

G PH DATABASES graphs, and network analysis. and network analysis. network analysis. analysis. scalable, and relationship-centric approach to data relationship-centric approach to data approach to data to data data otal<sup>Databases and Knowledge</sup> Overall, graph databases provide a flexible, graph databases provide a flexible, databases provide a flexible, provide a flexible, a flexible, Inrecent years, graph databases and knowledge surede aie querying, ELSE aie querying, ELSE querying, ELSE ELSE RESSS graphs have emerged as powerful solutions in the interconnected digftal digftal env ronments. ronments. field of data management, offering novel approaches to handling complex, highly 5.2.1.2 Key Features of Graph Databases interconnected data. Traditional relational Graph databases are designed to handle highly databases, though highly effective for structured connected data with efficiency and flexibility. and tabular data, struggle with the increasing demand for dynamic relationships and flexible Schema flexibility schemas. Graph-based models address this gap by One of their standout features is schema flexibility, prioritising relationships and enabling intuitive data__@l!0wing developers to add or modify node and representation, thus supporting modern relationship types without rigid structural applications like recommendation engines, fraud constraints. This makes graph databases ideal for detection, semantic search, and Al-driven evolving data models and dynamic applications. analytics. 

scalable, and relationship-centric approach to data relationship-centric approach to data approach to data to data data Overall, graph databases provide a flexible, graph databases provide a flexible, databases provide a flexible, provide a flexible, a flexible, surede aie querying, ELSE aie querying, ELSE querying, ELSE ELSE RESSS interconnected digftal digftal env ronments. ronments. 

###### Fast traversal 

5.2.1.1 Understanding Graph Databases Graph databases are a specialised type of NoSQL database designed to represent and store data in graph structures, emphasising relationships between entities. Unlike traditional relational databases that use tables, graph databases use a model made up of nodes, edges, and properties. Nodes represent entities such as people, locations, events, or products. Edges (also called relationships) connect these nodes and describe how the entities are related—for example, "friend of "purchased' or “located in’: Each node or edge perhevonmearicste niche cermaltore SIRS ISCASALORS GES identifiers. 

Thisauucturaretocts recitworit watworteard allows for intuitive modeling of connected data. For instance, a social network, logistics system, or recommendation engine can be naturally and efficiently represented as a graph. 

One of the biggest advantages of graph databases is their ability to traverse relationships quickly and directly, making them ideal for complex queries involving multiple connections. This makes graph databases particularly useful in domains like fraud . 

PUNT key strength is fast traversal. Satthe relational SELEESES)that rely on costly joins, graph GELEWESES use direct pointers between connected entities (nodes), enabling rapid navigation across REESERE HPS SCN MableOi PO. WALES from cope Cally usetoliol eh tke shortest P path, recommendation engines, or fraud detection. 

: KeaROsenS ; 

KeaROsenS ; ebb catabeses Iso support pate storage of peauonstips: dapat) net leeches)ae WreRecee citizens rather than Saatig|TEE through foreign keys. This ensures efficient querying and storage of complex networks; such as social connections or cain ets 

Finally, their intuitive data modeling closely mirrors eai world entities ne ope interectops. Jat iS sired es odes (Sndites) and Sages - (relationships). making it easier to visualise and SESeIea that reflect eae ARIES or domain logic. This approach simplifies both ee ple ial cee a ig quitcell Tenstnar diese eawueemalon ees Celt ociuelhiedS uchnyceleu Mee lEIN se inten eee isl: UNI SEANCES commerce, and artificial intelligence. 

‘© Copyright 2025 MIVA Open University All Rights Reserved 

129 

Emerging Trends in Database Systems 

### 6 M I a 

###### 5.2.1.3 Knowledge Graphs: Semantic Layer 

###### Over Graphs 

A knowledge graph is a more enriched and semantic form of a graph database. Itembeds meaningintothe data by linking concepts through well-defined ontologies and vocabularies. Unlike plain graph databases, knowledge graphs include metadata, reasoning capabilities and often integrate data from multiple sources. 

###### Core Components of Knowledge Graphs 

Knowledge graphs are advanced graph-based data structures that enhance data with semantic context, enabling intelligent data integration and reasoning. They share foundational elements with graph databases, including entities (nodes) and relationships (edges), which represent real-world objects and the connections between them. 

###### + Ontologies 

Adistinguishing feature of knowledge graphs is the use of ontologies, which define the structure of the data through classes, properties, and rules. Ontologies provide a shared vocabulary and schema that enable consistent interpretation of data across systems and domains. 

###### + Inference engine 

Another critical component is the inference engine, which applies logical rules to the data, allowing systems to deduce new facts and relationships that are not explicitly stated. This supports advanced reasoning and automation in data analysis. Knowledge graphs also adhere to Linked Data principles, using URIs (Uniform Resource Identifiers) and RDF (Resource Description Framework) to publish and connect data across the web. This makes them interoperable and suitable for integration with external datasets. 

These components together make knowledge graphs powerful tools in Al and machine learning, where they enhance data understanding, support natural language processing, improve search relevance, and enable context-aware applications. They bridge structured and unstructured data, enabling machines to process information more like humans. 

###### 5.2.1.4. Tools and Technologies in Graph 

###### Databases and Knowledge Graphs 

Graph databases and knowledge graphs have gained traction across diverse sectors such as finance, healthcare, social media, and artificial intelligence. This growth has led to the emergence of arich ecosystem of tools, platforms, and query languages tailored for building and managing graph-based data solutions. These technologies are designed to enable efficient storage, traversal, reasoning, and querying of highly interconnected data. Below is an in-depth overview of the key tools and technologies that support the development and deployment of graph databases and knowledge graphs. 

###### A. Graph Database Platforms 

Graph database platforms are specialised databases designed to store, manage, and traverse graph data. These systems differ from traditional relational databases by treating relationships (edges) as primary components, enabling fast querying of connected data. 

###### NEO4J 

Neo4j is the most widely adopted opensource graph database platform. It uses the property graph model, where nodes and relationships can hold properties in the form of key-value pairs. Neo4j's defining feature is its proprietary query language, Cypher, which offers an intuitive, SQL-like syntax specifically designed for graph data. Neo4j is ideal for applications like fraud detection, recommendation engines, and social network analysis due to its robust support for complex graph traversal. Its ecosystem includes Neo4j Aura (a fully managed cloud service), integration with popular programming languages, and tools for data visualisation and analytics. 

© Copyright 2025 MIVA Open University AllRights Reserved 

130 

###### Emerging Trends in Database Systems 

yy AMAZON NEPTUNE Amazon Neptune is a fully managed graph database service provided by Amazon Web Services (AWS). It supports both the property graph and RDF (Resource Description Framework) models, enabling users to choose between Gremlin (for property graphs) and SPARQL (for RDF data) query languages. Neptune's architecture is built for high availability, durability, and scalability. It is commonly used in enterprise environments for building knowledge graphs, identity graphs, and fraud detection systems. Being a managed service, Neptune handles database administration tasks like backups, patching, and scaling. 

###### i ORIENTDB 

OrientDB is a multi-model database that : combines the features of graph databases with. those of document, key-value, and object-oriented models. This flexibility allows developers to model complex domains without switching technologies. OrientDB supports SOL-like queries with graph P POL ‘ CACHE ITEM ITE AIRES TON) developers with traditional database backgrounds. It’s especially useful for applications requiring multi-model data representation, such as complex CRM systems or data integration platforms. 

###### 04 

syneBIGERSnoe ; TigerGraph is an enterprise-grade graph GEESE galnlieeaiairetstg ins analytics and real-time graph processing. It is designed for performance at scale, capable of handling trillions of relationships and delivering sub-second query responses. 

### 6 M I a 

TigerGraph uses a powerful query language called GSQL and provides advanced analytics capabilities through built-in algorithms for community detection, shortest paths, and centrality. It is commonly applied in sectors like telecommunications, healthcare, and financial services where large-scale, real-time graph analysis is essential. 

###### 05 ARANGODB 

ArangoDB is another multi-mode! database supporting graph, document, and key-value data within a unified query engine. Its native query language, AQL (ArangoDB Query Language), supports graph traversals as well as document-style operations. ArangoDB provides a flexible and efficient way to handle heterogeneous acta ee ees ait ern mu erection an recommendation7 , systems to microservices and loT. 

Knowledge Graph Platforms Knowledge graph platforms extend graph ; databases with semantic technologies, reasoning engines, and standards-based data models such as RDF and OWL (Web Ontology Language). They are designed to encode domain knowledge, facilitate interoperability, and support Al-driven applications. 

###### STARDOG 

Stardog is an enterprise-grade knowledge graph platform that combines RDF triple stores with advanced reasoning capabilities and ontologybased data modeling. It supports SPARQL for queryingarrestorand includes which allows tools integration of for data data from disparate sources without moving them. Stardog is widely used in enterprise environments for data unification, metadata management, and Al workflows. Its support for inferencing enables the discovery of hidden relationships and enhances decision-making in complex domains. 

© Copyright 2025 MIVA Open University All Rights Reserved 

131 

LU 6 MMIVA OPEN UNIVERSITYI a 

###### Emerging Trends in Database Systems 

###### ONTOTEXT GRAPHDB 

RDF store. Used widely for publishing and querying Linked Open Data, Virtuoso powers major data hubs including DBpedia. . It supports advanced SPARQL features, federated queries, and web-scale data integration. 

GraphDB by Ontotext is a semantic graph database optimised for RDF data and SPARQL querying. It excels in handling large-scale linked data and provides support for inferencing and ontology management. It is commonly used in publishing, life sciences, and government sectors where semantic enrichment of dataand linked open data integration are important. GraphDB integrates well with text mining tools and supports faceted search and visualisation. 

###### GOOGLE KNOWLEDGE GRAPH 

The Google Knowledge Graph is not a 

commercial product but a large-scale internal system that powers Google Search. It connects billions of facts about people, places, and things, helping Google to deliver rich, contextual information in response to user queries. While _not directly accessible as a tool, directly accessible as a tool, Google's approach to building to building building its knowledge graph has inspired many organizations to build similar systems for semantic for semantic semantic search, virtual assistants, 

###### VIRTUOSO 

Virtuoso is a hybrid database that supports both _not directly accessible as a tool, directly accessible as a tool, graph and relational models. It can function as a approach to building to building building traditional RDBMS, a document store, anda inspired many organizations graph database. Virtuoso is especially known for systems for semantic for semantic semantic its robust SPARQL engine and high-performance —_ and Al applications. 

Query Languages for Graph and Knowledge Graphs 

Efficiently querying and analysing graph data requires specialised languages that support graph traversals, pattern matching, and semantic reasoning. 

###### Cypher 

Cypher is the declarative query language designed by Neo4j for querying property graphs. It uses a visually intuitive pattern-matching syntax that makes it easy to express graph . ee queries, such as finding shortest paths or i : ted ‘ iscovering connected components. 

Example: MATCH (a:Person)-[:FRIEND_OF]Me7 (b: Person)ge Le. SEEMISR! Wes Cypher's expressiveness and ease of use have F ; made it a widely adopted standard in the property graph community. 

Gremlin a P Gremlin is a graph traversal language used with Apache TinkerPop-compatible databases such as JanusGraph, Amazon Neptune, and OrientDB.; It ;is both a language and a virtual; machine,; supporting **i** mperative5 and functional: . programming styles. Gremlin allows users to describe‘1 than how to walk through the graph rather for complexjust what traversals data to return. and path-based This makes analytics. it ideal 

Example: g-.V().-has('name', q : "Alice').out('friend').values('name' ) 

Sonos SPARAQL (SPARQL Protocol and RDF Query IbaTeBEaENG TEST Terie we RUTREWET EN ETH guag See Na based knowledge- graphs. It is designed‘ to extract data from triple stores by matching graph patterns. SPARQL: Saassupports a wide: range of features ; including filters, optional patterns, and reasoning es! i . : capabilities when paired with OWLontologies. It is central to semantic web applications, linked data and ontolodicalreasonini PP . ; og 9: Example: ; SELECT ?friendName WHERE { Q ?person foaf:name "Alice" . ?person foaf:knows ?friend . ?friend foaf:name ?friendName . + 

© Copyright 2025 MIVA Open University AllRights Reserved 

132 

6 M I a DF tava ontw unuvensity 

###### Emerging Trends in Database Systems 

###### 5.2.1.6. Advantages of Graph-Based Approaches 

Graph-based approaches offer several advantages over traditional relational models, especially when dealing with highly connected data. 

High performance One of the most significant benefits is their high performance for relationship queries. Graph databases use direct pointers to traverse relationships, making operations like shortest path calculation or neighbourhood searches extremely fast and efficient—far superior to join-heavy queries in relational databases. 

###### 78 

Flexible data modeling d=: Q Anothermodeling. major Graphadv d **a** tabasesntage is do flexible not require data predefined schemas, allowing easy updates to data structures as new types of nodes or relationships emerge. This adaptability is ideal for dynamic domains like social networks, recommendation engines, and knowledge management systems. 

Em Realtime insights ; Graph databases also support real-time 8 insights. Since they don't rely on complex hi queries: canbe executed dynamically and efficiently, even with large and evolving datasets. This enables faster decision-making and immediate response to user queries or business events. 

sts 8 

Alintegration Finally, graph-based systems offer enhanced Al integration. By preserving the context and semantics of data through meaningful relationships, they support Al applications like natural language understanding, reasoning, and recommendation. Knowledge graphs, in particular, enrich machine learning models with domain-specific insights and improve interpretability, making graph technology acritical enabler in modern intelligent systems. 

\X oa 

###### 5.2.1.7. Challenges and Limitations of Graph-Based Approaches 

While graph databases and knowledge graphs offer powerful capabilities, they also come with several challenges and limitations. 

Scalability One major issue is scalability. Managing very large graphs—such as social networks or knowledge graphs with billions of nodes and edges—demands specialised storage systems and optimised algorithms to maintain performance. 

Standardisation . r Anotherrelational ch d **a** llengetabases,is standardisation. which are governed Unlike by established standards like SQL and ACID properties, graph technologies lack universally accepted frameworks. Different platforms use varied data models (e.g., property graph vs. RDF) and query languages (e.g., Cypher, SPARQL, Gremlin), leading to interoperability issues. The learning curve can also be steep. Developers and data analysts must learn new query languages and rethink how data is modeled, especially if they come froma relational background. This can slow adoption and increase training costs. 

m - para iptegration . vl Lastly, data integration posesa significant challenge. Building a comprehensive graph from multiple sources often requires extensive schema mapping, entity resolution, and data cleaning. Aligning concepts across heterogeneous datasets is complex but essential for ensuring accuracy and usability. Despite these hurdles, continued innovation in tools and standards is helping to address many of these limitations. 

© Copyright 2025 MIVA Open University AllRights Reserved 

134 

Emerging Trends in Database Systems 

LU 6 MMIVA OPEN UNIVERSITYI a 

###### 5.2.1.8. Future Directions of Graph Databases and Knowledge Graphs 

The future of graph databases and knowledge graphs is being shaped by the convergence of artificial intelligence (Al), big data, and semantic technologies, driving new capabilities and broader adoption. One emerging trend is the integration of Graph Neural Networks (GNNs), which apply deep learning to graph structures. GNNs enable predictive modeling based on node relationships, powering advanced applications like fraud detection, recommendation systems, and social network analysis. 

Another key direction is the development of hybrid systems, which combine graph databases with relational and document-based models. These systems offer greater flexibility by supporting diverse data types and enabling seamless interaction between different database paradigms. 

The rise of cloud-native graph services is also accelerating adoption. Providers like Amazon, Microsoft, and Google are offering fully managed graph databases that scale automatically and simplify deployment, making it easier for organisations to integrate graph technologies without heavy infrastructure costs. 

Finally, Explainable Al (XAl) is gaining traction, with knowledge graphs playing a central role. By embedding contextual and semantic relationships, knowledge graphs enhance Al transparency and interpretability, allowing users to understand how decisions are made. These advancements position graph technologies as essential tools in the next generation of intelligent, data-driven applications. 

EXPLAINABLE AI yt ¢a e eeN Nv i Qn —\. j ]]|| ee e e Explain Explain Explain Explain to Justify to Control to Discover to Improve 

Graph databases and knowledge graphs represent a significant shift in the way data is modeled, stored, and queried, especially for complex, highly connected systems. They offer intuitive data structures, fast relationship traversal, and semantic understanding—features increasingly essential in Al-driven applications. As tools and techniques mature, and as real-world use cases continue to expand; graph-based systems are likely to become integral to the next generation of intelligent data platforms. Organisations that invest in mastering these technologies stand to gain a competitive edge in deriving deeper insights and building smarter applications. 

© Copyright 2025 MIVA Open University AllRights Reserved 

135 

Emerging Trends in Database Systems 



<!-- Start of picture text -->
“<br>Ss) MIVAMOPEN IUNIVERSITY T<br><!-- End of picture text -->

J) 

### SUMMARY 

This session explores key emerging trends in database systems that are transforming how organisations store, manage, and analyse data in a rapidly evolving digital landscape. Al-powered databases, such as Oracle Autonomous DB, introduce automation by using machine learning to handle tasks like indexing, anomaly detection, and performance tuning—minimising human intervention and enhancing security. Blockchain databases and distributed ledgers offer decentralised and immutable records, vital for trust and transparency in sectors like finance, supply chain, and healthcare. Additionally, edge databases support real-time responsiveness by processing data closer to users and devices, while serverless databases eliminate the need for infrastructure management, enabling cost-effective, scalable solutions for dynamic workloads. 

Graph databases and knowledge graphs further expand the capabilities of data systems by focusing on relationships and semantic meaning. Graph models, used in tools like Neo4j and Amazon Neptune, efficiently represent interconnected data for applications like fraud detection and recommendation engines. Knowledge graphs enhance this with ontologies and inference engines, enabling Al-powered insights and context-aware systems. Despite challenges in scalability, standardisation, and data integration, these technologies are becoming essential for industries seeking real-time, intelligent data applications. The growing integration of graph neural networks, cloud-native services, and explainable Al highlights their role in the future of database innovation. 

J) 

#### CONCLUSION 

The shift towards intelligent, decentralised, and flexible database systems underscores the need for IT professionals to adapt to new architectures and tools. Mastery of Al integration, blockchain systems, edge computing, and graph-based data models equips organisations to meet the increasing demand for scalable, secure, and insight-driven applications. These emerging technologies are not merely enhancements—they represent the future foundation of intelligent data management. 

© Copyright 2025 MIVA Open University AllRights Reserved 

136 

STUDY SESSION STIX 

Introduction to Data Security and Data Privacy 

###### Introduction to Data Security and Data Privacy 

» J Ss) MIVAMOPEN UNIVERSITYI T 

In the digital age, data has become one of the most Cybercriminals are constantly developing constantly developing developing valuable assets for individuals, organisations, and sophisticated methods to exploit these to exploit these exploit these these governments. The vast amounts of information vulnerabilities, resulting in costly data generated, collected, and stored daily include personal, _ loss of consumer trust, loss of consumer trust, of consumer trust, consumer trust, trust, legal penalties, and and financial, health, and business data. As reliance on reputational damage damage for affected organisations. digital systems grows, so do the risks associated with data breaches, cyberattacks, and misuse of sensitive Furthermore, the ethical ethical implications of data of data data information. This underscores the critical importance of M 5 data security and data privacy, two interrelated yet handling are increasinglyi are increasinglyi increasinglyii underjj scrutiny. Questions, ; distinct concepts that form the foundation of trust in aroundreese surveillance,reese surveillance, surveillance, profiling, data ownership, ownership, Ee cicttal Seeeyeein algorithmic bias have raised bias have raised have raised raised public awareness and awareness and g v . concern about data about data data practices. Organisations are 

Cybercriminals are constantly developing constantly developing developing more sophisticated methods to exploit these to exploit these exploit these these vulnerabilities, resulting in costly data breaches, _ loss of consumer trust, loss of consumer trust, of consumer trust, consumer trust, trust, legal penalties, and and reputational damage damage for affected organisations. 

Furthermore, the ethical ethical implications of data of data data M 5 , handling are increasinglyi are increasinglyi increasinglyii underjj scrutiny. Questions, aroundreese surveillance,reese surveillance, surveillance, profiling, data ownership, ownership, and algorithmic bias have raised bias have raised have raised raised public awareness and awareness and concern about data about data data practices. Organisations are now expected not only to comply with legal requirements but also to adopt ethical approaches that respect user autonomy and promote transparency. 

Data privacy is concerned with how data is collected, used, shared, and stored, particularly personal and sensitive information. It focuses on individuals’ rightsto control their personal information and understand how organisations handle their data. Key principles of data privacy include transparency, informed consent, limitati ddata minimisation. Th anlites lofi ten an - e bbe lone _ abe Chae ih a ise fais eona TSQUIGRONS SUCIIES te Veneta pata Pretecuon Regulation (GDPR) in the European Union, the . California Consumer Privacy Act (CCPA), and others around the world. 

Inconclusion, data security and data privacy are f i essentialmanagement. compon Th **e** ynts are of necessaryresponsible to protectdata individuals’ rights, preserve trust, and ensure the reliable operation of digital systems. As digital 3 P transformationaes continuesane to accelerate, . organisations must prioritise robusté securityGs frameworks and transparent privacy policies to safeguard data in an ever-evolving threat landscape. 

KR oC i Seetegecececene ete, «Bh Weereenen Data protection GR 3, caeeracy | Whilexxx data; XK securityXXXis protectsXH dataxxx from5 externalxX xx threats, data privacy governs internal practices related to data use. For example, an organisation may have strong data security measures in place to prevent hacking9 but still violate Domesprivacy laws if it collects personal data without consent or uses it for unintended purposes. Therefore, both aspects must work together to ensure comprehensive data protection. 

Learning Outcomes When you have studied this session, you should be able to: 611 Explain Data Privacy 

- 6.2 State Principles and Laws of Data Privacy 

6.3 Discuss Nigeria Data Protection Act (NDPA) 2025 6.4 Analyse the challenges of ensuring data privacy 6.5iol Describeting thedat bestaypractices for Oe ee Dee DU eCy, 

Thewith significancethe ryrise of cloud of data computing, securityF mobile and privacy devices,has the grown Internet of Things (loT), and big data analytics. These technologies increase the complexity and scale of data environments, creating new vulnerabilities and challenges. 

© Copyright 2025 MIVA Open UniversityAllRights Reserved 

138 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Introduction to Data Security and Data Privacy 

###### Part A DATABAS E P RIVACYY: ISS U ES AN D FUTURE TRENDS 

6.1.1 Introduction to Data Privacy Data has become one of the most valuable resources because individuals, businesses, and governments rely heavily on it for informed decision-making, communication, commerce, and service delivery. As the collection, processing, and . . shalind 6l.date Become MolePelvasive, COnCems surrounding the privacy of personal and sensitive information have intensified. 

Data privacy is the concept that governs the proper handling, processing, storage, and usage of data—particularly personal data—in a way that respects individuals’ rights and maintains public trust 

This session introduces the concept of data privacy and discusses its importance, key principles, legal frameworks, challenges, and best practices. Data privacy refers to the right of individuals to control how their personal information is collected, used, and shared. Personal data includes any information that can identify an individual directly or indirectly—such as name, address, phone number, email, financial records, health information, and even online behaviour. 

The central goal of data privacy is to protect individuals from unauthorised access, misuse, and exploitation of their data. It also ensures transparency and accountability in how organisations handle user information. 

###### 6.1.1.1 .importance of Data Privacy{ 

In today’s digital world, the importance of data privacy has become greater than ever. With the increasing amount of personal information collected, stored, and shared by organisations, protecting this data is essential. Several factors explain why data privacy has gained such 

significance, including the protection of individual torights, comply the impact with laws, on and trust the and role reputation, of privacy the need practices in reducing security risks. ® 

Protection of Individual Rights At its core, data privacy is about safeguarding fundamental human rights. Every individual has theright to control their personal sldoneusistea are SMAI eet aed Privacy Beseree peas Sugiits to privacy, freedom of expression, and protection from discrimination are respected. 

Without strong privacy protections, individuals could be subjected to surveillance, identity theft, discrimination, or misuse of their personal information. In democratic societies, protecting privacy is closely tied to maintaining individual freedom and human dignity. 

© Trust and Reputation Trust is a vital component of any relationship between organisations and their customers. Consumers today are highly aware of how their data is collected and used. Organisations that demonstrate a 

commitment to protecting data privacy can build stronger relationships with their customers. 

When people feel that their information is safe, they are more willing to engage and SMEOCENE STR OGANS NEMS) GEMINI) violations can severely damage an organisation's reputation. A single data breach or privacy scandal can lead to widespread public outrage, loss of customer confidence, and long-term harm to the brand. Rebuilding trust after such incidents is often extremely difficult and costly. 

© Copyright 2025 MIVA Open University AllRights Reserved 

139 

###### Introduction to Data Security and Data Privacy 

03) Compliance with Laws The legal landscape regarding data privacy has become much stricter in recent years. Governments around the world have introduced comprehensive privacy laws to regulate the collection, processing, and storage of personal data. 

Examples include the General Data Protection Regulation (GDPR) in the European Union, the California Consumer Privacy Act (ccPA) inthe United States, and similar laws in many other countries. These jaws often impose heey lines and penalties for non-compliance. As a result, organisations are under strong legal obligations to implement privacy protections, obtain user consent, provide data access and deletion options, and report data breaches promptly. Failure to comply not only results in financial losses but can also invite lawsuits and regulatory scrutiny. 

###### 04) 

###### Security Risk Mitigation 

Good data privacy practices also contribute directly to overall cybersecurity. By limiting the amount of data collected, minimising how long data is stored, and restricting access to only necessary users, organisations can reduce the attack surface for cybercriminals. 

Privacy-focused data handling lowers the risk of breaches, leaks, and unauthorised access. Furthermore, even if a breach occurs, the damage is minimised when sensitive information is properly encrypted or anonymised. Thus, data privacy is not just about legal compliance or public relations—it [STOGEST INGEstrategy, SCHIST SSNY 

### 6 M I a 

continues to grow as digital technologies become In conclusion, the importance of data privacy more integrated into our lives. Protecting individual rights, building trust, complying with laws, and mitigating security risks all depend on strong data privacy practices. Organisations that prioritise privacy are better positioned to succeed in today’s data-driven world. 

###### 6.1.1.2 Core Principles of Data Policy 

Data privacy is governed by a set of core principles that guide how personal information should be handled. These principles are embedded in major global frameworks and regulations, such as the General Data Protection Regulation (GDPR) in A Europe, the California Consumer Privacy Act (COPA) in the United States, and others. They provide a foundation for organisations to manage personal data responsibly and ensure the rights of individuals are respected. The most common data privacy principles include transparency, consent, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, and accountability. 

TransparencyTransparencyrequires organisations to clearly inform individuals about how their personal data will be collected, used, shared, and stored. This principle emphasises the importance of openness, ensuring that individuals understand what happens to their data. Privacy notices and clear communication are essential tools for maintaining transparency. 

###### Consent 

Consent is a critical principle that ensures individuals have control over their personal data. Organisations must obtain informed and explicit consent from individuals before collecting or processing their data. Consent must be freely given, specific, informed, and unambiguous, with the option for individuals to withdraw it at any time. 

© Copyright 2025 MIVA Open University AllRights Reserved 

140 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Introduction to Data Security and Data Privacy 

###### Purpose Limitation 

Under the purpose limitation principle, data should be collected only for specified, legitimate purposes. Organisations are not allowed to use personal data for new or unrelated purposes without obtaining further consent from the individual. This ensures that data is not misused or repurposed beyond its original intent. 

###### Accountability 

Accountability requires organisations to take responsibility for complying with data privacy principles and to demonstrate their compliance. This involves maintaining documentation, conducting impact assessments, training staff, and being prepared to show regulators and 

individuals how privacy obligations are being met. 

###### Data Minimisation 

In summary, these core principles serve as the backbone of effective data privacy management. of effective data privacy management. effective data privacy management. data privacy management. privacy management. management. Organisations that adhere to transparency, that adhere to transparency, adhere to transparency, to transparency, consent, purpose limitation, data minimisation, minimisation, accuracy, storage limitation, integrity and confidentiality, and accountability not only comply with only comply with comply with with legal standards but also build also build build trust with their customers and their customers and customers and protect their reputations in an increasingly data-driven world. 

Data minimisation emphasises collecting onlythe — backbone of effective data privacy management. of effective data privacy management. effective data privacy management. data privacy management. privacy management. management. data necessary for the intended purpose. By Organisations that adhere to transparency, that adhere to transparency, adhere to transparency, to transparency, consent, limiting data collection to what is essential, purpose limitation, data minimisation, minimisation, accuracy, organisations reduce the risks associated with storage limitation, integrity and confidentiality, data breaches, misuse, or unnecessary exposure. accountability not only comply with only comply with comply with with legal standards It also helps in maintaining trust with individuals. but also build also build build trust with their customers and their customers and customers and 

###### Accuracy 

Maintaining the accuracy of personal data is a core obligation. Organisations must ensure that thesGate they holds covrece complcterand Up. to-date. Regular reviews and updates are necessary,to preventt.errors:thatcouldharm individuals or affect important decisions based on thelrintonpanon: 

###### 6.11.3 Global Data Protection Laws 

In response to the growing importance of data privacy, various countries around the world have developed comprehensive data protection laws. These laws are designed to safeguard individuals’ ser sonal information, impose strict responsibilities on organisations, and promote trust in digital services. Among the most influential and well-known data protection regulations are the General Data Protection Regulation (GDPR) of the European Union, the California Consumer Privacy Act (CCPA) of the United States, and India’s proposed Personal Data Protection Bill. 

###### Storage Limitation 

The storage limitation principle states that personal data should not be kept longer than necessary. Once the original purpose for which the data was collected has been fulfilled, the data should be securely deleted or anonymised unless there is a legal requirement to retain it. This reduces the risk of outdated or unnecessary data being compromised. 

Cates) General Data Protection GDPR | Regulation (GDPR) VY - European Union ce) | CaliforniaPrivacy Act Consumer (CCPA) ~ United States 

ThisIntegrity principle and Confidentialityfocuses on protecting personal data against unauthorised access, alteration, disclosure, or destruction. Organisations must implement strong security measures such as encryption, access controls, and regular security assessments to ensure the integrity and confidentiality of the data they handle. 

ce) 

PDPB | Protection Bill ~~ - India (Proposed) 

© Copyright 2025 MIVA Open University AllRights Reserved 

141 

Introduction to Data Security and Data Privacy 

### 6 M I a 

WY (GDPR) - European Union 

The GDPR, which came into effect in May 2018, is widely regarded as one of the most comprehensive and influential data protection laws globally. It aims to give individuals in the European Union (EU) significant control over their personal data. Under GDPR, individuals have rights such asthe right to access their data, the right to correct inaccuracies, the right to delete data ("right to be forgotten"), and the right to data portability. Organisations are required to obtain clear consent for data processing, implement strong data protection measures, and notify authorities of data breaches within 72 hours. GDPR also introduced strict penalties for non-compliance, with fines that can reach up to 4% of a company’s global annual revenue or €20 million, whichever is higher. Beyond Europe, GDPR has influenced data protection practices around the world, becoming a benchmark for privacy regulations. 

###### (cc) | CaliforniaAct (CCPA) Consumer- United States Privacy 

In the United States, the California Consumer Privacy Act (CCPA) represents a significant step toward strengthening consumer privacy rights. Enacted in 2018 and effective from January 2020, the CCPA grants California residents several important rights over their personal data. These rights include the ability to know what personal information a business collects, to request access to that Ties eln GEE Sits wscllsschny Ciche opt out of the sale of their data to third . . . parties. FE oraThe CCPATCS applies to businesses SIRE revenue, data collection,. or data sales. 

Although the CCPA is specific to California, its influence extends nationwide because many companies adjust their data practices across all U.S. operations to meet CCPA standards. The CCPA has paved the way for further privacy legislation in other States and at the federal level. 

###### th | Personal Data Protection soc UI ENN Greece) 

India, recognising the importance of protecting its citizens’ personal information, has proposed the Personal Data Protection Bill. Although itis still under consideration, this bill is expected to bring significant changes once enacted. Modeled in part on GDPR, the bill aims to regulate the collection, processing, and storage of personal data by both government and private entities. Key provisions include the requirement for organisations to obtain consent before processing data, obligations to ensure data security, and rights for individuals to access and correct their personal creationinformati **o** fn. a The Data bill Protection also proposes Authority the of India to oversee enforcement and ensure accountability. Once passed, this law will have a major impact on how businesses operate in India and handle personal data. 

In conclusion, global data protection laws such as the GDPR, CCPA, and India’s proposed Personal Data Protection Bill highlight the growing international focus on safeguarding privacy. 

These regulations not only protect individual rights - see but also set high standards for organisational accountability,F transparency, and data securityob in the digital age. 

© Copyright 2025 MIVA Open University AllRights Reserved 

142 

Introduction to Data Security and Data Privacy 

4 Ss) M | T 

Parta B 

b. The right to correct or delete data c. The right to data portability The right to data portability right to data portability to data portability data portability portability d. The rightBiel to object to The rightBiel to object to rightBiel to object toBiel to object to to object to object to to ekprocessiniprocessini ‘i 

DATA P R I VAC Y: c. The right to data portability The right to data portability right to data portability to data portability data portability portability CHALLENGES, BEST d. The rightBiel to object to The rightBiel to object to rightBiel to object toBiel to object to to object to object to to ekprocessiniprocessini ‘i PRACTICES, AND LEGAL Con PLIANCE 4. Data Security Obligations Organisations are required to implement 6.2.1 Nigeria Data Protection Data Protection Protection Law appropriate technical and organisational Nigeria’s primary legal framework legal framework framework for data data (NEESLE SHO SSE ASC AGELEN ETE protection is the Nigeria Data Protection Act the Nigeria Data Protection Act Nigeria Data Protection Act Data Protection Act Protection Act Act (IR BSASSSIRSESSS HSS GEILE 

6.2.1 Nigeria Data Protection Data Protection Protection Law Nigeria’s primary legal framework legal framework framework for data data protection is the Nigeria Data Protection Act the Nigeria Data Protection Act Nigeria Data Protection Act Data Protection Act Protection Act Act (NDPA) 2023, which builds upon earlier regulations plonesafeguardingguarengelishOSpersonalmprehensive I data.. SeregimeThe forreplacesP q th the Nigeria Data Protection Regulation (NDPR) 2019 and aligns Nigeria's data protection standards more closely with global frameworks like the EU’s GDPR 

5. Cross-Border Data Transfer: Personal data can only be transferred outside Nigeria where adequate data protection is ensured, or with data subject ‘ consent and appropriate safeguards. 



<!-- Start of picture text -->
Asm<br>5 (f| a 6.DataData controllers Breach  mustNotification: notify the NDPC and<br>. vs affected individuals of data breaches that<br>pose significant risks to rights and freedoms.<br>GeneralProtection RegulationData protection RegulationNigerian Data 7. Data Protection Officers+  (DPOs)=<br>Certain organisations are mandated to<br>Key Features of the Nigeria Data Protection Act Features of the Nigeria Data Protection Act of the Nigeria Data Protection Act the Nigeria Data Protection Act Nigeria Data Protection Act Data Protection Act Protection Act Act eppolhta DEO to oversee compliatice efforts<br><!-- End of picture text -->

Key Features of the Nigeria Data Protection Act Features of the Nigeria Data Protection Act of the Nigeria Data Protection Act the Nigeria Data Protection Act Nigeria Data Protection Act Data Protection Act Protection Act Act (NDPA) 2023: 1. Creation of a Regulatory Body The Act establishes the Nigeria Data Protection Commission (NDPC) to oversee compliance, issue guidelines, and enforce penalties for breaches. 

6. Sanctions and Penalties The NDPChas the authority to impose fines and penalties for non-compliance, which may include substantial financial penalties depending on the severity of the breach 

> 2. Legal Basis for Data Processing: Data controllers must have a lawful basis for contractualprocessing personalnecessity,data,legalincludingobligations, consent,and legitimate interests. 



<!-- Start of picture text -->
Data Cyber<br>protection security<br>ogeeres,<br><!-- End of picture text -->

The NDPA 2023 marks a significant advancement in 3. Data Subject Rights: Nigeria's data protection landscape. It emphasises Individuals are granted rights such as: transparency, accountability, and the protection of a. The right to access their data Organisationsindividual rights operatingin the handlingin Nigeriaof personal must ensure data compliance to avoid sanctions and maintain public 2025 MIVA Open UniversityAllRights Reserved UniversityAllRights ReservedAllRights Reserved Reserved Hist 

© Copyright 2025 MIVA Open UniversityAllRights Reserved UniversityAllRights ReservedAllRights Reserved Reserved 

143 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### Introduction to Data Security and Data Privacy 

###### 6.2.2 Challenges of Ensuring Data Privacy 

Despite increasing awareness and stronger legal frameworks, ensuring data privacy remains acomplex challenge for organisations and individuals alike. Several factors contribute to the difficulty in safeguarding personal information in today’s digital world, including rapid technological advances, the widespread proliferation of data, cross-border data flow complications, low user awareness, and the constant tension between personalisation and privacy. 

6.2.2.1 Rapid* Technologicals Advances Emerging technologies such as artificial intelligence (Al), big data analytics, and the Internet of Things (loT) have transformed how data is generated and used. These technologies continuously produce vast amounts of personal data, often in real-time and across various platforms. The speed and volume of data creation outpace traditional privacy protection methods. As new applications and services emerge, Privacy frameworks struggle to keep up, making ‘ challenging to ensure that personal information is pended app opriately.and securely 

###### 6.2.2.2 Data Proliferation 

Today, data is stored not just within corporate databases but across numerous systems, personal devices, and cloud-based services. This widespread distribution of data—known as data proliferation— makes it significantly harder to control, monitor, and protect personal information. Data may be duplicated, transferred, or shared among multiple parties, increasing the risk of unauthorised access, data breaches, and loss of control over sensitive information. 

###### 6.2.2.3 Cross-Border Data Flows 

Globalisation has led to the seamless movement of data across national borders. However, privacy regulations differ from one jurisdiction to another. ati a ! Organisations operating internationally must comply with multiple and sometimes conflicting privacy laws. For example, the strict requirements of the European Union's GDPR might clash with more lenient laws elsewhere. 

‘Navigating these complex regulatory environments adds legal and operational burdens to businesses 4nd creates uncertainty about how data should be managed to meet all obligations. 

###### 6.2.2.4 User Awareness 

| Binalol chal ence brosecrig deta privacy [Sine General las ofaWals bese ai ong Usetsy any | individuals do not fully understand now their data is collected, used, or shared by companies and online services. They often agree to lengthy privacy pc **o** liciesnsent without questionable. readingoethem, lack making of rialinformed makes it difficult for users to protect themselves and for organisations to claim that they have obtained truly informed consent for data processing activities. 

###### 6.2.2.5 Balancing Personalisation and Privacy 

Modern businesses strive to personalise their services to enhance customer experience, relying heavily on user data to do so. Personalised recommendations, targeted advertising, and customised services are all built upon analysing user behaviour and preferences. However, this use of personal data can conflict with privacy expectations. Users may enjoy the benefits of personalisation but may not be comfortable with the amount of personal data collected to enable it. Striking a balance between providing personalised experiences and respecting user privacy is a difficult but essential task for organisations. 



<!-- Start of picture text -->
We Ls<br>BS os S % — , =<br>ros NS ry * Se =<br>> ~ ~*- = a? es<br>= “ ——<br>— _ , Re<br>so -.4 os ae<br>aa 7 4 oo i<br>f =<br><!-- End of picture text -->

© Copyright 2025 MIVA Open University AllRights Reserved 

144 

LU 6 **M** IVA OPEN UNIVERSITYI a 

###### Introduction to Data Security and Data Privacy 

ITQ 21: How doesa well-defined IT strategy contribute to strategic innovation, operational efficiency, customer satisfaction, risk management, and agility in businesses? 

ITA21 Awell-defined IT strategy drives strategic innovation by enabling rapid product development and service launch, improves operational efficiency through process automation and system integration, enhances customer satisfaction by ensuring seamless digital experiences, manages risk and regu Ene)I ceempliance Dsthr:rough) integr:Wels security and data protection, and boosts a . . agility by adopting scalable, flexible systems - . that allow quick adaptation to changes. 

6.2.3 Best Practices for Implementing Data Privacy Ensuring strong data privacy is no longer optional for organisations; it is a crucial requirement for building trust, maintaining compliance, and protecting individual rights. To implement effective dataprivacy strategies, organisations must follow recognised best practices: that proactively safeguard personal . Z a information. These practices include Privacy by . . Design and Default, conducting Data Protection Impact Assessments (DPIAs), enforcing. strong access controls, promoting; user education,; rformi f dit King dat Perrerming FeQuianeucitsipPying cata anonymisation techniques, and maintaining transparent privacy. policies._ 

6.2.3.2 Data Protection Impact Assessments (DPIA | ( ) | Before launching new: projects ot processing activities that involve personal data, organisations should conduct Data Protection Impact Assessments. A DPIA helps identify and mitigate privacy risks early in the project lifecycle. It involves evaluating how personal data is collected, processed, and stored, and assessing potential impacts on individual privacy. DPIAs are particularly important when introducing new technologies or large-scale data initiatives. 

###### 6.2.3.3 Strong Access Controls 

Implementing robust access controls is vital to ae ; i protect sensitive information from unauthorised ; ani, access. OrganisationsFo ‘ should follow the principle of least privilege, granting access to personal data only to employees who need it for their job roles. Multi-factor authentication, role-based access control (RBAC), and encryption can further enhance security and limit exposure to privacy breaches. 

###### 6 2.3.4 User Education and Awareness 

‘ , Employees2 play a critical‘nil role in data privacy protection. Organisations should provide regular training to ensure that staff members understand . i A i privacy regulations,oy internal: policies, and their responsibilities.: ‘ In addition, educating‘ users about theirempowers them data rights and to make safe informed online practices decisions about , _ ; sharing their information. 

###### 6.2.3.1 Privacy by Design and Default 

###### 6.2.3.5 Regular Audits and Reviews 

Privacy by Design and Default is a principle that calls Periodic privacy audits and reviews are essential to for integrating privacy measures into the ensure ongoing compliance with privacy laws and development of products, systems, and services from _ internal policies. Audits help organisations identify the very beginning, rather than treating privacyasan —_weaknesses, verify that privacy measures are being afterthought. This means designing systems that followed, and assess the effectiveness of data minimise data collection, limit access, and ensure protection strategies. Regular reviews also help data security by default. Features such as minimal organisations stay updated with changes in privacy data collection, secure data storage, and clear user regulations and technology. consent options should be built into the system's architecture. 

© Copyright 2025 MIVA Open University AllRights Reserved 

145 

Introduction to Data Security and Data Privacy 

UL 6 **M** IVA OPEN UNIVERSITYI a 

###### 6.2.3.6 Data Anonymisation and Masking 

One effective way to reduce privacy risks is by anonymising or masking personal data. Anonymisation involves removing identifiable information so that individuals cannot be reidentified, while data masking replaces sensitive data with fictional yet realistic data. These techniques are particularly useful when using data for testing, analysis, or sharing with third parties 

###### 6.2.3.7 Transparent Privacy Policies 

; 7 Clear and transparent privacy policies:are critical bet maintaining user trust. Organisations should provide easily Understandable information @bout how personal ee iscollected, used, stored, and shared. Privacy policies should also explain users’ rights and how:they.canexercise. hose nights:sucn as; Pequesting access to or deletion oftheir dats. 

© Copyright 2025 MIVA Open University AllRights Reserved 

In conclusion, adopting these best practices enables organisations to embed data privacy into their culture and operations. A proactive, transpeleiih and comprepapsiveepprosc ct only, protects ries but also)strenginens the organisation sreputationandresilienceagalnst regulatory risks and data breaches. 

Data privacy is no longer a peripheral concern but a central issue in the digital era. With increasing data collection and usage, safeguarding personal information is essential for protecting individual rights, maintaining public trust, and ensuring legal compliance. Effective data privacy requires a combination of legal frameworks, technological safeguards, ethical practices, and user awareness. As data continues to power modern life, upholding privacy will remain a key challenge and priority for individuals, businesses, and governments alike. 



<!-- Start of picture text -->
146<br><!-- End of picture text -->

Introduction to Data Security and Data Privacy 

“ Ss) MIVAMOPEN IUNIVERSITY T 

1) 

### SUMMARY 

In today's digital environment, databases are critical repositories for sensitive information, making database security essential. Database security involves protecting data from unauthorised access, breaches, misuse, and corruption. Its key objectives align with the CIA triad: ensuring confidentiality, integrity, and availability of data. Common threats include unauthorised access, SQL injection, malware, and privilege abuse. Essential components of database security include authentication, access control, encryption, auditing, backups, and firewalls. Best practices emphasise strong passwords, least privilege access, patching vulnerabilities, encryption, and regular audits. However, challenges like managing complex environments, insider threats, and compliance requirements persist. 

Data privacy focuses on protecting individuals’ rights over their personal information, ensuring data is collected, processed, and shared responsibly. It has become crucial due to growing data reliance, regulatory pressures, and public expectations. Key principles of data privacy include transparency, consent, purpose limitation, data minimisation, and accountability. Global laws like the GDPR (EU), CCPA (US), and HIPAA enforce privacy standards. Challenges include rapid tech advancements, cross-border data flows, and low user awareness. Organisations can strengthen data privacy through practices like Privacy by design, conducting impact assessments, strong access controls, user education, and clear Privacy policies. 

In Nigeria, the Nigeria Data Protection Act (NDPA) 2023 establishes a comprehensive legal framework for data protection, replacing the older NDPR. It creates the Nigeria Data Protection Commission (NDPC) to regulate compliance and enforce individuals’ rights such as data access, correction, and objection. The NDPA mandates strong data security, cross-border data transfer safeguards, breach notifications, and the appointment of Data Protection Officers (DPOs) for certain organisations. It aligns Nigeria's standards with global practices like GDPR and highlights transparency, accountability, and enforcement through significant penalties for violations. 

Together, database security, data privacy, and strong legal frameworks like Nigeria's NDPA 2023 form the foundation for safeguarding information and maintaining public trust in the digital age. 

1) 

#### CONCLUSION 

In today's interconnected digital environment, both database security and data privacy are essential pillars of a robust information system. While database security focuses on safeguarding data from unauthorised access and ensuring its confidentiality, integrity, and availability, data privacy emphasises the ethical and legal handling of personal information in a way that respects individual rights. Together, they form a comprehensive approach to protecting digital assets and user trust. The Nigeria Data Protection Act (NDPA) 2023 further reinforces these principles by providing a strong legal framework that aligns with global standards, mandating accountability and security in personal data processing. As threats and data usage continue to evolve, organisations must adopt layered security measures, uphold privacy principles, and comply with regulations to protect both data and people effectively. 

© Copyright 2025 MIVA Open University AllRights Reserved 

147 

Introduction to Data Security and Data Privacy 



<!-- Start of picture text -->
Ss) M I T<br><!-- End of picture text -->

Ajayi, O. (2023). Understanding Nigeria's Data Protection Act 2023. Lagos: Digital Rights Hub Press. 

Amazon Web Services (2023). AWS Database Services Overview. Retrieved from https://aws.amazon.com/ 

Atzeni, P., Ceri, S., Paraboschi, S., & Torlone, R. (2011). Database systems: Concepts, languages and architectures (2nd ed.). McGraw-Hill Education. 

Brewer, E. A. (2012). CAP Twelve Years Later: How the “Rules” Have Changed. Computer, 45(2), 23-29. https://doi.org/10.1109/MC.2012.37 

California Legislative Information. (2018). California Consumer Privacy Act (CCPA). State of California. Retrieved from https://leginfo.legislature.ca.gov 

Cattell, R. (2011). Scalable SQL and NoSQL data stores. ACM SIGMOD Record, 39(4), 12-27. https:// doi.org/10.1145/1978915.1978919 

Chandramouli, B., Goldstein, J., & Krishnan, S. (2020). Trillions and Trillions: Engineering SQL Engines for Big Data and Al Workloads. Communications of the ACM, 63(2), 72-81. https://doi.org/10.1145/3374179 

Cooper, B., Ramakrishnan, R., Srivastava, U., Silberstein, A., Bohannon, P., Jacobsen, H.-A., ... & Puz, N. (2008). PNUTS: Yahoo!'s hosted data serving platform. Proceedings of the VLDB Endowment, 1(2), 12771288. https://doi.org/10.14778/14541591454167 

Cramer, B. (2018). Al-Driven Databases: The Next Frontier in Data Management. O'Reilly Media. Retrieved from https://www.oreilly.com/library/view/ai-driven-databases/ 

Date, C. J. (2019). An Introduction to Database Systems (8th ed.). Addison-Wesley. 

Domingos, P. (2015). The master algorithm: How the quest for the ultimate learning machine will remake our world. Basic Books. 

Elmasri, R., & Navathe, S. B. (2015). Fundamentals of database systems (7th ed.). Pearson. 

Elmasri, R., & Navathe, S. B. (2016). Fundamentals of Database Systems (7th ed.). Pearson. 

Elmasri, R., & Navathe, S. B. (2021). Fundamentals of database systems (7th ed.). Pearson. 

European Union. (2016). General Data Protection Regulation (GDPR). Official Journal of the European Union. Retrieved from https://eur-lex.europa.eu/eli/reg/2016/679/0} 

Gartner. (2021). Hype Cycle forArtificial Intelligence, 2021. Retrieved from https://www.gartner.com/en/ documents 

Grolinger, K., Higashino, W. A., Tiwari, A., & Capretz, M. A. M. (2013). Data management in cloud environments: NoSQL and NewSQL data stores. Journal of Cloud Computing: Advances, Systems and Applications, 2(1), 1-24. https://doi.org/10.1186/2192-113X-2-22 

Hardy, S. (2021). Blockchain for everyone: A practical guide to the revolution. Apress. https:// doi.org/10.1007/978-1-4842-6101-9 

© Copyright 2025 MIVA Open University AllRights Reserved 

147 

Introduction to Data Security and Data Privacy 

# Ss) M I T 

Hecht, R., & Jablonski, S. (2011). NoSQL evaluation: A use case oriented survey. In Proceedings of the International Conference on Cloud and Service Computing (CSC) (pp. 336-341). IEEE. https:// doi.org/10.1109/CSC.2011.6138544 

Inmon, W.H., Strauss, D., & Neushloss, G. (2008). DW 2.0: The Architecture for the Next Generation of Data Warehousing. Morgan Kaufmann. 

Katal, A., Wazid, M., & Goudar, R. H. (2013). Big data: Issues, challenges, tools and good practices. 2013 Sixth International Conference on Contemporary Computing (IC3), 404-409. https://doi.org/10.1109/ 1C3.2013.6612229 

Kumar, V., & Chadha, A. (2011). An empirical study of temporal databases. International Journal of Computer Applications, 15(5), 15-21. https://doi.org/10.5120/1921-2609 

Kuner, C. (2020). Transborder data flows and data privacy law. Oxford University Press. 

Leavitt, N. (2010). Will NoSQL databases live up to their promise? IEEE Computer, 43(2), 12-14. https:// doi.org/10.1109/MC.2010.58 

McKeen, J. D., & Smith, H. A. (2019). IT strategy & innovation (4th ed.). Prospect Press. 

Microsoft Azure. (2023). Azure database security documentation. Retrieved from https:// docs.microsoft.com/en-us/azure/security/ 

Microsoft. (2023). What is DevOps?. https://learn.microsoft.com/en-us/devops/what-is-devops 

Miller, R. L. (2020). Graph databases: Introduction and applications with Neo4j. Springer. https:// doi.org/10.1007/978-1-4842-6005-0 

Moniruzzaman, A. B. M., & Hossain, S. A. (2013). NoSQL database: New era of databases for big data analytics—classification, characteristics and comparison. International Journal of Database Theory and Application, 6(4), 1-14. https://doi.org/10.14257/ijdta.2013.6.4.01 

National Institute of Standards and Technology (NIST). (2020). Framework for Improving Critical Infrastructure Cybersecurity (Version 11). U.S. Department of Commerce. https://doi.org/10.6028/ NIST.CSWP.04162018 

Nigeria Data Protection Commission. (2023). Nigeria Data Protection Act (NDPA). Abuja: NDPC. Retrieved from https://ndpc.gov.ng 

Oracle Corporation. (2023). Oracle database concepts: Query optimization and performance tuning. https://docs.oracle.com/en/database/oracle/oracle-database/23/tgdba/index.html 

Ozsu, M. T., & Valduriez, P. (2020). Principles of distributed database systems (4th ed.). Springer. https:// doi.org/10.1007/978-3-030-26253-2 

Pearlson, K. E., Saunders, C. S., & Galletta, D. F. (2019). Managing and using information systems: A strategic approach (7th ed.). Wiley. 

PostgreSQL Global Development Group. (2024). PostgreSQL 16 documentation: Query planning and optimization. https://www.postgresql.org/docs/16/query-planning.html| 

© Copyright 2025 MIVA Open University AllRights Reserved 

147 

Introduction to Data Security and Data Privacy 

# Ss) M I T 

Puthal, D., Malik, N., Mohanty, S. P., Kougianos, E., & Yang, C. (2018). The blockchain as a decentralised security framework. IEEE Consumer Electronics Magazine, 7(2), 18-21. https://doi.org/10.1109/ MCE.2017.2778306 

Rouse, M. (2023). Database security best practices. TechTarget. Retrieved from https:// searchsecurity.techtarget.com 

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). Database system concepts (7th ed.). McGraw-Hill Education. 

Stonebraker, M., & Cattell, R. (2011). 10 rules for scalable performance in ‘simple operation’ datastores. Communications of the ACM, 54(6), 72-80. https://doi.org/10.1145/19531221953144 

Stonebraker, M., & Cetintemel, U. (2005). "One size fits all?” An evaluation of the emerging new database revolution. Proceedings of the VLDB Endowment, 2(2), 1288-1299. https:// doi.org/10.14778/16876271687753 

Turban, E., Pollard, C., & Wood, G. R. (2018). Information technology for management: On-demand strategies for performance, growth, and sustainability (11th ed.). Wiley. 

Zhou, B., & Liu, F. (2021). Data privacy and trust in cloud computing. Springer. 

Zikopoulos, P, Eaton, C., DeRoos, D., Deutsch, T., & Lapis, G. (2012). Understanding big data: Analytics for enterprise class Hadoop and streaming data. McGraw-Hill Osborne Media. 

© Copyright 2025 MIVA Open University AllRights Reserved 

147 




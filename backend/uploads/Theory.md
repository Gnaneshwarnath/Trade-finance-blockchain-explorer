#  					DBMS





database is a collection of related data



dbms - database management system is a software or application which is used to organize and control database efficiently



er  - entitiy relationship diagram which is used for the visual representation of the structure of database and mainly used to demonstrate blueprint of the database structure



entity -  entity is a real world object about which we store data

entity set  - it is a collection of same type of entities

 	strong entity set - having sufficient entities

 	weak entity set - having low or no entities



relationship - connection between 2 or more entities



schema - logical structure  or representation of db (types )

##  																sorting and searching

cardinality constraint - no.of connections between the entities

 	- one - one

 	- one - many

 	- many - one

 	- many - many



attributes - properties owned by entities in entity set

 	simple - attribute cannot be divided further

 	composite - division of attribute contain simple attributes

 	complex - multiple division of attributes contain multiple attributes



constraint - restrictions or limitations imposed on database contents

 	domain constraint - specific value is assigned for the type of column

 	tuple uniqueness constraint - every tuple or row need to be unique in the table

 	key constraint - primary key need to be available to the table without having null val

 	referential integrity constraint - it specify the data need to be matched with other table by primary key or null val



closure of an attribute set - all the attributes that are in or derived from the attribute set



key - it is set of attributes that identify each tuple need to be unique

 	super key - it is a set of attributes that which it can identify every unique tuple

 	primary key - unique value in a column that defines unique tuple and no duplicates and not null

 	foreign key - it is key where connection of two tables with a reference as primary key in one of the table related with same data

 

decomposition - division of single relation into two or more relations



normalization - process of making database consistent by reducing data redundancy and ensuring integrity of the data without loss

 	1 NF - atomicity ( every attribute in the table need to be unique or null in a tuple )

 	2 NF - 1 NF + no partial dependency

 	3 NF - 2 NF + no transitive dependency

 	boycee-codd NF - 3NF + no internal dependency



transaction - a set of operations performing as a single unit



operations in transactions : R - read ( view )

 			     W - write ( update )



transaction states : Active state - it is the fisrt state of transaction cycle and it will be active until the instructions are followed

 		     commited state - all the opearations are successfully excecuted

 		     failed state - if one of the operations is failed then it is considered as a failed state

 		     aborted state - if a transaction is failed then it enter into aborted state which it will stop all the process and stop excecution

 		     terminated state - it is a state that which it enter after the commited state



ACID properties : atomicity - in a transaction it need to either complete all the operations or none of the operations, no partial transaction is allowed

 		  consistency - transaction need to be in any one of the valid state, no rules and constraints need to be broken

 		  isolation - no other transactions need to communicate or interfere with each other

 		  duarbility - if one transaction is in commited state then it need to be permanent even if the system crashes



schedules - order of operations of multiple transactions for execution

 

 	types - serial

 		non-serial



serial schedules - need to executed sequentially one after another

non-serial scedules - opeartions of multiple transactions executed concurrently



serializability - Ensures concurrent execution of transactions produces the same result as some serial execution.

 

 	types - Conflict Serializability - Transactions are serializable if all conflicting operations (read/write on same data by different transactions) are reordered without changing the outcome.

 		View Serializability - Transactions are serializable if the final database state and read values are the same as some serial schedule.



Concurrency Control Techniques :

 

 		1.Locking



 			Transactions lock data to prevent conflicts.



 			Types of Locks:



 				Shared Lock (S-lock) → For reading, multiple transactions can hold S-locks.



 				Exclusive Lock (X-lock) → For writing, only one transaction can hold X-lock; prevents others from reading/writing.



 		2.Two-Phase Locking (2PL)



 			Ensures conflict serializability.



 			Phases:



 				Growing Phase: Transaction acquires all required locks, cannot release any.



 				Shrinking Phase: Transaction releases locks, cannot acquire new locks.



 				Guarantees serializability but may cause deadlocks.





 		3.Time-Stamp Ordering



 				Assign unique timestamps to each transaction.

 

 				Transactions are executed based on timestamp order to prevent conflicts.



 				Ensures serializability without locking.



Deadlocks - A situation where two or more transactions wait indefinitely for resources locked by each other



indexing - technique used to improve data retrival from database

 

 	types - primary index - created on basis of primary key, unique and automatically ordered

 		secondary index - created on non-primary keys columns

 		clusterd index - physically rearranges the tables data, only one clustered index per table



B tree - B-Tree is a special tree data structure used in databases and file systems to store data in a sorted way and allow fast searching, inserting, and deleting.











#  															SQL









DDl - data defination language



 	used to define or to manage structure of database - create alter drop truncate rename

 

DML - data manipulation language

 

 	used for manipualtion of data in database - select insert update delete merge



DQl - data query language

 

 	used to retrive data from database - select

 

DCl - data control language

 

 	used to contol authority and access - grant revoke



Tcl - transaction control language

 

 	used to control transactions - commit rollback

 







#  					OS



os - os stands for operating system is an interface between the user and the hardware that manages system resources and allows programs to run efficiently.





types of os - batch os - set of similar jobs stored in memory for execution, a job is assigned to cpu only when the execution of previous job completes

 	      multiprogramming os - main memory consists of jobs in queue so, if a process executing and waited for some time for any resourse etc. then, os selects the next task in job queue and assigns to cpu

 	      multitasking os - combination of multiprogramming os and cpu scheduling to perform quick switches between jobs, The switch is so quick that the user can interact with each program as it runs.



process - a program under execution, each process is represented by a pcb (process control block)



process scheduling - arrival time

 		   - burst time

 		   - completion time

 		   - turn around time - completion time - arrival time

 		   - waiting time - TAT - burst time



thread - thread is a light weight process and forms basic unit of cpu utilization, a process can perform one or more task at same time, including multiple threads, a thread has its own program counter, register set, and stack and shares resources with other threads of the same process



scheduling algorithms - FCFS - First come first serve

 			SJF - shortest job first

 			SRTF - shortest remaing time first

 			LRTF - longest remaining time first

 			RR - Round robin

 			PQ - priority queue



critical condition - The Critical Section Problem is the challenge of designing a protocol so that processes can cooperate, share resources safely, and avoid race conditions, while satisfying certain correctness conditions.



 	critical section - The critical section is the part of a program where shared variables or resources are accessed or modified. Only one process or thread should execute in the critical section at a time.

 	remainder section - The remainder section is the part of the program outside the critical section.It does not access shared resources, so multiple processes can execute it simultaneously.

 	race condition - Two or more processes access shared data at the same time, and final result depends on the order of execution.

 



solution for critical condition :

 

 	mutual exclusion - if a process p1 is under critical section then, no other process need to enter criticla section

 	progress - if no process is in critical section, then the decision who enter next can't be delayed indefinitely

 	bounded waiting - a process can't wait forever to enter critical section





synchronization - used to co-ordinate multiple process or threads so they can share resources safely without conflicts



synchronization tools -- Mutual exclusion lock(mutex) - only one thread need to access critical section at a time and others must wait

 		      -- semaphores - it is a protected variable that used to lock the resource being used

 				- binary semaphores - works like mutex (0,1)

 				- counting semaphores - allows access to a fixed no.of resources



dead locks - it is a situation where one process is holding the resource and waiting for the another resource which is holding by another process



 	conditions of deadlock  - mutual exclusion - atleast one resource is non-sharable

 				- hold and wait - a process holds one resource and waiting for other resource

 				- no preemption - a resource cant be taken away until it realeases the resource

 				- circular wait - a set of process waiting for each other for resources in a circular way



 	dead lock handling - prevention or avoidance - ensure the system not to enter in a dead lock state

 			   - detection and recovery - if dead lock occur, do preemption to handle

 			   - ignore -  If deadlock is very rare, then let it happen and reboot the system. This is the approach that both Windows and UNIX take.





 	bankers algorithm - Banker’s Algorithm is a deadlock avoidance algorithm used in operating systems to decide whether granting a resource request will keep the system in a safe state.



memory management - memory need to shared among multiple process

 

 		  - overlays - the memory should contain only the available instructions and resources required at the given time

 		  - swapping - in multiprogramming, the instructions that have used at time slice are swapped out from memory

 

 	techniques - single partition allocation - memory is dived into 2 parts, one is used by the owner and other is used by user.

 		   - multi partion allocation -- fixed partion - the memory is divided into fixed size partitions

 					      -- variable partion - the memory is divided into variable sized partitions

 							- first fit

 							- best fit

 							- worst fit



paging - the physical memory is divided into equal sized frames.the main memory is divided into fixed size pages.the size of physical memory frame is equal to size of virtual memory frame

segmentation - Segmentation is a memory management technique that divides a process into logical segments such as code, data, and stack. and it can be implemented with or without paging



page fault - it is a interupt by hardware when running a program access a memory page that is mapped to virtual address space,but not loaded in physical memory

 

page replacement algorithms - Page replacement algorithms determine which memory page should be replaced when a new page needs to be loaded into a full main memory.

 

 	fifo - first in first out

 	lru  - last recently used

 	opt  - optimal page - the page that will not be used for the longest time



disk scheduling - i/o scheduling

 

 	seek time - time taken by the disc to move from current postion to required postion

 	rotational latency - time taken for the desired disk sector to come under the read/write head.

 	transfer time - time required for data transfer



 	algorithms -- FCFS - first come first serve

 		      SSTF - shortest seek time first

 		      SCAN - moves the disk head in one direction, servicing all requests until it reaches the end, then reverses direction and continues servicing requests.

 		     CSCAN - circular scan with uniform waiting time

 		      LOOk - same like scan but only moves to the ends

 		     CLOOK - same like cscan but after reahing end it jumps to first



kernel - it is a core part of os that which manages the hardware and provide services to programs or software



monolithic kernel - A monolithic kernel is an OS kernel where all core services run in kernel space as a single, tightly integrated system



micro kernel - it is a kernel design that keeps the kernel as small as possible, running only most essential services in kernel space, while moving the most os services to user space



macro kernel - combo of micro and monolithic



demand paging -  if an area of memory is not currently being used,it is swapped to disk to make room for an application's need



virtual memory - it is a memory management technique where each program look for a contigious address space even if the computer has low physical RAM.



fragmentation - process of memory wastage. it reduces the performance and capacity because memory is used inefficiently

 

 	internal fragmentation - it occurs when the sytem deal with fixed size allocations

 	external fragmentation - it occurs when the sytem deal with variable size allocations



Spooling - (Simultaneous Peripheral Operations On-Line) temporarily stores I/O data on disk to manage access to slow peripheral devices like printers.



starvation - it is situation where a process is waiting for the resource indefintely for a long time and resource allocated to other processs



aging - technique to avoid starvation by increasing priority of the process for the resource as long as the process waits



thrashing - it is a situation where cpu spend most of its time swaping pages rather tham executing instructions











#  				oops



class - blue print to create an object, which defines properties and behavior of that object

object - instance of a class that contains data





constructor - it is a special method that is used to intialize object when it is created, it automatically invoked when object is created

destructor -  it is a special method where it is automatically called when an object is deleted





self - self is a reference variable that points to the current object

attributes - these are kind of variables that are assossciated with class or object



decorator - it is a function which wrapes another function and modifies the behaviour of another function without changing the original function



static method - it is a decorator when there is no need of self reference for some methods so we use static method to bring it to class level





pillars of oop - abstraction, encapsualtion, inheritence, polymorphism3





**ABSTRACTION -** it is a oop concept that means hiding internal implementation and details and showing only the essential features to the user

 	- @abstractmethod

 	- you can not create an objecct for an abstract class



ENCAPSULATION - it is a oop concept where we wrap the data and methods together and protecting them from direct access

 	access specifiers - public     -  self.name

 			  - protected  -  self.\_name

 			  - private    -  self.\_\_name

 

INHERITANCE - it is a oop concept where one class can inherit or use methods of another class



 		single

 		multiple

 		multi-level

 		hierarichal



 	super method - it is a method which is used to call parent methods from child class

 	class method - it is used to modify the data or behaviour of the class



 	getter and setters - are methods used to access (get) and modify (set) the value of private variables safely.



POLYMORPHISM - it is a oop concept which the same function behaves differently based on object or datatype





#  				CN



network - 2 or more devices connected to communicate,share data, resources or services



 	types - LAN (land area network) - used for small area coverage

 		WAN (wide area network) - used for large area coverage

 		MAN (metropolitan area network) - used for city wide network

 		PAN (personal area network) - used for personal use

 		GAN (global area network) - used for global area



VPN (virtual private network) - it is a technology where it creates a secure, encrypted connection between your device and internet

 

 	types - remote access vpn - used by employees to access office network

 		site to site vpn - connects 2 office networks securely



topology - it is pattern like how computers or devices connected with each other



 	types - bus topology - connected in a single line , cheap , if one computer fails entire network is affected

 		star toplogy - all are connected to one single central hub, easy to manage, commonly used

 		ring topology - all are connected in circular manner, data flows in one direction

 		mesh topology - all systems are connected with eachother, reliable, expensive

 		tree topology - combo of star and bus, used in big organizations





IPv4(internet protocol version 4) - it is a address of a device in network or internet

 

 	types - public ip - used on internet, provided by isp(internet service provider)

 		private ip - used in a local network

 

 		IPv4 Class





 	Start 	       End Address      class



 	0.0.0.0    127.255.255.255 	A



 	128.0.0.0  191.255.255.255	B



 	192.0.0.0  223.255.255.255	C



 	224.0.0.0  239.255.255.255 	D



 	240.0.0.0  255.255.255.254 	E



OSI (open system interconnection) - it  is a 7 layer reference model where it depicts how data is shared from one computer and another computer



 	application layer - used by the user for interaction (HTTP, FTP, SMTP)

 	presentation layer - data format transaltion, encryption \& decryption, compression (TLS)

 	session layer - manages sessions between two users (netBIOs)

 	transport layer - ensures reliable data transfer, error control and flow control (UDP, TCP)

 	network layer - handles routing and path selection, uses ip addressing (IP)

 	datalink layer - converts data into frames, error detection mac address

 	physical layer - actual hardware transmission via cables, signals etc.,



DNS (domain name system)- translates human readable domain names into ip address

TCP(Transmission contorl protocol) - ensures relaible data transmission between 2 devices

UDP(user datagram protocol) - it is a connection-less tcp sends data without guarantee delivery

FTP(File transfer protocol) - transfer file between user and server in a network

SMTP(simple mail transfer protocol) - used to send mails

IP(internet protocol) - delivery of datapackets between one-another using ip-adress

ARP(address resolution protocol) - converts ip address into mac address within a network

ICMP(internet message control protocol) - error reporting



fire wall - it is a network security system where it monitors incoming and outgoing protocol with some predefined security rules

ping - it checks connection between network devices

 

unicast - 1-1 message transfer

broadcast - 1-many

multicast - 1-some



latency - the amount of time it takes for data to travel from source to destination.



error codes:



200 → Success



404 → Page not found



500 → Server error



403 → Forbidden



401 → Unauthorized



port numbers :



80 → HTTP



443 → HTTPS



22 → SSH



25 → SMTP



53 → DNS









#  				DJANGO



1\. What is Django?



High-level Python web framework



Follows MVT architecture



Rapid development + security + scalability



2\. Explain MVT architecture in Django



Model → Database structure



View → Business logic



Template → UI / HTML



Django handles controller internally



3\. Difference between Django and Flask



Django → Full-stack framework



Flask → Micro framework



Django has ORM, admin, auth built-in



4\. What is a Django project and a Django app?



Project → Entire website



App → Specific functionality/module



5\. What is Django ORM?



Converts Python models into DB tables



Avoids raw SQL



Improves security and maintainability



6\. What is a model in Django?



Python class representing DB table



Each attribute → column



Each object → row



7\. What are migrations?



Track DB schema changes



Commands:



makemigrations



migrate



8\. What happens when you run python manage.py runserver?



Starts Django development server



Loads settings, URLs, apps



Listens for HTTP requests



9\. What is a view?



Function or class



Receives request



Returns response (HTML/JSON)



10\. How does URL mapping work in Django?



URL → matched in urls.py



Calls corresponding view



View returns response



11\. What is a template?



HTML with Django template language



Used to display dynamic data



12\. Difference between {{ }} and {% %}



{{ }} → Display data



{% %} → Logic (loops, conditions)



13\. How do you pass data from view to template?



Using dictionary (context)



return render(request, "page.html", data)



14\. GET vs POST method



GET → Fetch data (visible in URL)



POST → Submit data (secure)



15\. What is CSRF token and why is it needed?



Protects from fake requests



Prevents cross-site request forgery



Mandatory for POST forms



16\. What are static files?



CSS, JS, images



Loaded using {% load static %}



17\. Difference between static files and media files



Static → Developer files



Media → User-uploaded files



18\. What is Django authentication?



Built-in login, logout, signup



Uses User model



Session-based authentication



19\. Explain request-response flow in Django



User hits URL



URL → View



View processes logic



Template renders



Response sent to user



20\. Explain your Django project (MOST IMPORTANT 🔥)



You must answer:



Problem statement



Features implemented



Tech stack



Data flow



Challenges faced





# &nbsp;					Projects



“My Restaurant Management System is a Django-based web application designed to manage menu items, customer orders, and billing efficiently. The admin can add or update menu items, staff can place orders, and the system automatically calculates the total bill and tracks order status. I used Django’s MVT architecture with ORM for database interaction, which made the application secure and scalable.”


drop table registrations;

create table registrations(

	EventID varchar(50), 
    registrations int, 
    date_time timestamp
);

insert into registrations
values
	("41BCDEFGHIJK", 20, "2024-04-20 11:30:00"),
    ("41BCDEFGHIJK", 11, "2024-04-20 11:25:00"),
    ("41BCDEFGHIJK", 3, "2024-04-20 11:20:00"),
    
    ("31EFGHIJK", 10, "2024-04-20 11:30:00"),
    ("31EFGHIJK", 30, "2024-04-20 11:25:00"),
    ("31EFGHIJK", 15, "2024-04-20 11:20:00") ,	
    
    ("34KLMNOPQ", 12, "2024-04-20 11:30:00"),
    ("34KLMNOPQ", 8, "2024-04-20 11:25:00"),
    ("34KLMNOPQ", 1, "2024-04-20 11:20:00"),
    
	("36TUVWXY", 12, "2024-04-20 11:12:00"),
    ("36TUVWXY", 8, "2024-04-20 10:25:00"),
    ("36TUVWXY", 18, "2024-04-20 9:20:00")
    
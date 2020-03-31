CREATE TABLE [users] (
	[Id] INTEGER PRIMARY KEY NOT NULL,
	[Username] NVARCHAR(100)  NOT NULL,
	[Password] NVARCHAR(100) NOT NULL,
	[Date] NVARCHAR(100) NOT NULL
);

CREATE TABLE [streetLevelCrimes] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[category] NVARCHAR(100)  NOT NULL,
	[location_type] NVARCHAR(100)  NOT NULL,
	[latitude] NVARCHAR(100)  NOT NULL,
	[longitude] NVARCHAR(100)  NOT NULL,
	[street_id] NVARCHAR(100)  NOT NULL,
	[street_name] NVARCHAR(100)  NOT NULL,
	[context] NVARCHAR(100) NOT NULL,
	[outcome_status] NVARCHAR(100) NOT NULL,
	[persistent_id] NVARCHAR(100) NOT NULL,
	[location_subtype] NVARCHAR(100) NOT NULL,
	[month] NVARCHAR(100) NOT NULL
);

CREATE TABLE [outcomesCrimes] (
	[Id] INTEGER  NOT NULL PRIMARY KEY,
	[persistent_id] NVARCHAR(100)  NOT NULL,
	[category_id] INTEGER  NOT NULL,
	[date] NVARCHAR(100)  NOT NULL,
	[person_id] NVARCHAR(100)  NOT NULL,
	[month] NVARCHAR(100) NOT NULL
);

CREATE TABLE [crimeCategories] (
	[Id] INTEGER  NOT NULL PRIMARY KEY,
	[name] NVARCHAR(100)  NOT NULL,
);

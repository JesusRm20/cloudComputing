CREATE TABLE [streetLevelCrimes] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[category_id] NVARCHAR(100),
	[location_type] NVARCHAR(100),
	[latitude] NVARCHAR(100),
	[longitude] NVARCHAR(100) ,
	[street_id] NVARCHAR(100),
	[street_name] NVARCHAR(100) ,
	[context] NVARCHAR(100),
	[outcome_status] NVARCHAR(100),
	[persistent_id] NVARCHAR(100),
	[location_subtype] NVARCHAR(100),
	[month] NVARCHAR(100)
);

CREATE TABLE [outcomesCrimes] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[persistent_id] NVARCHAR(100),
	[category] INTEGER,
	[date_1] NVARCHAR(100),
	[person_id] NVARCHAR(100)
);

CREATE TABLE [crimeCategories] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[name] NVARCHAR(100)  NOT NULL
);

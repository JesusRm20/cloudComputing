CREATE TABLE [users] (
	[Id] INTEGER PRIMARY KEY NOT NULL,
	[Username] NVARCHAR(100),
	[Password] NVARCHAR(100),
	[Date] NVARCHAR(100)
);

CREATE TABLE [streetLevelCrimes] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[category] NVARCHAR(100) DEFAULT 'N/A',
	[location_type] NVARCHAR(100) DEFAULT 'N/A',
	[latitude] NVARCHAR(100) DEFAULT 'N/A',
	[longitude] NVARCHAR(100)  DEFAULT 'N/A',
	[street_id] NVARCHAR(100) DEFAULT 'N/A',
	[street_name] NVARCHAR(100)  DEFAULT 'N/A',
	[context] NVARCHAR(100) DEFAULT 'N/A',
	[outcome_status] NVARCHAR(100) DEFAULT 'N/A',
	[persistent_id] NVARCHAR(100) DEFAULT 'N/A',
	[location_subtype] NVARCHAR(100) DEFAULT 'N/A',
	[month] NVARCHAR(100) DEFAULT 'N/A'
);

CREATE TABLE [outcomesCrimes] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[persistent_id] NVARCHAR(100),
	[category_id] INTEGER,
	[date_1] NVARCHAR(100),
	[person_id] NVARCHAR(100)
);

CREATE TABLE [crimeCategories] (
	[id] INTEGER  NOT NULL PRIMARY KEY,
	[name] NVARCHAR(100)  NOT NULL
);

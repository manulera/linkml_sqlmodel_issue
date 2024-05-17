-- # Class: "Person" Description: "A person"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: age Description: The age of the person
--     * Slot: team_id Description: The team to which the person belongs
-- # Class: "Team" Description: "A team"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing

CREATE TABLE "Team" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	age INTEGER, 
	team_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(team_id) REFERENCES "Team" (id)
);

USE pysports;

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS team;

CREATE TABLE team (
    team_id INT NOT NULL AUTO_INCREMENT,
    team_name VARCHAR(75) NOT NULL,
    mascot VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE players (
    player_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot)
    VALUES('University of Nebraska', 'Cornhuskers');
INSERT INTO team(team_name, mascot)
    VALUES('University of Iowa', 'Hawkeyes');

SELECT team_id FROM team WHERE team_name = 'University of Nebraska';

INSERT INTO players(first_name, last_name, team_id)
    VALUES('Chad', 'Hendren', '1');
INSERT INTO players(first_name, last_name, team_id)
    VALUES('Amy', 'Hendren', '1');
INSERT INTO players(first_name, last_name, team_id)
    VALUES('Roman', 'Mahoney', '1');

SELECT team_id FROM team WHERE team_name = 'University of Iowa';

INSERT INTO players(first_name, last_name, team_id)
    VALUES('Jenika', 'Hendren', '2');
INSERT INTO players(first_name, last_name, team_id)
    VALUES('Charlott', 'Hendren', '2');
INSERT INTO players(first_name, last_name, team_id)
    VALUES('Nicole', 'Hendren', '2');
CREATE TABLE ANIMAL_INS( 
  ANIMAL_ID VARCHAR(16) NOT NULL,
  ANIMAL_TYPE VARCHAR(32) NOT NULL,
  DATETIME DATETIME NOT NULL,
  INTAKE_CONDITION VARCHAR(32) NOT NULL,
  NAME VARCHAR(32),
  SEX_UPON_INTAKE VARCHAR(32) NOT NULL,
  PRIMARY KEY(ANIMAL_ID)
);

CREATE TABLE ANIMAL_OUTS(
  ANIMAL_ID VARCHAR(16) NOT NULL,
  ANIMAL_TYPE VARCHAR(32) NOT NULL,
  DATETIME DATETIME NOT NULL,
  NAME VARCHAR(32),
  SEX_UPON_OUTCOME VARCHAR(32) NOT NULL,
  PRIMARY KEY(ANIMAL_ID)
);

DROP TABLE IF EXISTS parcelles;
DROP TABLE IF EXISTS puits;

CREATE TABLE parcelles (
    id_parcelle INTEGER PRIMARY KEY,
    nom TEXT,
    culture TEXT,
    type_sol TEXT,
    surface_ha REAL,
    rendement_t_ha REAL,
    irrigue INTEGER   -- 1 = oui, 0 = non
);

CREATE TABLE puits (
    id_puits INTEGER PRIMARY KEY,
    nom TEXT,
    debit_m3_h REAL
);

INSERT INTO parcelles VALUES
(1,'Parcelle A','Blé','Argileux',12.5,3.2,0),
(2,'Parcelle B','Tomate','Limoneux',4.0,45.0,1),
(3,'Parcelle C','Orge','Sableux',9.0,2.1,0),
(4,'Parcelle D','Olivier','Limoneux',15.0,6.5,0),
(5,'Parcelle E','Pomme de terre','Limoneux',6.5,28.0,1),
(6,'Parcelle F','Blé','Argileux',10.0,3.5,0),
(7,'Parcelle G','Maïs','Argileux',7.5,7.8,0),
(8,'Parcelle H','Orge','Sableux',8.0,1.9,0);

INSERT INTO puits VALUES
(1,'Puits Nord',25),
(2,'Puits Centre',40),
(3,'Puits Sud',15);
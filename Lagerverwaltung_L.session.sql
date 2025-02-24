CREATE TABLE Produkte(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    preis INT,
    bestand INT
);
INSERT INTO Produkte(name,preis,bestand)
Values (
    'Gucci',
    '300',
    '200'
)
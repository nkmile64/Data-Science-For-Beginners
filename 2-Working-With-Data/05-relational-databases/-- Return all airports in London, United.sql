-- Return all airports in London, United Kingdom
SELECT Airports.name, Cities.city
FROM Airports
    INNER JOIN Cities
        ON Airports.city_id = Cities.id
WHERE Cities.city = "London"

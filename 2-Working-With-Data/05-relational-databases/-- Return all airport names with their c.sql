-- Return all airport names with their city and country
SELECT Airports.name, Cities.city, Cities.country
FROM Airports
    INNER JOIN Cities ON 
        Airports.city_id = Cities.id
/*Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA. */

SELECT * 
FROM CITY
WHERE population > 100000 AND CountryCode = 'USA';

/*Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.*/

SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID,2) = 0;

/*Query all columns for a city in CITY with the ID 1661.*/

SELECt *
FROM CITY
WHERE ID = 1661

/*Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically. */

SELECt CITY, length(CITY) from STATION
ORDER BY length(CITY),CITY ASC
limit 1;
SELECT CITY, length(CITY) from STATION
ORDER BY length(CITY) DESC
limit 1;

/*Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.*/

SELECT DISTINCT city 
FROM station 
WHERE city LIKE '%[a, e, i, o, u]';

/*Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.*/

SELECT DISTINCT City from Station 
WHERE left(city,1) in ('a','e','i','o','u') 
AND right(city, 1) in ('a','e','i','o','u')

/*Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.*/

SELECT DISTINCT city 
FROM station 
WHERE city NOT LIKE '[a, e, i, o, u]%';

/*Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.*/

SELECT DISTINCT City from Station 
WHERE left(city,1) not in ('a','e','i','o','u') 
OR right(city, 1) not in ('a','e','i','o','u')

/*Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.*/

SELECT DISTINCT City from Station 
WHERE left(city,1) not in ('a','e','i','o','u') 
AND right(city, 1) not in ('a','e','i','o','u')

/*Query the Name of any student in STUDENTS who scored higher than  75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.*/

SELECT Name
FROM STUDENTS
WHERE Marks>75
ORDER BY right(Name,3) ASC, ID ASC;



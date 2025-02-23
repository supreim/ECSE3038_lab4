# Lab 4

### Reason
The purpose of this project was to complete a lab assignment.

### Functionality
**Get /profile/**
The returns a single user dictionary with the fields id, last_updated, username, color and role. 
OR {} if no user has been created.

**POST /profile/**
This creates a user and inserts it into the database. The user must have the fields username, color and role.

**Get /tank/**
This returns a list of all the tanks with their individual id, location, lat and long.

**POST /tank/**
This accepts JSON data to be inserted into the Tanks collection if the required fields, location, lat and long are met and that a user has already been created.
    
**PATCH /tank/{id}**
This accepts JSON data to be updated with respect to the tank with the same id as in the url.

**DELETE /tank/{id}**
This removes the tank from the Tanks collection with the id that matches the id in the url.

### Q/A
- Your favourite low effort/non-fancy food and why
    - kfc wings 

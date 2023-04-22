# PROJECT TODO

- [ ] # TODO: Create validation to validate the license of the user and ensure the validated data bears a strong similarity to the user

- [ ] TODO: Create validator to validate the bank account number and check the nameon the bank account with the user's name if valid updates the user's bank_verified status to True else it stays false

- [ ] TODO: validate the card from paystack and ensure the card bears a similarity to the registered user

- [ ] IMPLEMENT REDIS FOR CACHING AND GEOSPACIAL DATA
- [ ] CREATE A MANAGER FOR TICKETS WITH CACHING ENABLED
- [ ] SETUP DJANGO-CACHEOPS TO AUTOMATICALLY CACHE FREQUENTLY USED QUERIES FROM THE DATABASE

- [ ] IMPROVE QUERIES BY THEIR MANAGERS ADDING REDIS TO THEM AND USING SIGNALS TO DELETE THE REDIS CACHE WHEN ANEW OBJECT IS ADDED TO THE QUERY AND ON A NFRESH QUERY FROM THE MANAGER ADD ALL TO THE QUERY LIST

- [*] READ ABOUT THE GENERIC RELATIONSHIP IMPLEMENTED FOR RIDES AND TICKETS
- [ ] ENSURE THE GOOGLE DISTANCE API FUNCTIONS BETTER
- [*] Write a celery task to submit emails without waiting for the server to respond
- [ ] Prevent copying text from my website

## PROJECT FEATURE TODO

- [ ] Build the live chat
- [ ] Build a Quotation and Milestone PDF generator
- [*] Build a Blogging System with Comments enabled similar to medium

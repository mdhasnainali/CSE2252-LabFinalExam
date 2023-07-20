Create a Django project called "DogProject" and set up a new Django app called "DogApp". Write the necessary commands to create the project and the app.

In the "DogApp" app, create a model called "DogShop" with the following fields:
name, price, breed, description
Write the code for the model and perform the necessary migrations.

Create a serializer for the "Dog" model in the "DogShop" app. The serializer should include all the fields from the model and provide validation for the fields.

Implement the views for CRUD operations (Create, Read, Update, Delete) for the "Dog" model using Django's class-based views. Ensure that the views follow RESTful principles.

Configure the URLs for the "DogShop" app to map to the appropriate views. Include the necessary URL patterns for listing all dogs, retrieving a single dog by ID, creating a new dog, updating an existing dog, and deleting a dog.

### Documentation
Imagine you have successfully implemented the RESTful API using Django for the "DogShop" app. Now, it's time to document your API endpoints. Write a step-by-step guide on how you would document the API endpoints using a tool of your choice.

* Provide an example of documenting all of the endpoints (e.g., retrieving a single dog by ID).
* Explain how you would handle authentication and authorization documentation for protected endpoints.

### Test
Testing is a critical aspect of API development to ensure its functionality and reliability. Design a testing strategy for the RESTful API you created using Django. Answer the following questions in your strategy: • How would you handle unit testing for your API endpoints? Provide an example.

* Describe how you would approach integration testing for your API.
* Explain how you would handle authentication and authorization testing for protected endpoints.
# API CRUD Operations in a React App

## Challenge

Now that you've grasped the fundamentals of using a REST API, it's time to build a simple React App that interacts with the same API. The provided application includes Read and Create operations with a basic UI.

Your challenge is to implement the **Update** and **Delete** operations in the app. By completing this, you will build an application with full CRUD (Create, Read, Update, Delete) support.

## Key Learnings

By completing this challenge, you will learn:

1. How to implement full CRUD operations in a React application.
2. How to make API calls using different HTTP methods (GET, POST, PUT, DELETE) within React.
3. How to manage state and update the UI based on API responses.

## User Story

As a developer,  
I want to extend an existing React application with Update and Delete functionality,  
So that the app supports all CRUD operations and I understand how to handle API calls in React.

## Acceptance Criteria

- The provided React app is updated to include:
  - **Update functionality**:
    - Users can edit an existing blog post by submitting new data.
    - The app sends a `PUT` request to the API to update the blog post.
  - **Delete functionality**:
    - Users can delete a blog post via a button click.
    - The app sends a `DELETE` request to the API to remove the blog post.
- The UI is updated dynamically based on the API responses for update and delete operations.
- Error handling is implemented to display feedback if an API call fails.

## Instructions

1. Install the dependencies and start the development server:

```bash
npm install
npm run dev
```

2. Familiarize yourself with the app structure and its existing functionality:

- The app already supports Read (displaying all blog posts) and Create (adding new blog posts).
- Review the API calls for these operations to understand how data is being fetched and posted.

3. Implement the following functionality:

Update:

- Add a button or form to edit an existing blog post.
- Use the PUT API endpoint to send updated data for a blog post to the server

```bash
PUT /blog/update/{id}/
```

Delete:

- Add a delete button for each blog post.
- Use the DELETE API endpoint to remove a specific blog post from the server.

```bash
DELETE /blog/get/delete/{id}/
```

4. Test your implementation:

- Create a new blog post using the existing functionality.
- Update a blog post and verify the changes persist in the database.
- Delete a blog post and confirm it no longer appears in the list.

5. Add error handling to manage API call failures, such as:

- Displaying error messages for failed PUT or DELETE requests.
- Ensuring the UI remains consistent if an operation fails.

## Additional Resources

- **React Documentation**: Learn more about React at the [official documentation](https://reactjs.org/).
- **Axios**: A popular library for making HTTP requests in React. Check out the [Axios documentation](https://axios-http.com/).
- **Django REST Framework**: Refer to the [Django REST Framework documentation](https://www.django-rest-framework.org/) for more details on the API.
- **MDN HTTP Methods**: Understand the different HTTP methods and their use cases at the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

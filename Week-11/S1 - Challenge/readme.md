# Implementing Authentication

## Challenge

In the next session, you'll be learning about authentication. However, within the API's Swagger documentation, you'll notice there are endpoints for signing up and logging in.

Your challenge is to build simple **Sign Up** and **Login** screens in React that use these endpoints. You should be able to:

1. Create a new user account via the **Sign Up** screen.
2. Test the login functionality by logging in with the created account and receiving an authentication token as a response.

## Key Learnings

By completing this challenge, you will learn:

1. How to implement basic authentication workflows in a React application.
2. How to send API requests for **Sign Up** and **Login** using HTTP POST methods.
3. How to manage and use authentication tokens in a client-side application.

## User Story

As a user,  
I want to create an account and log in to the application,  
So that I can securely access features that require authentication.

## Acceptance Criteria

- A **Sign Up** screen is created, allowing users to input and submit their details to the `/auth/signup/` endpoint.
- A **Login** screen is created, allowing users to log in with their credentials via the `/auth/login/` endpoint.
- Upon successful login, an authentication token is displayed or logged in the console.
- Error messages are displayed for failed sign-up or login attempts (e.g., invalid credentials or duplicate accounts).
- The app uses the API's Swagger documentation at `http://127.0.0.1:8000/` as a reference for endpoint structure and requirements.

## Instructions

1. **Review the Swagger Documentation**  
   Open a browser and navigate to `http://127.0.0.1:8000/` to review the API's Swagger documentation. Locate the following endpoints:

   - **Sign Up**: `POST /auth/signup/`
   - **Login**: `POST /auth/login/`

2. **Set Up the React App**  
   If you don’t have a React app set up already, create one:
   ```bash
   npm crate vite@latest
   cd auth-app
   npm install
   npm run dev
   ```
3. **Build the Sign-Up Screen**

4. Create a React component for the **Sign Up** screen.
5. Use an HTML form to collect the user’s sign-up details (e.g., username, password, email).
6. Use `axios` or `fetch` to send a `POST` request to `http://127.0.0.1:8000/auth/signup/` with the form data.
7. Handle success and error responses appropriately.

8. **Build the Login Screen**

9. Create a React component for the **Login** screen.
10. Use an HTML form to collect the user’s login credentials (e.g., username and password).
11. Use `axios` or `fetch` to send a `POST` request to `http://127.0.0.1:8000/auth/login/` with the credentials.
12. Display or log the authentication token received in the response.

13. **Test Your Implementation**

14. Test the **Sign Up** screen by creating a new user. Ensure that the account is successfully created.
15. Test the **Login** screen by logging in with the created account. Ensure that an authentication token is returned.

### Bonus Challenge

- Store the authentication token in local storage or a React state.
- Display a message like "Logged in successfully" after a successful login.

### Additional Resources

- **React Documentation**: Learn more about React at the [official documentation](https://reactjs.org/).
- **Axios Documentation**: A library for making HTTP requests. Visit the [Axios documentation](https://axios-http.com/).
- **Django REST Framework Authentication**: Understand the authentication workflows in DRF by reading the [official documentation](https://www.django-rest-framework.org/api-guide/authentication/).

Happy coding!

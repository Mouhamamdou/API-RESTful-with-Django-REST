# API Project Documentation

## Overview

The API project is a web application designed to manage projects, issues, and comments, akin to 
a task tracking system. The application facilitates project management tasks, including user 
authentication, project creation, issue tracking, and commenting functionalities, offering a
comprehensive tool for development teams.

## Features

- User Authentication: Utilizes Django's robust authentication system for user management, allowing 
  sign-up, login, and logout capabilities.

- Project Management: Users can create, update, and view projects. Each project can have multiple 
  contributors and a variety of issues (tickets) associated with it.

- Issue Tracking: Users can report, update, and manage issues within projects. Issues can be 
  categorized by type, status, and priority to streamline project workflows

- Comments: Allows users to add comments to issues.

- Permissions and Security: Implements custom permissions to ensure that users can only access 
  and modify their projects, issues, and comments, enhancing data security and privacy.

## Installation

1. Clone the repository:

	```bash
   git clone https://github.com/Mouhamamdou/API-RESTful-with-Django-REST.git

2. Set up a Virtual Environment:

   It's recommended to use a virtual environment for Python projects. You can create one using 
   python -m venv venv and activate it with source venv/bin/activate on Unix/Linux or venv\Scripts\activate on Windows.

3. Install Dependencies

   Install all required dependencies with pip:

   ```bash 
   pip install -r requirements.txt

4. Migrate the Database

   Apply migrations to create the database schema with:

	```bash
  python manage.py migrate.

5. Run the server

   Start the Django development server with:
  
	```bash
   python manage.py runserver. 

Access the application by navigating to http://localhost:8080 in your web browser.

## Usage

- API Endpoints: The project includes multiple RESTful endpoints for managing users, projects,
  issues, and comments. Access these endpoints through HTTP requests to create, retrieve, 
  update, or delete resources.

- Authentication: Access to most endpoints requires authentication. Utilize the provided JWT
  endpoints for obtaining tokens.

- Project and Issue Management: Authenticated users can create new projects, add issues to project,
  and manage project contributors.

- Commenting: Users can comment on issue to discuss project tasks and updates. 

## Development

This project follows the Django REST Framework's conventions for structuring an API:

- Models: Located in 'models.py', define the data structure.

- Serializers: Found in 'serializers.py', they handle querysets and model instances conversion to
  JSON format.

- views: Defined in 'views.py', control the logic and response for incoming HTTP requests.

- Permissions: Custom permissions in 'permissions.py' ensure users can only access and modify
  their data.

- URLs: The 'urls' files route URLs to their respective views, organizing the API endpoints.

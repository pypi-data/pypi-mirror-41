![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-staff

Staff app. Syncs with Slack.

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-staff
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'tokenservice',
      'staff',
  ]

  #########################
  # staff settings
  # Token for a slack app with users:read & users:read.email permission scopes
  STAFF_SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
  ```

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```


##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/staff"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```

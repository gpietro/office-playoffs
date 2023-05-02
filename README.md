# Office Playoffs

![project logo](/static/webapp/images/project_logo.svg)

This is a weekend project that I worked on in collaboration with ChatGPT. Our aim was to test pair programming and refresh our knowledge on Django. The result is an open source office tournament app organizer that can be used to manage tournaments for ping pong or any other sport that you have in your office.

Feel free to use this project and let us know what you think. If you have any suggestions or improvements that you would like to contribute, please feel free to submit a pull request on GitHub.

<br/>

![project screenshot](/docs/project_screenshot.png)

<br/>

## Project Structure

The project is built with Django and follows a standard Django app structure. The main project directory is `sparrow_tournament/`, and the web application is in the `webapp/` directory. The templates for rendering the web pages are in the `templates/` directory, and static files are stored in the `static/` directory.

<br/>

## Deploying the App

This app can be easily deployed on Heroku with the included `Procfile`. Simply create a Heroku app and push the code to it. The app will be automatically deployed, and the `Procfile` will ensure that the app is run correctly.

<br/>

## Running the App

To run the app locally, first, install the dependencies by running:

```
pip install -r requirements.txt
```

Next, make the necessary database migration by running:

```
python manage.py makemigrations
python manage.py migrate
```

You need to create a `.env` with the variables:

```
SECRET_KEY='your-secret'
SITE_ID=1
DEBUG=True
```

Finally, start the local development server by running:

```
python manage.py runserver
```

The app will be running at `http://localhost:8000`

<br/>

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request on GitHub. We are always looking for ways to improve the app and make it more useful for office tournaments.

<br/>

## Acknowledgments

Big thanks to ChatGPT for being an amazing pair programming partner. It was great working with you, and I couldn't have done it without your assistance!
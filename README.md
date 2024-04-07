# Geology Guessr
#### Video Demo:  <[Video](https://youtu.be/ck5FOg_rz-Q)>
#### Description:

Geology Guesser represents an innovative and interactive web-based application meticulously crafted using the Flask framework in Python. This project aims to offer users an immersive and intellectually stimulating experience by combining elements of entertainment and education through a guessing game based on geological images. Geology Guesser is designed to engage users with its distinctive blend of user authentication, gameplay mechanics, and leaderboard functionalities.

## Project Structure

### app.py

At the foundation of Geology Guesser lies the `app.py` file, the cornerstone orchestrating the application's entire functionality. It serves as the central hub for:

#### User Authentication
Geology Guesser ensures secure user registration, login, and logout functionalities by employing password hashing using the Werkzeug library. This meticulous approach ensures that sensitive user credentials remain safeguarded against potential security threats.

#### Leaderboard Display
The application dynamically fetches data from the SQLite database to exhibit the top 10 scorers. This leaderboard feature acts as a motivational tool, inspiring healthy competition among users and highlighting the accomplishments of top performers.

#### Gameplay Mechanics
Geology Guesser engages users by presenting geological images and inviting them to guess the associated geological terms. Correct guesses trigger score increments, fostering user engagement and encouraging participation.

### Templates (/templates)

The `/templates` directory is a repository of crucial HTML templates responsible for rendering diverse user interface elements:

#### register.html and login.html
These pages serve as gateways, facilitating user account creation and login procedures. They provide an intuitive and user-friendly interface for both new users and existing members.

#### play.html
The play page is the interactive hub where users partake in the game. It dynamically presents geological images, prompting users to make guesses, thus enriching the overall user experience.

#### index.html
The index page showcases the leaderboard, spotlighting the top users alongside their respective scores. This feature offers users visibility into their achievements and motivates them to aim for higher ranks.

### Static Files (/static)

The `/static` directory is home to various static files, including images (`img1.png`, `img2.png`, `img3.png`, `img4.png`, `img5.png`) portraying a diverse array of geological feautres. These visual aids serve as cues during the gameplay, enhancing users' associations between terms and images.

## Design Considerations

### Flask Framework

The selection of Flask was a deliberate choice owing to its lightweight nature and adaptability. Its simplicity allowed for rapid development and seamless integration of various functionalities, including routing, HTML template rendering, and session management.

### SQLite Database

Geology Guesser optimally leverages an SQLite database (`users.db`) due to its simplicity and suitability for managing user-centric data. This relational database efficiently stores vital user information such as usernames, hashed passwords, and scores.

### Gameplay Logic

The game is thoughtfully designed to present users with geological images and prompt them to guess the associated terms. Upon correct guesses, users' scores are updated in the database, incentivizing continued participation and heightening user engagement.

### Security Measures

Geology Guesser prioritizes robust security measures to fortify user data protection:

#### Password Hashing
To bolster security, the application hashes passwords using the `generate_password_hash` function from the Werkzeug library. This cryptographic hashing ensures the integrity of user credentials, mitigating unauthorized access attempts.

#### Session Management
Flask-Session diligently manages user sessions, preventing sensitive information from being cached and bolstering the application's overall security posture.

## Future Enhancements

Several potential avenues for enhancing Geology Guesser's functionality exist:

### Game Complexity
Introducing multiple difficulty levels or expanding the repository of images and terms to diversify the game experience and challenge users with varying levels of geological knowledge.

### User Profiles
Implementing personalized user profiles to track individual progress, historical performances, and high scores, thereby enhancing user engagement and offering a tailored experience.

### Responsive Design
Optimizing the application's layout and functionality to ensure compatibility across a spectrum of devices and screen sizes, ensuring a seamless and inclusive user experience.

## Running the Application

To experience Geology Guesser:

- Ensure Python and the requisite libraries (Flask, Flask-Session, Werkzeug) are installed.
- Execute the `flask run` command.
- Access the application via a web browser using the provided URL (usually `http://127.0.0.1:5000/`).

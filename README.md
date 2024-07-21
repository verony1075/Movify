# Movie Recommendation Application

## Overview

This project is a full-stack web application designed to provide personalized movie recommendations and interactive movie trivia for users. It allows users to register, log in, and manage their profiles, submit movie reviews, get personalized movie recommendations, and play movie trivia games. Users can also save their favorite movies to a wishlist.

## Features

- **User Authentication and Session Management**: Secure registration, login, and profile management.
- **Movie Reviews**: Users can submit reviews with ratings and comments.
- **Personalized Recommendations**: Recommendations are generated based on user reviews.
- **Wishlist**: Users can save and manage their favorite movies.
- **Interactive Trivia Game**: Engaging trivia questions based on movies.
- **Dynamic Content Rendering**: Uses Jinja templates for dynamic web content.

## Technologies Used

- **Backend**:
  - Flask (web framework)
  - SQLite (database management)
  - Passlib (secure password hashing)
  - Cinemagoer (movie data retrieval)
  - OpenAPI (movie recommendations and trivia)
- **Frontend**:
  - HTML
  - CSS
  - JavaScript
  - Jinja (template rendering)

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/verony1075/movie-recommendation-app.git
    cd movie-recommendation-app
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python
    >>> from db import get_db
    >>> db = get_db()
    >>> with open('database.sql', 'r') as f:
    >>>     db.executescript(f.read())
    ```

5. **Run the application**:
    ```sh
    flask run
    ```

6. **Access the application**:
    Open your web browser and navigate to `http://localhost:5000`.

## File Structure

- **app.py**: Main application file with route definitions and app configurations.
- **movie_rec.py**: Contains functions for user registration, login, review submission, and recommendations.
- **openapi.py**: Handles interaction with the OpenAPI for movie recommendations and trivia.
- **db.py**: Database connection setup.
- **templates/**: Directory containing HTML templates rendered by Jinja.
  - **index.html**: Home page template.
  - **register.html**: User registration template.
  - **login.html**: User login template.
  - **profile.html**: User profile template.
  - **review.html**: Movie review submission template.
  - **recommend.html**: Movie recommendation form template.
  - **trivia_form.html**: Trivia question form template.
  - **trivia_questions.html**: Trivia questions display template.
  - **trivia_results.html**: Trivia results display template.
  - **user_reviews.html**: User reviews display template.
  - **wishlist.html**: User wishlist display template.
- **static/**: Directory containing static files (CSS, JavaScript, images).

## Usage

1. **Register and Log In**:
    - Navigate to the registration page to create a new account.
    - Use the login page to access your account.

2. **Submit Movie Reviews**:
    - Navigate to the review submission page.
    - Enter the movie title, rating, and comments, then submit the review.

3. **Get Recommendations**:
    - Navigate to the recommendations page.
    - Choose genre, age rating, and year range to get personalized recommendations.

4. **Play Movie Trivia**:
    - Navigate to the trivia page.
    - Enter a movie title to start a trivia game.

5. **Manage Wishlist**:
    - Search for movies and add them to your wishlist.
    - View and manage your wishlist from the dedicated page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any feature additions or bug fixes.

## Contact

For any questions or suggestions, please open an issue or contact me at [veronysuccess@gmail.com].

---

Feel free to customize the README further as per your project's needs.

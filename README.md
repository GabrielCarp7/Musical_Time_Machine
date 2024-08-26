# Musical Time Machine

A Python project that creates a personalized Spotify playlist based on the top 100 Billboard songs from a specific date. The project uses the Spotify API, and Beautiful Soup to accomplish this.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [API Used](#api-used)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Connects to Spotify using user credentials.
- Scrapes Billboard's website for the top 100 songs from a user-specified date.
- Automatically creates a Spotify playlist with these songs.
- User-friendly and customizable.

## Installation

### Prerequisites

- Python 3.8 or higher
- Spotify Developer Account
- Beautiful Soup 4

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GabrielCarp7/Musical_Time_Machine.git
    cd Musical_Time_Machine
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Spotify API credentials:**

    - Open `main.py`.
    - Replace placeholders with your `access_token`, `user_id`, `playlist_name`, and `playlist_description`.

    ```python
    access_token = "your_access_token"
    user_id = "your_user_id"
    playlist_name = "Your Playlist Name"
    playlist_description = "Your Playlist Description"
    ```

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Enter a date:**

    When prompted, input a date in the format `YYYY/MM/DD` (e.g., `1995/05/12`).

3. **View your playlist:**

    The script scrapes the Billboard website and creates a Spotify playlist with the top 100 songs from the entered date.

## Technologies

- **Backend:** Python
- **Web Scraping:** Beautiful Soup
- **API:** Spotify Web API
- **Date Handling:** Python's datetime module

## API Used

- **[Spotify Web API](https://developer.spotify.com/documentation/web-api/)**: Used to create and manage Spotify playlists.
- **[Billboard Hot 100](https://www.billboard.com/charts/hot-100)**: The source for top 100 songs.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact

Gabriel Carp - [LinkedIn](https://www.linkedin.com/in/gabriel-carp-3b704022b/)

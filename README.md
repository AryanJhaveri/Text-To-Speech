# text-to-speech
Convert Text To Speech Using Python And Flask


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Explanation](#file-explanation)
  - [app.py](#apppy)
  - [templates/index.html](#templatesindexhtml)
  - [text_to_speech](#text_to_speech)
    - [components](#components)
      - [get_accent.py](#get_accentpy)
      - [textToSpeech.py](#texttospeechpy)
    - [constants](#constants)
    - [entity](#entity)
      - [config_entity.py](#config_entitypy)
    - [exception](#exception)
    - [logger](#logger)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```

2. Change into the project directory:
    ```sh
    cd Text-To-Speech
    ```

3. Create a virtual environment:
    ```sh
    python -m venv tts_env
    ```

4. Activate the virtual environment:

    On Windows:
    ```sh
    tts_env\Scripts\activate
    ```

    On macOS/Linux:
    ```sh
    source tts_env/bin/activate
    ```

5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

3. Use the dropdown to select an accent, enter text in the textbox, and click the "Submit" button to generate and play the audio file.


## File Explanation

### app.py
- **Description**: The main entry point for the Flask application.
- **Functionality**: Sets up the routes for the home page and the prediction endpoint.

### templates

#### index.html
- **Description**: The main HTML file containing the user interface for the text-to-speech application.
- **Functionality**: Includes a dropdown for accent selection, a textbox for input text, and a submit button to generate the audio.

### text_to_speech

#### artifact
- **tts_audio**: 
  - **Description**: Stores generated audio files.
- **tts_text**: 
  - **Description**: Stores input text files.

#### components

##### get_accent.py
- **Description**: Contains functions related to accents.
  - **Functions**:
    1. `get_accent_message()`: Retrieves available accent messages.
    2. `get_accent_tld()`: Retrieves the top-level domain (TLD) for the selected accent.

##### textToSpeech.py
- **Description**: Contains the `TTSapplication` class.
  - **Functions**:
    1. `text2speech(text, accent)`: Converts input text to speech using the GTTS library and saves the audio file.

#### constants
- **Description**: Holds constant values used across the project.

#### entity

##### config_entity.py
- **Description**: Defines configuration entities used for setting up the application.

#### exception
- **Description**: Defines custom exceptions for the application.

#### logger
- **Description**: Sets up logging configurations for the application.

## Additional Notes
- The `artifact` directory contains subdirectories for storing generated audio and text files.
- The `tts_env` directory is the virtual environment for the project.

Make sure to activate the virtual environment before running the application to ensure all dependencies are correctly installed.


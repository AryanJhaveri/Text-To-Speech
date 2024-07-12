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
- The main entry point for the Flask application. It sets up the routes for the home page and the prediction endpoint.

### templates

#### index.html
- The main HTML file containing the user interface for the text-to-speech application. It includes a dropdown for accent selection, a textbox for input text, and a submit button to generate the audio.

### text_to_speech

#### artifact
- Contains subdirectories `tts_audio` for storing generated audio files and `tts_text` for storing input text files.

#### components

##### get_accent.py
- Contains functions to get available accents and their corresponding top-level domains (TLDs).

##### textToSpeech.py
- Contains the `TTSapplication` class which handles the conversion of text to speech using the GTTS library.

#### constants
- Holds constant values used across the project.

#### entity

##### config_entity.py
- Defines configuration entities used for setting up the application.

#### exception
- Defines custom exceptions for the application.

#### logger
- Sets up logging configurations for the application.

## Additional Notes
- The `artifact` directory contains subdirectories for storing generated audio and text files.
- The `tts_env` directory is the virtual environment for the project.

Make sure to activate the virtual environment before running the application to ensure all dependencies are correctly installed.



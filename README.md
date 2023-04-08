# Hackfest'23

## TEAM MEMBERS:
* ATISH SHAH
* SHASHANK SHUKLA
* PRATYUSH RAJ
* ARYAN KSHIRSAGAR
* KAUSHAL SRIVASTAVA


## Table of contents
* [General info](#general-info)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

## General info
This project aims to create a Chrome extension voice bot that will help visually impaired individuals order food online. As part of this project, we will be integrating a speech-to-text library to enable the voice bot to convert the user's spoken commands into text.

## Prerequisites
To use the speech-to-text library, you will need to have the following installed:
* Python programming language
* Pyttsx3 library
* Google Cloud SDK

## Installation
* Install the Pyttsx3 library by running the following command:
```
$ pip install pyttsx3
```
* Install the Google Cloud SDK by following the instructions provided in the Google Cloud SDK documentation.
* Once the Google Cloud SDK is installed, set up a Google Cloud project and enable the Cloud Speech-to-Text API by following the instructions provided in the Google Cloud Speech-to-Text API documentation.

## Usage
* To use the speech-to-text library, you will need to import the library and authenticate with the Google Cloud project that you set up earlier.
* Then set up a speech recognizer and microphone using the speech_recognition library, listens for speech input, and converts the speech to text using the Google Cloud Speech-to-Text API.

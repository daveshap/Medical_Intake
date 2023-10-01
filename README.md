# Medical Device Disclaimer

This software, found under this repository and licensed under the MIT license, is an experimental project and is NOT a medical device. It is not intended to be used as a medical device or as a substitute for professional medical advice, diagnosis, or treatment. 

The software is designed to test artificial intelligence's ability to perform patient intake, chart notes, and offer investigative and diagnostic aid. However, it is important to note that this software has NOT been tested, validated, or approved by the Food and Drug Administration (FDA) or any other regulatory body for medical devices. 

The software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

The use of this software is purely for scientific inquiry and should not be used for diagnosing or treating health problems, or for prescribing any medication or other treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or interpreted from the software.

By using this software, you acknowledge and agree that you understand this disclaimer and that you use the software at your own risk. If you do not agree with this disclaimer, do not use the software. 

This disclaimer may be updated from time to time, and it is the responsibility of the user to review and comply with the current version of the disclaimer.

# Usage

It's pretty much automatic. Just fire up `chat.py` and it will take you through the whole process. Everything will be saved out to `logs/`


# Symptom Sage Chatbot

Symptom Sage is an interactive chatbot that aids in capturing patient symptoms and generating assessments, facilitating smoother patient-intake processes.

## Features

- **Interactive Conversations**: Engage in real-time conversations with the chatbot to describe symptoms.
- **Assessment Generation**: Receive risk and category assessments based on the provided symptoms.
- **Report Generation**: Generate a detailed report including hypothesis, clinical assessment guide, and referral recommendations.
- **Downloadable Outputs**: Download the generated assessments and reports for further use.
- **User-Friendly Interface**: A web-based interface built with Streamlit for ease of use.
- **Modular Codebase**: A clean, modular codebase ensuring easy maintenance and updates.
- **FAISS KB search**:Is able to have hypothesis re-inforced with domain specific information
## Installation

1. Clone this repository:

git clone https://github.com/Gravtas-J/symptom-sage-chatbot.git
cd symptom-sage-chatbot


2. Install the required packages:

pip install -r requirements.txt


3. Run Streamlit:

streamlit run GUI.py

or for embedded search feature:

streamlit run GUI_embed.py

If you are wanting to use local embedded VS store make sure you have a file "embeddings.pkl" - my other repo https://github.com/Gravtas-J/EMBEDATRON3000 can help if you don't have them. Not included for copywrite reasons. 


Now, open your web browser and go to `http://localhost:8501` to interact with the Symptom Sage Chatbot.

It can also be accessed over a network with 'http:[your IP]:8501

## Usage

1. Initiate a conversation by describing the patient's symptoms.
2. Click on "Generate Assessment" to receive risk and category assessments.
3. Click on "Generate Report" to receive a detailed report including hypothesis and clinical assessments.
4. Download the assessments and reports as needed.
5. Click "Reset Conversation" to start a new session.

## Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or create a pull request.

## License

Learning Use License Refer to LICENCE for further details 

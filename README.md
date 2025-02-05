🚀 **[Live Demo](https://jerryblessed.pythonanywhere.com/)**

# Light Talk

**Light Talk** is a smart, AI-powered consultancy platform designed to revolutionize the way clients connect with expert consultants. By leveraging Twilio’s robust messaging and calling APIs along with cutting-edge AI, Light Talk enables seamless communication via SMS, voice calls, and WhatsApp. The platform even features an interactive live avatar that simulates the expert's persona for a more engaging and personalized experience.

---

## Inspiration

In today’s fast-paced world, getting timely access to expert advice is more critical than ever. Traditional communication methods like emails and scheduled calls often result in delays and missed opportunities. Research indicates that businesses utilizing mobile messaging (e.g., SMS) experience up to a **45% faster response time** compared to email ([SAS Insights](https://www.sas.com/en_us/insights/articles/marketing/text-message-marketing.html)). Inspired by this, we set out to create a platform that makes expert consultancy both fast and accessible—regardless of physical location.

---

## What It Does

- **Instant Communication:**  
  Communicate instantly via:
  - **SMS:** Enjoy rapid responses (up to 45% faster than email).
  - **Voice Calls:** Have real-time, engaging conversations.
  - **WhatsApp:** Tap into a channel with over **2 billion users** worldwide ([Statista](https://www.statista.com/statistics/260819/number-of-monthly-active-whatsapp-users/)).

- **Live Avatar Interaction:**  
  Experience a human-like avatar that simulates expert interactions, making consultations feel more personal and engaging.

- **Flexible Pricing Plans:**  
  - **Free Version:** 3 minutes of consultation.
  - **Gold Plan:** 20 minutes daily for $30/month.
  - **Diamond Plan:** 1 hour daily for $85/month.

- **Verified Experts:**  
  We rigorously verify all consultants, ensuring that only qualified professionals are available for advice.

- **Seamless UI/UX:**  
  A clean, intuitive interface makes it easy for clients to reach out and receive timely guidance.

- **SaaS Model for Consultants:**  
  Consultants can also subscribe to our platform to offer their expertise, enabling them to connect with clients efficiently while generating recurring revenue.

---

![Light Talk Architecture](https://raw.githubusercontent.com/Jerryblessed/light-talk/refs/heads/main/diagram-export-2-5-2025-11_08_15-PM%5B1%5D.png)

## How We Built It

- **Backend:**  
  - Built using Python and Flask for a lightweight, scalable server.
  - Integrated with Twilio’s APIs to handle SMS, voice, and WhatsApp communication.

- **Frontend:**  
  - Developed with Bootstrap for responsive and modern design.
  - Simple, intuitive UI/UX ensuring an effortless user experience.

- **Security & Configuration:**  
  - Sensitive credentials are managed via a `.env` file using `python-dotenv` for secure environment variable management.
  - Dependencies include `itsdangerous`, `flask>=0.9`, `six`, `twilio>=6.0.0`, and `python-dotenv`.

- **Scalability:**  
  Designed as a SaaS, Light Talk is ready to grow with your business—from individual consultants to larger consultancy firms.

---

## Installation

### Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)
- A Twilio account with valid credentials

### Dependencies

The project depends on:
```
itsdangerous
flask>=0.9
six
twilio>=6.0.0
python-dotenv
```

Install dependencies via:

```bash
pip install -r requirements.txt
```

### Setup

#### Clone the Repository:
```bash
git clone https://github.com/yourusername/light-talk.git
cd light-talk
```

#### Create a .env File:
In the root directory, create a `.env` file with the following contents (replace placeholder values with your actual keys):

```
TWILIO_ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
TWILIO_FROM=YOUR_TWILIO_PHONE_NUMBER
TWILIO_CONVERSATION_ID=YOUR_TWILIO_CONVERSATION_ID
SECRET_KEY=YOUR_SECRET_KEY
AZURE_SPEECH_API_KEY=YOUR_AZURE_SPEECH_API_KEY
AZURE_OPENAI_ENDPOINT=YOUR_AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY=YOUR_AZURE_OPENAI_API_KEY
STT_LOCALES=en-US,de-DE,es-ES,fr-FR,it-IT,ja-JP,ko-KR,zh-CN
TTS_VOICE=en-GB-RyanNeural
```

#### Run the Application:
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`.

---

## Project Structure
```
light-talk/
├── example.py              # Main Flask application
├── requirements.txt    # List of Python dependencies
├── .env                # Environment variables (not tracked in version control)
├── templates/          # HTML templates
│   └── example.html    # Main interface for consultancy communication
│   └── chat.html       # Main interface for avatar consultancy communication
├── static/             # Static assets (CSS, JS, images)
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── chat.js
└── README.md           # This file
```

---

## Contributing

We welcome contributions from the community! If you’d like to enhance Light Talk or fix a bug, please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you’d like to modify.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or feedback, please contact Your Name.

---

## Flask-Twilio

Make Twilio voice/SMS calls with Flask

[![Build Status](https://travis-ci.org/lpsinger/flask-twilio.svg?branch=master)](https://travis-ci.org/lpsinger/flask-twilio)  
[![Doc Status](https://readthedocs.org/projects/flask-twilio/badge/?version=latest)](http://flask-twilio.readthedocs.io/en/latest/)


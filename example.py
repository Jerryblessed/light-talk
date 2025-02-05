#!/usr/bin/env python
"""
Demo Flask-Twilio application with environment variables.
"""

import os
import socket
from dotenv import load_dotenv
from flask import flash, Flask, render_template, request
from flask_twilio import Twilio, Response
from twilio.base.exceptions import TwilioRestException
from twilio.twiml.messaging_response import Message
from twilio.twiml.voice_response import Say
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Azure openAI configuration
load_dotenv()


# Application configuration
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))
app.config['TWILIO_ACCOUNT_SID'] = os.getenv('TWILIO_ACCOUNT_SID')
app.config['TWILIO_AUTH_TOKEN'] = os.getenv('TWILIO_AUTH_TOKEN')
app.config['TWILIO_FROM'] = os.getenv('TWILIO_FROM', '+16085576875')
TWILIO_CONVERSATION_ID = os.getenv('TWILIO_CONVERSATION_ID')

twilio = Twilio(app)
client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/twiml')
@twilio.twiml
def test_call():
    """View for producing the TwiML document."""
    say = request.values.get('say', '1')
    sms = request.values.get('sms', '1')
    custom_message = request.values.get('custom_message', 'Default Message')
    send_whatsapp = request.values.get('send_whatsapp', 'off') == 'on'
    
    resp = Response()
    if say == '1':
        resp.append(Say(custom_message, voice='female'))
    if sms == '1':
        resp.append(Message(custom_message))

    # Send WhatsApp message if the checkbox is checked
    if send_whatsapp and TWILIO_CONVERSATION_ID:
        try:
            message = client.conversations \
                .v1 \
                .conversations(TWILIO_CONVERSATION_ID) \
                .messages \
                .create(author='system', body=custom_message)
                
            flash(f"WhatsApp message sent: {message.sid}", 'success')
        except TwilioRestException as e:
            flash(f"Failed to send WhatsApp message: {e.msg}", 'danger')

    return resp


@app.route('/', methods=['GET'])
def index_get():
    """Main form view."""
    return render_template('example.html', to=request.values.get('to', app.config['TWILIO_FROM']))


@app.route('/', methods=['POST'])
def index_post():
    """Main form action."""
    try:
        call_selected = 'call' in request.form.getlist('call_option')
        sms_selected = 'sms' in request.form.getlist('call_option')
        whatsapp_selected = 'whatsapp' in request.form.getlist('call_option')

        to = request.form.get('to', app.config['TWILIO_FROM'])
        custom_message = request.form.get('custom_message', 'Jesus Loves You 😁')

        if call_selected:
            twilio.call_for('test_call', to, say='1', sms='0', custom_message=custom_message)

        if sms_selected:
            client.messages.create(
                body=custom_message,
                from_=app.config['TWILIO_FROM'],
                to=to
            )

        if whatsapp_selected and TWILIO_CONVERSATION_ID:
            try:
                message = client.conversations \
                    .v1 \
                    .conversations(TWILIO_CONVERSATION_ID) \
                    .messages \
                    .create(author='system', body=custom_message)
                
                flash(f"WhatsApp message sent: {message.sid}", 'success')
            except TwilioRestException as e:
                flash(f"Failed to send WhatsApp message: {e.msg}", 'danger')

        flash('Request was successfully sent.', 'success')

    except TwilioRestException as e:
        flash(f'Failed to process request: {e.msg}', 'danger')

    return index_get()


# Start application
if __name__ == '__main__':
    app.run(debug=True)

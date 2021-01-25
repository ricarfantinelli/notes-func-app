import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:
    value = "Sending email from my Azure Functions HTTP Trigger (Ricardo)"
    message = {
        "personalizations": [ {
          "to": [{
            "email": "fantaere@gmail.com"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] Email test - Ricardo",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Email has been successfully sent.")
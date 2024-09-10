# Cybersecurity-Projects 👷
~ Gaining practical experience in cybersecurity with projects, labs and code.

## 1. Tracking Pixel ♓
Did you know you can do a lot of things just with a simple email. An attacker or malicious user harvest information from the target using a tracking pixel.

You can embed a very small, 1x1 size image or gif, which is practically invisible to eyes (specially when it's transparent).

- Attacker: Hosts the `pixel.jpg` file and embeds it to `harmless_mail.eml`. Then serves it through a simple server `tracking_server.py`
- Victim: Opens the email file `harmless_mail.eml` and loads the remote content (the pixel image)

Upon opening the email, the `user-agent` details will be known to the attacker.

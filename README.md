# EmailSender

`EmailSender` is a Python class designed to simplify sending emails through an SMTP server. With this utility, you can easily send emails with a subject and message body, using a configurable SMTP server and credentials.

---

## Features

- Send emails via an SMTP server (e.g., Gmail, Yahoo, etc.).
- Secure communication using TLS.
- Easy-to-use interface with clear methods and arguments.

---

## Installation

1. Clone the repository or download the file containing the `EmailSender` class:

   ```bash
   git clone https://github.com/mhrafin/Send-Email.git
   cd Send-Email
   ```

2. Ensure you have Python 3.x installed on your machine.

---

## Usage

### Example Code

```python
from email_sender import EmailSender

# Initialize EmailSender
email = EmailSender(
    smtp_host="smtp.gmail.com", 
    sender_email="your_email@gmail.com", 
    sender_password="your_app_password"
)

# Send an email
email.send_email(
    recipient_email="recipient_email@example.com",
    subject="Hello!",
    email_body="This is a test email sent using EmailSender."
)
```

### Parameters

#### Constructor (`__init__`)

- **`smtp_host` (str):** The SMTP server address (e.g., `smtp.gmail.com`).
- **`sender_email` (str):** The email address of the sender.
- **`sender_password` (str):** The password or app-specific password of the sender.

#### Method (`send_email`)

- **`recipient_email` (str):** The email address of the recipient.
- **`subject` (str):** The subject of the email.
- **`email_body` (str):** The body content of the email.

---

## Requirements

- Python 3.6+
- Internet connection to access the SMTP server
- SMTP server credentials (e.g., Gmail requires app-specific passwords for security)

---

## Notes

1. For Gmail users, enable "Less Secure Apps" or create an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for better security.
2. Ensure your SMTP host, email, and password are valid before running the program.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or additional features.

---

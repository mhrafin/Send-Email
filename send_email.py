import smtplib


class EmailSender:
    """Handles sending emails via an SMTP server."""

    def __init__(self, smtp_host: str, sender_email: str, sender_password: str) -> None:
        """
        Constructs the EmailSender instance.

        Args:
            smtp_host (str): The SMTP server address (e.g., 'smtp.gmail.com').
            sender_email (str): The email address of the sender.
            sender_password (str): The password or app-specific password of the sender.
        """
        self.smtp_host = smtp_host
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, email_body: str) -> None:
        """
        Sends an email with the specified subject and body.

        Args:
            recipient_email (str): The email address of the recipient.
            subject (str): The subject of the email.
            email_body (str): The body of the email.
        """
        try:
            with smtplib.SMTP(self.smtp_host) as connection:
                connection.starttls()
                connection.login(user=self.sender_email, password=self.sender_password)
                connection.sendmail(
                    from_addr=self.sender_email,
                    to_addrs=recipient_email,
                    msg=f"Subject: {subject}\n\n{email_body}",
                )
        except Exception as e:
            print(f"Failed to send email: {e}")

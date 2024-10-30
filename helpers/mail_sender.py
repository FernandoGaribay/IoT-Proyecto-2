import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import modules.mail_credentials as credentials

sender_email = credentials.SENDER_EMAIL
sender_password = credentials.SENDER_PASSWORD
subject = "QuantumBank Correspondence"

class MailSender():
    
    def send_email(self, recipient_email, message = None, folder_path=None):
        try:
            if not os.path.isdir(folder_path):
                print(f"La ruta {folder_path} no es una carpeta válida.")
                return

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename={filename}')
                        msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)

            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)

            server.quit()
            print(f"Correo enviado a {recipient_email} con éxito, incluyendo los archivos de {folder_path}.")

        except Exception as e:
            print(f"Ocurrió un error al enviar el correo: {e}")
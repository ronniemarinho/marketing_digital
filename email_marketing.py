import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_host = 'smtp.gmail.com'  # Insira o host do servidor SMTP
smtp_port = 465  # Insira a porta do servidor SMTP
smtp_usuario = 'fatecadamantinaemail@gmail.com'  # Insira seu endereço de e-mail
#smtp_usuario = 'ronnieshida@gmail.com'  # Insira seu endereço de e-mail

smtp_senha = 'fatecadamantinaemail0*'  # Insira sua senha de e-mail
#smtp_senha = 'Niltonilda1*'  # Insira sua senha de e-mail


# Criar uma mensagem de e-mail
msg = MIMEMultipart()
msg['From'] = smtp_usuario
msg['To'] = 'ronnieshida@gmail.com'
msg['Subject'] = 'Email marketing'

# Adicionar corpo do e-mail
mensagem = 'Olá,\n\nEste é um exemplo de e-mail enviado usando Python.\n\nAtenciosamente,\nSeu Nome'
msg.attach(MIMEText(mensagem, 'plain'))

# Conectar ao servidor SMTP e enviar e-mail
try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_usuario, smtp_senha)
    server.sendmail(smtp_usuario, 'destinatario@example.com', msg.as_string())
    server.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Falha ao enviar e-mail: {e}")

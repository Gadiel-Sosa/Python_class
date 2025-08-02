class Email:
    def enviar(self):
        print('Enviar email...')
        
class Sms:
    def enviar(self):
        print('Enviar SMS...')
        
class Push:
    def enviar(self):
        print('Notificación push...')
        
def hacer_notificación(notificacion):
    notificacion.enviar()

email = Email()
sms = Sms()
push = Push()

email.enviar()
sms.enviar()
push.enviar()
    
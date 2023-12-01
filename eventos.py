class EventManager:
    def __init__(self):
        # Inicializa un diccionario para almacenar a los suscriptores
        self.subscribers = {}

    def subscribe(self, event, callback):
        # Suscribe un callback a un evento particular
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        # Cancela la suscripción del callback al evento
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)

    def notify(self, event, data=None):
        # Notifica a todos los suscriptores del evento con los datos indicados
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)

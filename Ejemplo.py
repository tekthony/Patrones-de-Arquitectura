class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def emit(self, event_type):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback()

# Crear una instancia de EventBus
bus = EventBus()

# Definir una función suscriptora
def handle_event():
    print("¡Evento manejado!")

# Suscribir la función al evento 'evento'
bus.subscribe('evento', handle_event)

# Emitir el evento 'evento'
bus.emit('evento')

# Resultado esperado:
# ¡Evento manejado!

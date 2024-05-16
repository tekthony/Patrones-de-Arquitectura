# Patrones arquitectonicos:
> [!NOTE]
> 👍 Un **patron arquitectonicos** es una solucion general y reutilizable a un problema comun en la arquitectura de software dentro de un contexto
dado. Los patrones arquitectonicos son la habilidad de organizacion a nivel de carpetas dentro del proyecto de software

# Patrones arquitectonicos:

1. PATRON DE CAPAS
2. PATRON CLIENTE-SERVIDOR
3. PATRON MAESTRO-ESCLAVO
4. PATRON FILTRO DE TUBERIA
5. PATRON DE INTERMEDIARIO
6. PATRON DE IGUAL A IGUAL
7. PATRON DE BUS EVENTO
8. MODELO-VISTAS-CONTROLADOR
9. ARQUITECTURA LIMPIA
10. ARQUITECTURA HEXAGONAL



# Patron de `BUS EVENTO`

# `Tema 1: `

Introducción al Patrón de Bus Evento
## ¿Qué es el Patrón de Bus Evento?

El patrón de bus evento es un diseño arquitectónico utilizado en el desarrollo de software para facilitar la comunicación entre componentes de un sistema sin que estos componentes estén directamente acoplados. En lugar de que los componentes se comuniquen directamente entre sí, utilizan un "bus" de eventos centralizado para enviar y recibir mensajes.

## Propósito y Beneficios
El propósito principal del patrón de bus evento es desacoplar los componentes de un sistema, lo que mejora la modularidad, la reutilización y la mantenibilidad del código. Algunos de los beneficios clave incluyen:

• `Desacoplamiento:` Los componentes no necesitan conocer la existencia de otros componentes para comunicarse.

• `Flexibilidad:` Permite agregar, eliminar o modificar componentes sin afectar al resto del sistema.

• `Reusabilidad:` Los componentes pueden ser reutilizados en diferentes contextos sin modificar su lógica interna.

`Ejemplo:`

Imaginemos un sistema de gestión de eventos en una aplicación web. En lugar de que cada componente de la interfaz de usuario esté directamente conectado a los demás para comunicar cambios en los datos, se utiliza un bus de eventos. Cuando un componente modifica un dato relevante, emite un evento a través del bus. Otros componentes que están suscritos a ese tipo de evento pueden responder en consecuencia, actualizando su estado o realizando otras acciones.

# `Tema 2: `

Implementación del Patrón de Bus Evento en la Programación

Elementos del Patrón de Bus Evento

• `Emisor de Eventos:` Componente que genera eventos y los envía al bus de eventos.

• `Suscriptor:` Componente que se registra para recibir ciertos tipos de eventos del bus.

• `Evento:` Objeto que encapsula información relevante sobre un cambio o acción que ha ocurrido en el sistema.

## Ejm

``` python

class EventBus:
    def __init__(self):
        self.subscribers = {}  

# Diccionario para almacenar suscriptores por tipo de evento

# Método para suscribir una función a un tipo de evento

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = [] 

# Inicializa la lista de suscriptores si no existe

        self.subscribers[event_type].append(callback)  # Agrega la función de suscripción a la lista

# Método para emitir un evento

    def emit(self, event_type):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback()  # Llama a cada suscriptor asociado al evento

# Crear una instancia de EventBus

bus = EventBus()

# Función de suscripción al evento 'saludo'

def saludar():
    print("Hola mundo!")

# Función de suscripción al evento 'despedida'

def despedirse():
    print("Adiós mundo!")

# Suscribir las funciones a sus respectivos eventos

bus.subscribe('saludo', saludar)
bus.subscribe('despedida', despedirse)

# Emitir el evento 'saludo'

bus.emit('saludo')  

# Esto imprimirá "Hola mundo!"

# Emitir el evento 'despedida'

bus.emit('despedida')  

# Esto imprimirá "Adiós mundo!"

```



Mejores Prácticas y Consideraciones
Evitar exceso de acoplamiento: No todos los eventos deben pasar por el bus; utiliza el patrón de manera selectiva.
Gestión de errores: Implementa manejo de errores adecuado para eventos asíncronos.
Limpieza de suscripciones: Asegúrate de eliminar las suscripciones una vez que ya no sean necesarias para evitar posibles fugas de memoria.



# Tema 3: 

Aplicaciones del Patrón de Bus Evento en la Informática
Casos de Uso.

1. Aplicaciones Web Interactivas: Para actualizar la interfaz de usuario en respuesta a acciones del usuario.

2. Sistemas de Gestión de Eventos en Tiempo Real: Para notificar a los usuarios sobre eventos importantes en tiempo real.

3. Arquitecturas Orientadas a Eventos: En sistemas distribuidos donde diferentes componentes necesitan comunicarse de manera eficiente.
Ejemplo en Aplicación Web

Supongamos una aplicación de tablero de tareas colaborativo. Cuando un usuario agrega una nueva tarea, se emite un evento al bus de eventos. Los demás usuarios que estén visualizando el tablero recibirán este evento y podrán ver la nueva tarea sin necesidad de recargar la página.





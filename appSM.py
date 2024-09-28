from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.audio import SoundLoader  # Importa el reproductor de audio



class SM(ScreenManager):
    # A través de esta clase accedemos al diseño
    pass



class MainApp(MDApp):
    def build(self): # acá accedemos a un tema
        self.theme_cls.theme_style = 'Light' # al iniciar la app estará oscuro
        self.theme_cls.primary_palette = 'Teal' # paleta de color azul verdoso
        Builder.load_file('design.kv') # cargo el archivo kv

        self.sound = None  # Inicializar self.sound como None

        return SM() # Retorna clase para los screen
    
    # Método para cargar y reproducir sonido
    def load_sound(self):
        self.sound = SoundLoader.load('sound/audio_med.mp3')  # Reemplaza con la ruta de tu archivo
        if self.sound:
            self.sound.play()

    # Método para pausar el sonido
    def play_pause_sound(self):
        if not self.sound:
            return

        # Si el sonido se está reproduciendo, guarda la posición actual y detén el sonido
        if self.sound.state == 'play':
            self.position = self.sound.get_pos()  # Guarda la posición actual en segundos
            self.sound.stop()  # Detiene el sonido, pero la posición ya está guardada

        # Si el sonido está detenido, reprodúcelo desde la posición donde fue pausado
        else:
            if hasattr(self, 'position'):
                self.sound.seek(self.position)  # Usa el método seek() para reanudar desde la posición
            self.sound.play()  # Reproduce desde la última posición


    # Método para detener el sonido
    def stop_sound(self):
        # Verifica si self.sound está definido antes de intentar detener el sonido
        if self.sound and self.sound.state == 'play':
            self.sound.stop()
    
    # Para cambiar el estilo de la pantalla (negro a blanco)
    def change_style(self, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    
if __name__ == "__main__":
    MainApp().run()
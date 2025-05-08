from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

from view.gui.own_classes import BackgroundLabel

class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.contenedor = BoxLayout(orientation = "vertical",
                                    spacing = dp(5))
        self.contenedor_labels = GridLayout(cols = 2,
                                            spacing = dp(13),
                                            padding = dp(15),
                                            size_hint = (1, 1))

        with self.contenedor_labels.canvas.before:
            Color(0.98, 0.98, 0.98, 1)  
            self.bg_rect = Rectangle(pos=self.contenedor_labels.pos, size=self.contenedor_labels.size)
        
        self.contenedor_labels.bind(size = self._actualizar_background, pos = self._actualizar_background)

        self.titulo = BackgroundLabel(text = "Resultados",
                            font_size = 55,
                            height = 150,
                            size_hint = (1, None),
                            background_color = (0.25, 0.25, 0.3, 1))
        self.contenedor.add_widget(self.titulo)


        self.label_prima = BackgroundLabel(text = "Tu prima es:",
                                size_hint = (1 , None),
                                height = 100,
                                font_size = 30,
                                background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_prima)

        self.prima = TextInput(size_hint = (1 , None),
                                height = 100,
                                font_size = 25)
        self.contenedor_labels.add_widget(self.prima)


        self.label_cesantias = BackgroundLabel(text = "Tus cesantias son:",
                                    size_hint = (1 , None),
                                    height = 100,
                                    font_size = 30,
                                    background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_cesantias)

        self.cesantias = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25)
        self.contenedor_labels.add_widget(self.cesantias)


        self.label_intereses_cesantias = BackgroundLabel(text = "Tus intereses sobre las cesantias son:",
                                                size_hint = (1 , None),
                                                height = 100,
                                                font_size = 30,
                                                background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_intereses_cesantias)

        self.intereses_cesantias = TextInput(size_hint = (1 , None),
                                            height = 100,
                                            font_size = 25)
        self.contenedor_labels.add_widget(self.intereses_cesantias)


        self.label_vacaciones = BackgroundLabel(text = "tus vacaciones son:",
                                        size_hint = (1 , None),
                                        height = 100,
                                        font_size = 30,
                                        background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_vacaciones)

        self.vacaciones = TextInput(size_hint = (1 , None),
                                    height = 100,
                                    font_size = 25)
        self.contenedor_labels.add_widget(self.vacaciones)


        self.label_indemnizacion = BackgroundLabel(text = "tu indemnizacion es:",
                                        size_hint = (1 , None),
                                        height = 100,
                                        font_size = 30,
                                        background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_indemnizacion)

        self.indemnizacion = TextInput(size_hint = (1 , None),
                                        height = 100,
                                        font_size = 25)
        self.contenedor_labels.add_widget(self.indemnizacion)


        self.label_total_liquidacion = BackgroundLabel(text = "tu liquidacion es:",
                                            size_hint = (1 , None),
                                            height = 100,
                                            font_size = 30,
                                            background_color = (0.2, 0.2, 0.2, 1))
        self.contenedor_labels.add_widget(self.label_total_liquidacion)

        self.total_liquidacion = TextInput(size_hint = (1 , None),
                                            height = 100,
                                            font_size = 25)
        self.contenedor_labels.add_widget(self.total_liquidacion)

        self.contenedor.add_widget(self.contenedor_labels)

        self.regresar_inicio = Button(text = "Volver",
                            font_size = 30,
                            size_hint = (1, 0.15),
                            background_color = (0.18, 0.44, 0.75, 1))
        self.regresar_inicio.bind(on_press = self.volver_inicio)
        self.contenedor.add_widget(self.regresar_inicio)

        self.add_widget(self.contenedor)
    
    def _actualizar_background(self, *args):
        self.bg_rect.pos = self.contenedor_labels.pos
        self.bg_rect.size = self.contenedor_labels.size
    
    def actualizar_resultados(self, resultados):
        self.prima.text = resultados.get("prima", "0")
        self.cesantias.text = resultados.get("cesantias", "0")
        self.intereses_cesantias.text = resultados.get("intereses_cesantias", "0")
        self.vacaciones.text = resultados.get("vacaciones", "0")
        self.indemnizacion.text = resultados.get("indemnizacion", "0")
        self.total_liquidacion.text = resultados.get("total_liquidacion", "0")

    def volver_inicio(self, sender):
        self.manager.get_screen("main").reiniciar_calculadora()
        self.manager.current = "main"

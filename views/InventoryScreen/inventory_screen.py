from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, IconLeftWidget
from kivymd.uix.list import ThreeLineIconListItem
from kivy.clock import Clock

from utils import load_kv
import json
import bcrypt

load_kv(__name__)

class InventoryScreen(MDScreen):
    def buscar(self, item):
        #accedir a l'aplicació en execució
        app = MDApp.get_running_app()
        dataDispositius = app.getDeviceData()
        
        searchDevice = [search_field for search_field in dataDispositius if item.lower() in search_field['id_inventory'].lower()]
        
        #actualitzar la llista filtrada
        searchDeviceList = self.ids.list
        searchDeviceList.clear_widgets()
        
        for result in searchDevice:
            searchDeviceList.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                            icon="laptop"
                        ), 
                    
                    text=f"Dispositiu: {result['id_inventory']}",
                    secondary_text=f"Num Inv: {result['inventory_number']}",
                    tertiary_text=f"ID Disp: {result['id_device']}"
                    
                )
            )

    
    def on_enter(self, *args):
        Clock.schedule_once(self.load_data)
    
    def load_data(self, dt):
        scroll = ScrollView()
        
        print(open('assets/inventory.json').read()) #! NO VA..., no entra a l'on_start
        
        # Leer los datos del archivo "inventory.json"
        with open("assets/inventory.json", "r") as f:
            inventory = json.load(f)

        # Crear el layout principal
        layout = MDBoxLayout()
        layout.add_widget(scroll)

        # Crear la lista y añadir los elementos
        self.list = layout

        for device in inventory:
            item = ThreeLineIconListItem(
                IconLeftWidget(
                    icon="laptop",
                ),
                text=f"Dispositiu: {device['id_inventory']}",
                secondary_text=f"Num Inv: {device['inventory_number']}",
                tertiary_text=f"ID Disp: {device['id_device']}"
            )

            print(self)
            print(self.ids)
            app = MDApp.get_running_app()
            self.ids.list.add_widget(item)

        # obtenir la pantalla inventari
        current_screen = app.sm.get_screen("inventory")
        print('CURRENT SCREEN')
        print(current_screen)

        # retornem la llista de dispositius
        return layout
    
    def open_camera(self, *args):
        app = MDApp.get_running_app()
        app.root.current = "QR"
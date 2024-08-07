import flet as ft
import configparser
import os
def apply_theme(page: ft.Page, config: configparser.ConfigParser):
    page.theme_mode = config['DEFAULT']['theme']
    page.update()
    
def check_cfg(config: configparser.ConfigParser):
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            config['DEFAULT'] = {'theme': 'light', 'language': 'en'}
            config.write(configfile)     
            
def settings_page(page: ft.Page):
    config = configparser.ConfigParser()
    check_cfg(config)   
    def on_theme_change(e):
        config['DEFAULT']['theme'] = 'dark' if e.control.value else 'light'
        apply_theme(page, config)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            
    config.read('config.ini')
    
    page.add(ft.Checkbox(
        on_change=on_theme_change,
        label='Dark theme',
        value = (config['DEFAULT']['theme'] == 'dark')
    ))
    

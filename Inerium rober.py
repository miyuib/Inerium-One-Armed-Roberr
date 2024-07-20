import dearpygui.dearpygui as dpg
import os
import json
import time

CONFIG_DIR = os.path.join(os.path.expanduser("~"), "Documents", "inerium")
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

def save_config(filename):
    config = {
        "silent_aim": dpg.get_value("silent_aim"),
        "draw_fov": dpg.get_value("draw_fov"),
        "fov_scale": dpg.get_value("fov_scale"),
        "godmode": dpg.get_value("godmode"),
        "speedhack": dpg.get_value("speedhack"),
        "fov": dpg.get_value("fov"),
        "no_recoil": dpg.get_value("no_recoil"),
        "anti_aim": dpg.get_value("anti_aim"),
        "esp_box": dpg.get_value("esp_box"),
        "esp_line": dpg.get_value("esp_line"),
        "esp_guard": dpg.get_value("esp_guard"),
        "esp_card": dpg.get_value("esp_card"),
        "esp_vzlomitem": dpg.get_value("esp_vzlomitem"),
        "esp_player": dpg.get_value("esp_player"),
        "color": dpg.get_value("color"),
        "unlock_skills": dpg.get_value("unlock_skills")
    }
    try:
        with open(os.path.join(CONFIG_DIR, filename), 'w') as file:
            json.dump(config, file, indent=4)
        print(f"Config saved: {filename}")
        update_config_list()
    except Exception as e:
        print(f"Error saving config: {e}")

def load_config(filename):
    try:
        with open(os.path.join(CONFIG_DIR, filename), 'r') as file:
            config = json.load(file)
            for key, value in config.items():
                if dpg.does_item_exist(key):
                    dpg.set_value(key, value)
        print(f"Loaded config data: {filename}")
    except FileNotFoundError:
        print("Config file not found")
    except Exception as e:
        print(f"Error loading config: {e}")

def list_configs():
    return [f for f in os.listdir(CONFIG_DIR) if f.endswith(".json")]

def update_config_list():
    dpg.configure_item("config_list", items=list_configs())

def delete_config(filename):
    try:
        os.remove(os.path.join(CONFIG_DIR, filename))
        update_config_list()
        print(f"Deleted config: {filename}")
    except Exception as e:
        print(f"Error deleting config: {e}")

def setup_gui():
    dpg.create_context()
    dpg.create_viewport(title='Game Cheat Menu', width=800, height=600, resizable=False)
    dpg.setup_dearpygui()

    with dpg.handler_registry():
        dpg.add_key_down_handler(key=dpg.mvKey_Insert, callback=lambda s, a: toggle_viewport())

    with dpg.window(label="INERIUM | One-Armed-Robber", width=800, height=600, tag="main_window"):
        with dpg.tab_bar():
            with dpg.tab(label="Aim"):
                dpg.add_checkbox(label="Silent Aim", tag="silent_aim")
                dpg.add_checkbox(label="Draw FOV", tag="draw_fov")
                dpg.add_slider_float(label="FOV Scale", default_value=1.0, min_value=0.1, max_value=100.0, tag="fov_scale")

            with dpg.tab(label="Player"):
                dpg.add_checkbox(label="GodMode", tag="godmode")
                dpg.add_checkbox(label="Speedhack", tag="speedhack")
                dpg.add_slider_float(label="FOV", default_value=1.0, min_value=0.1, max_value=100.0, tag="fov")
                dpg.add_checkbox(label="No Recoil", tag="no_recoil")
                dpg.add_checkbox(label="Anti Aim", tag="anti_aim")
                dpg.add_button(label="Kill Guard", callback=lambda: print("Kill Guard activated"))
                dpg.add_button(label="Kill Player", callback=lambda: print("Kill Player activated"))
                dpg.add_button(label="Open All Doors", callback=lambda: print("Open All Doors activated"))
                dpg.add_button(label="Open All Windows", callback=lambda: print("Open All Windows activated"))
                dpg.add_button(label="Disable cam/gurd", callback=lambda: print("Disable Fuel activated"))

            with dpg.tab(label="ESP"):
                dpg.add_checkbox(label="ESP Box", tag="esp_box")
                dpg.add_checkbox(label="ESP Line", tag="esp_line")
                dpg.add_checkbox(label="ESP Guard", tag="esp_guard")
                dpg.add_checkbox(label="ESP Card", tag="esp_card")
                dpg.add_checkbox(label="ESP Vzlomitem", tag="esp_vzlomitem")
                dpg.add_checkbox(label="ESP Player", tag="esp_player")
                dpg.add_color_picker(label="Color", tag="color")

            with dpg.tab(label="Free"):
                dpg.add_checkbox(label="Unlock Skills", tag="unlock_skills")
                dpg.add_button(label="Give 1,000,000$", callback=lambda: print("Give 1,000,000$ activated"))
                dpg.add_button(label="Give 10,000,000$", callback=lambda: print("Give 10,000,000$ activated"))
                dpg.add_button(label="github(nowork)", callback=lambda: print("Donate activated"))

            with dpg.tab(label="Config"):
                dpg.add_input_text(label="Config Name", tag="config_name", default_value="config.json")
                dpg.add_button(label="Save Config", callback=lambda: save_config(dpg.get_value("config_name")))
                dpg.add_button(label="Load Config", callback=lambda: load_config(dpg.get_value("config_name")))
                dpg.add_button(label="Refresh List", callback=update_config_list)
                dpg.add_listbox(label="Config List", items=list_configs(), tag="config_list")
                dpg.add_button(label="Delete Config", callback=lambda: delete_config(dpg.get_value("config_list")))

    dpg.show_viewport()

    try:
        while True:
            dpg.render_dearpygui_frame()
            time.sleep(0.05)
    except KeyboardInterrupt:
        dpg.destroy_context()

def toggle_viewport():
    viewport = dpg.get_viewport()
    if viewport['visible']:
        dpg.hide_viewport()
    else:
        dpg.show_viewport()

if __name__ == "__main__":
    setup_gui()


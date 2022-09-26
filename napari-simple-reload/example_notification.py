from napari.settings import get_settings
from napari import run, Viewer
import logging

settings = get_settings()
settings.application.console_notification_level = "debug"
settings.application.gui_notification_level = "debug"
viewer = Viewer()
viewer.window.add_plugin_dock_widget("napari-simple-reload", "Autogenerated")
logging.getLogger("napari_simple_reload").setLevel(logging.DEBUG)
run()

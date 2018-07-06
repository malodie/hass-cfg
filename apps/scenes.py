import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#

class Scenes(hass.Hass):

  def initialize(self):
      self.listen_state(self.scene_change, "input_select.office_scene")

  def scene_change():
      option = self.select_option("input_select.office_scene")
      self.call_service(self, hue.hue_activate_scene, group_name = "Office", scene_name = option)

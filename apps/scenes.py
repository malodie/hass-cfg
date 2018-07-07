import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#

class Scenes(hass.Hass):

  def initialize(self):
      self.listen_state(self.scene_change, "input_select.office_scene")
      self.log("At least it started.")

  def scene_change(self, entity, attribute, old, new, kwargs):
      option = self.get_state("input_select.office_scene")
      self.log(option)
      self.log("Okay, we also got the change")
      self.call_service(self, hue.hue_activate_scene, group_name = "Office", scene_name = option)

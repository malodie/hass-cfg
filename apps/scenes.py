import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#

class Scenes(hass.Hass):

  def initialize(self):
      self.log("At least it started.")
      self.listen_state(self.scene_change, "input_select.office_scene")

  def scene_change(self, entity, attribute, old, new, kwargs):
      option = self.get_state("input_select.office_scene")
      self.log(option)
      self.log("Okay, we also got the change")
      outputting = self.call_service("hue/hue_activate_scene", group_name = "Office", scene_name = option)
      self.log(outputting)

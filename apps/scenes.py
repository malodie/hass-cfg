import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#

class Scenes(hass.Hass):

  def initialize(self):
      self.location = self.args['location']
      self.selector = self.args['selector']
      self.listen_state(self.scene_change, "input_select.office_scene", self.location, self.selector)

  def scene_change(self, entity, attribute, old, new, kwargs):
      option = self.get_state("input_select.office_scene")
      self.log("Changing the light temp.")
      self.call_service("hue/hue_activate_scene", group_name = "Office", scene_name = option)

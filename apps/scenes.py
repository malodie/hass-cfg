import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#

class Scenes(hass.Hass):

  def initialize(self):
      select = self.args["selector"]
      loc = self.args["location"]
      self.log("Aww yiss")
      self.log(select)
      self.log(loc)
      self.listen_state(self.scene_change, self.args["selector"])

  def scene_change(self, entity, attribute, old, new):
      self.log(select)
      self.log(loc)
      self.log(self.args["selector"])
      self.log(self.args["location"])
      option = self.get_state(self.args["selector"])
      self.log("Changing the light temp.")
      self.call_service("hue/hue_activate_scene", group_name = self.args["location"], scene_name = option)

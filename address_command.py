import sublime_plugin

class AddressbarCommand(sublime_plugin.WindowCommand):
	on_done = None
	on_change = None
	on_cancel = None

	def run(self):
		self.window.show_input_panel(
			'Address',
			self.window.active_view().file_name(),
			self.on_done,
			self.on_change,
			self.on_cancel
		)

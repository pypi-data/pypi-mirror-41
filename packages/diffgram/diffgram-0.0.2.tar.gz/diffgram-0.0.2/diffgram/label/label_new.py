import warnings


def label_new(self, 
			  label,
			  ignore_duplicates=True):
	"""

	Arguments
		self,
		label_list, a list of label strings
		
	Expects

	Returns

	"""

	# Check if already exists
	name = label.get('name', None)
	if not name:
		raise Exception("Please provide a key of name with a value of label")

	label_file_id = self.name_to_file_id.get(name, None)

	if ignore_duplicates is True:
		if label_file_id:
			warnings.warn("\n\n '" + name + "' label already exists and was skipped." + \
				"\n Set ignore_duplicates = False to bypass this check. \n")
			return

	endpoint = "/api/v1/project/" + self.project_string_id + \
			   "/label/new"

	response = self.session.post(self.host + endpoint,
								 json = label)

	data = response.json()

	if data["log"]["success"] == True:
		pass
	else:
		raise Exception(data["log"]["errors"])
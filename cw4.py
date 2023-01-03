def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for users in group_dictionary:
		# Now go through the users in the group
		for user in group_dictionary[users]:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
            user_groups("{}".format(users)) = group_dictionary[users][user]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
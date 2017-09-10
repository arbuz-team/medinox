
export let list_configs = {};

list_configs.register = {
	username:           'length_3',
	password:           'safety_password',
	email:              'email_no_in_db',
};

list_configs.login = {
	email:              'email',
	password:           'password_login',
};

list_configs.user_address = {
	full_name:          'full_name',
	address_line:       'no_empty',
	city:               'proper_name',
	region:             'proper_name',
	postcode:           'no_empty',
	country:            'proper_name',
};

list_configs.root_address = {
	full_name:          'proper_name',
	address_line:       'no_empty',
	city:               'proper_name',
	region:             'proper_name',
	postcode:           'no_empty',
	country:            'proper_name',
	email:              'email',
};

list_configs.forgot_password = {
	email:              'email_in_db',
};

list_configs.email_contact = {
	client:             'proper_name',
	email:              'email',
	message:            'no_empty',
};
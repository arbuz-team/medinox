
export let list_configs = {};

list_configs.register = {
	email:              'email_no_in_db',
	username:           'length_3',
	phone:              'length_3',
	password:           'safety_password',
};

list_configs.login = {
	email:              'email',
	password:           'password_login',
};

list_configs.user_address = {
	name:               'proper_name',
	surname:            'proper_name',
	address_line:       'no_empty',
	city:               'proper_name',
	region:             'proper_name',
	postcode:           'no_empty',
	country:            'proper_name',
};

list_configs.root_address = {
	name:               'proper_name',
	surname:            'proper_name',
	address_line:       'no_empty',
	city:               'proper_name',
	region:             'proper_name',
	postcode:           'no_empty',
	country:            'proper_name',
	email:              'email',
};

list_configs.shop_address = {
	name:               'proper_name',
	surname:            'proper_name',
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

list_configs.change_password = {
	password:            'safety_password',
};

list_configs.email_contact = {
	client:             'proper_name',
	email:              'email',
	message:            'no_empty',
};
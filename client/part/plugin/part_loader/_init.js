/**
 * Created by mrskull on 17.07.17.
 */

import * as data_utilities from '../../../arbuz/js/data_utilities'


export function Part_Loader(config)
{

	if(typeof config === 'undefined')
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}


	this.settings = {
		name: undefined,
		url: undefined,

		container: undefined,

		duration_show: 150,
		duration_hide: 100,

		opacity_show: 1,
		opacity_hide: 0.4,
	};


	// -- Load settings
	data_utilities.add_to_settings(config, this, 'name');
	data_utilities.add_to_settings(config, this, 'container');

	data_utilities.add_to_settings(config, this, 'duration_show');
	data_utilities.add_to_settings(config, this, 'duration_hide');

	data_utilities.add_to_settings(config, this, 'opacity_show');
	data_utilities.add_to_settings(config, this, 'opacity_hide');


	this.variables = {
		url: undefined,
		post_data: undefined,
		reload: false,

		error: undefined,
		external_callback: undefined,

		can_do_load: true,
		can_do_redirect: true,
		redirect_time_out: undefined,
	};
}
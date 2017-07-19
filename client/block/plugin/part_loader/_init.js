/**
 * Created by mrskull on 17.07.17.
 */

import {add_to_settings} from 'arbuz/plugin/utilities/data'


export function Part_Loader(config)
{

	if(typeof config === 'undefined')
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}


	this._settings = {
		part_name: 		undefined,
		post_name: 		undefined,

		container: 		undefined,

		duration_show: 	150,
		duration_hide: 	100,

		opacity_show: 	1,
		opacity_hide: 	0.4,
	};

	this._variables = {
		post_url: 			undefined,
		post_data: 			undefined,

		external_callback: 	undefined,
		redirect_time_out: 	undefined,
	};

	this._state = {
		reload: 			false,

		can_do_load: 		true,
		can_do_redirect: 	true,
	};


	// -- Load settings
	add_to_settings(config, this, 'part_name');
	this._settings.post_name = '__'+ this._settings.part_name +'__';

	add_to_settings(config, this, 'container');

	add_to_settings(config, this, 'duration_show');
	add_to_settings(config, this, 'duration_hide');

	add_to_settings(config, this, 'opacity_show');
	add_to_settings(config, this, 'opacity_hide');

}
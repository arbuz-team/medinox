/**
 * Created by mrskull on 07.01.17.
 */

import {Part_Loader_Part}     			from 'part/plugin/part_loader/part'
import {Plugins_Motion_Controllers} 	from 'part/plugin/part_motion/controllers'
import {Form_Controllers}  				from 'form/js/controllers'
import {Post_Button_Controllers}        from 'form/plugin/post_button/controllers'


/**
 *    Defining private variables
 */

let
	container = '.searcher',

	config_loader = {
		name: 'searcher',
		container: container,
	},


	searcher_loader = new Part_Loader_Part(config_loader),

	searcher_motion_controllers = new Plugins_Motion_Controllers({
		container: '#SEARCHER',
		content: container,
		open: 'right',
		can_open_by: 'width',
		can_open_to: 1000,
		duration_open: 200,
		duration_close: 200,
	}),

	post_button_controllers = new Post_Button_Controllers({
		container: '#SEARCHER'
	}),

	searcher_form_controllers = new Form_Controllers(config_loader);


/**
 *    Defining public functions
 */

export let

	define = function()
	{
		APP.add_own_event('searcher_open', searcher_motion_controllers.plugin_open);

		searcher_motion_controllers.define();
		searcher_form_controllers.define();
		post_button_controllers.define();
	},


	get_content = function()
	{
		searcher_loader.define();
		searcher_loader.load_content();

		searcher_motion_controllers.set_start_position();
	};


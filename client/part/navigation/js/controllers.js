/**
 * Created by mrskull on 24.11.16.
 */

import {Part_Loader_Part}     			from 'part/plugin/part_loader/part'
import {Plugins_Motion_Controllers}     from 'part/plugin/part_motion/controllers'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'


/**
 *    Defining private variables
 */

let
	navigation_loader = new Part_Loader_Part({
		name: 'navigation',
		url: '/navigation/',

		container: '#NAVIGATION .navigation',

		auto_first_loading: true,
	}),

	navigation_motion_controllers = new Plugins_Motion_Controllers({
		container: '#NAVIGATION',
		content: '.navigation',
		open: 'down',

		can_open_by: 'width',
		can_open_to: 675,

		duration_open: 300,
		duration_close: 150,
	}),

	event_button_controllers = new Event_Button_Controllers({
		container: '#NAVIGATION'
	});


/**
 *    Defining public functions
 */

export let
	define = function()
	{
		APP.add_own_event('navigation_close', navigation_motion_controllers.plugin_close);
		APP.add_own_event('navigation_open', navigation_motion_controllers.plugin_open);

		navigation_motion_controllers.define();
		event_button_controllers.define();
	},


	get_content = function()
	{
		navigation_loader.define();
		navigation_loader.load_content();

		navigation_motion_controllers.set_start_position();
	},


	plugin_open = function()
	{
		navigation_motion_controllers.plugin_open();
	};



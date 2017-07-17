/**
 * Created by mrskull on 07.01.17.
 */

import {Part_Loader_Part}     			from '../../plugin/part_loader/part'
import {Plugins_Motion_Controllers}     from '../../plugin/part_motion/controllers'
import {Form_Controllers}               from '../../../form/js/controllers'
import {Post_Button_Controllers}        from '../../../form/plugin/post_button/controllers'
import {Event_Button_Controllers}       from '../../../form/plugin/event_button/controllers'


/**
 *    Defining private variables
 */

let
	container = '.cart',

	config_loader = {
		name: 'cart',
		container: container,
		load_meta_tags: true,
	},


	cart_loader = new Part_Loader_Part(config_loader),

	cart_motion_controllers = new Plugins_Motion_Controllers({
		container: '#CART',
		content: container,
		open: 'left',
		can_open_by: 'width',
		can_open_from: 0,
		duration_open: 200,
		duration_close: 200,
	}),

	post_button_controllers = new Post_Button_Controllers({
		container: '#CART > '+ container,
	}),

	event_button_controllers = new Event_Button_Controllers({
		container: '#CART'
	}),

	cart_form_controllers = new Form_Controllers(config_loader),


	manage_key = function(event)
	{
		if(event.keyCode === 27)
			cart_motion_controllers.plugin_close();

		if(event.ctrlKey && event.shiftKey && event.keyCode === 88)
		{
			event.preventDefault();
			if(cart_motion_controllers.is_open())
				cart_motion_controllers.plugin_close();
			else
				cart_motion_controllers.plugin_open();
		}
	};


/**
 *    Defining public functions
 */

export let

	define = function()
	{
		APP.add_own_event('cart_open', cart_motion_controllers.plugin_open);
		APP.add_own_event('cart_close', cart_motion_controllers.plugin_close);
		APP.add_own_event('cart_open_or_close', open_or_close);

		$('body').keydown(manage_key);

		cart_form_controllers.define();
		cart_motion_controllers.define();
		post_button_controllers.define();
		event_button_controllers.define();
	},


	get_content = function()
	{
		cart_loader.define();
		cart_loader.load_content();
		cart_motion_controllers.set_start_position();
	},


	plugin_open = cart_motion_controllers.plugin_open,


	plugin_close = cart_motion_controllers.plugin_close,


	open_or_close = function()
	{
		APP.throw_event(EVENTS.part.close_navigation);

		if(cart_motion_controllers.is_open())
			plugin_close();
		else
			plugin_open();
	},


	reload = function()
	{
		cart_motion_controllers.plugin_open();
	};

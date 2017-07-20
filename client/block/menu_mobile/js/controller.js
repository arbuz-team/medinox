/**
 * Created by mrskull on 24.11.16.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/part'
import {Block_Motion_Controllers}     from 'block/plugin/block_motion/controller'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'



export function Menu_Mobile_Controller()
{
	if(typeof Menu_Mobile_Controller.instance === 'object')
		return Menu_Mobile_Controller.instance;

	Menu_Mobile_Controller.instance = this;


	let
		navigation_loader = new Block_Loader_Part({
			part_name: 'navigation',
			container: '#NAVIGATION .navigation',
		}),

		navigation_motion_controller = new Block_Motion_Controllers({
			container: '#NAVIGATION',
			content: '.navigation',
			open: 'down',

			can_open_by: 'width',
			can_open_to: 675,

			duration_open: 300,
			duration_close: 150,
		}),

		event_button_controller = new Event_Button_Controllers({
			container: '#NAVIGATION'
		});


	this.plugin_open = function()
	{
		navigation_motion_controller.plugin_open();
	};


	this.define = function()
	{
		APP.add_own_event('navigation_close', navigation_motion_controller.plugin_close);
		APP.add_own_event('navigation_open', navigation_motion_controller.plugin_open);

		navigation_motion_controller.define();
		event_button_controller.define();
	};


	this.get_content = function()
	{
		navigation_loader.define();
		navigation_loader.load_content();

		navigation_motion_controller.set_start_position();
	};
}



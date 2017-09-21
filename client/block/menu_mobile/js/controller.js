/**
 * Created by mrskull on 24.11.16.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/block'
import {Block_Motion_Controllers}       from 'block/plugin/block_motion/controller'
import {define_event_button}            from 'form/plugin/event_button/define'



export function Menu_Mobile_Controller()
{
	if(typeof Menu_Mobile_Controller.instance === 'object')
		return Menu_Mobile_Controller.instance;

	Menu_Mobile_Controller.instance = this;


	let
		container_id =          '#MENU_MOBILE',
		container =             '.menu_mobile',
		part_name =             'menu_mobile',

		loader = new Block_Loader_Part({
			part_name:          part_name,
			container:          container,
		}),

		motion_controller = new Block_Motion_Controllers({
			container:          container_id,
			content:            container,
			open:               'down',

			can_open_by:        'width',
			can_open_to:        675,

			duration_open:      300,
			duration_close:     150,
		});


	this.plugin_open = function()
	{
		motion_controller.plugin_open();
	};


	this.define = function()
	{
		APP.add_own_event(part_name +'_close', motion_controller.plugin_close);
		APP.add_own_event(part_name +'_open', motion_controller.plugin_open);

		motion_controller.define();
		define_event_button({
			container: container_id,
		});
	};


	this.get_content = function()
	{
		loader.define();
		loader.load_content();

		motion_controller.set_start_position();
	};
}



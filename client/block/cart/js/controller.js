/**
 * Created by mrskull on 07.01.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/block'
import {Block_Motion_Controllers}       from 'block/plugin/block_motion/controller'
import {Form_Controllers}               from 'form/js/controller'
import {define_post_button}             from 'form/plugin/post_button/define'
import {define_event_button}            from 'form/plugin/event_button/define'



export function Cart_Controller()
{
	if(typeof Cart_Controller.instance === 'object')
		return Cart_Controller.instance;

	Cart_Controller.instance = this;


	let
		container_id = '#CART',
		container = '.cart',
		part_name = 'cart',

		config_loader = {
			part_name: part_name,
			container: container,
		},


		cart_loader = new Block_Loader_Part(config_loader),
		cart_motion_controller = new Block_Motion_Controllers({
			container: container_id,
			content: container,
			open: 'left',
			can_open_by: 'width',
			can_open_from: 0,
			duration_open: 200,
			duration_close: 200,
		}),

		cart_form_controller = new Form_Controllers(config_loader),


		manage_key = function(event)
		{
			if(event.keyCode === 27)
				cart_motion_controller.plugin_close();

			if(event.ctrlKey && event.shiftKey && event.keyCode === 88)
			{
				event.preventDefault();
				if(cart_motion_controller.is_open())
					cart_motion_controller.plugin_close();
				else
					cart_motion_controller.plugin_open();
			}
		};



	this.plugin_open = () => cart_motion_controller.plugin_open();

	this.plugin_close = () => cart_motion_controller.plugin_close();


	this.open_or_close = () =>
	{
		APP.throw_event(EVENTS.part.close_menu_mobile);

		if(cart_motion_controller.is_open())
			this.plugin_close();
		else
			this.plugin_open();
	};


	this.reload = () =>
	{
		this.plugin_open();
	};


	this.define = () =>
	{
		APP.add_own_event('cart_open', this.plugin_open);
		APP.add_own_event('cart_close', this.plugin_close);
		APP.add_own_event('cart_open_or_close', this.open_or_close);

		$('body').keydown(manage_key);

		cart_form_controller.define();
		cart_motion_controller.define();
		define_event_button({
			container: container_id,
		});
		define_post_button(config_loader);
	};


	this.get_content = function()
	{
		cart_loader.define();
		cart_loader.load_content();
		cart_motion_controller.set_start_position();
	};
}
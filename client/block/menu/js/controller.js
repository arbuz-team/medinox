/**
 * Created by mrskull on 08.01.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/block'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'



export function Menu_Controller()
{
	if(typeof Menu_Controller.instance === 'object')
		return Menu_Controller.instance;

	Menu_Controller.instance = this;


	let
		header_loader = new Block_Loader_Part({
			part_name: 'menu',
			container: '.menu',
		}),

		event_button_controller = new Event_Button_Controllers({
			container: '#MENU'
		});


	this.get_height = function()
	{
		return $('#MENU').outerHeight();
	};


	this.define = function()
	{
		event_button_controller.define();
	};


	this.get_content = function()
	{
		header_loader.define();
		header_loader.load_content();
	};
}

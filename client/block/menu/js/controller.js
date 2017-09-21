/**
 * Created by mrskull on 08.01.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/block'
import {define_event_button}            from 'form/plugin/event_button/define'



export function Menu_Controller()
{
	if(typeof Menu_Controller.instance === 'object')
		return Menu_Controller.instance;

	Menu_Controller.instance = this;


	let
		container_id =          '#MENU',
		container =             '.menu',
		part_name =             'menu',


		loader = new Block_Loader_Part({
			part_name: part_name,
			container: container,
		});


	this.get_height = function()
	{
		return $(container_id).outerHeight();
	};


	this.define = function()
	{
		define_event_button({
			container: container_id
		});
	};


	this.get_content = function()
	{
		loader.define();
		loader.load_content();
	};
}

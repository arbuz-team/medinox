/**
 * Created by mrskull on 07.01.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/part'
import {Block_Motion_Controllers} 	from 'block/plugin/block_motion/controller'
import {Form_Controllers}  				from 'form/js/controller'
import {Post_Button_Controllers}        from 'form/plugin/post_button/controllers'



export function Search_Controller()
{
	if(typeof Search_Controller.instance === 'object')
		return Search_Controller.instance;

	Search_Controller.instance = this;


	let
		container = '.searcher',

		config_loader = {
			part_name: 'searcher',
			container: container,
		},


		searcher_loader = new Block_Loader_Part(config_loader),

		searcher_motion_controller = new Block_Motion_Controllers({
			container: '#SEARCHER',
			content: container,
			open: 'right',
			can_open_by: 'width',
			can_open_to: 1000,
			duration_open: 200,
			duration_close: 200,
		}),

		post_button_controller = new Post_Button_Controllers({
			container: '#SEARCHER',
			part_name: 'searcher',
		}),

		searcher_form_controller = new Form_Controllers(config_loader);



	this.define = function()
	{
		APP.add_own_event('searcher_open', searcher_motion_controller.plugin_open);

		searcher_motion_controller.define();
		searcher_form_controller.define();
		post_button_controller.define();
	};


	this.get_content = function()
	{
		searcher_loader.define();
		searcher_loader.load_content();

		searcher_motion_controller.set_start_position();
	};
}


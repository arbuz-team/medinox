/**
 * Created by mrskull on 18.07.17.
 */

import {Form_Controllers}           from 'form/js/controller'
import {Post_Button_Controllers}    from 'form/plugin/post_button/controllers'
import {Event_Button_Controllers}   from 'form/plugin/event_button/controllers'
import {Little_Form_Controllers}    from 'form/plugin/little_form/controllers'
import {Dialog_Loader_View} 		from './view'
import {models} from "form/plugin/file_converter/views";



export function Dialog_Loader_Controller(config)
{
	let
		config_loader = {
			part_name: config.part_name,
			container: config.container,
		},


		view = new Dialog_Loader_View(config),

		form_controller = new Form_Controllers(config_loader),
		post_button_controller = new Post_Button_Controllers(config_loader),
		event_button_controller = new Event_Button_Controllers(config_loader),
		little_form_controller = new Little_Form_Controllers(config_loader);



		// ----------------------------------------------------


	this.reload_content = function()
	{
	    return view.send_request();
	};


	this.get_content = function(button)
	{
		return new Promise((resolve) =>
		{
			view.collect_data(button);

			view.send_request().then(resolve);
		});
	};


	this.set_loading = function()
	{
		view.set_loading();
	};


	this.define = function()
	{
		form_controller.define();
		post_button_controller.define();
		event_button_controller.define();
		little_form_controller.define();
		$(config.internal_button, config.container).click(view.send_form);
	};
}

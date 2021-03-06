/**
 * Created by mrskull on 18.07.17.
 */

import {Form_Controllers}           from 'form/js/controller'
import {define_post_button}         from 'form/plugin/post_button/define'
import {define_event_button}        from 'form/plugin/event_button/define'
import {Little_Form_Controllers}    from 'form/plugin/little_form/controllers'

import {define_directory_tree}      from 'block/plugin/directory_tree/define'
import {Notifications_Controller}   from 'block/plugin/notifications/js/controller'

import {Dialog_Loader_View} 		from './view'




export function Dialog_Loader_Controller(config)
{
	let
		config_loader = {
			part_name: config.part_name,
			container: config.container,
		},


		view =                          new Dialog_Loader_View(config),

		form_controller =               new Form_Controllers(config_loader, true),
		little_form_controller =        new Little_Form_Controllers(config_loader),
		notifications_controller =      new Notifications_Controller(config_loader);



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
		view.set_text({
			title: '<div class="container-part-loading"> Loading... </div>',
			content: '<div class="dialog-message"> Loading... </div>',
		})
	};


	this.set_text = function(data)
	{
		data.content =
			'<div class="dialog-content-part">'+ data.content +'</div>'+
			'<div class="dialog-content-part">'+
				'<button class="button event_button"' +
						'type="button"' +
						'data-name="button_close_dialog"' +
						'data-event="part.close_dialog">' +
					'Close</button>' +
			'</div>';

		view.set_text(data);
		this.define();
	};


	this.set_error = function(data)
	{
		data.content =
			'<div class="dialog-content-part">'+ data.content +'</div>'+
			'<div class="dialog-content-part">'+
				'<button class="button event_button"' +
						'type="button"' +
						'data-name="redirect_website_error"' +
						'data-event="redirect_website(url:/,uri:/)">' +
					'Redirect to home</button>' +
				'<button class="button event_button"' +
						'type="button"' +
						'data-name="reaload_website_error"' +
						'data-event="reload_website">' +
					'Reload page</button>' +
				'<button class="button event_button"' +
						'type="button"' +
						'data-name="button_close_dialog"' +
						'data-event="part.close_dialog">' +
					'Close</button>' +
			'</div>';

		view.set_text(data);
		this.define();
	};


	this.define = function()
	{
		form_controller.define();
		define_post_button(config_loader);
		define_event_button(config_loader);
		define_directory_tree(config_loader);
		little_form_controller.define();
		notifications_controller.define();

		$(config.internal_button, config.container).click(view.send_form);
	};
}

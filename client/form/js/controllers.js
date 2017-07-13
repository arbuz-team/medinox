/**
 * Created by mrskull on 24.11.16.
 */

import {Form_Models} 		from './models'
import * as validator 		from '../plugin/validator/controllers'
import * as auto_form 		from '../plugin/auto_form/controllers'
import * as selected_form 	from '../plugin/selected_form/controllers'
import * as file_converter 	from '../plugin/file_converter/controllers'

export let Form_Controllers = function(content_loader_controllers)
{
	let
		form_models = new Form_Models(content_loader_controllers),
	    variables = form_models.variables;


	/**
	 *    Defining private functions
	 */

	let

		prepare_form_to_send = function(event)
		{
			let
				form_action = $(this).attr('action'),
				protocol;

			if(typeof form_action === 'string')
				protocol = form_action.substring(0, 4);

			if(protocol !== 'http')
			{
				event.preventDefault();

				let
					form_name = $(this).data('name'),
					url = $(this).attr('action'),
					form_object = $(this).serialize_object();

				variables.list_to_reload = $(this).data('reload');
				variables.url_to_redirect = $(this).data('redirect');
				variables.list_event = $(this).data('event');

				form_models.send(form_name, url, form_object);
			}
		};


	/**
	 *    Defining public functions
	 */

	this.define = function()
	{
		let $container = $(content_loader_controllers.container);

		$('form', $container).submit(prepare_form_to_send);

		validator.define($container);
		auto_form.define($container);
		selected_form.define($container);
		file_converter.define($container);
	};

};


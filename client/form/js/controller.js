/**
 * Created by mrskull on 24.11.16.
 */

import {Form_Models} 		from './model'
import * as validator 		from 'form/plugin/validator/controllers'
import * as auto_form 		from 'form/plugin/auto_form/controllers'
import * as selected_form 	from 'form/plugin/selected_form/controllers'
import * as file_converter 	from 'form/plugin/file_converter/controllers'

export let Form_Controllers = function(config)
{
	let
		form_models = new Form_Models(config),
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

				variables.form_name =   $(this).data('name');
				variables.post_url =    $(this).attr('action');
				variables.post_data =   $(this).serialize_object();
				variables.reload =      $(this).data('reload');
				variables.redirect =    $(this).data('redirect');
				variables.event =       $(this).data('event');
				variables.delay =       $(this).data('delay');

				form_models.send();
			}
		};


	/**
	 *    Defining public functions
	 */

	this.define = function()
	{
		let
			$container = $(config.container),
			config_form = {
				post_name:      '__'+ config.part_name +'__',
				$container:     $container,
			};

		$('form', $container).each(function()
		{
			if($(this).data('name') === 'values')
				console.log(this);
		});
		$('form', $container).submit(prepare_form_to_send);

		validator.define(config_form);
		auto_form.define(config_form);
		selected_form.define(config_form);
		file_converter.define(config_form);
	};

};


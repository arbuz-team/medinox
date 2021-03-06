/**
 * Created by mrskull on 24.11.16.
 */

import {Form_Models} 		            from './model'
import {Dialog_Form_Models} 		    from './model_for_dialog'
import * as validator 		            from 'form/plugin/validator/controllers'
import * as auto_form 		            from 'form/plugin/auto_form/controllers'
import {Selected_Form_Controller} 	    from 'form/plugin/selected_form/controllers'
import {Feature_Setter} 	            from 'form/plugin/feature_setter/controller'
import * as file_converter 	            from 'form/plugin/file_converter/controllers'
import {Address_Switcher_Controller}    from 'form/plugin/address_switcher/controller'
import {Currency_Converter_Controller}  from 'form/plugin/currency_converter/js/controller'



export let Form_Controllers = function(config, is_dialog)
{
	let
		address_switcher = new Address_Switcher_Controller(config),
		currency_converter = new Currency_Converter_Controller(config),
		selected_form = new Selected_Form_Controller(config),
		feature_setter = new Feature_Setter(config),
		form_models,
	    variables;


	if(is_dialog === true)
		form_models = new Dialog_Form_Models(config);
	else
		form_models = new Form_Models(config);


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

		$('form', $container).submit(prepare_form_to_send);

		validator.define(config_form);
		auto_form.define(config_form);
		file_converter.define(config_form);
		feature_setter.define(config_form);
		selected_form.define();
		address_switcher.define();
		currency_converter.define();
	};

};


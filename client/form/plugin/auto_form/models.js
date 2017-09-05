/**
 * Created by mrskull on 17.01.17.
 */

import {Request_Manager_Main} 	from 'arbuz/plugin/request_manager/main'
import {is_defined} from 'arbuz/plugin/utilities/data'



export let Auto_Form_Models = function(config)
{
	let request_manager = new Request_Manager_Main();

	this.settings = {
		post_name:  undefined,

		form:       undefined,
		fields:     undefined,

		origin:     undefined,
		redirect:   undefined,
		reload:     undefined,
		delay:      undefined,
	};

	let
		variables = {
			post_data:  {},
		},

		state = {
			response:   false,
			error:      false,
		},


		load_settings = () =>
		{
			if(typeof config !== 'undefined')
			{
				// -- Form
				if(typeof config.form !== 'undefined')
				{
					this.settings.post_name = config.post_name;
					this.settings.form = config.form;

					let $form = this.settings.form;
					this.settings.origin = $form.data('origin');
					this.settings.redirect = $form.data('redirect');
					this.settings.reload = $form.data('reload');
					this.settings.delay = $form.data('delay');
				}


				// -- Fields
				if(typeof config.fields !== 'undefined')
					this.settings.fields = config.fields;
			}
		};

	load_settings();

	/////////////////////////

	this.get_state_response = function()
	{
		if(state.response)
			return true;
		else
			return false;
	};

	this.set_state_response = function(setter)
	{
		if(setter)
			state.response = true;
		else
			state.response = false;
	};

	this.get_state_error = function()
	{
		if(state.error)
			return true;
		else
			return false;
	};

	this.set_state_error = function(setter)
	{
		if(setter)
			state.error = true;
		else
			state.error = false;
	};

	// --------------------------------------------------


	this.prepare_post_data = function(name, value, action, field)
	{
		variables.post_data = {};

		variables.post_data[this.settings.post_name] = this.settings.origin;
		variables.post_data._name_ = name;
		variables.post_data.value = value;

		if(is_defined(action))
			variables.post_data.action = action;

		if(is_defined(field))
			variables.post_data.field = field;
	};


	this.send = function()
	{
		this.set_state_response(false);

		return request_manager.send(undefined, variables.post_data, this.settings.post_name);
	};


};
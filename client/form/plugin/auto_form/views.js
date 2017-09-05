/**
 * Created by mrskull on 17.01.17.
 */

import {recognise_status}   from 'arbuz/plugin/utilities/response'
import {Auto_Form_Models}   from './models'


export let Auto_Form_Views = function(config)
{
	let
		models = new Auto_Form_Models(config),
		that = this,
		sent_http_request = setTimeout(function(){}, 0);

	this.models = models;


	// ----------------------------------------------------

	let check_is_number = function(event)
	{
		let
			keycode = event.keyCode,

			valid =
				(keycode === 8 || keycode === 46)       // backspace & delete
				|| keycode > 47 && keycode < 58        // number keys
				|| (keycode > 95 && keycode < 112)     // numpad keys
		;

		return valid;
	};


	let check_is_not_number_or_functionaly = function(event)
	{
		let
			keycode = event.keyCode,

			valid =
				//(keycode === 8 || keycode === 46)       // backspace & delete
				// || keycode > 47 && keycode < 58        // number keys
				keycode === 32 || keycode === 13          // spacebar & return key(s) (if you want to allow carriage returns)
				|| (keycode > 64 && keycode < 91)         // letter keys
				// || (keycode > 95 && keycode < 112)     // numpad keys
				|| (keycode > 185 && keycode < 193)       // ;=,-./` (in order)
				|| (keycode > 218 && keycode < 223)       // [\]' (in order)
				|| keycode == 16                          // shift
				|| event.ctrlKey || event.shiftKey
				|| (keycode > 105 && keycode < 110)         // "*-+,"
				|| keycode == 111                         // "/"
		;

		return valid;
	};


	let check_is_not_functionaly = function(event)
	{
		let
			keycode = event.keyCode,

			valid =
				//(keycode === 8 || keycode === 46)       // backspace & delete
				keycode > 47 && keycode < 58        // number keys
				|| keycode === 32 || keycode === 13          // spacebar & return key(s) (if you want to allow carriage returns)
				|| (keycode > 64 && keycode < 91)         // letter keys
				|| (keycode > 95 && keycode < 112)     // numpad keys
				|| (keycode > 185 && keycode < 193)       // ;=,-./` (in order)
				|| (keycode > 218 && keycode < 223)       // [\]' (in order)
				|| keycode == 16                          // shift
				|| event.ctrlKey || event.shiftKey
				|| (keycode > 105 && keycode < 110)         // "*-+,"
				|| keycode == 111                         // "/"
		;

		return valid;
	};


	this.try_press_number_max_3 = function(event)
	{

		if(check_is_not_number_or_functionaly(event))
		{
			event.preventDefault();
		}
		else
		{
			let length = $(this).val().length;
			if(length > 2 && check_is_not_functionaly(event))
				event.preventDefault();
		}
	};


	this.send_if_number_only = function(event)
	{
		if(check_is_number(event))
		{
			let
				$field = $(this),

				name = $field.data('name'),
				value = $field.val();

			that.send_default(name, value);
		}
	};


	let check_is_key_code_enter = function(event)
	{
		return event.keyCode === 13;
	};


	this.send_checkbox = function()
	{
		let
			$field = $(this),

            name = $field.attr('name'),
			value = $field.val(),
			action;

		if($field.is(':checked'))
			action = 'append';
		else
			action = 'delete';

		models.prepare_post_data(name, value, action);

		send();
	};


	this.send_default = function(name, value)
	{
		let $field;

		if(name && value)
		{
			models.prepare_post_data(name, value);
		}
		else
		{
			$field = $(this);

			models.prepare_post_data($field.data('name'), $field.val());
		}

		send();
	};


	this.send_on_enter = function(event)
	{
		if(check_is_key_code_enter(event))
		{
			event.preventDefault();
			let
				$field = $(this);

			models.prepare_post_data($field.attr('name'), $field.val());

			send();
		}
	};


	/**
	 *    Defining private functions
	 */

	let

		show_changes = function()
		{
			let
				delay,

				function_for_setTimeout = function()
				{
					if(models.get_state_response() && models.get_state_error() === false)
					{
						APP.DATA.delay = delay;

						if(models.settings.redirect)
						{
							APP.DATA.redirect = models.settings.redirect;

							APP.throw_event(EVENTS.redirect);
						}
						else if(models.settings.reload)
						{
							APP.throw_event(EVENTS.part['reload_'+ models.settings.reload]);
						}
					}

					else if(models.get_state_error())
					{
						return false;
					}

					else
					{
						sent_http_request = setTimeout(function_for_setTimeout, 100);
					}
				};


			if(typeof models.settings.delay !== 'undefined')
				delay = models.settings.delay;
			else
				delay = 0;


			clearTimeout(sent_http_request);
			sent_http_request = setTimeout(function_for_setTimeout, delay);
		},


		is_error = function(code)
		{
			return recognise_status(code) === 'error';
		},


		set_response = function(response)
		{
			if(is_error(response.code))
			{
				models.set_state_error(true);
				models.set_state_response(false);
				return false;
			}

			models.set_state_error(false);
			models.set_state_response(true);


		},


		send = function()
		{
			models.send().then(response =>
			{
				set_response(response);
			});
			show_changes();
		};

};



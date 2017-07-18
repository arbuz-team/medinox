/**
 * Created by mrskull on 18.12.16.
 */

import {Post_Button_Models} from './models'
import * as utilities from 'form/js/utilities'


export let Post_Button_Views = function(config)
{
	let
		models = new Post_Button_Models(config),


		set_text = {

			insert: function(text)
			{
				let $button = $(models.settings.button);

				if(set_text.if_is_not_text())
					return false;

				if($button.hasClass('is-text_icon'))
					$button.find('.button-text').html(text);
				else
					$button.html(text);
			},

			if_is_not_text: function()
			{
				return $(models.settings.button).hasClass('is-icon');
			},



			sending: function()
			{
				if(set_text.if_is_not_text())
					return false;

				clearTimeout(set_text.set_waiting);
				clearTimeout(set_text.set_standard);

				set_text.insert(models.settings.text_sending);
			},


			set_waiting: undefined,
			waiting: function()
			{
				if(set_text.if_is_not_text())
					return false;

				set_text.set_waiting = setTimeout(function(){
					set_text.insert(models.settings.text_waiting);
				}, models.settings.delay_text_waiting);
			},


			done: function()
			{
				if(set_text.if_is_not_text())
					return false;

				clearTimeout(set_text.set_waiting);
				set_text.insert(models.settings.text_done);
			},


			set_standard: undefined,
			standard: function()
			{
				if(set_text.if_is_not_text())
					return false;

				set_text.set_standard = setTimeout(function(){
					set_text.insert(models.settings.text_standard);
				}, models.settings.delay_text_standard);
			},


			error: function()
			{
				if(set_text.if_is_not_text())
					return false;

				clearTimeout(set_text.set_waiting);
				clearTimeout(set_text.set_standard);

				set_text.insert(models.settings.text_error);
			},
		},


		start_loading = function()
		{
			models.state.is_loading = true;
			set_text.sending();
			set_text.waiting();
		},


		is_error = function(JSON_response, status)
		{
			if(status !== 'success')
			{
				set_text.error();
				return true;
			}

			let response = JSON.parse(JSON_response);

			if (response.__button__ !== 'true')
			{
				set_text.error();
				return true;
			}

			return false;
		},


		end_loading = function(JSON_response, status)
		{
			let events;

			models.state.is_loading = false;

			if(is_error(JSON_response, status))
				return false;

			set_text.done();


			events = {
				reload: models.settings.button_reload,
				redirect: models.settings.button_redirect,
				events: models.settings.button_event,
				delay: models.settings.button_delay,
			};

			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);

			set_text.standard();
		};


	this.start = function()
	{
		if(models.is_loading())
			return false;

		start_loading();
		models.send_post(end_loading);
	};

	this.models = models;

};
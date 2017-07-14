/**
 * Created by mrskull on 21.01.17.
 */

import * as utilities from './utilities'


export let Form_Models = function(content_loader_controllers)
{
    let that = this;

	/**
	 *    Defining settings
	 */

	this.loader_controllers = content_loader_controllers;

	this.variables = {
		name:           undefined,
		reload:     	undefined,
		redirect:    	undefined,
		event:         	undefined,
		delay:         	undefined,
	};


	/**
	 *    Defining private functions
	 */

	let

		prepare_post_data = function(form_name, post_data)
		{
			if(!post_data)
				post_data = {};

			post_data.__form__ = form_name;

			return post_data;
		},


		end_loading = function(HTML_response, status)
		{
			if(utilities.html_is_error(HTML_response, status))
				return false;

			let events = {
				reload: that.variables.reload,
				redirect: that.variables.redirect,
				events: that.variables.event,
				delay: that.variables.delay,
			};

			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
		};


	/**
	 *    Defining public functions
	 */

	this.send = function(form_name, url, post_data)
	{
		post_data = prepare_post_data(form_name, post_data);

		if(typeof this.loader_controllers !== 'undefined')
			this.loader_controllers.load(url, post_data, end_loading);
		else
			console.error('Valid config object.');
	};

};
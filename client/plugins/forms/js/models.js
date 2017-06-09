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
		name:               undefined,
		list_to_reload:     undefined,
		url_to_redirect:    undefined,
		list_event:         undefined,
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

			utilities.reload_plugins(that.variables.list_to_reload);
			utilities.redirect_ground(that.variables.url_to_redirect);
			utilities.launch_event(that.variables.list_event);
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
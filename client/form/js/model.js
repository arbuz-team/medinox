/**
 * Created by mrskull on 21.01.17.
 */

import * as utilities 			from './utilities'
import {Block_Loader_Form}     	from '../../block/plugin/block_loader/form'


export let Form_Models = function(config)
{
    let form_loader = new Block_Loader_Form(config);

	/**
	 *    Defining settings
	 */

	this.variables = {
		form_name:      undefined,
		post_url:       undefined,
		post_data:      undefined,

		reload:     	undefined,
		redirect:    	undefined,
		event:         	undefined,
		delay:         	undefined,
	};


	/**
	 *    Defining private functions
	 */

	let

		prepare_post_data = () =>
		{
			let variables = this.variables;

			if(!variables.post_data)
				variables.post_data = {};

			variables.post_data._name_ = variables.form_name;
		},


		end_loading = () =>
		{
			let variables = this.variables,
				events;

			events = {
				reload: variables.reload,
				redirect: variables.redirect,
				events: variables.event,
				delay: variables.delay,
			};

			utilities.reload_plugins(events);
			utilities.redirect_ground(events);
			utilities.launch_event(events);
		};


	/**
	 *    Defining public functions
	 */

	this.send = function()
	{
		let
			post_url = this.variables.post_url,
			post_data = this.variables.post_data;

		prepare_post_data();

		form_loader.load_simple_content(post_url, post_data).then(end_loading);
	};

};
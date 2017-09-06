/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} 	                from 'arbuz/js/structure'
import {add_to_settings, select_number} 	from 'arbuz/plugin/utilities/data'
import {Request_Manager_Block} 		        from 'arbuz/plugin/request_manager/block'
import {Block_Loader} 				        from './_controller'
import {timeout_promise}                    from "arbuz/plugin/utilities/standard";


export function Block_Loader_Part(config)
{
	Block_Loader.call(this, config);

	this._settings.load_meta_tags = false;

	add_to_settings(config, this, 'load_meta_tags');
}

Block_Loader_Part.prototype = Object.create(Block_Loader.prototype);





// --------------------------    MODEL    --------------------------

Block_Loader_Part.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data[this._settings.post_name] = 'content';

	this._variables.post_data = post_data;
};


Block_Loader_Part.prototype._send_request = function()
{
	let
		url = this._variables.post_url,
		data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Block();

	this._response = request_manager.next(url, data, post_name);
};

// --------------------------    VIEW    --------------------------


Block_Loader_Part.prototype._load_head_of_page = function()
{
	if(this._settings.load_meta_tags)
	{
		data_controller.change_much({
			title: APP.DATA.title,
			description: APP.DATA.description
		});

		$('title').html(data_controller.get('title'));
		$('meta[ name="description" ]').attr('content', data_controller.get('description'));
	}
};


Block_Loader_Part.prototype._receive_response = function()
{
	return new Promise((resolve, reject) =>
	{
		this._response.then(response =>
		{
			let precise_data;

			if(this._check_for_errors(response))
				reject(response);

			else if(this._is_redirect(response))
				precise_data = {
					status: 'success',
					code: response.code,
					url: response.url,
				};

			else
				precise_data = {
					html: response.html,
					status: 'success',
					code: response.code,
				};

			resolve(precise_data);
		});
	});
};


// --------------------------    DEFINE    --------------------------


Block_Loader_Part.prototype.redirect = function(change_url)
{
	return new Promise((resolve) =>
	{
		let
			url = APP.DATA.redirect || data_controller.get('path'),
			delay = select_number(APP.DATA.delay, 0),
			state = this._state,
			variables = this._variables;

		state.can_do_redirect = true;
		clearTimeout(variables.redirect_time_out);

		variables.redirect_time_out = setTimeout(() =>
		{
			if(state.can_do_redirect === true)
			{
				let request_manager = new Request_Manager_Block();

				change_url(url);

				this.load_content(url).then(resolve);
				request_manager.send_list();
			}

		}, delay);
	});
};


Block_Loader_Part.prototype.reload = function()
{
	timeout_promise().then(() => {
		this.load_content();
	});
};


Block_Loader_Part.prototype._is_redirect = function(response)
{
	return response && response.code === 302;
};


Block_Loader_Part.prototype.load_content = function(post_url, post_data)
{
	return new Promise(resolve =>
	{
		this._get_content(post_url, post_data);

		this._hide_content().then(() =>
		{
			this._receive_response().then(response =>
			{
				if(this._is_redirect(response))
					resolve(response);

				this._set_content(response);

				this._load_head_of_page();

				this._prepare_content_to_show();

				this._show_content().then(() =>
				{
					resolve(response);
				});
			});
		});
	});
};


Block_Loader_Part.prototype.load_simple_content = function(url, post_data)
{
	let
		request_manager = new Request_Manager_Block(),
		result = this.load_content(url, post_data);

	request_manager.send_list();
	return result;
};


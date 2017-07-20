/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} 			from 'arbuz/js/structure'
import {add_to_settings} 			from 'arbuz/plugin/utilities/data'
import {Request_Manager_Block} 		from 'arbuz/plugin/request_manager/block'
import {Block_Loader} 				from './_controller'


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
		post_data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Block();

	this._response = request_manager.next(undefined, post_data, post_name);
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

			if(this._check_for_errors(response))
				reject(response);

			else
			{
				let precise_data = {
						html: response.html,
						status: 'success',
						code: response.code,
					};

				resolve(precise_data);
			}
		});
	});
};


// --------------------------    DEFINE    --------------------------

Block_Loader_Part.prototype.reload = function()
{
	let delay = 0;

	if(typeof APP.DATA.delay !== 'undefined')
	{
		delay = APP.DATA.delay;
		APP.DATA.delay = undefined;
	}

	setTimeout(() => {
		this.load_simple_content();
	}, delay);
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
				this._load_head_of_page();

				this._set_content(response);

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
	let request_manager = new Request_Manager_Block();

	this.load_content(url, post_data);
	request_manager.send_list();
};


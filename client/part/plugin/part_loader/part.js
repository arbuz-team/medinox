/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} 		from 'arbuz/js/structure'
import {add_to_settings} 		from 'arbuz/plugin/utilities/data'
import {Request_Manager_Part} 	from 'arbuz/plugin/request_manager/part'
import {Part_Loader} 			from './_controller'


export function Part_Loader_Part(config)
{
	Part_Loader.call(this, config);

	this._settings.load_meta_tags = false;

	add_to_settings(config, this, 'load_meta_tags');
}

Part_Loader_Part.prototype = Object.create(Part_Loader.prototype);





// --------------------------    MODEL    --------------------------

Part_Loader_Part.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data[this._settings.post_name] = 'content';

	this._variables.post_data = post_data;
};


Part_Loader_Part.prototype._send_request = function(actually_url)
{
	let
		post_data = this._variables.post_data,
		request_manager = new Request_Manager_Part();

	this.response = request_manager.next(actually_url, post_data);
};

// --------------------------    VIEW    --------------------------


Part_Loader_Part.prototype._load_header_page = function(object)
{
	data_controller.change_much({
		title: object.title,
		description: object.description
	});

	$('title').html(data_controller.get('title'));
	$('meta[ name="description" ]').attr('content', data_controller.get('description'));
};


Part_Loader_Part.prototype._after_show_content = function()
{
	if(this.settings.load_meta_tags && APP.DATA)
		this._load_header_page(APP.DATA);
};


Part_Loader_Part.prototype._receive_response = function()
{
	return new Promise((resolve, reject) =>
	{
		this.response.then((response) =>
		{

			if(this._check_for_errors(response))
			{
				reject(response);
			}
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

Part_Loader_Part.prototype.reload = function()
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


Part_Loader_Part.prototype.load_simple_content = function(url, post_data, callback)
{
	let request_manager = new Request_Manager_Part();

	this.load_content(url, post_data, callback);
	request_manager.send_list();
};


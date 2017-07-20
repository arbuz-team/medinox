/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Form} 	from 'arbuz/plugin/request_manager/form'
import {Block_Loader_Part} 		from './part'


export function Block_Loader_Form(config)
{
	Block_Loader_Part.call(this, config);
}

Block_Loader_Form.prototype = Object.create(Block_Loader_Part.prototype);





// ------------------------------------------


Block_Loader_Form.prototype._send_request = function(actually_url)
{
	let
		post_data = this.variables.post_data,
		request_manager = new Request_Manager_Form();

	this.response = request_manager.send(actually_url, post_data);
};


Block_Loader_Form.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data._direct_ = this.settings.part_name;

	this.variables.post_data = post_data;
};


Block_Loader_Form.prototype._receive_response = function()
{
	return new Promise((resolve) =>
	{
		this.response.then((response) =>
		{

			let precise_data = {
					html: response,
					status: 'success',
					code: 200,
				};

			resolve(precise_data);
		});
	});
};


Block_Loader_Form.prototype.load_simple_content = function(url, post_data, callback)
{
	this.load_content(url, post_data, callback);
};

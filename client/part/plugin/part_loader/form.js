/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Form} 	from 'arbuz/plugin/request_manager/form'
import {Part_Loader_Part} 		from './part'


export function Part_Loader_Form(config)
{
	Part_Loader_Part.call(this, config);
}

Part_Loader_Form.prototype = Object.create(Part_Loader_Part.prototype);





// ------------------------------------------


Part_Loader_Form.prototype.send_request = function(actually_url)
{
	let
		post_data = this.variables.post_data,
		request_manager = new Request_Manager_Form();

	this.response = request_manager.send(actually_url, post_data);
};


Part_Loader_Form.prototype.prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data._direct_ = this.settings.name;

	this.variables.post_data = post_data;
};


Part_Loader_Form.prototype.receive_response = function()
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


Part_Loader_Form.prototype.load_simple_content = function(url, post_data, callback)
{
	this.load_content(url, post_data, callback);
};

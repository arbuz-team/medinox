/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from '../../../arbuz/js/structure'
import {add_to_settings} from '../../../arbuz/plugin/utilities/data'
import {Request_Manager_Part} from '../../../arbuz/plugin/request_manager/part'
import {Part_Loader} from './_controller'


export function Part_Loader_Part(config)
{
	Part_Loader.call(this, config);

	this.settings.load_meta_tags = false;

	add_to_settings(config, this, 'load_meta_tags');
}

Part_Loader_Part.prototype = Object.create(Part_Loader.prototype);





// ------------------------------------------

Part_Loader_Part.prototype.prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	if( typeof post_data.__content__ === 'undefined')
		post_data['__content__'] = this.settings.name;


	this.variables.post_data = post_data;
};


Part_Loader_Part.prototype.send_request = function(actually_url)
{
	let
		post_data = this.variables.post_data,
		request_manager = new Request_Manager_Part();

	this.response = request_manager.next(actually_url, post_data);
};



Part_Loader_Part.prototype.load_header_page = function(object)
{
	data_controller.change_much({
		title: object.title,
		description: object.description
	});

	$('title').html(data_controller.get('title'));
	$('meta[ name="description" ]').attr('content', data_controller.get('description'));
};


Part_Loader_Part.prototype.after_show_content = function(data)
{
	if(this.external_callback)
		this.external_callback(data.html, data.status, data.code);

	if(this.settings.load_meta_tags && APP.DATA)
		this.load_header_page(APP.DATA);
};


Part_Loader_Part.prototype.receive_response = function()
{
	return new Promise((resolve) =>
	{
		this.response.then((response) =>
		{
			let data = response[this.settings.name],
				precise_data = {
					html: data.html,
					status: 'success',
					code: data.status,
				};

			resolve(precise_data);
		});
	});
};




Part_Loader_Part.prototype.load_simple_content = function(url, post_data, callback)
{
	let request_manager = new Request_Manager_Part();

	this.load_content(url, post_data, callback);
	request_manager.send_list();
};


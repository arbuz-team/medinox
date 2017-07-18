/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {Request_Manager_Part} from 'arbuz/plugin/request_manager/part'
import {Part_Loader} from './_init'




Part_Loader.prototype.if_reload = function(url)
{
	let
		old_url = data_controller.get('path'),
		new_url = url;

	return old_url === new_url || !new_url;
};


Part_Loader.prototype.refresh_data = function()
{
	data_controller.reset();
};


Part_Loader.prototype.refresh_events = function()
{
	APP.throw_event( EVENTS.define );
};


Part_Loader.prototype.check_for_errors = function(status, code)
{
	let
		$container = $(this.settings.container),
		error = this.variables.error;

	if(status !== 'success')
		if(error === true)
			$container.html('An error has occurred while connecting to server. ' +
					'Please, refresh website or check your connect with network.');
		else
		{
			this.variables.error = true;

			this.prepare_post_data({__content__: 'ground'});
			this.send_request('/statement/' + code + '/');
			this.receive_response().then(() =>
			{
				this.show_content();
			});

			return true;
		}
	return false;
};


Part_Loader.prototype.prepare_content_to_change = function(url, post_data)
{
	this.variables.can_do_redirect = false;
	this.variables.reload = this.if_reload(url);

	this.refresh_data();
	this.prepare_post_data(post_data);
};


Part_Loader.prototype.prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	if( typeof post_data.__form__ === 'undefined')
		if( typeof post_data.__content__ === 'undefined')
			post_data['__content__'] = this.settings.part_name;


	this.variables.post_data = post_data;
};


Part_Loader.prototype.send_request = function(actually_url)
{
	let
		post_data = this.variables.post_data,
		request_manager = new Request_Manager_Part();

	this.response = request_manager.send(actually_url, post_data);
};


Part_Loader.prototype.receive_response = function()
{
	return new Promise((resolve) =>
	{
		this.response.then((response) =>
		{
			let data = response.__content__[this.settings.part_name],
				precise_data = {
					html: data.html,
					code: data.status,
				};

			if(200 <= data.status < 300)
				precise_data.status = 'success';
			else if(400 <= data.status < 600)
				precise_data.status = 'error';


			resolve(precise_data);
		});
	});
};
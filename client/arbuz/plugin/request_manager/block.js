/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {Request_Manager} from './_controller'


export function Request_Manager_Block()
{
	if(typeof Request_Manager_Block.instance === 'object')
		return Request_Manager_Block.instance;

	Request_Manager.call(this);

	this._sending = undefined; // After will be promise

	Request_Manager_Block.instance = this;
}

Request_Manager_Block.prototype = Object.create(Request_Manager.prototype);




Request_Manager_Block.prototype._add_request = function(url, post_data)
{
	if(typeof this._sending === 'undefined')
		this._clear_request();

	if(typeof this._data.url === 'undefined')
		this._data.url = url;

	this._data.list.push(post_data);
};


Request_Manager_Block.prototype._clear_request = function()
{
	this._data = {
		url: undefined,
		list: [],
	};

	this._sending = false;
};


Request_Manager_Block.prototype._prepare_post_data = function()
{
	let post_data = {};

	if(this._data.list.length)
	{
		// --- Converting list of parts to string
		this._data.list.forEach((element) =>
		{
			if(element)
			{
				Object.assign(post_data, element);
			}
			else
				return false;
		});


		// --- Add CRSF TOKEN
		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	}


	return false;
};


Request_Manager_Block.prototype._run_sending = function()
{
	if(this._sending === false)
		this._sending = new Promise((resolve, reject) =>
		{
			let
				timer = setTimeout(() =>
				{
					this._catch_timeout_error();
				}, 3000),


				send_and_wait = () =>
				{
					clearTimeout(timer);


					if(this._sending === false)
						reject('Request Manager error: Promise doesn\'t exist.');

					this._send_request().then(response =>
					{
						window.removeEventListener('send_request', send_and_wait, false);

						resolve(response);
					});
				};


			window.addEventListener('send_request', send_and_wait, false);
		});

	return this._sending;
};


Request_Manager_Block.prototype.next = function(url, post_data, post_name)
{
	return new Promise((resolve, reject) =>
	{
		this._add_request(url, post_data);

		this._run_sending().then(response =>
		{
			this._clear_request();

			if(typeof response.json[post_name] !== 'undefined')
				response = response.json[post_name];
			else
				reject('Request_Manager_Block error: Invalid response.');

			resolve(response);
		});
	});
};


delete Request_Manager_Block.prototype.send;


Request_Manager_Block.prototype.send_list = function()
{
	APP.throw_event(window.EVENTS.send_request);
};
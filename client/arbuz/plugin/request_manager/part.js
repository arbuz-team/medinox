/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {Request_Manager} from './_init'


export function Request_Manager_Part()
{
	if(typeof Request_Manager_Part.instance === 'object')
		return Request_Manager_Part.instance;

	Request_Manager.call(this);

	Request_Manager_Part.instance = this;
}

Request_Manager_Part.prototype = Object.create(Request_Manager.prototype);




Request_Manager_Part.prototype.add_request = function(url, post_data)
{
	if(this.sending === undefined)
		this.clear_request();

	if(this.requests.url === undefined)
		this.requests.url = url;

	this.requests.list.push(post_data);
};


Request_Manager_Part.prototype.clear_request = function()
{
	this.requests = {
		url: undefined,
		list: [],
	};

	this.sending = false;
};


Request_Manager_Part.prototype.post_data_prepare = function()
{
	let post_data = {
		__content__: '',
	};


	if(this.requests.list.length)
	{
		// --- Converting list of parts to string
		this.requests.list.forEach((element) =>
		{
			if(element.__content__)
			{
				post_data.__content__ += element.__content__ +' ';

				delete element.__content__;
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


Request_Manager_Part.prototype.run_sending = function()
{
	if(this.sending === false)
		this.sending = new Promise((resolve, reject) =>
		{
			let
				timer = setTimeout(() =>
				{
					this.catch_timeout_error();
				}, 3000),


				send_and_wait = () =>
				{
					clearTimeout(timer);


					if(this.sending === false)
						reject('Request Manager error: Promise doesn\'t exist.');

					else
						this.send_request().then((response) =>
						{
							window.removeEventListener('send_request', send_and_wait, false);
							resolve(response);
						});
				};


			window.addEventListener('send_request', send_and_wait, false);
		});

	return this.sending;
};


Request_Manager_Part.prototype.next = function(url, post_data)
{
	this.add_request(url, post_data);

	return new Promise((resolve) =>
	{
		this.run_sending().then((response) =>
		{
			this.clear_request();

			let data = response.__content__;

			resolve(data);
		});
	});
};


Request_Manager_Part.prototype.send_list = function()
{
	APP.throw_event(window.EVENTS.send_request);
};
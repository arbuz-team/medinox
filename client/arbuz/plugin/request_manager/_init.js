/**
 * Created by mrskull on 15.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {object_to_formdata} from 'arbuz/plugin/utilities/data'


export function Request_Manager()
{
	this.requests = undefined;
	this.sending = undefined; // After will be promise


	this.request = obj => {
		return new Promise((resolve, reject) =>
		{
			let
				xhr = new XMLHttpRequest(),
				method = obj.method || "GET",
				data = object_to_formdata(obj.data);

			xhr.open(method, obj.url);

			if(obj.headers)
			{
				Object.keys(obj.headers).forEach(key =>
				{
					xhr.setRequestHeader(key, obj.headers[key]);
				});
			}

			xhr.onload = () =>
			{
				if (xhr.status >= 200 && xhr.status < 300)
					resolve(xhr.response);
				else
					resolve(xhr.response);
			};
			xhr.onerror = () => resolve(xhr.response);
			xhr.send(data);
		});
	};
}






Request_Manager.prototype.add_request = function(url, post_data)
{
	if(this.sending === undefined)
		this.clear_request();

	if(this.requests.url === undefined)
		this.requests.url = url || '';

	this.requests.data = post_data || {};
};


Request_Manager.prototype.clear_request = function()
{
	this.requests = {
		url: undefined,
		data: {},
	};

	this.sending = false;
};


// --------------

Request_Manager.prototype.preprocess_url = function()
{
	let url = this.requests.url;

	if(url && url.substring && url.substring(0, 1) === '/')
		return url;
	else
		return data_controller.get('path');
};


Request_Manager.prototype.post_data_prepare = function()
{
	if(this.requests.data)
	{
		let post_data = this.requests.data;

		// --- Add CRSF TOKEN
		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	}

	return false;
};


Request_Manager.prototype.send_request = function()
{
	return new Promise((resolve, reject) =>
	{
		let
			post_url = this.preprocess_url(),
			post_data = this.post_data_prepare();

		if(post_data)
		{
			this.request({
				method: 'POST',
				url: post_url,
				data: post_data,
			})
			.then(resolve)
			.catch(reject);
		}
		else
			reject('Request Manager error: Invalid post data.');
	});
};


Request_Manager.prototype.catch_timeout_error = function()
{
	console.error('Request Manager error: Request Timeout. ' +
		'Run `send` in Request Manager.');

	this.clear_request();
};


// --------------

Request_Manager.prototype.send = function(url, post_data)
{
	this.add_request(url, post_data);

	return new Promise((resolve) =>
	{
		this.send_request().then((data) =>
		{
			this.clear_request();

			resolve(data);
		})
		.catch((data) =>
		{
			console.log('Co jest?!');
			console.log(data);
		});
	});
};
/**
 * Created by mrskull on 15.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {object_to_formdata} from 'arbuz/plugin/utilities/data'


export function Request_Manager()
{
	this._data = undefined;


	let
		pack_response = (json, code) =>
		{
			try
			{
				return {
					json: JSON.parse(json),
					code: code,
				};
			}
			catch(err)
			{
				this._show_error(json);
				return false;
			}
		},


		check_status = function(code)
		{
			return code >= 200 && code < 400;
		};


	this._request = obj => {
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
				if(check_status(xhr.status))
					resolve(pack_response(xhr.response, xhr.status));
				else
					reject(pack_response(xhr.response, xhr.status));
			};
			xhr.onerror = () => reject(pack_response(xhr.response, xhr.status));
			xhr.send(data);
		});
	};
}



// --------------------------    REQUEST    --------------------------


Request_Manager.prototype._clear_request = function()
{
	this._data = {
		url: undefined,
		data: {},
	};
};


Request_Manager.prototype._add_request = function(url, post_data)
{
	if(this._sending === undefined)
		this._clear_request();

	if(this._data.url === undefined)
		this._data.url = url || '';

	this._data.data = post_data || {};
};


Request_Manager.prototype._preprocess_url = function()
{
	let url = this._data.url;

	if(url && url.substring && url.substring(0, 1) === '/')
		return url;
	else
		return data_controller.get('path');
};


Request_Manager.prototype._post_data_prepare = function()
{
	if(this._data.data)
	{
		let post_data = this._data.data;

		// --- Add CRSF TOKEN
		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	}

	return false;
};


Request_Manager.prototype._send_request = function()
{
	return new Promise((resolve, reject) =>
	{
		let
			post_url = this._preprocess_url(),
			post_data = this._post_data_prepare();

		if(post_data)
		{
			this._request({
				method: 'POST',
				url: post_url,
				data: post_data,
			})
			.then(resolve)
			.catch(response =>
			{
			    this._show_error(response);
			    reject('Request Manager error: Invalid response.');
			});
		}
		else
			reject('Request Manager error: Invalid post data.');
	});
};


// --------------------------    RESPONSE    --------------------------


Request_Manager.prototype._show_error = function(response)
{
	let new_tab = window.open('', '_blank');
	new_tab.document.write(response);
	new_tab.init();
	new_tab.focus();
};


Request_Manager.prototype._catch_timeout_error = function()
{
	console.error('Request Manager error: Request Timeout. ' +
		'Run `send` in Request Manager.');

	this._clear_request();
};
/**
 * Created by mrskull on 15.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {object_to_formdata} from 'arbuz/plugin/utilities/data'
import * as model from 'arbuz/plugin/request_manager/_model'


export function Request_Manager()
{
	let
		error = false,

		pack_response = (json, code) =>
		{
			try
			{
				let data = {
					json: JSON.parse(json),
					code: code,
				};

				console.log(data);
				console.groupEnd();
				return data;
			}
			catch(e)
			{
				let data = {
					json: json,
					code: code,
				};
				error = true;

				console.log(data);
				console.groupEnd();

				// this._show_error(json);

				return data;
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

			error = false;
			model._request_status = true;

			console.group('Request data: ');
			console.log(obj.url);
			console.log(obj.data);

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
				if(error === false)
					if(check_status(xhr.status))
						resolve(pack_response(xhr.response, xhr.status));
					else
						reject(pack_response(xhr.response, xhr.status));
			};
			xhr.onerror = () =>
			{
				if(error === false)
					reject(pack_response(xhr.response, xhr.status));
			};
			xhr.send(data);
		});
	};
}




// --------------------------    REQUEST    --------------------------


Request_Manager.prototype._clear_request = function()
{
	model._data = {
		url: undefined,
		data: {},
	};
};


Request_Manager.prototype._add_request = function(post_url, post_data)
{
	if(model._data.url === undefined)
		model._data.url = post_url || '';

	model._data.data = post_data || {};
};


Request_Manager.prototype._prepare_url = function()
{
	let url = model._data.url;

	if(url && url.substring && url.substring(0, 1) === '/')
		return url;
	else
		return data_controller.get('path');
};


Request_Manager.prototype._prepare_post_data = function()
{
	if(model._data.data)
	{
		let post_data = model._data.data;

		// --- Add CRSF TOKEN
		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	}

	return false;
};


Request_Manager.prototype._send_request = function()
{
	model._request_promise = new Promise((resolve, reject) =>
	{
		let
			post_url = this._prepare_url(),
			post_data = this._prepare_post_data();


		if(post_data)
		{
			this._clear_request();

			this._request({
				method: 'POST',
				url: post_url,
				data: post_data,
			})
			.then((response) =>
			{
				model._request_status = false;
				resolve(response);
			})
			.catch(response =>
			{
				model._request_status = false;
			    reject({
				    content: 'Request Manager error: Invalid response.',
				    code: response.code,
			    });
			});
		}
		else
		{
			console.trace();
			console.warn(post_data);
			reject({
				content: 'Request Manager error: Invalid post data.',
				code: undefined,
			});
		}
	});

	return model._request_promise;
};


// --------------------------    RESPONSE    --------------------------


Request_Manager.prototype._show_error = function(response)
{
	let new_tab = window.open('', '_blank');
	new_tab.document.write(response);
	new_tab.focus();
};


Request_Manager.prototype._catch_timeout_error = function()
{
	console.error('Request Manager error: Request Timeout. ' +
		'Run `send` in Request Manager.');

	this._clear_request();
};
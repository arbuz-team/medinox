/**
 * Created by mrskull on 19.07.17.
 */

import {Request_Manager} 		from './_init'
import * as model from 'arbuz/plugin/request_manager/_model'

export {Request_Manager} 		from './_init'



// --------------------------    QUEUE OF REQUEST    --------------------------


Request_Manager.prototype._add_to_queue = function(data)
{
	let

		do_step = (resolve, reject) =>
		{
			this._make_request(data, resolve, reject);
		},


		promise = new Promise((resolve, reject) =>
		{
			let
				length = this._queue.length,
				last_number = length - 1;

			if(length === 0)
				model._request_promise.then(() => do_step(resolve, reject));
			else
				model._queue[last_number].promise.then(() => do_step(resolve, reject));
		}),


		queue_data = Object.assign({promise: promise}, data);


	model._queue.push(queue_data);

	return promise;
};



// --------------------------    CONTROLLER    --------------------------


Request_Manager.prototype._make_request = function(data, resolve, reject)
{
	let
		post_url = data.post_url,
		post_data = data.post_data,
		post_name = data.post_name;

	this._add_request(post_url, post_data);

	this._send_request().then((response) =>
	{
		this._clear_request();

		if(typeof response.json[post_name] !== 'undefined')
			response = response.json[post_name];
		else
		{
			console.error('Request_Manager error: Invalid response.');
			reject('Request_Manager error: Invalid response.');
		}

		resolve(response);
	})
	.catch(reject);
};


Request_Manager.prototype.send = function(post_url, post_data, post_name)
{
	if(typeof post_name === 'undefined')
	{
		console.error('Request_Manager error: Invalid variable "post_name"');
		return false;
	}

	let data = {
		post_url: post_url,
		post_data: post_data,
		post_name: post_name,
	};

	if(model._request_status === false)

		return new Promise((resolve, reject) =>
		{
			this._make_request(data, resolve, reject);
		});

	else
		return this._add_to_queue(data);
};
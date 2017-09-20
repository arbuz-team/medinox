/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from 'arbuz/js/structure'
import {Request_Manager} from './_init'
import './_controller'
import * as model from 'arbuz/plugin/request_manager/_model'


export function Request_Manager_Block()
{
	if(typeof Request_Manager_Block.instance === 'object')
		return Request_Manager_Block.instance;

	Request_Manager.call(this);

	model._sending = undefined; // After will be promise
	model._data_block = {}; // After will be promise

	this._clear_request();

	Request_Manager_Block.instance = this;
}

Request_Manager_Block.prototype = Object.create(Request_Manager.prototype);




Request_Manager_Block.prototype._add_request = function(url, post_data)
{
	if(typeof model._data_block.url === 'undefined')
		model._data_block.url = url;

	model._data_block.list.push(post_data);
};


Request_Manager_Block.prototype._clear_request = function()
{
	model._sending = false;

	model._data_block = {
		url: undefined,
		list: [],
	};

	model._data = {
		url: undefined,
		data: {},
	};

};


Request_Manager_Block.prototype._prepare_block_post_data = function()
{
	let post_data = {};

	if(model._data_block.list.length)
	{
		// --- Converting list of parts to string
		model._data_block.list.forEach((element) =>
		{
			if(element)
				Object.assign(post_data, element);
			else
				return false;
		});


		// --- Add CRSF TOKEN
		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	}

	return false;
};


Request_Manager_Block.prototype._add_to_queue = function()
{
	let
		data = {
			post_url: undefined,
			post_data: this._prepare_block_post_data(),
		},


		do_step = (resolve) =>
		{
			resolve(data);
		},


		promise = new Promise((resolve) =>
		{
			let
				length = model._queue.length,
				last_number = length - 1;

			if(length === 0)
				model._request_promise.then(() => do_step(resolve));
			else
				model._queue[last_number].promise.then(() => do_step(resolve));
		}),


		queue_data = Object.assign({promise: promise}, data);

	model._queue.push(queue_data);

	return promise;
};


Request_Manager_Block.prototype._make_request = function(timer, send_and_wait, resolve, reject)
{
	clearTimeout(timer);

	if(model._sending === false)
		reject('Request Manager error: Promise doesn\'t exist.');


	this._send_request().then(response =>
	{
		resolve(response);
	})
	.catch(reject);
};


Request_Manager_Block.prototype._run_sending = function()
{
	if(model._sending === false)
		model._sending = new Promise((resolve, reject) =>
		{
			let
				throw_exception = () =>
				{
					this._catch_timeout_error();
				},


				send_and_wait = () =>
				{
					window.removeEventListener('send_request', send_and_wait, false);

					if(model._request_status === false)
					{
						let timer = setTimeout(throw_exception, 3000);

						model._data.url = model._data_block.url;
						model._data.data = this._prepare_block_post_data();

						this._make_request(timer, send_and_wait, resolve, reject);
					}
					else
					{
						this._add_to_queue().then((data) =>
						{
							let timer = setTimeout(throw_exception, 3000);

							model._data.url = model._data_block.url;
							model._data.data = data.post_data;

							this._make_request(timer, send_and_wait, resolve, reject);
						});
					}
				};

			window.addEventListener('send_request', send_and_wait, false);
		});

	return model._sending;
};


Request_Manager_Block.prototype.next = function(post_url, post_data, post_name)
{
	return new Promise((resolve, reject) =>
	{
		this._add_request(post_url, post_data);

		this._run_sending().then(response =>
		{
			if(typeof response.json[post_name] !== 'undefined')
				response = response.json[post_name];
			else
				reject({
					content: 'Request_Manager_Block error: Invalid response.',
					code: response.code,
				});

			resolve(response);
		})
		.catch(reject);
	});
};


delete Request_Manager_Block.prototype.send;


Request_Manager_Block.prototype.send_list = function()
{
	APP.throw_event(window.EVENTS.send_request);
};
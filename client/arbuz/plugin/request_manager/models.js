/**
 * Created by mrskull on 16.07.17.
 */

import {data_controller} from '../../js/structure'


let
	requests,
	sending, // After will be promise


	add_request = function(url, post_data)
	{
		if(sending === undefined)
			clear_request();

		if(requests.url === undefined)
			requests.url = url;

		requests.list.push(post_data);
	},


	clear_request = function()
	{
		requests = {
			url: undefined,
			list: [],
		};

		sending = false;
	},


	preprocess_url = function()
	{
		console.log('url');
		let url = requests.url;

		if(url && url.substring && url.substring(0, 1) === '/')
			return url;
		else
			return data_controller.get('path');
	},


	post_data_prepare = function()
	{
		let post_data = {
			__content__: '',
		};

		for(let i = 0; i < requests.list.length; ++i)
		{
			if(i !== 0)
				post_data.__content__ += ' ';

			post_data.__content__ += requests.list[i].__content__;
		}

		post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

		return post_data;
	},


	send_queue = function()
	{
		return new Promise(function(resolve, reject)
		{
			let
				url = preprocess_url(),
				post_data = post_data_prepare();

			$.ajax({
				type: 'POST',
				url: url,
				data: post_data,
				complete: resolve,
			});
		});
	},


	run_sending = function()
	{
		if(sending === false)
		{
			sending = new Promise(function(resolve, reject)
			{
				window.APP.add_own_event('send_request', function()
				{
					send_queue().then(function(response, status)
					{
					    let data = response.__content__;

						resolve(data);
						reject(data);
					});
				});
			});
		}

		return sending;
	};


export {add_request, clear_request, run_sending};
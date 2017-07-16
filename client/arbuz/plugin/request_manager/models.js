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


		if(requests.list.length)
		{
			// --- Converting list of parts to string
			requests.list.forEach(function(element)
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
	},


	send_queue = function()
	{
		return new Promise(function(resolve, reject)
		{
			let
				url = preprocess_url(),
				post_data = post_data_prepare();

			if(post_data)
				$.ajax({
					type: 'POST',
					url: url,
					data: post_data,
					complete: resolve,
				});

			else
				reject(post_data);
		});
	},


	catch_timeout_error = function()
	{
		console.error('Request Manager error: Request Timeout. ' +
			'Run `send` in Request Manager.');

		clear_request();
	},


	run_sending = function()
	{
		if(sending === false)
			sending = new Promise(function(resolve, reject)
			{
				let
					timer = setTimeout(catch_timeout_error, 3000),


					send_request = function()
					{
						clearTimeout(timer);

						if(sending === false)
							reject('Request Manager error: Promise doesn\'t exist.');

						else
							send_queue().then(function(response)
							{
								let data = response.__content__;

								window.removeEventListener('send_request', send_request, false);

								resolve(data);
							});
					};


				window.addEventListener('send_request', send_request, false);
			});

		return sending;
	};


export {add_request, clear_request, run_sending};
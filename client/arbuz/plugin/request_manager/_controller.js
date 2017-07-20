/**
 * Created by mrskull on 19.07.17.
 */

import {Request_Manager} 		from './_init'

export {Request_Manager} 		from './_init'



Request_Manager.prototype.send = function(post_url, post_data, post_name)
{
	if(typeof post_name === 'undefined')
	{
		console.error('Request_Manager error: Invalid variable "post_name"');
		return false;
	}


	return new Promise((resolve, reject) =>
	{
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
		.catch((data) =>
		{
			console.error(data);
		});
	});
};
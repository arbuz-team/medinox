/**
 * Created by mrskull on 15.07.17.
 */

import * as models from './models'


export let Request_Manager = function()
{
	let that = this;


	// --------------

	this.next = function(url, post_data)
	{
		console.log('next');

		models.add_request(url, post_data);


		return new Promise(function(resolve, reject)
		{
			models.run_sending().then(function(data)
			{
				models.clear_request();

			    resolve(data);
			});
		})
	};


	this.send = function()
	{
		window.APP.throw_event(window.EVENTS.send_request);
	};
};
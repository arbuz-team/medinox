/**
 * Created by mrskull on 17.07.17.
 */

import {recognise_status} 	    from 'arbuz/plugin/utilities/response'
import {is_empty} 	            from 'arbuz/plugin/utilities/data'
import {Request_Manager_Main} 	from 'arbuz/plugin/request_manager/main'
import {Block_Loader} 			from './_controller'



export function Block_Loader_Dialog(config)
{
	Block_Loader.call(this, config);
}

Block_Loader_Dialog.prototype = Object.create(Block_Loader.prototype);







// --------------------------    MODEL    --------------------------


Block_Loader_Dialog.prototype._send_request = function()
{
	let
		post_data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Main();

	this._response = request_manager.send(undefined, post_data, post_name);
};


// --------------------------    VIEW    --------------------------


Block_Loader_Dialog.prototype._close_dialog_if_no_content = function(response)
{
	if(recognise_status(response.code) === 'success' && is_empty(response.html))
	{
		APP.DATA.delay = 0;
		APP.throw_event(EVENTS.part.close_dialog);
		return true;
	}

	return false;
};


// --------------------------    CONTROLLER    --------------------------


Block_Loader_Dialog.prototype.load_content = function(post_url, post_data)
{
	return new Promise(resolve =>
	{
		this._get_content(post_url, post_data);

		this._hide_content().then(() =>
		{
			this._receive_response().then(response =>
			{
				if(this._close_dialog_if_no_content(response))
					resolve(response);

				this._set_content(response);

				this._prepare_content_to_show();

				this._show_content().then(() =>
				{
					resolve(response);
				});
			});
		});
	});
};


Block_Loader_Dialog.prototype.define = function()
{
};
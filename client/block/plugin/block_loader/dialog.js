/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Dialog} 	from 'arbuz/plugin/request_manager/dialog'
import {Block_Loader} 				from './_controller'



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
		request_manager = new Request_Manager_Dialog();

	this.response = request_manager.send(undefined, post_data, post_name);
};




Block_Loader_Dialog.prototype.close_dialog_if_json = function(response, status)
{
	if(status !== 'success')
		return false;

	if(response === '{"__form__": "true"}')
	{
		APP.DATA.delay = 0;
		APP.throw_event(EVENTS.part.close_dialog);
		return true;
	}

	return false;
};


Block_Loader_Dialog.prototype.load_content = function(post_url, post_data)
{
	return new Promise((resolve) =>
	{
		this._get_content(post_url, post_data);

		this._hide_content().then(() =>
		{
			this._receive_response().then(response =>
			{
				if(this.close_dialog_if_json(response))
					return false;

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
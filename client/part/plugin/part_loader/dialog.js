/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Dialog} 	from 'arbuz/plugin/request_manager/dialog'
import {Part_Loader} 				from './_controller'



export function Part_Loader_Dialog(config)
{
	Part_Loader.call(this, config);
}

Part_Loader_Dialog.prototype = Object.create(Part_Loader.prototype);







// --------------------------    MODEL    --------------------------


Part_Loader_Dialog.prototype._send_request = function()
{
	let
		post_data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Dialog();

	this.response = request_manager.send(undefined, post_data, post_name);
};




Part_Loader_Dialog.prototype.close_dialog_if_json = function(response, status)
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


Part_Loader_Dialog.prototype.load_content = function(post_url, post_data)
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


Part_Loader_Dialog.prototype.define = function()
{
};
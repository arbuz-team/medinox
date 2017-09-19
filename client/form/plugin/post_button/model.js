/**
 * Created by mrskull on 31.01.17.
 */

import {Post_Button}     from './_init'
export {Post_Button}     from './_init'

import {Request_Manager_Main}   from 'arbuz/plugin/request_manager/main'
import {timeout_promise}        from 'arbuz/plugin/utilities/standard'
import {recognise_status}       from 'arbuz/plugin/utilities/response'




Post_Button.prototype._is_loading = function()
{
	return this._variables.is_loading === true;
};


Post_Button.prototype._is_not_loading = function()
{
	return this._variables.is_loading === false;
};


Post_Button.prototype._set_loading = function()
{
	this._variables.is_loading = true;
};


Post_Button.prototype._set_end_loading = function()
{
	this._variables.is_loading = false;
};


Post_Button.prototype._is_error = function(response)
{
	return recognise_status(response.code) !== 'success';
};


Post_Button.prototype._prepare_post_data = function()
{
	let
		data = {},
		post_name = this._settings.post_name,

		value = this._button_data.value,
		action = this._button_data.action,
		other_1 = this._button_data.other_1,
		other_2 = this._button_data.other_2,
		other_3 = this._button_data.other_3;


	data[post_name] = 'button';
	data._name_= action;

	if(value)
		data.value = value;

	data.other_1 = other_1 || '';
	data.other_2 = other_2 || '';
	data.other_3 = other_3 || '';

	this._settings.post_data = data;
};


Post_Button.prototype._send_post = function()
{
	return new Promise((resolve) =>
	{
		timeout_promise(200).then(() =>
		{
			let
				post_url = this._settings.url,
				post_data = this._settings.post_data,
				post_name = this._settings.post_name,
				request_manager = new Request_Manager_Main();


			request_manager
				.send(post_url, post_data, post_name)
				.then(resolve, resolve);
		});
	});
};

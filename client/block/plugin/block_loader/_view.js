/**
 * Created by mrskull on 17.07.17.
 */

import * as img_loader      from './img_loader';
import {Block_Loader} 		from './_init'



// --------------------------    RESPONSE    --------------------------


Block_Loader.prototype._hide_content = function()
{
	return new Promise((resolve) =>
	{
		let
			container = this._settings.container,
			opacity = this._settings.opacity_hide,
			duration = this._settings.duration_hide;

		$(container).animate({opacity: opacity}, duration, resolve);
	});
};


Block_Loader.prototype._get_content = function(post_url, post_data)
{
	this._prepare_to_change_content(post_url);
	this._prepare_post_data(post_data);

	this._send_request();
};



// --------------------------    RESPONSE    --------------------------


Block_Loader.prototype._receive_response = function()
{
	return new Promise((resolve) =>
	{
		this.response.then((response) =>
		{
			resolve(this._preprocess_response(response));
		});
	});
};


Block_Loader.prototype._prepare_content_to_show = function()
{
	if(this._state.reload === false)
		$(this._settings.container).scrollTop(0);

	this._refresh_events();
	img_loader.define();
};


Block_Loader.prototype._set_content = function(response)
{
	$(this._settings.container).html(response.html)
};


Block_Loader.prototype._show_content = function()
{
	return new Promise((resolve) =>
	{
		let
			container = this._settings.container,
			opacity = this._settings.opacity_show,
			duration = this._settings.duration_show;

		$(container).animate({opacity: opacity}, duration, resolve);
	});
};
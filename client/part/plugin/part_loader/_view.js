/**
 * Created by mrskull on 17.07.17.
 */

import * as img_loader      from './img_loader';
import {Part_Loader} 		from './_init'





Part_Loader.prototype.hide_content = function()
{
	return new Promise((resolve) =>
	{
		let
			container = this.settings.container,
			opacity = this.settings.opacity_hide,
			duration = this.settings.duration_hide;

		$(container).animate({opacity: opacity}, duration, resolve);
	});
};


Part_Loader.prototype.prepare_content_to_show = function(data)
{
	let
		$container = $(this.settings.container),
		error = this.variables.error;

	if(this.variables.reload === false)
		$container.scrollTop(0);

	if(this.check_for_errors(data.status, data.code))
		return false;

	if(error !== true || status === 'success')
		$container.html(data.html);

	this.variables.error = false;
	this.variables.url = '';

	this.refresh_events();
	img_loader.define();
};


Part_Loader.prototype.show_content = function()
{
	return new Promise((resolve) =>
	{
		let
			container = this.settings.container,
			opacity = this.settings.opacity_show,
			duration = this.settings.duration_show;

		$(container).animate({opacity: opacity}, duration, resolve);
	});
};


Part_Loader.prototype.after_show_content = function(data)
{
	if(this.external_callback)
		this.external_callback(data.html, data.status, data.code);
};


Part_Loader.prototype.load_content = function(url, post_data, callback)
{
	this.variables.url = url;
	this.external_callback = callback;

	this.prepare_content_to_change(url, post_data);

	this.send_request(url);

	this.hide_content().then(() =>
	{
		this.receive_response().then((data) =>
		{
			this.prepare_content_to_show(data);

			this.show_content().then(() =>
			{
				this.after_show_content(data);
			});
		});
	});
};
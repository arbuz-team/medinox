/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} 	from 'arbuz/js/structure'
import {select_number} 	from 'arbuz/plugin/utilities/data'
import {timeout_promise} 	from 'arbuz/plugin/utilities/standard'

import {Part_Loader} 		from './_init'
import './_model'
import './_view'

export {Part_Loader} 		from './_init'




Part_Loader.prototype.redirect = function()
{
	return new Promise((resolve) =>
	{
		let
			url = APP.DATA.redirect || data_controller.get('path'),
			delay = select_number(APP.DATA.delay, 0),
			state = this._state,
			variables = this._variables;

		state.can_do_redirect = true;
		clearTimeout(variables.redirect_time_out);

		variables.redirect_time_out = setTimeout(() =>
		{
			if(state.can_do_redirect === true)
				this.load_content(url).then(resolve);
		}, delay);
	});
};


Part_Loader.prototype.reload = function()
{
	return new Promise((resolve) =>
	{
		let delay = select_number(APP.DATA.delay, 0);

		timeout_promise(delay).then(() =>
		{
			this.load_content().then(resolve);
		})
	});
};


Part_Loader.prototype.load_content = function(post_url, post_data)
{
	return new Promise((resolve) =>
	{
		this._get_content(post_url, post_data);

		this._hide_content().then(() =>
		{
			this._receive_response().then((response) =>
			{
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


Part_Loader.prototype.define = function()
{
	APP.add_own_event(this._settings.part_name +'_reload', () =>
	{
		this.reload();
	});
};
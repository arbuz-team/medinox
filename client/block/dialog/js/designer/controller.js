/**
 * Created by mrskull on 18.07.17.
 */

import {timeout_promise} from 'arbuz/plugin/utilities/standard'
import {Dialog_Designer_View} from './view'


export function Dialog_Designer_Controller(config)
{

	let
		view = new Dialog_Designer_View(config),


	// --------------------------------------------------------

		cancel_event = function(event)
		{
			event.stopPropagation();
		},

		close_with_cancel_event = (event) =>
		{
			cancel_event(event);
			this.close();
		},

		close_with_delay = () =>
		{
			return new Promise((resolve) =>
			{
				let delay = 0;

				if(APP.DATA.delay >= 0)
					delay = APP.DATA.delay;
				else
					delay = 2000;


				timeout_promise(delay).then(() =>
				{
					this.close().then(resolve);
				});
			});
		};

	// --------------------------------------------------------


	this.set_loading = function()
	{
		return view.dim();
	};


	this.unset_loading = function()
	{
		return view.lighten();
	};


	this.close = function()
	{
		return view.hide();
	};


	this.open = function()
	{
		return view.show();
	};


	// --------------------------------------------------------

	this.define = function()
	{
		$(view.selector.html_id).click(close_with_cancel_event);
		$(view.selector.window).click(cancel_event);
	};
}
/**
 * Created by mrskull on 31.08.17.
 */

import * as model                   from './model'
import {event_broker}               from 'arbuz/plugin/utilities/event'
import {Currency_Converter_View}    from './view'


export function Currency_Converter_Controller(config)
{
	if(!config || !config.container)
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}

	let container = config.container,
		view = new Currency_Converter_View();


	this.define = function()
	{
		$(model.selector.checkbox, container)   .each(event_broker(view.change_status_field))
												.change(event_broker(view.change_status_field));

		$(model.selector.button, container)     .click(event_broker(view.calculate));
	}
}

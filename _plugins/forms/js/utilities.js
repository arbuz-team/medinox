/**
 * Created by mrskull on 08.05.17.
 */

export let

	html_is_error = function(HTML_response, status)
	{
		if(status !== 'success')
			return true;

		if(HTML_response === '')
			return true;

		return false;
	},


	json_is_error = function(JSON_response, status)
	{
		if(status !== 'success')
			return true;

		let response = JSON.parse(JSON_response);

		if(response.__button__ !== 'true')
			return true;

		return false;
	},


	reload_plugins = function(plugins)
	{
		let
			plugins_array, array_length;

		if(!plugins || typeof plugins !== 'string')
			return false;

		plugins_array = plugins.split(' ');
		array_length = plugins_array.length;

		for(let i = 0; i < array_length; ++i)
			if(plugins_array[i])
			{
				window.APP.DATA.delay = 0;
				window.APP.throw_event(window.EVENTS.plugins['reload_'+ plugins_array[i]]);
			}
	},


	redirect_ground = function(url)
	{
		if(!url || typeof url !== 'string')
			return false;

		window.APP.DATA.redirect = url;
		window.APP.DATA.delay = 100;
		window.APP.throw_event(window.EVENTS.redirect);
	},


	launch_event = function(event)
	{
		let
			split_event,
			ready_event = window.EVENTS;

		if(!event || typeof event !== 'string')
			return false;

		split_event = event.split('.');

		for(let i = 0; split_event.length > i; ++i)
			ready_event = ready_event[split_event[i]];

		if(ready_event.constructor === Event)
		{
			window.APP.DATA.delay = 100;
			window.APP.throw_event(ready_event); // example plugins.close_cart
		}
	};
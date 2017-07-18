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


	prepare_delay = function(data)
	{
		let delay = data.delay;

		if(delay >= 0)
			APP.DATA.delay = delay;
		else
			APP.DATA.delay = 0;
	},


	reload_plugins = function(data)
	{
		let
			plugins = data.reload, // examples: "cart ground header navigation"
			plugins_array,
			array_length;

		if(!plugins || typeof plugins !== 'string')
			return false;

		plugins_array = plugins.split(' ');
		array_length = plugins_array.length;

		for(let i = 0; i < array_length; ++i)
			if(plugins_array[i])
			{
				prepare_delay(data);
				APP.throw_event(EVENTS.part['reload_'+ plugins_array[i]]);
			}
	},


	redirect_ground = function(data)
	{
		let url = data.redirect; // examples: "/contact/" or "https://google.com/"

		if(!url || typeof url !== 'string')
			return false;

		APP.DATA.redirect = url;
		prepare_delay(data);
		APP.throw_event(EVENTS.redirect);
	},


	launch_event = function(data)
	{
		let
			events = data.events, // events examples: "plugins.close_cart plugins.close_dialog"
			events_array,
			array_length;

		if(!events || typeof events !== 'string')
			return false;

		events_array = events.split(' ');
		array_length = events_array.length;


		for(let i = 0; i < array_length; ++i)
			if(events_array[i])
			{
				let select_event = events_array[i],
					split_event,
					ready_event = EVENTS;

				split_event = select_event.split('.');

				for(let i = 0; split_event.length > i; ++i)
					if(typeof ready_event[split_event[i]] === 'undefined')
						console.error('Launch Event error: Event doesn\'t exist.');
					else
						ready_event = ready_event[split_event[i]];


				if(ready_event.constructor === Event)
				{
					prepare_delay(data);
					APP.throw_event(ready_event); // example plugins.close_cart
				}
				else
					console.error('Event error: This event doesn\'t exist');
			}
	};
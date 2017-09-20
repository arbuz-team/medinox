/**
 * Created by mrskull on 08.05.17.
 */

import {Request_Manager_Block} from 'arbuz/plugin/request_manager/block'
import {timeout_promise} from 'arbuz/plugin/utilities/standard'
import {} from 'arbuz/plugin/utilities/data'


let

	get_event_creator = function(events, text_event)
	{
		let
			fun,
			end_position_of_function = text_event.indexOf('(');

	    if(end_position_of_function > 0)
	    {
		    let fun_string = text_event.slice(0, end_position_of_function);

		    fun = events[fun_string];

	    	if(typeof fun !== 'undefined' && fun.constructor !== Event)
				return fun;
	    }
	},


	get_args_from_event = function(text_event)
	{
		let
			bracket_1 = text_event.indexOf('('),
			bracket_2 = text_event.indexOf(')'),
			args_obj = {};

		if(bracket_1 >= 0 && bracket_2 > bracket_1)
		{
			let
				start_slice = bracket_1 + 1,
				end_slice = bracket_2,

				phrase = text_event.slice(start_slice, end_slice),
				split_args;

			if(phrase.indexOf(',') > 0)
				split_args = phrase.split(',');
			else
				split_args = [phrase];


			for(let i = 0; split_args.length > i; ++i)
			{
				let
					arg = split_args[i],
					value_position = arg.indexOf(':'),
					name = arg.slice(0, value_position),
					value = arg.slice(value_position + 1);

				if(name && value)
					args_obj[name] = value;
			}


			return args_obj;
		}

		return {}
	};


export let

	request_manager = new Request_Manager_Block(),


	get_data = function(elem, name)
	{
		return $(elem).data(name);
	},


	get_and_remove_data = function(elem, name)
	{
		let
			data = get_data(elem, name);

		// $(elem).removeAttr('data-'+ name);

		return data;
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
			plugins = data.reload, // examples: "cart ground dialog"
			plugins_array,
			array_length,
			delay = 0;

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


		if(typeof APP.DATA.delay !== 'undefined')
		{
			delay = APP.DATA.delay;
			APP.DATA.delay = undefined;
		}

		timeout_promise(delay).then(() => {
			request_manager.send_list();
		});
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
			events = data.events, // events examples: "part.close_cart part.close_dialog"
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
					events = EVENTS,
					ready_event;

				split_event = select_event.split('.');

				for(let i = 0; split_event.length > i; ++i)
					if(typeof events[split_event[i]] === 'undefined')
					{
						let
							fun = get_event_creator(events, split_event[i]),
							args = get_args_from_event(split_event[i]);

						if(fun && args)
							ready_event = fun(args);
						else
							console.error('Launch Event error: Event '+ split_event[i] +' doesn\'t exist.');
					}
					else
						ready_event = events[split_event[i]];


				if(ready_event.constructor === Event || ready_event.constructor === CustomEvent)
				{
					prepare_delay(data);
					APP.throw_event(ready_event); // example part.close_cart
				}
				else
					console.error('Event error: This event doesn\'t exist');
			}
	};
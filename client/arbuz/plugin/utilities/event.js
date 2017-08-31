/**
 * Created by mrskull on 31.08.17.
 */


export let

	event_broker = function(fun)
	{
		return function(event)
		{
			fun(this, event);
		};
	};
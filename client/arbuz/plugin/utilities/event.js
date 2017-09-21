/**
 * Created by mrskull on 31.08.17.
 */


export let

	event_creator = function(name)
	{
		return function(args)
		{
			return new CustomEvent(name, {
				'detail': args,
			});
		};
	},


	event_broker = function(fun)
	{
		return function(event)
		{
			fun(this, event);
		};
	};
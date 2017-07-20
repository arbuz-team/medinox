/**
 * Created by mrskull on 18.07.17.
 */


export let

	timeout_promise = function(delay)
	{
	    return new Promise(function(resolve)
	    {
	        setTimeout(function()
	        {
				resolve();
	        }, delay);
	    });
	};
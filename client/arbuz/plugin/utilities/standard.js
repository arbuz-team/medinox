/**
 * Created by mrskull on 18.07.17.
 */

import {is_not_number} from "arbuz/plugin/utilities/data";



export let

	timeout_promise = function(delay)
	{
		if(is_not_number(delay))
			delay = 0;

	    return new Promise(function(resolve)
	    {
	        setTimeout(function()
	        {
				resolve();
	        }, delay);
	    });
	};
/**
 * Created by mrskull on 20.07.17.
 */


export let


	recognise_status = function(code)
	{
		if(code >= 200 && code < 300)
	        return 'success';

		if(code >= 300 && code < 400)
			return 'redirect';

		return 'error';
	};
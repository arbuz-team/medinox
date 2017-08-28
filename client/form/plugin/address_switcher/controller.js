/**
 * Created by mrskull on 28.08.17.
 */

import {Address_Switcher} from './main'


export function Address_Switcher_Controller(config)
{
	if(!config || !config.container)
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}

	this.container = config.container;


	let
		add_switcher = function()
		{
			new Address_Switcher(this);
		};


	this.define = function()
	{
		$('.form-address_switcher', this.container).each(add_switcher);
	}
}

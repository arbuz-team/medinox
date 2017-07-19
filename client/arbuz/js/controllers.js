/**
 * Created by mrskull on 24.11.16.
 */

import * as searcher_controllers      	from 'block/searcher/js/controllers'
import * as cart_controllers          	from 'block/cart/js/controllers'
import * as navigation_controllers    	from '../../block/menu_mobile/js/controllers'
import * as header_controllers        	from '../../block/menu/js/controllers'
import * as dialog_controllers        	from 'block/dialog/js/controller'

import * as ground_controllers        	from 'block/ground/js/controllers'

import {Request_Manager_Block} 			from 'arbuz/plugin/request_manager/block'


/*---------------- Wydarzenia na stronie ----------------*/

let

	reload_sign_in = function(permissions)
	{
		return function()
		{
			let
				delay = APP.DATA.delay,

				reload = function()
				{
					APP.throw_event(EVENTS.part.reload_header);
					APP.throw_event(EVENTS.part.reload_navigation);

					if(permissions === 'root')
						APP.throw_event(EVENTS.part.reload_searcher);

					if(permissions === 'user')
						APP.throw_event(EVENTS.part.reload_cart);
				};

			if(delay)
				setTimeout(reload, delay);
			else
				reload();
		};
	},

	reload_website = function()
	{
		let delay;

		if(APP.DATA.delay)
			delay = APP.DATA.delay;
		else
			delay = 0;

		setTimeout(function()
		{
			window.location.reload();
		}, delay);
	},


	define = function()
	{
		$('*').off(); // Usuń wszystkie wydarzenia ze wszystkich elementów

		searcher_controllers.define();
		cart_controllers.define();
		navigation_controllers.define();
		header_controllers.define();
		dialog_controllers.define();
		ground_controllers.define();
	};


export let start = function()
{
	let request_manager = new Request_Manager_Block();

	APP.add_own_event('define', define);
	APP.add_own_event('reload_website', reload_website);
	APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
	APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));

	searcher_controllers.get_content();
	cart_controllers.get_content();
	navigation_controllers.get_content();
	header_controllers.get_content();
	ground_controllers.get_content();

	request_manager.send_list();

	define();
};
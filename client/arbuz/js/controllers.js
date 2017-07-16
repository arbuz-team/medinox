/**
 * Created by mrskull on 24.11.16.
 */

import * as searcher_controllers      from '../../part/searcher/js/controllers'
import * as cart_controllers          from '../../part/cart/js/controllers'
import * as navigation_controllers    from '../../part/navigation/js/controllers'
import * as header_controllers        from '../../part/header/js/controllers'
import * as dialog_controllers        from '../../part/dialog/js/controllers'

import * as ground_controllers        from '../../part/ground/js/controllers'

import {Request_Manager} from '../plugin/request_manager/main'


/*---------------- Wydarzenia na stronie ----------------*/

let

	reload_sign_in = function(permissions)
	{
		return function()
		{
			let
				delay = window.APP.DATA.delay,

				reload = function()
				{
					window.APP.throw_event(window.EVENTS.plugins.reload_header);
					window.APP.throw_event(window.EVENTS.plugins.reload_navigation);

					if(permissions === 'root')
						window.APP.throw_event(window.EVENTS.plugins.reload_searcher);

					if(permissions === 'user')
						window.APP.throw_event(window.EVENTS.plugins.reload_cart);
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

		if(window.APP.DATA.delay)
			delay = window.APP.DATA.delay;
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
	let request_manager = new Request_Manager();

	window.APP.add_own_event('define', define);
	window.APP.add_own_event('reload_website', reload_website);
	window.APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
	window.APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));

	searcher_controllers.get_content();
	cart_controllers.get_content();
	navigation_controllers.get_content();
	header_controllers.get_content();
	ground_controllers.get_content();

	request_manager.send();

	define();
};
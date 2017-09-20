/**
 * Created by mrskull on 24.11.16.
 */

import {Search_Controller}      	from 'block/searcher/js/controller'
import {Cart_Controller}         	from 'block/cart/js/controller'
import {Menu_Mobile_Controller}    	from 'block/menu_mobile/js/controller'
import {Menu_Controller}            from 'block/menu/js/controller'
import {Dialog_Controller}        	from 'block/dialog/js/controller'
import {Ground_Controller}        	from 'block/ground/js/controller'

import {Request_Manager_Block} 	    from 'arbuz/plugin/request_manager/block'



export function Page_Controller()
{
	if(typeof Page_Controller.instance === 'object')
		return Page_Controller.instance;

	Page_Controller.instance = this;


	let
		searcher_controller = new Search_Controller(),
		cart_controller = new Cart_Controller(),
		menu_mobile_controller = new Menu_Mobile_Controller(),
		menu_controller = new Menu_Controller(),
		dialog_controller = new Dialog_Controller(),
		ground_controller = new Ground_Controller(),


		reload_sign_in = function(permissions)
		{
			return function()
			{
				let
					request_manager = new Request_Manager_Block(),
					delay = APP.DATA.delay,

					reload = function()
					{
						menu_mobile_controller.get_content();
						menu_controller.get_content();

						if(permissions === 'root')
							searcher_controller.get_content();

						if(permissions === 'user')
							cart_controller.get_content();

						request_manager.send_list();
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


		redirect_website = function(event)
		{
			let args = event.detail;

			if(args.url)
			window.location = args.url;
		},


		define = () =>
		{
			let $textarea = $('textarea');

			$('*').off(); // Usuń wszystkie wydarzenia ze wszystkich elementów

			window.autosize.destroy($textarea);
			window.autosize($textarea);
			searcher_controller.define();
			cart_controller.define();
			menu_mobile_controller.define();
			menu_controller.define();
			dialog_controller.define();
			ground_controller.define();
		};


	APP.add_own_event('define', define);
	APP.add_own_event('reload_website', reload_website);
	APP.add_own_event('redirect_website', redirect_website);
	APP.add_own_event('reload_user_sign_in', reload_sign_in('user'));
	APP.add_own_event('reload_root_sign_in', reload_sign_in('root'));


	this.get_height = function()
	{
		return $('#CONTAINER').innerHeight();
	};


	this.start = function()
	{
		define();
		let request_manager = new Request_Manager_Block();

		searcher_controller.get_content();
		cart_controller.get_content();
		menu_mobile_controller.get_content();
		menu_controller.get_content();
		ground_controller.get_content();

		request_manager.send_list();

	};
}
/**
 * Created by mrskull on 24.11.16.
 */


window.EVENTS = {
	send_request:               new Event('send_request'),
	define:                     new Event('define'),
	redirect:                   new Event('redirect'),
	reload_website:             new Event('reload_website'),

	part: {
		open_cart:              new Event('cart_open'),
		open_menu_mobile:       new Event('menu_mobile_open'),
		open_searcher:          new Event('searcher_open'),

		open_or_close_cart:     new Event('cart_open_or_close'),

		close:                  new Event('plugins_close'),
		close_cart:             new Event('cart_close'),
		close_menu_mobile:      new Event('menu_mobile_close'),
		close_dialog:           new Event('dialog_close'),

		reload_root_sign_in:    new Event('reload_root_sign_in'),
		reload_user_sign_in:    new Event('reload_user_sign_in'),

		reload_menu_mobile:     new Event('menu_mobile_reload'),
		reload_menu:            new Event('menu_reload'),
		reload_cart:            new Event('cart_reload'),
		reload_searcher:        new Event('searcher_reload'),
		reload_ground:          new Event('ground_reload'),
		reload_dialog:          new Event('dialog_reload'),
	},
};
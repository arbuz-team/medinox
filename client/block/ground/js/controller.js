/**
 * Created by mrskull on 08.01.17.
 */

import {Ground_View}        from './view'


export function Ground_Controller()
{
	if(typeof Ground_Controller.instance === 'object')
		return Ground_Controller.instance;

	Ground_Controller.instance = this;


	let
		view = new Ground_View(),
		model = view.model,


		transfer_event = function(fun) // don't use for APP.add_own_event!!!
		{
			return function(event)
			{
				fun(this, event);
			}
		};


	this.is_redirect = response =>
	{
		return model.is_redirect(response);
	};
	this.change_url = url => model.change_url(url);
	this.load_single_ground_content = () => model.load_single_ground_content();


	this.define = function()
	{
		view.change_height_content();

		$('a').click( transfer_event( view.go_to_link));
		APP.add_own_event('redirect', model.redirect_ground);
		APP.add_own_event('popstate', model.back_url);
		$(window).resize( transfer_event( view.change_height_content));


		let $container = $(model.container);

		$('.change_length', $container)
			.click( transfer_event( view.change_to_long));
		$('.change_length .change_length-button', $container)
			.click( transfer_event( view.change_to_long_or_short));

		model.ground_form_controller.define();
		model.define_post_button(model.config_loader);
		model.event_button_controller.define();
	};


	this.get_content = function()
	{
		model.ground_loader.define();
		model.load_ground_content();
	};
}
/**
 * Created by mrskull on 08.01.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/part'
import {Page_Controller}                from 'arbuz/js/controllers';
import {Menu_Controller}     			from 'block/menu/js/controller'

import {Form_Controllers}               from 'form/js/controller'
import {Post_Button_Controllers}        from 'form/plugin/post_button/controllers'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'



export function Ground_Controller()
{
	if(typeof Ground_Controller.instance === 'object')
		return Ground_Controller.instance;

	Ground_Controller.instance = this;


	let
		container = '.ground',

		config_loader = {
			part_name: 'ground',
			container: container,
			load_meta_tags: true,
		},
		config_form = {
			part_name: 'ground',
			container: container,
		},


		ground_loader = new Block_Loader_Part(config_loader),

		post_button_controller = new Post_Button_Controllers(config_form),
		event_button_controller = new Event_Button_Controllers(config_form),
		ground_form_controller = new Form_Controllers(config_loader),

		page_controller = new Page_Controller(),
		menu_controller = new Menu_Controller(),


	/**
	 *    Defining private functions
	 */


		change_url = function(url)
		{
			history.pushState('', url, url);
		},


		go_to_link = function(event)
		{
			let
				url = $(this).attr('href'),
				protocol = url.substring(0, 4);


			if(protocol !== 'http')
				if(event.which === 1)
				{
					event.preventDefault();
					APP.throw_event(EVENTS.part.close);

					change_url(url);

					ground_loader.load_simple_content(url);
				}
		},


		redirect = function(event)
		{
			change_url(APP.DATA.redirect);
			ground_loader.redirect(event);
		},


		back_url = function()
		{
			event.preventDefault();
			ground_loader.load();
		},


		change_height_start_banner = function($container, height_container)
		{
			let
				width_website = page_controller.get_height(),
				height_start_banner = 0;

			if(height_container > 768)
				height_start_banner = height_container - 386;

			if(height_start_banner === 0 || width_website < 1000)
			{
				$('.ground-block.start .block-content-image', $container).hide();
				$('.ground-block.start .block-content-recommended-title', $container).show();
			}
			else
			{
				$('.ground-block.start .block-content-image', $container).show().height(height_start_banner);
				$('.ground-block.start .block-content-recommended-title', $container).hide();
			}
		},


		change_height_content = function()
		{
			let

				$container = $(container),
				height = {
					window: page_controller.get_height(),
					header: menu_controller.get_height(),
					ground_top: $container.position().top,
				},
				height_container = height.window - height.header - height.ground_top;

			$container.height(height_container);
			change_height_start_banner($container, height_container)
		},


		change_to_long_or_short = function(event)
		{
			let $element = $(this).parents('.change_length');
			event.stopPropagation();

			if($element.hasClass('is-long'))
				$element.removeClass('is-long');
			else
				$element.addClass('is-long');
		},


		change_to_long = function(event)
		{
			event.stopPropagation();

			$(this).addClass('is-long');
		};



	this.define = function()
	{
		change_height_content();

		$('a').click(go_to_link);
		APP.add_own_event('redirect', redirect);
		APP.add_own_event('popstate', back_url);
		$(window).resize(change_height_content);


		let $container = $(container);

		$('.change_length', $container).click(change_to_long);
		$('.change_length .change_length-button', $container).click(change_to_long_or_short);

		ground_form_controller.define();
		post_button_controller.define();
		event_button_controller.define();
	};


	this.get_content = function()
	{
		ground_loader.define();
		ground_loader.load_content();
	};
}
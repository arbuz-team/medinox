/**
 * Created by mrskull on 22.08.17.
 */

import {Ground_Model}       from './model'


export function Ground_View()
{
	let model;

	this.model = new Ground_Model();
	model = this.model;

	this.go_to_link = function(that, event)
	{
		let
			url = $(that).attr('href'),
			protocol = url.substring(0, 4),
			mailto = url.substring(0, 7);


		if(protocol !== 'http' && protocol !== 'tel:' && mailto !== 'mailto:')
			if(event.which === 1)
			{
				event.preventDefault();
				APP.throw_event(EVENTS.part.close);

				model.change_url(url);

				model.load_single_ground_content(url);
			}
	};


	this.change_height_start_banner = function($container, height_container)
	{
		let
			width_website = model.page_controller.get_height(),
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
	};


	this.change_height_content = () =>
	{
		let

			$container = $(model.container),
			height = {
				window: model.page_controller.get_height(),
				header: model.menu_controller.get_height(),
				ground_top: $container.position().top,
			},
			height_container = height.window - height.header - height.ground_top;

		$container.height(height_container);
		this.change_height_start_banner($container, height_container);
	};


	this.change_to_long_or_short = function(that, event)
	{
		let $element = $(that).parents('.change_length');
		event.stopPropagation();

		if($element.hasClass('is-long'))
			$element.removeClass('is-long');
		else
			$element.addClass('is-long');
	};


	this.change_to_long = function(that, event)
	{
		event.stopPropagation();

		$(that).addClass('is-long');
	};
}
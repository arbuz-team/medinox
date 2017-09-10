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


	this._change_height_ground = function()
	{
		let
			$ground = $(model.container),
			height = {
				window: model.page_controller.get_height(),
				header: model.menu_controller.get_height(),
				ground_top: $ground.position().top,
			},
			height_ground = height.window - height.header - height.ground_top;

		$ground.height(height_ground);
	};


	this._change_height_ground_by_spacer = function()
	{
		let
			$ground =           $(model.container),
			$ground_block =     $ground.find('.ground-block'),
			$spacer =           $ground.find('.ground-block-spacer'),
			$footer =           $ground.find('.footer'),
			height = {
				window:             model.page_controller.get_height(),
				header:             model.menu_controller.get_height(),
				ground_top:         $ground.position().top,
				ground_blocks:      0,
				footer:             parseInt($footer.outerHeight()),
			},
			height_spacer = height.window - height.header - height.ground_top - height.footer;

		if($ground_block.length)
			$ground_block.each(function()
			{
				height.ground_blocks += parseInt($(this).outerHeight());
			});

		height_spacer -= height.ground_blocks;

		if(height_spacer > 0)
		{
			console.log($spacer.length);
			if($spacer.length < 1)
				$($footer).before('<div class="ground-block-spacer">&nbsp;</div>');

			$ground.find('.ground-block-spacer').height(height_spacer);
		}
		else if($spacer.length)
			$spacer.remove();
	};


	this.change_height_content = () =>
	{
		this._change_height_ground();
		this._change_height_ground_by_spacer();
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
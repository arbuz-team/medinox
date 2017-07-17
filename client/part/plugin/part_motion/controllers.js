/**
 * Created by mrskull on 06.01.17.
 */

import {Plugins_Motion_Views} from './views'


export let Plugins_Motion_Controllers = function(config)
{
	let
		plugin_motion_views = new Plugins_Motion_Views(config),
		settings = plugin_motion_views.models.settings;

	this.views = plugin_motion_views;

	///////////////////////////////

	let

		// swipe_open = function()
		// {
		//   if(plugin_motion_views.models.check_possibility_of_swipe())
		//     plugin_motion_views.plugin_open();
		// },


		// swipe_close = function()
		// {
		//   if(plugin_motion_views.models.check_possibility_of_swipe())
		//     plugin_motion_views.plugin_close();
		// },
		//
		//
		// pre_swipe_open = function(event)
		// {
		//   let y = event.gesture.center.y - event.gesture.distance;
		//
		//   if(y <= 70)
		//     swipe_open();
		// },


		pre_plugin_close = function()
		{
			let
				container = settings.container,
				$container = $(container),
				$window = $(window);

			if(container !== '#CART')
				plugin_motion_views.plugin_close();
			else if($container.outerWidth() === $window.width())
				plugin_motion_views.plugin_close();
		},


		if_horizontal_resize = function(callback)
		{
			let
				window_width,
				set_window_width = function()
				{
					window_width = window.innerWidth;
				};

			set_window_width();

			return function()
			{
				let
					new_window_width = window.innerWidth;

				if(window_width != new_window_width)
				{
					set_window_width();
					callback();
				}
			}
		},


		stop_propagation = function(event)
		{
			event.stopPropagation();
		};


	this.set_start_position = function()
	{
		let
			$container = $(settings.container),
			position,
			width = $container.outerWidth(),
			direction_open = settings.direction_open,
			direction_close = settings.direction_close;

		settings.height = '100%';
		settings.width = width;

		if(direction_open === 'top' || direction_open === 'bottom')
			position = -settings.height;

		else if(direction_open === 'left' || direction_open === 'right')
			position = -width;

		if(position)
			$($container).css(direction_close, position);
	};


	//////////////////////////////////////////

	this.define = function()
	{
		let
			$window = $(window),
			$body = $('body'),
			$container = $(settings.container),
			$content = $(settings.content),
			$hide = $(settings.container +' > '+ settings.hide);

		// -- Swipe events
		// if(settings.direction_open === 'top' || settings.direction_open === 'bottom')
		//   $body.hammer().on(settings.swipe_open, pre_swipe_open);
		// else
		//   $body.hammer().on(settings.swipe_open, swipe_open);
		//
		// $body.hammer().on(settings.swipe_close, swipe_close);
		// $body.data('hammer').get('swipe').set({ direction: Hammer.DIRECTION_ALL });



		if(settings.container !== '#CART' && settings.container !== '#NAVIGATION')
		{
			$body.click(plugin_motion_views.plugin_close);
			$hide.click(plugin_motion_views.plugin_close);
			$container.click(stop_propagation);
			this.set_start_position();
		}

		else if(settings.container === '#NAVIGATION')
		{
			$container.click(plugin_motion_views.plugin_close);
			$content.click(stop_propagation);
			this.set_start_position();
		}

		else if($container.outerWidth() === $window.width())
				this.set_start_position();


		$window.resize(if_horizontal_resize(this.set_start_position));
		$window.resize(if_horizontal_resize(plugin_motion_views.plugin_close));

		APP.add_own_event('plugins_close', pre_plugin_close);
		APP.throw_event(EVENTS.part.close);

	};


	this.plugin_open = plugin_motion_views.plugin_open;
	this.plugin_close = plugin_motion_views.plugin_close;
	this.is_open = plugin_motion_views.is_open;
};
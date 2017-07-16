/**
 * Created by mrskull on 08.01.17.
 */

import {Plugins_Loader_Controllers}     from '../../plugin/part_loader/controllers'
import {Event_Button_Controllers}       from '../../../form/plugin/event_button/controllers'


/**
 *    Defining private variables
 */

let
	header_loader_controllers = new Plugins_Loader_Controllers({
		name: 'header',
		url: '/navigation/',

		container: '#HEADER > .header',

		auto_first_loading: true,
	}),

	event_button_controllers = new Event_Button_Controllers({
		container: '#HEADER'
	});


/**
 *    Defining public functions
 */

export let

	define = function()
	{
		event_button_controllers.define();
	},


	get_content = function()
	{
		header_loader_controllers.define();
	};
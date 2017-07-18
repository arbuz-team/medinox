/**
 * Created by mrskull on 08.01.17.
 */

import {Part_Loader_Part}     			from 'part/plugin/part_loader/part'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'


/**
 *    Defining private variables
 */

let
	header_loader = new Part_Loader_Part({
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
		header_loader.define();
		header_loader.load_content();
	};
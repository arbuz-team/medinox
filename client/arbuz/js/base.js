/*    JavaScript    */

import {Dictionary} from 'arbuz/plugin/dictionary/base';

/*---------------- Interfejs funkcji standardowych ----------------*/

/**
 *    Defining global veriables
 */

window.APP = {};
APP.DATA = {};
APP.dictionary = new Dictionary();


/**
 *    Defining global functions
 */

APP.add_own_event = function add_own_event(name, callback)
{
	window.removeEventListener(name, callback, false);
	window.addEventListener(name, callback, false);
};


APP.throw_event = function throw_event(event)
{
	window.dispatchEvent(event);
};


$.prototype.serialize_object = function()
{
	let
		fields = $(this).serializeArray(),
		form_object = {};

	// Appending normal fields to array
	$.each( fields , function( i, field )
	{
		form_object[ field.name ] = field.value;
	});

	return form_object;
};


APP.add_if_isset = function(from, to, from_what, to_what)
{
	if(typeof from[from_what] !== 'undefined')
		if(from_what && to_what)
			to[to_what] = from[from_what];
		else if(from_what)
			to[from_what] = from[from_what];
};
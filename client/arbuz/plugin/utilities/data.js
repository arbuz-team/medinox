/**
 * Created by mrskull on 17.07.17.
 */


export let

	is_undefined = function(object)
	{
		return typeof object === 'undefined';
	},


	is_not_undefined = function(object)
	{
	  return typeof object !== 'undefined';
	},


	// -----------------------------

	add_to_object = function(from, to, from_what, to_what)
	{
		if(is_undefined(from[from_what]))
			return false;

		if(from_what && to_what)
			to[to_what] = from[from_what];
		else if(from_what)
			to[from_what] = from[from_what];
	},


	add_to_settings = function(from, to, from_what, to_what)
	{
		if(is_undefined(to) && is_undefined(to.settings))
		{
			console.error('Data Utilities error: Invalid object.');
			return false;
		}

		add_to_object(from, to.settings, from_what, to_what);
	};
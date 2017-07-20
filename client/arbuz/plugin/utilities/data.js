/**
 * Created by mrskull on 17.07.17.
 */


export let


	is_undefined = function(object)
	{
		return typeof object === 'undefined';
	},


	is_defined = function(object)
	{
	  return typeof object !== 'undefined';
	},


	is_number = function(object)
	{
		return typeof object === 'number';
	},


	is_not_number = function(object)
	{
		return typeof object !== 'number';
	},


	is_empty = function(string)
	{
		return string === '';
	},


	// -----------------------------


	object_to_formdata = function(obj)
	{
		let form_data = new FormData();

		for(let prop in obj)
			if(obj.hasOwnProperty(prop))
				form_data.append(prop, obj[prop]);

		return form_data;
	},


	select_number = function(to_checking, emergency)
	{
		if(is_number(to_checking))
			return to_checking;

		if(is_number(emergency))
			return emergency;

		console.error('Utilities data error: Variable emergency is not number.');
		return undefined;
	},


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
		if(is_undefined(to) && is_undefined(to._settings))
		{
			console.error('Data Utilities error: Invalid object.');
			return false;
		}

		add_to_object(from, to._settings, from_what, to_what);
	};
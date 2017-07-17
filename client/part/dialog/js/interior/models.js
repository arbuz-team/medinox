/**
 * Created by mrskull on 21.01.17.
 */

import {Part_Loader_Dialog} from '../../../plugin/part_loader/dialog'


let

	dialog_loader = new Part_Loader_Dialog({
		name: 'dialog',

		container: '.dialog',

		duration_show: 0,
		duration_hide: 0,
	});


///////////////////////////////////////

export let

	selectors = {
		container: '#DIALOG',
		buttons: '#DIALOG .dialog-content-button',
	},

	variables = {},

	reset_variables = (function()
	{
		let define = function()
		{
			variables = {
				type: '',
				name: '',
				value: '',
				other_1: '',
				other_2: '',
				other_3: '',
				post_data: undefined,
			};
		};
		define();

		return define;
	})(),


	is_error = function(response, status)
	{
		if(status !== 'success')
			return true;

		if(response !== '{"__form__": "true"}')
			return true;

		return false;
	},


	prepare_post_data = function(post_data)
	{
		if(post_data) // if is form
			variables.post_data = post_data;

		else // if is normal dialog
		{
			if(!variables.post_data)
				variables.post_data = {};

			variables.post_data['dialog_type'] = variables.type;
			variables.post_data['dialog_name'] = variables.name;

			if(variables.value)
				variables.post_data['dialog_value'] = variables.value;

            variables.post_data['dialog_other_1'] = variables.other_1;
            variables.post_data['dialog_other_2'] = variables.other_2;
            variables.post_data['dialog_other_3'] = variables.other_3;
		}
	},


	load = function(url, post_data, callback)
	{
		prepare_post_data(post_data);

		dialog_loader.load_content(url, variables.post_data, callback);
	},


	reload = function(callback)
	{
		dialog_loader.load_content(undefined, variables.post_data, callback);
	};
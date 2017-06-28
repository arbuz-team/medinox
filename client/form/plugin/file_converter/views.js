/**
 * Created by mrskull on 23.01.17.
 */

import * as image_convert_models from './models'


export let

	models = image_convert_models,
	settings = models.settings,


	get_base64 = function(file, callback)
	{
		callback.loading();

		let reader = new FileReader();
		reader.readAsDataURL(file);

		reader.onload = function(){
			callback.done(file.name, reader.result);
		};

		reader.onerror = function(error){
			callback.error(error);
		};
	},


	Callback_Functions = function(field)
	{
		let
			$field = $(field),
			$parent_field = $field.parent(),
			$button_shell = $parent_field.children(settings.button_shell);


		this.loading = function()
		{
			$button_shell.html('Coverting...');
		};


		this.done = function(name, result)
		{
			let
				hidden_input_base64 = settings.input_hidden.start + field.name + settings.input_hidden.end_base64,
				hidden_input_name = settings.input_hidden.start + field.name + settings.input_hidden.end_name;

			$(hidden_input_base64).val(result);
			$(hidden_input_name).val(name);
			setTimeout(() => {
				$button_shell.html('Is ready / change');
			}, 500);
		};


		this.error = function()
		{
			setTimeout(() => {
				$button_shell.html('Error / select again');
			}, 500);
		};

	};
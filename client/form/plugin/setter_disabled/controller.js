/**
 * Created by mrskull on 19.09.17.
 */


export let Setter_Disabled = function(config)
{
	if(typeof config === 'undefined' && typeof config.container === 'undefined')
	{
		console.error('Exeption error: invalid container.');
		return {};
	}


	let
		change_input_status = function()
		{
		    let
			    $checkbox = $(this),
			    id = $checkbox.data('id'),
			    status = $checkbox.is(':checked') === false,
		        $input = $('.set_disabled[data-id='+ id +']', config.container);

			$input.prop('disabled', status);
		};


	this.define = function()
	{
		let $checkbox = $('.if_disabled', config.container);

		$checkbox.change(change_input_status);
	};
};
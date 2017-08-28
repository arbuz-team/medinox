/**
 * Created by mrskull on 28.08.17.
 */


export function Address_Switcher(button)
{
	let
		$button = $(button),
		address = $button.data('address'),
		$form = $button.parents('form'),


		receive_event = function()
		{
			$form.attr('action', address);
			$form.submit();
		};


	$(button).click(receive_event);
}
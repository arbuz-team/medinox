/**
 * Created by mrskull on 28.08.17.
 */


export function Address_Switcher(button)
{
	let
		$button = $(button),
		new_address = $button.data('address'),
		$form = $button.parents('form'),


		receive_event = function()
		{
			let old_address = $form.attr('action');

			$form.data('reload', 'cart');
			$form.data('event', 'part.open_cart');
			$form.attr('action', new_address);
			$form.submit();
			$form.attr('action', old_address);
			$form.data('reload', '');
			$form.data('event', '');
		};


	$(button).click(receive_event);
}
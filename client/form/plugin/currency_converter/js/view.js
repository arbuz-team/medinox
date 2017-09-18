/**
 * Created by mrskull on 31.08.17.
 */

import * as model from './model'


export function Currency_Converter_View()
{
	this.change_status_field = function(checkbox)
	{
		let
			$checkbox =     $(checkbox),
			checked =       $checkbox.prop('checked'),
			$column =       $checkbox.parents(model.selector.column),
			$input =        $(model.selector.input, $column),
			$button =       $(model.selector.button, $column);

		if(checked)
		{
			$input.prop('disabled', false);
			$button.prop('disabled', false);
		}
		else
		{
			$input.prop('disabled', true);
			$button.prop('disabled', true);
		}
	};


	this.calculate = function(button)
	{
		let
			$button =           $(button),
			$column =           $button.parents(model.selector.column),
			$container =        $column.parents(model.selector.container),
			$input =            $(model.selector.input, $column),
			base_price =        $input.val(),
			base_currency =     $column.data('currency'),

			$buttons =          $(model.selector.button, $container),

			list_of_currencies =    [];

		$buttons.each(function()
		{
			let
				$a_button =     $(this),
				$a_column =     $a_button.parents(model.selector.column),
				currency =      $a_column.data('currency');

			if(base_currency !== currency)
				list_of_currencies.push(currency);
		});


		if(base_price && base_currency && list_of_currencies)
			model.get_price(base_price, base_currency, list_of_currencies).then((array) =>
			{
				for(let i = 0; array.length > i; ++i)
				{
					let
						currency = array[i].currency,
						price = array[i].price,
						$input_for_setting = $(model.selector.input, model.selector.column +'[data-currency='+ currency +']');

					$input_for_setting.val(price);
				}
			});
	};
}
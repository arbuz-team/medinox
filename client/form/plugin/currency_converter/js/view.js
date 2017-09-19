/**
 * Created by mrskull on 31.08.17.
 */

import * as model from './model'


export function Currency_Converter_View()
{
	this.change_status_field = function(input)
	{
		let
			$input =        $(input),
			$column =       $input.parents(model.selector.column),
			$button =       $(model.selector.button, $column);

		if($column.data('currency') === 'EUR' || $column.data('currency') === 'GBP')
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

			url = $container.data('url'),

			$all_columns =          $(model.selector.column, $container),

			list_of_currencies =    [];

		$all_columns.each(function()
		{
			let
				currency =      $(this).data('currency');

			if(base_currency !== currency)
				list_of_currencies.push(currency);
		});


		if(base_price && base_currency && list_of_currencies)
			model.get_price(url, base_price, base_currency, list_of_currencies).then((array) =>
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
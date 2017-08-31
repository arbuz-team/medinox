/**
 * Created by mrskull on 31.08.17.
 */

import {Request_Manager} from 'arbuz/plugin/request_manager/_controller'


let

	request_manager = new Request_Manager(),


	prepare_currencies = function(list)
	{
		let text = '';

		for(let i = 0; list.length > i; ++i)
		{
			if(i === 0)
				text += list[i];
			else
				text += ' '+ list[i];
		}

		return text;
	},


	receive_data = function(resolve)
	{
		return function(response)
		{
			let
				list = JSON.parse(response.html),
				array = [];

			if(typeof list.EUR !== 'undefined')
				array.push({
					currency: 'EUR',
					price: list.EUR,
				});
			if(typeof list.PLN !== 'undefined')
				array.push({
					currency: 'PLN',
					price: list.PLN,
				});
			if(typeof list.GBP !== 'undefined')
				array.push({
					currency: 'GBP',
					price: list.GBP,
				});

			resolve(array);
		};
	};



export let

	selector = {
		container:  '.currency_converter',
		column:     '.currency_converter-col',
		checkbox:   '.currency_converter-checkbox',
		input:      '.currency_converter-field',
		button:     '.currency_converter-button',
	},



	get_price = function(base_price, base_currency, list_of_currencies)
	{
		return new Promise((resolve) =>
		{
			let
				content = '__ground__',

				data = {
					__ground__:     'get',
					_name_:         'exchange_rate',
					amount:         base_price,
					currency_from:  base_currency,
					currencies_to:  prepare_currencies(list_of_currencies),
				};

			request_manager.send('/currency/', data, content).then(receive_data(resolve));
		});
	};

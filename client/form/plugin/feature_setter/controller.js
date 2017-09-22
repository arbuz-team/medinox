/**
 * Created by mrskull on 19.09.17.
 */


export let Feature_Setter = function(config)
{
	if(typeof config === 'undefined' && typeof config.container === 'undefined')
	{
		console.error('Exeption error: invalid container.');
		return {};
	}


	let
		get_setters = function($setter)
		{
			let
				$form = $setter.parents('form'),
				name = $setter.attr('name');

		    return $('.if_feature[name='+ name +']', $form);
		},


		set_feature = function()
		{
			let
				$setter = $(this),
				id = $setter.data('id'),
				$elem_id = $('.set_feature[data-id='+ id +']', config.container),
				feature = $elem_id.data('feature');

			$elem_id.prop(feature, true);
		},


		change_input_status = function()
		{
		    let
			    $setter = $(this),
				id = $setter.data('id'),
			    type = $setter.attr('type'),
				status = $setter.is(':checked') === false,
				$all_setters = get_setters($setter),
				$elem_id = $('.set_feature[data-id='+ id +']', config.container),
			    feature = $elem_id.data('feature');

		    if(type === 'radio')
				$all_setters.each(set_feature);

			$elem_id.prop(feature, status);
		};


	this.define = function()
	{
		let $all_setters = $('.if_feature', config.container);

		$all_setters.each(set_feature);

		$all_setters.click(change_input_status);
	};
};
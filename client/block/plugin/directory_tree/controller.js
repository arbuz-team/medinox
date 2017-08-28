/**
 * Created by mrskull on 22.08.17.
 */


export function Directory_Tree(config)
{
	if(!config || !config.container)
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}

	this.container = config.container;



	let change_state = function()
	{
		let
			$parent = $(this).parent().parent(),
			$list = $parent.children('.directory_tree-list'),
			$all_lists = $parent.find('.directory_tree-list'),
			is_open = $list.hasClass('is-open');

		if(is_open)
			$all_lists.removeClass('is-open').addClass('is-close');
		else
			$list.removeClass('is-close').addClass('is-open');
	};


	this.define = function()
	{
		$('.directory_tree-name', this.container).click(change_state);
	}
}

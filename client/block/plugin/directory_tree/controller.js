/**
 * Created by mrskull on 22.08.17.
 */


export function Directory_Tree(container)
{
	if(!container)
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}

	this.container = container;



	let change_state = function()
	{
		let
			$parent = $(this).parent().parent(),
			$arrow = $parent.children('.directory_tree-single').children('.directory_tree-name').children('.directory_tree-arrow'),
			$list = $parent.children('.directory_tree-list'),
			$all_lists = $parent.find('.directory_tree-list'),
			is_open = $list.hasClass('is-open');

		if(is_open)
		{
			if($arrow.hasClass('is-open'))
				$arrow.removeClass('is-open').addClass('is-close');
			$all_lists.removeClass('is-open').addClass('is-close');
		}
		else
		{
			if($arrow.hasClass('is-close'))
				$arrow.removeClass('is-close').addClass('is-open');
			$list.removeClass('is-close').addClass('is-open');
		}
	};


	this.define = function()
	{
		$('.directory_tree-name', this.container).click(change_state);
	};

	this.define();
}

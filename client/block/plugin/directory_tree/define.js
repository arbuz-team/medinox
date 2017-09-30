
import {Directory_Tree} from './controller'



export let

	define_directory_tree = function(config)
	{
		let $element = $('.directory_tree', config.container);

		$element.each(function()
		{
			new Directory_Tree(this);
		});
	};

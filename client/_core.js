/**
 * Created by mrskull on 24.11.16.
 */

// import './autosize-master/dist/autosize';
import './arbuz/js/base';
import * as page_controller from './arbuz/js/controllers';

window.APP.add_own_event('load', () => {
	page_controller.start();
});


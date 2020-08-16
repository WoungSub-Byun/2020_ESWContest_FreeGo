import React from 'react';
import $ from 'jquery';

import './test.scss';

function sendAjax() {
	$.ajax({
		type: 'POST',
		url: './hello.py',
		data: { param: 'text' },
	}).done((o) => {
		console.log('python file complied');
	});
}

function PyTest() {
	return <div onClick={sendAjax}>testbutton</div>;
}
export default PyTest;

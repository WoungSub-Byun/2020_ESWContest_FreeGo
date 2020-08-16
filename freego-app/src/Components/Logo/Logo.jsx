import React, { Component } from 'react';
import classNames from 'classnames';
import './Logo.scss';
import logo from './snow.png';

function Logo({ page }) {
	return (
		<div className={classNames('frame', page)}>
			<img src={logo} className={classNames('img', page)} alt="snow" />
			<b className={classNames('Logo', page)}>freego</b>
		</div>
	);
}

Logo.defaultProps = {
	page: '',
};

export default Logo;

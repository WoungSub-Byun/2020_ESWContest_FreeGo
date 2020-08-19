import React from 'react';
import NextButton from '../../Components/Button/NextButton/NextButton';
import './RegisterNameContainer.scss';
import Logo from '../../Components/Logo/Logo';
import { Link } from 'react-router-dom';

function RegisterNameContainer() {
	const Loader = () => {};

	const username = '';

	return (
		<div>
			<Logo className="logo" />
			<p>이름을 입력하세요</p>
			<input type="text" value={username} />
			<Link>
				<NextButton page="/tutorial" inputData className="btn" />
			</Link>
		</div>
	);
}

export default RegisterNameContainer;

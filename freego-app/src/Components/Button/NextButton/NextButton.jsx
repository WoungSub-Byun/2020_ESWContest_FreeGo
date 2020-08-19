import React from 'react';
import './NextButton.scss';
import { Link } from 'react-router-dom';

function NextButton({ page }) {
	return (
		<div>
			<Link to={page}>
				<button className="btn" type="button">
					다음
				</button>
			</Link>
		</div>
	);
}
export default NextButton;

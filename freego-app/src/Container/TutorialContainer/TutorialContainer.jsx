import React, { useState, useReducer, Component } from 'react';
import classNames from 'classnames';

import './TutorialContainer.scss';
import GraylistImg from './graylist.png';
import WhitelistImg from './whitelist.png';
import Cursor1Img from './cursor1.png';
import Cursor2Img from './cursor2.png';
import ReceipeImg from './receipe.png';

function TutorialContainer() {
	const [pageView, setPageView] = useState({
		num: 1,
		view: {
			page1: 'empty',
			page2: 'fill',
			page3: 'fill',
		},
	});

	return (
		<div
			className="mainframe"
			onClick={() => {
				if (pageView.num === 1) {
					setPageView({
						num: 2,
						view: {
							page1: 'fill',
							page2: 'empty',
							page3: 'fill',
						},
					});
				} else if (pageView.num === 2) {
					setPageView({
						num: 3,
						view: {
							page1: 'fill',
							page2: 'fill',
							page3: 'empty',
						},
					});
				}
			}}
		>
			<div
				className="skipbtn"
				onClick={() => {
					console.log('skip Button pressed...');
				}}
			>
				skip{'>>'}
			</div>
			<span>
				1. +버튼을 눌러
				<br />
				목록을 추가하세요
			</span>
			<img src={GraylistImg} className="img1" />
			<img src={Cursor1Img} className="clickmotion" />
			<div className="circles">
				<div
					className={classNames('pageCircle', pageView.view.page1)}
				/>
				<div
					className={classNames('pageCircle', pageView.view.page2)}
				/>
				<div
					className={classNames('pageCircle', pageView.view.page3)}
				/>
			</div>
		</div>
	);
}

export default TutorialContainer;

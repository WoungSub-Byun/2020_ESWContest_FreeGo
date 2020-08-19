import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import classNames from 'classnames';
import AppStartButton from '../../Components/Button/AppStartButton/AppStartButton';

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
			page1: 'fill',
			page2: 'empty',
			page3: 'empty',
		},
	});

	const IncreasePage = () => {
		if (pageView.num === 1) {
			setPageView({
				num: 2,
				view: {
					page1: 'empty',
					page2: 'fill',
					page3: 'empty',
				},
			});
		} else if (pageView.num === 2) {
			setPageView({
				num: 3,
				view: {
					page1: 'empty',
					page2: 'empty',
					page3: 'fill',
				},
			});
		}
	};

	const DecreasePage = () => {
		if (pageView.num === 2) {
			setPageView({
				num: 1,
				view: {
					page1: 'fill',
					page2: 'empty',
					page3: 'empty',
				},
			});
		} else if (pageView.num === 3) {
			setPageView({
				num: 2,
				view: {
					page1: 'empty',
					page2: 'fill',
					page3: 'empty',
				},
			});
		}
	};

	const SetView = (PageNum) => {
		switch (PageNum) {
			case 1:
				return (
					<>
						<div
							className="skipbtn"
							onClick={() => {
								setPageView({
									...pageView,
									num: 3,
								});
							}}
						>
							skip{'>>'}
						</div>
						<span>
							1. 버튼을 눌러
							<br />
							목록을 추가하세요
						</span>
						<img src={GraylistImg} className="explainImg" />
						<img src={Cursor1Img} className="motion" />
						<div className="Buttons">
							<div className="nextButton" onClick={IncreasePage}>
								{'>'}
							</div>
						</div>
					</>
				);
			case 2:
				return (
					<>
						<div
							className="skipbtn"
							onClick={() => {
								setPageView({
									...pageView,
									num: 3,
								});
							}}
						>
							skip{'>>'}
						</div>
						<span>
							2. 내 냉장고의 식품을
							<br />
							편하게 관리하세요
						</span>
						<img src={WhitelistImg} className="explainImg" />
						<img src={Cursor2Img} className="motion" />
						<div className="Buttons">
							<div className="lastButton" onClick={DecreasePage}>
								{'<'}
							</div>
							<div className="nextButton" onClick={IncreasePage}>
								{'>'}
							</div>
						</div>
					</>
				);
			case 3:
				return (
					<>
						<span>
							3. 재료를 사용한
							<br />
							레시피를 확인하세요.
						</span>
						<img
							src={ReceipeImg}
							className={classNames('explainImg', PageNum)}
						/>
						<div className="Buttons">
							<div className="lastButton" onClick={DecreasePage}>
								{'<'}
							</div>
							<div className="appStartButton">
								<Link to="/first">
									<AppStartButton />
								</Link>
							</div>
						</div>
					</>
				);
		}
	};

	return (
		<div className="mainframe">
			{SetView(pageView.num)}

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

import React from 'react';
import { Route } from 'react-router-dom';
import StartLoddingContainer from './Container/StartLoddingContainer/StartLoddingContainer';
import RegisterNameContainer from './Container/RegisterNameContainer/RegisteNameContainer';
import TutorialContainer from './Container/TutorialContainer/TutorialContainer';

export default Router = () => {
	return (
		<>
			<Route exact path="/" component={StartLoddingContainer} />
			<Route path="/firstregister" component={RegisterNameContainer} />
			<Route path="/tutorial" component={TutorialContainer} />
			<Route path="/main/:username" />
		</>
	);
};

import React, { Component } from 'react';
import './StartLoddingContainer.scss'
import StartLogo from '../../Components/Logo/Logo';

class StartLoddingContainer extends Component {
    render() {
        return (
            <div className="mainframe">
                <StartLogo page="start"/>
            </div>
        )
    }
}

export default StartLoddingContainer;
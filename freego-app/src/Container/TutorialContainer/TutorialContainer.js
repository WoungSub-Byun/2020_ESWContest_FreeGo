import React, { Component } from 'react';
import './TutorialContainer.scss';
import Img1 from './img1.png';
import Img2 from './img2.png';

class TutorialContainer extends Component {
    render() {
        return (
            <div className="mainframe">
                <div className="skipbtn"> skip{'>>'} </div>
                <span>1. +버튼을 눌러<br/>목록을 추가하세요</span>
                <img src={Img1} className="img1"/>
                <img src={Img2} className="clickmotion"/>
                <div className="circles">
                    <div className="pageCircle1"/>
                    <div className="pageCircle2"/>
                    <div className="pageCircle3"/>
                </div>
            </div>
        );
    }
}

export default TutorialContainer;
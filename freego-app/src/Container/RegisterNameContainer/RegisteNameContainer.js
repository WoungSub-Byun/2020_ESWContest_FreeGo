import React, { Component } from 'react';
import NextButton from '../../Components/Button/NextButton/NextButton';
import './RegisterNameContainer.scss'
import Logo from '../../Components/Logo/Logo';

class RegisterNameContainer extends Component {
    render() {
        return (
            <div>
                <Logo className="logo"/>
                <p>이름을 입력하세요</p>
                <input type='text'/>
                <NextButton page="RegisterName" className="btn"/>
            </div>
        )
    }
}


export default RegisterNameContainer;
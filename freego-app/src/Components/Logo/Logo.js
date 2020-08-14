import React, { Component } from 'react';
import './Logo.css';
import logo from './snow.png';

class Logo extends Component {

    static defaultProps = {
        page: ''
    }

    render() {
        const { page } = this.props;
        var handleClassName = "";
        if (page == "startcontainer"){
            handleClassName = 'start';
        }

        return (
            <div className={handleClassName+"frame"}>
                <img src={logo} className={handleClassName+"img"} alt="snow" />
                <b className={handleClassName+"Logo"}>freego</b>
            </div>
        )
    }
}

export default Logo;
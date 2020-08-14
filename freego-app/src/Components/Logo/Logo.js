import React, { Component } from 'react';
import classNames from 'classnames';
import './Logo.scss';
import logo from './snow.png';

class Logo extends Component {

    static defaultProps = {
        page: ''
    }

    render() {
        const { page } = this.props;

        return (
            <div className={classNames('frame', page)}>
                <img src={logo} className={classNames('img', page)} alt="snow" />
                <b className={classNames('Logo', page)}>freego</b>
            </div>
        )
    }
}

export default Logo;
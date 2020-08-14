import React, { Component } from 'react';

import './NextButton.scss'
class NextButton extends Component {
    
    render() {
        const { page } = this.props;

        return(
            <div>
                <button className="btn" type="button"> 다음</button>
            </div>
        )
    }
}

export default NextButton;
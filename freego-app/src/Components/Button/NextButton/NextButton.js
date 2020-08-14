import React, { Component } from 'react';
import './NextButton.css'
class NextButton extends Component {
    
    render() {
        const { page } = this.props;
        var whatPage;
        if (page === "RegisterName"){

        }
        return(
            <div>
                <button className="btn" type="button"> 다음</button>
            </div>
        )
    }
}

export default NextButton;
import React from "react";
import Pattern from "./Pattern"
import { PageHeader } from "react-bootstrap";

require('../css/fullstack.css');
var $ = require('jquery');

// import HeaderBackgroundImage from '../images/header.jpg';

export default class App extends React.Component {
    constructor(props) {
        super(props);
    }
    // addHeaderImg() {
    //     let headerBg = new Image();
    //     headerBg.src = HeaderBackgroundImage;
    // }

    render () {
        return (
            // <PageHeader>
            //     <div className='header-contents'>
            //     // {this.addHeaderImg()}
            //     <Pattern />
            //     </div>
            // </PageHeader>
            <Pattern />
        );
    }
}

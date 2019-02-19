import React from "react";
import MiniPatterns from "./MiniPatterns"
import { Button, Grid, Row, Col } from "react-bootstrap";


require('../css/fullstack.css');
var $ = require('jquery');


export default class App extends React.Component {
    constructor(props) {
        super(props);
        // this.state= {
        //     pattern_id : 781496
        // }

    }


    render () {
        return (
                <MiniPatterns />              
        );
    }
}

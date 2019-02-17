import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

var $ = require('jquery');

export default class Pattern extends React.Component {

    constructor(props){
        super(props);
        this.state = {description: 'Pattern goes here!'};

        this.getPythonPattern = this.getPythonPattern.bind(this);

    }

    setPattern(pattern_list){
        const pattern = pattern_list[0]
        this.setState({description: pattern.name});

    }

    getPythonPattern(){
        const route = 'patterns/knitting/ids/709323'
        $.get(window.location.href + route, (data) => {
            console.log(data);
            this.setPattern(data)
        });
    }

    render () {
        return (
            <Grid>
                <Row>
                <Col md={7} mdOffset={5}>
                    <h1>{this.state.description}</h1>
                    <hr/>
                </Col>
                </Row>
                <Row>
                <Col md={7} mdOffset={5}>
                    <Button bsSize="large" bsStyle="danger" onClick={this.getPythonPattern}>
                    Say Hello!
                    </Button>
                </Col>
                </Row>
            </Grid>
        );
    }

}
import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

var $ = require('jquery');

export default class Pattern extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            name: 'pattern.name' ,
            created_at: 'pattern.created_at',
            pattern_type: 'pattern.pattern_type',
            sizes: 'pattern.sizes',
            yardage: 'pattern.yardage',
            yarn_weight : 'pattern.yarn_weight',
            gauge : 'pattern.gauge',
            is_clothing : 'pattern.is_clothing',
            is_free : 'pattern.is_free',
            is_downloadable : 'pattern.is_downloadable',
            url : 'pattern.url',
            description : 'pattern.description',
            img_fullsize_url : 'pattern.img_fullsize_url',
            img_small_url: 'pattern.img_small_url'
        };

        this.getPythonPattern = this.getPythonPattern.bind(this);

    }

    setPattern(pattern_list){
        const pattern = pattern_list[0]
        this.setState({
            name: pattern.name ,
            created_at: pattern.created_at,
            pattern_type: pattern.pattern_type,
            sizes: pattern.sizes,
            yardage: pattern.yardage,
            yarn_weight : pattern.yarn_weight,
            gauge : pattern.gauge,
            is_clothing : pattern.is_clothing,
            is_free : pattern.is_free,
            is_downloadable : pattern.is_downloadable,
            url : pattern.url,
            description : pattern.description,
            img_fullsize_url : pattern.img_fullsize_url,
            img_small_url: pattern.img_small_url
        });

    }

    getPythonPattern(){
        const route = 'patterns/knitting/ids/781496'
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
                    <h1>{this.state.name}</h1>
                    Created at: {this.state.created_at}
                    <hr/>
                    <p>
                    Pattern Type: {this.state.pattern_type}
                    <br></br>
                    Available sizes: {this.state.sizes}
                    <br></br>
                    Yardage: {this.state.yardage}
                    <br></br>
                    Yarn weight: {this.state.yarn_weight}
                    <br></br>
                    Gauge: {this.state.gauge}
                    <br></br>
                    Is clothing: {this.state.is_clothing}
                    <br></br>
                    Is free: {this.state.is_free}
                    <br></br>
                    Is downloadble: {this.state.is_downloadable}
                    <br></br>
                    Url: {this.state.url}
                    </p>
                    <p>
                    Description: {this.state.description}
                    </p>
                </Col>
                </Row>
                <Row>
                <Col md={7} mdOffset={5}>
                    <Button bsSize="large" bsStyle="danger" onClick={this.getPythonPattern}>
                    Load Pattern!
                    </Button>
                </Col>
                </Row>
            </Grid>
        );
    }

}
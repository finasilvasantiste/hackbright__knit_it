import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";


var $ = require('jquery');


export default class Pattern extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            name: 'pattern.name' ,
            author : 'pattern.author',
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
            img_small_url: 'pattern.img_small_url',
            suggested_yarn : 'pattern.suggested_yarn',
            needles_required : 'pattern.needles'
        };

        this.getPythonPattern = this.getPythonPattern.bind(this);

    }

    setYarnText(yarn){
        const yarn_html = yarn.name + ' (' + yarn.weight + ')'

        return yarn_html
    }

    setSuggestedYarn(yarn_list){
        const yarn_unpacked = []

        for(let i = 0; i< yarn_list.length; i++){
            const yarn = this.setYarnText(yarn_list[i])
            yarn_unpacked.push(yarn)

        };

        return yarn_unpacked
    }

    setNeedlesRequired(needles_list){
        const needles_unpacked = []

        for(let i = 0; i< needles_list.length; i++){
            const needles = needles_list[i]['name']
            needles_unpacked.push(needles)

        };

        return needles_unpacked

    }


    setPattern(pattern_list){
        const pattern = pattern_list[0]

        const suggested_yarn = this.setSuggestedYarn(pattern.suggested_yarn)
        
        const needles_required = this.setNeedlesRequired(pattern.needles)


        const yarn_list = suggested_yarn.map((yarn) =>
            <li key={yarn.toString()}>
            {yarn}</li>
            );

        const needles_required_list = needles_required.map((needles) =>
            <li key={needles.toString()}>
            {needles}</li>
            );
               
        this.setState({
            name: pattern.name ,
            author : pattern.author,
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
            img_small_url: pattern.img_small_url,
            suggested_yarn : yarn_list,
            needles_required : needles_required_list
        });

    }

    getPythonPattern(){
        const route = '/patterns/knitting/ids/781496'

        $.get(route, (data) => {
        // $.get(window.location.href + route, (data) => {
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
                    By {this.state.author}
                    <br></br>
                    Created at {this.state.created_at}
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
                    Suggested Yarn: 
                    <ul>
                    {this.state.suggested_yarn}
                    </ul>
                    Needles required:
                    <ul>
                    {this.state.needles_required}
                    </ul>
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
import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

var $ = require('jquery');


export default class MiniPatterns extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          data: [
            {
                name: "mini_pattern.name",
                pattern_id: "mini_pattern.pattern_id",
                img_fullsize_url : "mini_pattern.img_fullsize_url",
                img_small_url : "mini_pattern.img_small_url"
            }
           ]
        };
    }


    setMiniPatterns(mini_patterns_list){
        /*
            Sets new state of component using mini patterns list.
        */
        this.setState({
            data : mini_patterns_list
        });

        this.props.callbackFromParent(this.state.data[0])
    }


    getPythonMiniPatterns(){
        /* 
            Gets mini patterns from python server and forwards it to set the new state of component.
        */

        // const pattern_id = this.state.pattern_id

        console.log('Inside Pattern');

        const route = '/patterns/knitting'

        $.get(route, (data) => {
        // $.get(window.location.href + route, (data) => {
            console.log(data);
            // this.setPattern(data)
            this.setMiniPatterns(data)
        });
    }

    componentDidMount() {
        this.getPythonMiniPatterns(); 
    }

    render(){
        return (
                <Col>
                    <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius efficitur nulla ut condimentum. Phasellus luctus lacinia nisi, nec porta neque placerat vitae. In sed gravida metus. Donec dolor felis, ultrices in lacus sit amet, posuere laoreet dolor. Mauris rhoncus mauris ac tellus finibus, cursus tincidunt lectus rutrum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin imperdiet sem quam, vitae molestie ipsum blandit quis. Donec viverra eros vitae augue euismod elementum. Suspendisse rhoncus massa vitae dolor dapibus, sit amet feugiat mauris rhoncus. Nam sapien felis, sagittis at sapien quis, vulputate vehicula ligula. Sed ac egestas justo, at fringilla est. Nam eleifend, nisl vitae maximus sagittis, felis massa dapibus elit, in pharetra justo ex non eros.
                    </p>
                    {this.state.data.map(d => 
                        <div key={d.name}>
                            <img src={d.img_small_url}/>
                            <br></br>
                            {d.name}
                        </div>
                    )}
                </Col>
            );
    }

}


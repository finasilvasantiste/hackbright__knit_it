import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

import Pattern from "./Pattern"

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
           ],
           pattern_id: 781496,
           page_number: 1
        };

        this.getPatternID = this.getPatternID.bind(this);
        this.getNextPage = this.getNextPage.bind(this);
    }


    setMiniPatterns(mini_patterns_list){
        /*
            Sets new state of component using mini patterns list.
        */
        this.setState({
            data : mini_patterns_list
        });

        // this.props.callbackFromParent(this.state.data[0])
    }


    getPythonMiniPatterns(increment){
        /* 
            Gets mini patterns from python server and forwards it to set the new state of component.
        */
        let next_page

        if (increment){
            next_page = this.state.page_number + 1
        }else{
            next_page = this.state.page_number
        };

        const route = '/patterns/knitting/page/'

        this.setState({
            page_number : next_page
        })


        $.get(route + next_page, (data) => {
            console.log(data);
            this.setMiniPatterns(data)
        });
    }

    getPatternID(pattern_id){
        console.log('Click!')
        console.log(pattern_id)

        this.setState({
            pattern_id : pattern_id
        });

    };

    getNextPage(){
        this.getPythonMiniPatterns(true); 
    }

    componentDidMount() {
        this.getPythonMiniPatterns(false); 
    }

    render(){
        return (
            <Row>
                <Col md={7} >
                    <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius efficitur nulla ut condimentum. Phasellus luctus lacinia nisi, nec porta neque placerat vitae. In sed gravida metus. Donec dolor felis, ultrices in lacus sit amet, posuere laoreet dolor. Mauris rhoncus mauris ac tellus finibus, cursus tincidunt lectus rutrum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin imperdiet sem quam, vitae molestie ipsum blandit quis. Donec viverra eros vitae augue euismod elementum. Suspendisse rhoncus massa vitae dolor dapibus, sit amet feugiat mauris rhoncus. Nam sapien felis, sagittis at sapien quis, vulputate vehicula ligula. Sed ac egestas justo, at fringilla est. Nam eleifend, nisl vitae maximus sagittis, felis massa dapibus elit, in pharetra justo ex non eros.
                    </p>
                    {this.state.data.map(d => 
                        <div key={d.name} onClick={()=>this.getPatternID(d.pattern_id)}>
                            <img src={d.img_small_url}/>
                            <br></br>
                            {d.name}
                            <br></br>
                            {d.pattern_id}
                        </div>
                    )}
                </Col>
                <Col md={5}>
                    <Pattern id={this.state.pattern_id}/> 
                </Col> 
                <Button bsSize="large" bsStyle="danger" onClick={this.getNextPage}>
                  Next Page!
                </Button>
            </Row>
            );
    }

}


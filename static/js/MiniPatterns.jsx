import React from "react";
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";

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
           page_number: 1,
           query : '%20',
           button_query : ' '
        };

        this.getPatternID = this.getPatternID.bind(this);
        this.getNextPage = this.getNextPage.bind(this);
        this.getPreviousPage = this.getPreviousPage.bind(this);
        this.getQuery = this.getQuery.bind(this);
        this.resetResults = this.resetResults.bind(this)
    }


    setMiniPatterns(mini_patterns_list){
        /*
            Sets new state of component using mini patterns list.
        */
        this.setState({
            data : mini_patterns_list
        });

    }


    getPythonMiniPatternsByQuery(query, next_page){

        const route_query = '/patterns/knitting/query/'
        const route_page = '/page/'

        this.setState({
            page_number : next_page,
            query : query
        })

        $.get(route_query + query + route_page + next_page, (data) => {
            console.log(data);
            this.setMiniPatterns(data)
        });
    }


    setPage(increment, decrement){
        /*
            Sets page number to use for api call. 
            If current page is first page and user tries to get previous page,
            no call is executed.
        */

        const query = this.state.query

        if (increment){
            this.getPythonMiniPatternsByQuery(query, this.state.page_number + 1)
        }else{
            if(decrement){
                if (this.state.page_number > 1){
                    this.getPythonMiniPatternsByQuery(query, this.state.page_number - 1)
                }else{
                    console.log('No previous page! Already on page '+ this.state.page_number)
                }
            }else{
                this.getPythonMiniPatternsByQuery(query, this.state.page_number)
            }
        };

    }

    getPatternID(pattern_id){
        /*
            Gets pattern_id from selected mini pattern.
        */
        console.log('Click!')
        console.log(pattern_id)

        this.setState({
            pattern_id : pattern_id
        });

    };


    getNextPage(){
        /*
            Gets next page of results.
        */
        console.log('Next Page:')
        console.log(this.state.query)

        this.setPage(true, false); 
    }


    getPreviousPage(){
        /*
            Gets previous page of results.
        */

        console.log(this.state.query)

        this.setPage(false, true); 
    }



    getQuery(is_reset = false){
        // query = 'Query!'
        // console.log(this.state.button_query.value)
        let query_string = String(this.state.button_query.value)
        
        if(is_reset == true){
            query_string = '%20'
        }

        console.log(query_string)

        this.setState({
            query : query_string
        });

        this.getPythonMiniPatternsByQuery(query_string, 1)

    }

    resetResults(){
        this.getQuery(true)
    }

    componentDidMount() {
        this.setPage(false, false); 
    }

    render(){
        return (
            <Grid>
            <Row><Form>
                  <FormGroup controlId="formBasicEmail">
                    <FormControl inputRef={node => this.state.button_query = node}  type="text" placeholder="Enter email" />
                  </FormGroup>
                    <Button bsStyle="info" onClick={this.getQuery}>
                        Search!
                    </Button>
                    <Button bsStyle="info" onClick={this.resetResults}>
                        Reset Results!
                    </Button>
                </Form>
            </Row>
            <Row>
                <Col md={7} >
                    <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius efficitur nulla ut condimentum. Phasellus luctus lacinia nisi, nec porta neque placerat vitae. In sed gravida metus. Donec dolor felis, ultrices in lacus sit amet, posuere laoreet dolor. Mauris rhoncus mauris ac tellus finibus, cursus tincidunt lectus rutrum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin imperdiet sem quam, vitae molestie ipsum blandit quis. Donec viverra eros vitae augue euismod elementum. Suspendisse rhoncus massa vitae dolor dapibus, sit amet feugiat mauris rhoncus. Nam sapien felis, sagittis at sapien quis, vulputate vehicula ligula. Sed ac egestas justo, at fringilla est. Nam eleifend, nisl vitae maximus sagittis, felis massa dapibus elit, in pharetra justo ex non eros.
                    </p>
                    <p>
                        <Button bsSize="large" bsStyle="danger" onClick={this.getPreviousPage}>
                          Previous Page!
                        </Button>
                        <Button bsSize="large" bsStyle="danger" onClick={this.getNextPage}>
                          Next Page!
                        </Button>
                    </p>
                    {this.state.data.map(d => 
                        <div key={d.pattern_id} onClick={()=>this.getPatternID(d.pattern_id)}>
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
            </Row>
            </Grid>
            );
    }

}


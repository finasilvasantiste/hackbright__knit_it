import React from "react";
import MiniPatterns from "./MiniPatterns"
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";


require('../css/fullstack.css');
// import $ from 'jquery'


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            query : '%20',
            button_query : ' '
        }

        this.getQuery = this.getQuery.bind(this);
        this.resetResults = this.resetResults.bind(this)

    }

    getQuery(is_reset = false){
        /*
            Sets the new value for query in state. 
        */
        let query_string = String(this.state.button_query.value)
        
        if(is_reset == true){
            query_string = '%20'
        }

        // console.log(query_string)

        this.setState({
            query : query_string
        });

    }


    resetResults(){
        /*
            Resets the search results to (empty string) search results.
        */
        this.getQuery(true)
    }


    render () {
        return (
                <Grid>
                    <Row>
                        <Form>
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
                        <MiniPatterns query={this.state.query} />  
                </Grid>
        );
    }
}

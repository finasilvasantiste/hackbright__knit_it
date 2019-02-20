import React from "react";
import MiniPatterns from "./MiniPatterns"
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";


require('../css/fullstack.css');
// import $ from 'jquery'


export default class SearchMiniPatterns extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            logging: {
                email : 'Fina',
                password_hash : 'jsdkfjkh4',
                email_button : '',
                password_hash_button : '',
                is_logged_in : false
            },
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

    setLogIn(){
        console.log('Logging in!')
    }

    setLogOut(){
        console.log('Logging out!')
    }


    render () {
        return (
                <div>
                    <Row>
                  <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <a className="navbar-brand" href="/">Knit It</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                      <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                      <ul className="navbar-nav mr-auto">
                        <li className="nav-item active">
                          <a className="nav-link" href="/">Home <span className="sr-only">(current)</span></a>
                        </li>
                        <li className="nav-item">
                          <a className="nav-link" href="/">Link</a>
                        </li>
                        <li className="nav-item dropdown">
                          <a className="nav-link dropdown-toggle" href="/" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Dropdown
                          </a>
                          <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a className="dropdown-item" href="/">Action</a>
                            <a className="dropdown-item" href="/">Another action</a>
                            <div className="dropdown-divider"></div>
                            <a className="dropdown-item" href="/">Something else here</a>
                          </div>
                        </li>
                        <li className="nav-item">
                          <a className="nav-link disabled" href="/">Disabled</a>
                        </li>
                      </ul>
                      <form className="form-inline my-2 my-lg-0">
                            <FormControl inputRef={node => this.state.button_query = node}  type="text" placeholder="Enter query" />
                            <Button bsStyle="warning" onClick={this.getQuery} className="mr-sm-2" >
                                Search
                            </Button>
                            <Button bsStyle="warning" onClick={this.resetResults} className="mr-sm-2" >
                                Reset Results
                            </Button>
                      </form>
                    </div>
                  </nav>
                    </Row>
                        <MiniPatterns query={this.state.query} is_logged_in={this.state.logging.is_logged_in} />  
                </div>
        );
    }
}

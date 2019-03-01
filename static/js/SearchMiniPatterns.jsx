import React from "react";
import MiniPatterns from "./MiniPatterns";
import RegisterForm from "./RegisterForm";
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";


require('../css/fullstack.css');
import $ from 'jquery'


export default class SearchMiniPatterns extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            user: {
                email : '',
                input_email : '',
                input_password : '',
                is_logged_in : false
            },
            query : '%20',
            button_query : ' '
        }

        this.getQuery = this.getQuery.bind(this);
        this.resetResults = this.resetResults.bind(this);
        this.setLogIn = this.setLogIn.bind(this);
        this.setLogOut = this.setLogOut.bind(this);
        // this.getRegisterForm = this.getRegisterForm.bind(this);

    }

    getQuery(is_reset = false){
        /*
            Sets the new value for query in state. 
        */
        let query_string = String(this.state.button_query.value)
        // console.log(this.state.button_query.value)
        
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

    updateLogInStatus(respFromServer, email){
        /*
            Updates user log in status according to server response.
        */
        if(respFromServer['success']== 'true'){
            this.setState({
                user: {
                    is_logged_in : true,
                    email: email
                    }
                });
        }
    };

    sendAuthToServer(email, password){
        /*
            Sends auth values to server for log in.
        */

        const route_part_1 = '/auth/log_in/'
        const route_part_2 = '+'


        $.get(route_part_1 + email + route_part_2 + password, (data) => {
            console.log(data);
            this.updateLogInStatus(data, email);
        });

    }

    setLogIn(){
        /*
            Sends auth values to server to log user in.
        */
        console.log('Logging in!');

        const email = String(this.state.user.input_email.value);
        const password = String(this.state.user.input_password.value);

        if (email != this.state.user.email){
            if (this.state.user.is_logged_in == false){
                this.sendAuthToServer(email, password);
            }
        }else{
            this.sendAuthToServer(email, password);
        };
        
    }


    setLogOut(){
        /*
            Logs user out, no auth values required.
        */
        console.log('Logging out!')

        if (this.state.user.is_logged_in == true){
            this.setState({
                user: {
                    is_logged_in : false
                    }
            });
        }

    }


    render () {
        return (
                <div>
                    <Row>
                  <nav className="navbar navbar-expand-lg navbar-light bg-light container-fluid">
                    <a className="navbar-brand" href="/">Knit It</a>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                      <form className="form-inline my-2 my-lg-0">
                            <FormControl inputRef={node => this.state.button_query = node}  type="text" placeholder="Enter query" className="mr-sm-2" />
                            <Button bsStyle="warning" onClick={this.getQuery} className="mr-sm-2" >
                                Search
                            </Button>
                            <Button bsStyle="warning" onClick={this.resetResults} className="mr-sm-2" >
                                Reset Results
                            </Button>
                      </form>
                        <form className="form-inline my-2 my-lg-0">
                            <FormControl inputRef={node => this.state.user.input_email = node}  type="text" placeholder="Email" className="mr-sm-2"/>
                            <FormControl inputRef={node => this.state.user.input_password = node}  type="text" placeholder="Password" className="mr-sm-2"/>
                            <Button bsStyle="info" onClick={this.setLogIn} className="mr-sm-2" >
                                Log in
                            </Button>
                            <Button bsStyle="info" onClick={this.setLogOut} className="mr-sm-2" >
                                Log out
                            </Button>
                      </form>
                      <RegisterForm is_logged_in={this.state.user.is_logged_in}/>
                    </div>
                  </nav>
                    </Row>
                        <MiniPatterns query={this.state.query} is_logged_in={this.state.user.is_logged_in} email={this.state.user.email} />  
                </div>
        );
    }
}

import React from "react";
import MiniPatterns from "./MiniPatterns";
import RegisterForm from "./RegisterForm";
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl, Modal, ModalHeader, ModalBody, ModalFooter } from "react-bootstrap";


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
                is_logged_in : false,
                unsuccessful_log_in_attempt: false
            },
            favorites: {
                data: 'favorites.data'
            },
            query : '%20',
            button_query : ' ',
            modal : ' ',
            modal_show : false
        }

        this.getQuery = this.getQuery.bind(this);
        this.resetResults = this.resetResults.bind(this);
        this.setLogIn = this.setLogIn.bind(this);
        this.setLogOut = this.setLogOut.bind(this);
        this.handleModalShow = this.handleModalShow.bind(this);
        this.handleModalClose = this.handleModalClose.bind(this);

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
                    email: email,
                    unsuccessful_log_in_attempt: false
                    }
                });
        }else{
            this.setState({
                user: {
                    is_logged_in : false,
                    unsuccessful_log_in_attempt: true
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


    setFavoriteItems(items_list){
        /*
            Returns html representation of items in list.
        */
        return items_list.map((pattern) =>
            <li key={pattern.pattern_id.toString()}>
            {pattern.pattern_id}, {pattern.name}</li>
            );
    }


    setFavorites(favorites_list){
    /*
        Returns html representation of items in list.
    */

        const favorites_elems = this.setFavoriteItems(favorites_list)

        // console.log('HTML FAV')
        // console.log(favorites_elems)
        this.setState({
            favorites : {
                data : favorites_elems
            }
        })
    }


    getFavoritesList(){
        /*
            Returns list with pattern_id and pattern_name from patterns in favorites list.
        */
        const email = this.state.user.email
        const route_pre = '/'
        const route_post = '/favorites/get'


        $.get(route_pre + email + route_post, (data) => {    
            console.log('FAVORITES')
            console.log(data)
            this.setFavorites(data)

        });

    }


    clearLogInInputFields(){
        $('#email_input').val('')
        $('#password_input').val('')
    }


    setLogIn(){
        /*
            Logs user in by given email and password.
        */
        console.log('Logging in!');

        const email = String(this.state.user.input_email.value);
        const password = String(this.state.user.input_password.value);

        this.clearLogInInputFields()

        if(this.state.user.is_logged_in == false){
            this.sendAuthToServer(email, password);
        }else{
            console.log('You need to log out first before you can log in again!')
        }
        
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
        }else{
            console.log('You\'re not logged in, so you can\'t log out!')
        }

    }


    handleModalClose() {
        this.setState({ modal_show: false });
    }


    handleModalShow() {
        this.getFavoritesList()
        this.setState({ modal_show: true });
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
                            <FormControl id="email_input" inputRef={node => this.state.user.input_email = node}  type="text" placeholder="Email" className="mr-sm-2"/>
                            <FormControl id="password_input" inputRef={node => this.state.user.input_password = node}  type="text" placeholder="Password" className="mr-sm-2"/>
                            <Button bsStyle="info" onClick={this.setLogIn} className={this.state.user.is_logged_in ? 'mr-sm-2 disabled' : 'mr-sm-2'} >
                                Log in
                            </Button>
                            <Button bsStyle="info" onClick={this.setLogOut} className={!this.state.user.is_logged_in ? 'mr-sm-2 disabled' : 'mr-sm-2'} >
                                Log out
                            </Button>
                          <div>
                            { this.state.user.is_logged_in
                              ? <p>You're logged in as {this.state.user.email}.</p>
                              : null
                            }
                            { this.state.user.unsuccessful_log_in_attempt
                              ? <p>Log in unsuccessful! Please try again.</p>
                              : null
                            }
                        </div>
                      </form>
                      { this.state.user.is_logged_in
                        ? <div>
                        <Button bsStyle="success" onClick={this.handleModalShow} className={!this.state.user.is_logged_in ? 'mr-sm-2 disabled' : 'mr-sm-2'} >
                                My favorites
                            </Button> 
                            {this.state.modal}
                            </div>
                        : <RegisterForm is_logged_in={this.state.user.is_logged_in}/>
                      }
                    </div>
                  </nav>
                    </Row>
                        <MiniPatterns query={this.state.query} is_logged_in={this.state.user.is_logged_in} email={this.state.user.email} />  

                <Modal className={this.state.modal_show ? 'show' : ''} show={this.state.modal_show} onHide={this.handleModalClose}>
                  <Modal.Header>
                    <Modal.Title>My favorites</Modal.Title>
                  </Modal.Header>
                  <Modal.Body>
                  <p>{this.state.favorites.data}</p>
                  </Modal.Body>
                  <Modal.Footer>
                    <Button onClick={this.handleModalClose}>
                      Close
                    </Button>
                  </Modal.Footer>
                </Modal>

                </div>

        );
    }
}

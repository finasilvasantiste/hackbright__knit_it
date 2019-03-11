import React from "react";
import SearchResults from "./SearchResults";
import RegisterForm from "./RegisterForm";
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl, Modal, ModalHeader, ModalBody, ModalFooter } from "react-bootstrap";
import $ from 'jquery'

// require('../css/fullstack.css');

export default class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            user: {
                email : '',
                is_logged_in : false,
                unsuccessful_log_in_attempt: false
            },
            favorites: {
                data: ''
            },
            pattern_id : '',
            isQueueSelection : false,
            query : '%20',
            modal : ' ',
            modal_show : false,
            modal_login_show : false
        }

        this.getQuery = this.getQuery.bind(this);
        this.resetResults = this.resetResults.bind(this);
        this.setLogIn = this.setLogIn.bind(this);
        this.setLogOut = this.setLogOut.bind(this);
        this.handleModalShow = this.handleModalShow.bind(this);
        this.handleModalClose = this.handleModalClose.bind(this);
        this.getPatternID = this.getPatternID.bind(this);
        this.handleLoginModalShow = this.handleLoginModalShow.bind(this);
        this.handleLoginModalClose = this.handleLoginModalClose.bind(this);

    }


    clearLogInInputFields(){
        /*
            Sets log in input fields to empty string.
        */
        $('#email_input').val('')
        $('#password_input').val('')
    }


    clearSearchInputField(){
        /*
            Sets search input field to empty string.
        */
        $('#search_input').val('')
    }


    getQuery(is_reset = false){
        /*
            Sets the new value for query in state. 
        */
        // let query_string = String(this.state.button_query.value)
        
        let query_string = $('#search_input').val()

        if(is_reset == true){
            query_string = '%20'
        }

        this.setState({
            query : query_string
        });

    }


    resetResults(){
        /*
            Resets the search results to (empty string) search results.
        */
        this.getQuery(true)
        this.clearSearchInputField()
    }


    updateLogInStatus(respFromServer, email){
        /*
            Updates user log in status according to server response.
        */
        if(respFromServer['success']){
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

    getPatternID(pattern_id){
        console.log('@@@@ LOADING PATTERN @@@@')

        console.log(pattern_id)

        this.setState({
            pattern_id : pattern_id,
            isQueueSelection : true
        })
    }


    setFavoriteItems(items_list){
        /*
            Returns html representation of items in list.
        */
        return items_list.map((pattern) =>
            <li key={pattern.pattern_id.toString()} onClick={()=>this.getPatternID(pattern.pattern_id)}>
            {pattern.name}</li>
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

    setLogIn(){
        /*
            Logs user in by given email and password.
        */
        const email = $('#email_input').val()
        const password = $('#password_input').val()

        this.clearLogInInputFields()

        const regex_match = new RegExp("[A-Za-z0-9]+@$")
        const isValidEmail = regex_match.test(email);


        if(this.state.user.is_logged_in == false){
            if(isValidEmail){
                if(password.length >= 1){
                    console.log('Logging in!');
                    this.sendAuthToServer(email, password);
                }
            }
        }
        
    }


    setLogOut(){
        /*
            Logs user out, no auth values required.
        */
        console.log('Logging out!')

        if (this.state.user.is_logged_in){
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
        this.setState({ 
            modal_show: false,
            isQueueSelection : false 
        });
    }


    handleModalShow() {
        this.getFavoritesList()
        this.setState({ modal_show: true });
    }

    handleLoginModalShow(){
        this.setState({ modal_login_show: true });
    }

    handleLoginModalClose(){
        this.setState({ modal_login_show: false });
    }


    render () {
        return (
                <div>
                    <Row>
                      <nav className="navbar logo navbar-expand-lg navbar-light bg-light container-fluid">
                        <a className="navbar-brand" href="/">KNIT IT</a>
                        <div className="mr-auto">
                          <form className="form-inline my-2 my-lg-0">
                                <FormControl id="search_input" type="text" placeholder="Enter query" className="mr-sm-2" />
                                <Button bsStyle="danger" onClick={this.getQuery} className="mr-sm-2" >
                                    Search
                                </Button>
                                <Button bsStyle="outline-danger" onClick={this.resetResults} className="mr-sm-2" >
                                    Reset Results
                                </Button>
                          </form>
                          </div>    
                          <div className="ml-auto">
                              <div style={{"display" : "flex"}}>
                              <div className="login-status">
                            { this.state.user.is_logged_in
                              ? <p>Logged in as {this.state.user.email}</p>
                              : null
                            }
                            { this.state.user.unsuccessful_log_in_attempt
                              ? <p>Log in unsuccessful! Please try again.</p>
                              : null
                            }
                           </div>
                          { this.state.user.is_logged_in
                            ? 
                            <Button bsStyle="danger" onClick={this.handleModalShow} className={!this.state.user.is_logged_in ? 'mr-sm-2 disabled' : 'mr-sm-2'} >
                                    My favorites
                                </Button> 
                                
                            : <RegisterForm is_logged_in={this.state.user.is_logged_in}/>
                          }
                          { !this.state.user.is_logged_in
                            ? 
                                <Button bsStyle="outline-secondary" onClick={this.handleLoginModalShow}>
                                    Log in
                                </Button> 
                            : 
                            <Button bsStyle="outline-secondary" onClick={this.setLogOut}  >
                                    Log out
                                </Button>
                          }
                          </div>
                          </div>
                      </nav>
                    </Row>
                        <SearchResults showQueue={this.state.modal_show} query={this.state.query} is_logged_in={this.state.user.is_logged_in} email={this.state.user.email} pattern_id={this.state.pattern_id} isQueueSelection={this.state.isQueueSelection}/>  

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
                <Modal className={this.state.modal_login_show ? 'show' : ''} show={this.state.modal_login_show} onHide={this.handleModalClose}>
                  <Modal.Header>
                    <Modal.Title>Log in</Modal.Title>
                  </Modal.Header>
                  <Modal.Body>
                  <form className="form-inline my-2 my-lg-0">
                    <FormControl id="email_input" type="text" placeholder="Email" className="mr-sm-2"/>
                    <FormControl id="password_input" type="text" placeholder="Password" type="password" className="mr-sm-2"/>           
                    <div><br/><Button bsStyle="outline-secondary" onClick={this.setLogIn} className={this.state.user.is_logged_in ? 'mr-sm-2 disabled' : 'mr-sm-2'} >
                        Submit
                    </Button>
                    </div>
                  </form>
                  </Modal.Body>
                  <Modal.Footer>
                    <Button onClick={this.handleLoginModalClose}>
                      Close
                    </Button>
                  </Modal.Footer>
                </Modal>

                </div>

        );
    }
}

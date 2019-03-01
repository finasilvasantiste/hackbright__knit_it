import React from "react";
import { Button, Modal, ModalHeader, ModalBody, ModalFooter, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";

import $ from 'jquery'


export default class RegisterForm extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
          show: false,
          user: {
              input_email : '',
              input_password : '',
              is_logged_in : this.props.is_logged_in,
          },
          is_registered : false
    };

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.registerUser = this.registerUser.bind(this);
  }

  handleClose() {
    this.setState({ show: false });
  }

  handleShow() {
    // console.log('Modal handleShow')
    this.setState({ show: true });
  }


  updateRegistrationStatus(respFromServer){
    /*
      Updates user log in status according to server response.
    */

      if(respFromServer['success']== 'true'){
          this.setState({
              is_registered : true
              });
      }

      console.log('Resp from server:', respFromServer['success'])
  }


  sendRegistrationToServer(email, password){
    /*
      Sends registration values to server for registration.
    */

      const route_part_1 = '/auth/register/'
      const route_part_2 = '+'

      console.log(email , ' ', password)

      $.get(route_part_1 + email + route_part_2 + password, (data) => {
          console.log(data);
          this.updateRegistrationStatus(data);
      });

  }


  registerUser(){
    /*
      Registers a user by given email adress and password.
      Shows user if registration was successful.
    */
    console.log('Registering!');

    const email = String(this.state.user.input_email.value);
    const password = String(this.state.user.input_password.value);

    
    if (this.state.user.is_logged_in){
        console.log('You need to log out before you can register!')
    }else{
        this.sendRegistrationToServer(email, password)
    }

  }

  componentWillReceiveProps(nextProps){
      this.setState({
          user: {
              is_logged_in : nextProps.is_logged_in
          }
      });

  }


  render() {
    return (
      <div>
        <Button onClick={this.handleShow}>
          Register
        </Button>

        <Modal className={this.state.show ? 'show' : ''} show={this.state.show} onHide={this.handleClose}>
          <Modal.Header>
            <Modal.Title>Register</Modal.Title>
          </Modal.Header>
          <Modal.Body>

            Success: {this.state.is_registered}
          <form className="form-inline my-2 my-lg-0">
                <FormControl inputRef={node => this.state.user.input_email = node}  type="text" placeholder="Email" className="mr-sm-2"/>
                <FormControl inputRef={node => this.state.user.input_password = node}  type="text" placeholder="Password" className="mr-sm-2"/>
                <Button bsStyle="info" onClick={this.registerUser} className="mr-sm-2" >
                    Register
                </Button>
          </form>
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.handleClose}>
              Close
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }
}
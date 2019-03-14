import React from "react";
import NavBar from "./NavBar"
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl, Navbar, Nav, NavDropdown } from "react-bootstrap";


require('../css/fullstack.css');


export default class App extends React.Component {
    constructor(props) {
        super(props);
    }


    render () {
        return (
                <Grid fluid={true}>
                    <NavBar />  
                </Grid>
        );
    }
}


                

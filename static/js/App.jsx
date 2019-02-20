import React from "react";
// import MiniPatterns from "./MiniPatterns"
import SearchMiniPatterns from "./SearchMiniPatterns"
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl, Navbar, Nav, NavDropdown } from "react-bootstrap";


require('../css/fullstack.css');
// import $ from 'jquery'


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            // email : 'Fina',
            // password_hash : 'jsdkfjkh4',
            // email_button : '',
            // password_hash_button : '',
            // is_logged_in : false

        }

    }


    render () {
        return (
                <Grid>
                    <SearchMiniPatterns />  
                </Grid>
        );
    }
}


                

import React from "react";
import Pattern from "./Pattern"
import MiniPatterns from "./MiniPatterns"
import { Button, Grid, Row, Col } from "react-bootstrap";


require('../css/fullstack.css');
var $ = require('jquery');


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state= {
            pattern_id : 781496
        }

        this.getPatternID = this.getPatternID.bind(this);
    }

    getPatternID(dataFromMiniPattern){
        // console.log(dataFromMiniPattern)
        this.setState({
            pattern_id : dataFromMiniPattern.pattern_id

        });

        
        console.log('Pattern_id from App: '+this.state.pattern_id)
    }


    render () {
        return (
            <Grid>
                <Row>
                    <Col md={7} >
                        <MiniPatterns callbackFromParent={this.getPatternID} />
                    </Col>
                    <Col md={5}>
                        <Pattern id={this.state.pattern_id}/> 
                    </Col>                
                </Row>
            </Grid>
        );
    }
}
